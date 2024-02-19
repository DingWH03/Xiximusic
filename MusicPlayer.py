import sys
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl, Slot
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtMultimedia import QMediaFormat
import diskcache

import os
import requests
import threading
import random
from functools import partial
from Utils import clean_cache, DownLoadThread, RequestApi_multithread



class MusicPlayer(QMainWindow):
    def __init__(self, diskcache, api, cache_folder):
        self.api = api # 网易云音乐api引用
        self.player = QMediaPlayer()
        self.audioOutput = QAudioOutput()
        self.player.setAudioOutput(self.audioOutput) # 初始化音乐播放器
        # self.player.positionChanged.connect(self.positionChanged)
        # self.player.durationChanged.connect(self.durationChanged)
        #self.player.playbackStateChanged.connect(self.stateChanged)
        self.player.mediaStatusChanged.connect(self.mediaStatusChanged)
        #self.player.errorOccurred.connect(self._player_error)
        self.volume = float(1) # 记录音量大小(0~1)
        self.audioOutput.setVolume(self.volume)
        self.player.setSource('')
        self.cache = diskcache # widget传来的cache引用
        self.playing = False # 追踪播放状态
        self.play_sequence = 0 ; # 规定0为歌单顺序播放，1为歌单内随机播放，2为单曲循环
        self.shuffled_playlist = []

        # 歌曲信息(属性)
        self.music_url = '' # 歌曲链接
        self.music_name = 'No Music' # 歌曲名称
        self.playlist_id = '' # 歌单id
        self.is_playlist = False # 标志是否为歌单，用来判断是否自动播放下一首和切换上下曲
        self.index = '' # 歌曲在歌单中的顺序
        self.song_id = ''
        self.singer_name = ''
        self.album_name = ''
        self.duration = self.player.duration()
        self.position = self.player.duration()
        self.loved_status = False

        self.playlist = [] # 记录歌单
        self.cache_dir = cache_folder+'/song' # 歌曲缓存地址
        self.max_size = 1000 * 1024 * 1024 # 缓存大小 1000 MB
        self.initCache()
        # 创建一个threading.Thread对象，指定target和args
        clean_thread = threading.Thread(target=clean_cache, args=(self.cache_dir, self.max_size))
        # 调用start方法，启动新的线程
        clean_thread.start()

    def initCache(self):
        # 如果～/.cache/music目录不存在，创建一个
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)

    def set_music(self, URL, music_id, Name = None):
        self.music_url = URL;
        self.music_name = Name
        self.song_id = music_id
        # print(self.music_name)
        # 设置音乐文件的路径
        music_file = os.path.join(self.cache_dir, f"{music_id}.mp3")
        # 如果音乐文件不存在，从URL下载并保存到～/.cache/music目录下
        if not os.path.exists(music_file):
            download_thread = DownLoadThread(URL, music_file)
            download_thread.downloaded.connect(partial(self.on_downloaded_set_music, music_file, download_thread))
            download_thread.start()
            return 0
        else:
            self.stop_play()
            self.player.setSource(QUrl.fromLocalFile(music_file))
            return 1 # 返回值为1,不调用多线程下载，需要set_music之后执行start_play()

    def on_downloaded_set_music(self, music_file, thread):
        # print(music_file)
        thread.quit()
        self.stop_play()
        self.player.setSource(QUrl.fromLocalFile(music_file))
        self.start_play()

    # 播放音乐
    def start_play(self):
        if self.player.playbackState() != QMediaPlayer.PlayingState:
            self.player.play()
            self.playing = True

    # 停止播放
    def stop_play(self):
        if self.player.playbackState() != QMediaPlayer.StoppedState:
            self.player.stop()
            # print("stopped!")
            self.playing = False

    # 暂停播放
    def pause_play(self):
        # 只有正在播放时才能暂停
        if self.player.playbackState() == QMediaPlayer.PlayingState:
            self.player.pause()
            self.playing = False

    # 重置播放器
    def reset_player(self):
        # 音乐为空
        self.music = None
        self.stop_play()
        self.playing = False

    def toggle_playback(self):
        if self.playing:
            self.pause_play()
        else:
            self.start_play()

    # 设置音量大小（0-100）
    def set_volume(self,value):
        self.volume = float(value/100)
        self.audioOutput.setVolume(self.volume)

    # 通过歌曲id自动调用网易云api获取播放url
    def playmusic_byID(self, id, name):
        self.is_playlist = False
        self.music_name = name
        # url = self.api.get_song_url_v1(id)[0].get('url')
        self.stop_play()
        api_thread = RequestApi_multithread(self.api.get_song_url_v1, id)
        api_thread.requested.connect(partial(self.on_got_musicURL, id, name, api_thread))
        api_thread.start()


    # 通过歌曲index查找playlist获取id自动调用网易云api获取播放url
    def playmusic_byIndex(self, index, name = None):
        self.index = index
        id = self.playlist[index].get('id')
        name = self.playlist[index]['name']
        self.music_name = name
        # print(self.playlist)
        self.loved_status = self.playlist[index]['loved']
        # url = self.api.get_song_url_v1(id)[0].get('url')
        self.stop_play()
        api_thread = RequestApi_multithread(self.api.get_song_url_v1, id)
        api_thread.requested.connect(partial(self.on_got_musicURL, id, name, api_thread))
        api_thread.start()

    def on_got_musicURL(self, id, name, api_thread, data):
        url = data[0].get('url')
        if url: # 如果歌曲无法播放则自动切换下一曲
            if self.set_music(url, id, name):
                self.start_play()
        else:
            self.play_next()

    # 设置播放列表
    def setPlaylist(self, playlist_id):
        self.is_playlist = True
        self.playlist_id = playlist_id
        #print(self.cache[f"playlist{playlist_id}"])
        self.playlist = self.cache[f"playlist{playlist_id}"]
        #print(self.playlist)

    # 设置播放顺序
    def setPlaysequence(self, sequence):
        if sequence>=0 and sequence<=2:
            self.play_sequence = sequence
            if sequence == 1:
                self.shuffled_playlist = self.playlist.copy()
                random.shuffle(self.shuffled_playlist)
                self.shuffled_playlist, self.playlist = self.playlist, self.shuffled_playlist
                # self.playmusic_byIndex(0)
            # elif sequence == 0:c
                # self.shuffled_playlist, self.playlist = self.playlist, self.shuffled_playlist
                # self.playmusic_byIndex(0)
            elif sequence == 2:
                self.shuffled_playlist, self.playlist = self.playlist, self.shuffled_playlist

    # 备用 设置歌曲名
    def setMusicName(self, index):
        name = self.playlist[index]['name']
        self.music_name = name

    # 上一首
    def play_previous(self):
        if self.is_playlist and self.index - 1 >= 0:
            self.index -= 1
            name = self.playlist[self.index]['name']
            self.playmusic_byIndex(self.index, name)
        elif self.is_playlist and self.index == 0:
            # If it's the first song in the playlist, play the last song
            self.index = len(self.playlist) - 1
            name = self.playlist[self.index]['name']
            self.playmusic_byIndex(self.index, name)
        else:
            # If not a playlist, do nothing or handle as needed
            pass

    # 下一曲
    def play_next(self):
        if self.is_playlist and self.index + 1 < len(self.playlist):
            self.index += 1
            name = self.playlist[self.index]['name']
            self.playmusic_byIndex(self.index, name)
        elif self.is_playlist and self.index + 1 == len(self.playlist):
            # If it's the last song in the playlist, play the first song
            self.index = 0
            name = self.playlist[self.index]['name']
            self.playmusic_byIndex(self.index, name)
        else:
            # If not a playlist, do nothing or handle as needed
            pass

    def setPlaylist_search_song(self, cachename):
        self.is_playlist = True
        self.playlist = self.cache[cachename]
        # print(self.playlist)

    # @Slot()
    # def positionChanged(self, position):
    #     if position % 1000 <= 50:
    #         s = int(position/1000) + 1
    #         # print(s)
    #         self.position = position

    # @Slot()
    # def durationChanged(self, duration):
    #     self.duration = duration

    @Slot()
    def stateChanged(self, state):
        print(f'stateChanged: {state}')
        print(self.playing)

    @Slot()
    def _player_error(self, error, error_string):
        print(error, error_string)

    @Slot()
    def mediaStatusChanged(self, status):
        if status == QMediaPlayer.EndOfMedia:
            if self.play_sequence == 2:
                self.playmusic_byIndex(self.index)
            else:
                self.play_next()

