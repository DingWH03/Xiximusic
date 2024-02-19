# This Python file uses the following encoding: utf-8
import sys
import base64
import requests
from datetime import datetime
import os
import threading
from functools import partial
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtCore import Qt, QByteArray, QBuffer, QIODevice, QSize
from PySide6.QtGui import QImage, QPixmap, QAction, QIcon
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QToolButton, QSizePolicy, QMessageBox, QMenu, QSlider, QWidgetAction
from PySide6.QtWidgets import QSpacerItem, QSystemTrayIcon
import diskcache

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

from subwidget import HomeItemQToolButton, SongItemWidget, lyricItem, MoreHomeItemQToolButton, CustomScrollArea
from NeteaseMusicApi import NTCMAPI
from MusicPlayer import MusicPlayer
from Utils import get_cache_folder, RequestApi_multithread, refresh_song_detail, split_lyrics, setPixmap_multithread


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget() # 初始化主widget对象撰写一封自荐
        self.ui.setupUi(self)  # 显示主widget
        self.setWindowTitle("XiXiMusic") # 设置窗口标题
        self.cache_folder = get_cache_folder() # 初始化缓存文件夹
        self.cache = diskcache.Cache(self.cache_folder + "/cache") # 创建一个缓存对象
        self.uid = '' # 记录登陆用户的uid
        self.api = NTCMAPI(self.cache_folder) # 初始化网易云api
        self.musicPlayer = MusicPlayer(self.cache, self.api, self.cache_folder) # 初始化音乐播放器
        self.previous_page = []
        if not self.api.netease_cloud_music_api.cookie:
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_login) # 检测登陆状态判断是否需要登陆
        else:
            self.fill_home() # 填充首页
            self.init_ui()

        # self.api.refresh_login()
#------------------------------信号与槽连接------------------------------------
        self.ui.myInfo_pushButton.clicked.connect(self.the_myInfo_button_was_clicked) # 左侧边栏我的信息按钮
        self.ui.delete_Cookie_PushButton.clicked.connect(self.the_delete_Cookie_PushButton_was_clicked) # 我的页面退出登录按钮
        self.ui.captcha_Sent_PushButton.clicked.connect(self.the_captcha_Sent_PushButton_was_clicked) # 登录页面发送验证码按钮
        self.ui.captcha_Verify_PushButton.clicked.connect(self.the_captcha_Verify_PushButton_was_clicked) # 登录页面验证码登录按钮
        self.ui.frontpage_pushButton.clicked.connect(self.the_frontpage_pushButton_was_clicked) # 左边栏的首页按钮
        self.ui.pause_bottom_bar_pushButton.clicked.connect(self.the_pause_bottom_bar_pushButton_was_clicked) # 下边栏的暂停按钮
        self.ui.pause_pushButton_in_playerpage.clicked.connect(self.the_pause_bottom_bar_pushButton_was_clicked) # 播放页面的暂停按钮
        self.ui.pushButton_back_in_playlist.clicked.connect(self.the_pushButton_back_in_playlist_was_clicked) # 歌单返回到主页按钮
        self.ui.pushButton_return_to_home_in_page_home_more_item.clicked.connect(self.the_pushButton_return_to_home_in_page_home_more_item_was_clicked)
        self.ui.previous_music_bottom_bar_pushButton.clicked.connect(self.the_previous_music_bottom_bar_pushButton_was_clicked) # 下边栏的上一曲按钮
        self.ui.next_music_bottom_bar_pushButton.clicked.connect(self.the_next_music_bottom_bar_pushButton_was_clicked) # 下边栏的下一曲按钮
        self.ui.pushButton_set_volume_in_bottom_bar.clicked.connect(partial(self.the_pushButton_set_volume_was_clicked, self.ui.pushButton_set_volume_in_bottom_bar)) # 下边栏的调节音量按钮
        self.ui.pushButton_set_volume_in_playerpage.clicked.connect(partial(self.the_pushButton_set_volume_was_clicked, self.ui.pushButton_set_volume_in_playerpage)) # 播放页面的调节音量按钮
        self.ui.previous_music_pushButton_in_playerpage.clicked.connect(self.the_previous_music_bottom_bar_pushButton_was_clicked) # 播放页面的上一曲按钮
        self.ui.next_music_pushButton_in_playerpage.clicked.connect(self.the_next_music_bottom_bar_pushButton_was_clicked) # 播放页面的下一曲按钮
        self.musicPlayer.player.mediaStatusChanged.connect(self.handle_MediaStatus_Changed) # 音乐切换时自动更新显示的歌曲名称
        self.musicPlayer.player.playbackStateChanged.connect(self.handleStateChanged) # 音乐切换时自动更新暂停键图标
        self.ui.search_pushButton.clicked.connect(self.the_search_pushButton_was_clicked) # 左侧边栏的搜索键
        self.ui.pushButton_confirm_to_search_song.clicked.connect(self.the_pushButton_confirm_to_search_song_was_clicked) # 搜索页面的搜索歌曲按钮
        self.ui.pushButton_confirm_to_search_album.clicked.connect(self.the_pushButton_confirm_to_search_album_was_clicked) # 搜索页面的搜索专辑按钮
        self.ui.pushButton_confirm_to_search_playlists.clicked.connect(self.the_pushButton_confirm_to_search_playlists_was_clicked) # 搜索页面的搜索歌单按钮
        self.ui.pushButton_confirm_to_search_singer.clicked.connect(self.the_pushButton_confirm_to_search_singer_was_clicked) # 搜索页面的搜索歌手按钮
        self.ui.pushButton_player_return_to_main.clicked.connect(self.the_pushButton_player_return_to_main_was_clicked) # 播放页面的返回按钮
        self.ui.pushButton_music_play.clicked.connect(self.the_pushButton_music_play_was_clicked) # 下边栏专辑图像（切换到播放器按钮）
        self.musicPlayer.player.positionChanged.connect(self.positionChanged) # 更新歌曲当前进度
        self.musicPlayer.player.durationChanged.connect(self.durationChanged) # 更新歌曲总时长
        self.ui.horizontalSlider_time_in_bottom_bar.sliderMoved.connect(self.updatePosition) # 拖动下边栏进度条改变歌曲进度
        self.ui.horizontalSlider_music_progress_in_playerpage.sliderMoved.connect(self.updatePosition) # 拖动播放页面进度条改变歌曲进度
        self.ui.pushButton_menu_in_bottom_bar.clicked.connect(self.on_the_pushButton_menu_in_bottom_bar_was_clicked) # 下边栏的菜单按钮
        self.ui.pushButton_play_sequence_in_playerpage.clicked.connect(self.on_the_pushButton_play_sequence_was_clicked) # 播放页面的循环按钮
        self.ui.pushButton_play_sequence_in_bottom_bar.clicked.connect(self.on_the_pushButton_play_sequence_was_clicked) # 下边栏的循环按钮
        self.ui.favor_music_bottom_bar_pushButton.clicked.connect(self.on_the_favor_music_was_clicked) # 下边栏的喜欢按钮
        self.ui.favor_music_pushButton_in_playerpage.clicked.connect(self.on_the_favor_music_was_clicked) # 播放页面的喜欢按钮
#------------------------------类的函数定义-------------------------------------
    def closeEvent(self, event):
        '''在窗口关闭事件中连接槽函数'''
        self.on_close_event(event)

    def on_close_event(self, event):
        # 此处编写关闭事件时要执行的操作
        reply = QMessageBox.question(self, '提示', '需要后台运行吗？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.ignore()
            self.hide()
        else:
            # 在这里添加你的关闭窗口前的其他操作
            self.cache.close()
            event.accept()
        return

    def exit_application(self):
        # 在这里添加你的关闭窗口前的其他操作
        self.cache.close()
        # 关闭系统托盘图标
        self.tray_icon.hide()
        # 退出应用程序
        QApplication.quit()

    def init_ui(self):
        # 设置主页面样式表
        self.setStyleSheet("""
                    QWidget {
                        background-color: #2E2E2E; /* 设置暗色背景 */
                        color: white; /* 设置文本颜色为白色 */
                    }

                    QPushButton {
                        background-color: rgba(0, 0, 0, 0);  /* 设置按钮的背景颜色 */
                        color: white; /* 设置按钮文本颜色为白色 */
                        border: None; /* 设置按钮边框 */
                        padding: 5px; /* 设置按钮内边距 */
                    }

                    QPushButton:hover {
                        background-color: #505050; /* 设置鼠标悬停时按钮的背景颜色 */
                    }
                """)

        # 创建系统托盘图标
        self.tray_icon = QSystemTrayIcon(self)
        self.tray_icon.setToolTip('XixiMusic')
        self.tray_icon.setIcon(QIcon('icon.png'))
        self.tray_icon.setVisible(True)

        # 创建系统托盘菜单
        tray_menu = QMenu(self)

        # # 创建包含label的QWidgetAction
        # label_action = QWidgetAction(self)
        # label_action.setDefaultWidget(self.ui.label_playing_music_name)

        restore_action = tray_menu.addAction('恢复')
        # tray_menu.addAction(label_action)
        pause_action = tray_menu.addAction('暂停/播放')
        previous_song_action = tray_menu.addAction('上一曲')
        next_song_action = tray_menu.addAction('下一曲')
        exit_action = tray_menu.addAction('退出')

         # 连接菜单项的槽函数
        restore_action.triggered.connect(self.show_window)
        exit_action.triggered.connect(self.exit_application)
        pause_action.triggered.connect(self.the_pause_bottom_bar_pushButton_was_clicked)
        previous_song_action.triggered.connect(self.the_previous_music_bottom_bar_pushButton_was_clicked)
        next_song_action.triggered.connect(self.the_next_music_bottom_bar_pushButton_was_clicked)

        # 将菜单设置到托盘图标
        self.tray_icon.setContextMenu(tray_menu)

        self.ui.pushButton_music_play.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: none;")
        # 加载图标
        self.more_icon = QPixmap(os.getcwd() + '/image/more.png')
        self.play_icon = QPixmap(os.getcwd() + '/image/play.png')
        self.lovemusic = QPixmap(os.getcwd() + '/image/love.png')
        self.lovedmusic = QPixmap(os.getcwd() + '/image/loved.png')
        self.pause_icon = QPixmap(os.getcwd() + '/image/pause.png')
        self.next_song_icon = QPixmap(os.getcwd() + '/image/next_song.png')
        self.previous_song_icon = QPixmap(os.getcwd() + '/image/previous_song.png')
        self.myinfo_icon = QPixmap(os.getcwd() + '/image/myinfo.png')
        self.search_icon = QPixmap(os.getcwd() + '/image/search.png')
        self.home_icon = QPixmap(os.getcwd() + '/image/home.png')
        self.gedanxunhuan_icon = QPixmap(os.getcwd() + '/image/gedanxunhuan.png')
        self.suijibofang_icon = QPixmap(os.getcwd() + '/image/suijibofang.png')
        self.danquxunhuan_icon = QPixmap(os.getcwd() + '/image/danquxunhuan.png')
        self.volumeon_icon = QPixmap(os.getcwd() + '/image/volumeon.png')
        self.settings_icon = QPixmap(os.getcwd() + '/image/settings.png')
        self.return_icon = QPixmap(os.getcwd() + '/image/return.png')
        self.menu_icon = QPixmap(os.getcwd() + '/image/menu.png')
        self.playlist_icon = QPixmap(os.getcwd() + '/image/playlist.png')

        self.ui.previous_music_bottom_bar_pushButton.setIconSize(self.ui.previous_music_bottom_bar_pushButton.size())
        self.ui.next_music_bottom_bar_pushButton.setIconSize(self.ui.next_music_bottom_bar_pushButton.size())
        self.ui.previous_music_pushButton_in_playerpage.setIconSize(self.ui.previous_music_pushButton_in_playerpage.size())
        self.ui.next_music_pushButton_in_playerpage.setIconSize(self.ui.next_music_pushButton_in_playerpage.size())
        self.ui.pause_pushButton_in_playerpage.setIconSize(self.ui.pause_pushButton_in_playerpage.size())
        self.ui.pause_bottom_bar_pushButton.setIconSize(self.ui.pause_bottom_bar_pushButton.size())
        self.ui.myInfo_pushButton.setIconSize(self.ui.myInfo_pushButton.size())
        self.ui.search_pushButton.setIconSize(self.ui.search_pushButton.size())
        self.ui.frontpage_pushButton.setIconSize(self.ui.frontpage_pushButton.size())
        self.ui.pushButton_play_sequence_in_bottom_bar.setIconSize(self.ui.pushButton_play_sequence_in_bottom_bar.size())
        self.ui.pushButton_play_sequence_in_playerpage.setIconSize(self.ui.pushButton_play_sequence_in_playerpage.size())
        self.ui.pushButton_set_volume_in_bottom_bar.setIconSize(self.ui.pushButton_set_volume_in_bottom_bar.size())
        self.ui.pushButton_set_volume_in_playerpage.setIconSize(self.ui.pushButton_set_volume_in_playerpage.size())
        self.ui.settings_pushButton.setIconSize(self.ui.settings_pushButton.size())
        self.ui.pushButton_player_return_to_main.setIconSize(self.ui.pushButton_player_return_to_main.size())
        self.ui.pushButton_return_to_home_in_page_home_more_item.setIconSize(self.ui.pushButton_return_to_home_in_page_home_more_item.size())
        self.ui.pushButton_back_in_playlist.setIconSize(self.ui.pushButton_back_in_playlist.size())
        self.ui.pushButton_menu_in_bottom_bar.setIconSize(self.ui.pushButton_menu_in_bottom_bar.size())
        self.ui.pushButton_now_playlist_in_bottom_bar.setIconSize(self.ui.pushButton_now_playlist_in_bottom_bar.size())
        self.ui.pushButton_now_playlist_in_playerpage.setIconSize(self.ui.pushButton_now_playlist_in_playerpage.size())
        self.ui.favor_music_pushButton_in_playerpage.setIconSize(self.ui.favor_music_pushButton_in_playerpage.size())
        self.ui.favor_music_bottom_bar_pushButton.setIconSize(self.ui.favor_music_bottom_bar_pushButton.size())

        self.ui.previous_music_bottom_bar_pushButton.setIcon(self.previous_song_icon)
        self.ui.next_music_bottom_bar_pushButton.setIcon(self.next_song_icon)
        self.ui.previous_music_pushButton_in_playerpage.setIcon(self.previous_song_icon)
        self.ui.next_music_pushButton_in_playerpage.setIcon(self.next_song_icon)
        self.ui.pause_pushButton_in_playerpage.setIcon(self.play_icon)
        self.ui.pause_bottom_bar_pushButton.setIcon(self.play_icon)
        self.ui.myInfo_pushButton.setIcon(self.myinfo_icon)
        self.ui.search_pushButton.setIcon(self.search_icon)
        self.ui.frontpage_pushButton.setIcon(self.home_icon)
        self.ui.pushButton_play_sequence_in_bottom_bar.setIcon(self.gedanxunhuan_icon)
        self.ui.pushButton_play_sequence_in_playerpage.setIcon(self.gedanxunhuan_icon)
        self.ui.pushButton_set_volume_in_bottom_bar.setIcon(self.volumeon_icon)
        self.ui.pushButton_set_volume_in_playerpage.setIcon(self.volumeon_icon)
        self.ui.settings_pushButton.setIcon(self.settings_icon)
        self.ui.pushButton_player_return_to_main.setIcon(self.return_icon)
        self.ui.pushButton_return_to_home_in_page_home_more_item.setIcon(self.return_icon)
        self.ui.pushButton_back_in_playlist.setIcon(self.return_icon)
        self.ui.pushButton_menu_in_bottom_bar.setIcon(self.menu_icon)
        self.ui.pushButton_now_playlist_in_bottom_bar.setIcon(self.playlist_icon)
        self.ui.pushButton_now_playlist_in_playerpage.setIcon(self.playlist_icon)
        self.ui.favor_music_pushButton_in_playerpage.setIcon(self.lovemusic)
        self.ui.favor_music_bottom_bar_pushButton.setIcon(self.lovemusic)

        # self.ui.page_player.setStyleSheet("background-color: lightgreen;")
        # self.ui.pushButton_music_play.setStyleSheet("border: 0px;")
        self.ui.pushButton_music_play.setIconSize(self.ui.pushButton_music_play.size())
        self.ui.label_albumPic_in_playerpage.setScaledContents(True) # 自动调整图片大小
        self.ui.scrollarea_more_item = CustomScrollArea() # 首页更多按钮点击之后的widget
        self.ui.verticalLayout_page_home_more_item.addWidget(self.ui.scrollarea_more_item)
        # tab_album 搜索专辑页面
        self.ui.scrollarea_tab_album = CustomScrollArea()
        self.ui.verticalLayout_tab_album.addWidget(self.ui.scrollarea_tab_album)
        # tab_playlists 搜索歌单页面
        self.ui.scrollarea_tab_playlists = CustomScrollArea()
        self.ui.verticalLayout_tab_playlists.addWidget(self.ui.scrollarea_tab_playlists)
        # tab_singer 搜索专辑页面
        self.ui.scrollarea_tab_singer = CustomScrollArea()
        self.ui.verticalLayout_tab_singer.addWidget(self.ui.scrollarea_tab_singer)


    def qr_show(self): #展示登陆二维码
        base64_qrcode = self.api.login_qr()
        qrcode_image = self.utils.base64_to_qimage(qrcode_image)

    def set_icon(self, iconURL, button):
        pixmap = get_image(iconURL, self.cache_folder + '/image')
        button.setIcon(pixmap)

    def fill_top_song(self, api_thread_top_song, data): # category 1
        api_thread_top_song.quit()
        self.cache['top_song_cache'] = data
        for i in range(0, 6):
        # for i in range(0, len(data)):
            album_info = data[i]['album']
            pic_url = album_info['picUrl']
            song_name = data[i]['name']
            #print(f"Song Name: {song_name}, Pic URL: {pic_url}"
            item = HomeItemQToolButton(song_name, pic_url, 1, i, self.ui.horizontalLayout_top_song, self, self.ui.main)
            # print('s')
            # self.create_select_toolbotton(song_name, pic_url, 1, i, self.ui.horizontalLayout_top_song)
        more_item = MoreHomeItemQToolButton(self.more_icon, data, 1, self.ui.horizontalLayout_top_song, self, self.ui.main)

    def fill_top_playlists(self, api_thread_top_playlists, data): # category 2
        # data = self.api.get_top_playlists()
        api_thread_top_playlists.quit()
        self.cache['top_lists_cache'] = data
        # for i in range(0, len(data)):
        for i in range(0, 6):
            #album_info = data[i]['album']
            coverImgUrl = data[i]['coverImgUrl']
            playlist_name = data[i]['name']
            #print(f"{playlist_name}, {coverImgUrl}")
            item = HomeItemQToolButton(playlist_name, coverImgUrl, 2, i, self.ui.horizontalLayout_top_playlists, self, self.ui.main)
            # self.create_select_toolbotton(playlist_name, coverImgUrl, 2, i, self.ui.horizontalLayout_top_playlists)
        more_item = MoreHomeItemQToolButton(self.more_icon, data, 2, self.ui.horizontalLayout_top_playlists, self, self.ui.main)


    def fill_personalized(self, api_thread_personalized, data): # category 3
        # data = self.api.get_personalized()
        api_thread_personalized.quit()
        self.cache['personalized_cache'] = data
        # for i in range(0, len(data)):
        for i in range(0, 6):
            #album_info = data[i]['album']
            coverImgUrl = data[i]['picUrl']
            playlist_name = data[i]['name']
            #print(f"{playlist_name}, {coverImgUrl}")
            item = HomeItemQToolButton(playlist_name, coverImgUrl, 3, i, self.ui.horizontalLayout_personalized, self, self.ui.main)
            # self.create_select_toolbotton(playlist_name, coverImgUrl, 3, i, self.ui.horizontalLayout_personalized)
        more_item = MoreHomeItemQToolButton(self.more_icon, data, 3, self.ui.horizontalLayout_personalized, self, self.ui.main)

    def fill_recommend_resource(self, api_thread_recommend_resource, data): # category 4
        # data = self.api.get_recommend_resource()
        api_thread_recommend_resource.quit()
        self.cache['recommend_resource_cache'] = data
        # for i in range(0, len(data)):
        for i in range(0, 6):
            #album_info = data[i]['album']
            coverImgUrl = data[i]['picUrl']
            playlist_name = data[i]['name']
            #print(f"{playlist_name}, {coverImgUrl}")
            # self.create_select_toolbotton(playlist_name, coverImgUrl, 4, i, self.ui.horizontalLayout_recommend_resource)
            item = HomeItemQToolButton(playlist_name, coverImgUrl, 4, i, self.ui.horizontalLayout_recommend_resource, self, self.ui.main)
        more_item = MoreHomeItemQToolButton(self.more_icon, data, 4, self.ui.horizontalLayout_recommend_resource, self, self.ui.main)

    def fill_toplist(self, api_thread_toplist, data): # category 5
        # data = self.api.get_toplist()
        api_thread_toplist.quit()
        self.cache['toplist_cache'] = data
        # for i in range(0, len(data)):
        for i in range(0, 6):
            #album_info = data[i]['album']
            coverImgUrl = data[i]['coverImgUrl']
            playlist_name = data[i]['name']
            #print(f"{playlist_name}, {coverImgUrl}")
            item = HomeItemQToolButton(playlist_name, coverImgUrl, 5, i, self.ui.horizontalLayout_toplist, self, self.ui.main)
            # self.create_select_toolbotton(playlist_name, coverImgUrl, 5, i, self.ui.horizontalLayout_toplist)
        more_item = MoreHomeItemQToolButton(self.more_icon, data, 5, self.ui.horizontalLayout_toplist, self, self.ui.main)

    def fill_playlist(self, playlist_name, playlist_id):
        # data = self.api.playlist_track_all(playlist_id)
        self.ui.label_in_playlist.setText(playlist_name)
        # 清理旧部件
        while self.ui.verticalLayout_playlist.count():
            item = self.ui.verticalLayout_playlist.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        api_thread = RequestApi_multithread(self.api.playlist_track_all, playlist_id)
        api_thread.requested.connect(partial(self.on_requested_fill_playlist, playlist_name, playlist_id, api_thread))
        api_thread.start()
        return

    def on_requested_fill_playlist(self, playlist_name, playlist_id, api_thread, data): # fill_playlist的多线程槽函数
        api_thread.quit()
        playlist = []
        index = 0
        for item in data:
            id = item.get('id')
            loved = False
            name = item.get('name')
            ar = item.get('ar')
            singer = ''
            for item_2 in ar:
                singer = singer + item_2.get('name') + '/'
            singer = singer[:-1]
            album = item.get('al').get('name')
            if id in self.api.likelist_ids:
                loved = True
            new_song = {"name": name, "id": id, "singer": singer, "album": album, "loved":loved}
            playlist.append(new_song)
            widget = SongItemWidget(self, self.cache, name, singer, album, id, index, self.api, loved, '', playlist_id)
            self.ui.verticalLayout_playlist.addWidget(widget)
            index = index + 1
        spacer_item = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.ui.verticalLayout_playlist.addSpacerItem(spacer_item)
        self.cache[f"playlist{playlist_id}"] = playlist
        return

    def fill_search_song_result(self, layout, keywords):
        data = self.cache[f'search_result_of_{keywords}']
        playlist = []
        index = 0
        cachename = f'search_result_of_playlist_{keywords}'
        for item in data:
            id = item.get('id')
            loved = False
            name = item.get('name')
            ar = item.get('ar')
            singer = ''
            for item_2 in ar:
                singer = singer + item_2.get('name') + '/'
            singer = singer[:-1]
            album = item.get('al').get('name')
            if id in self.api.likelist_ids:
                loved = True
            new_song = {"name": name, "id": id, "singer": singer, "album": album, "loved":loved}
            playlist.append(new_song)
            widget = SongItemWidget(self, self.cache, name, singer, album, id, index, self.api, loved, cachename)
            layout.addWidget(widget)
            index = index + 1
        self.cache[f'search_result_of_playlist_{keywords}'] = playlist

    def fill_home(self): # 多线程填充开始页面
        api_thread_top_song = RequestApi_multithread(self.api.get_top_song, type = 0)
        api_thread_top_song.requested.connect(partial(self.fill_top_song, api_thread_top_song))
        api_thread_top_song.start()

        api_thread_recommend_resource = RequestApi_multithread(self.api.get_recommend_resource)
        api_thread_recommend_resource.requested.connect(partial(self.fill_recommend_resource, api_thread_recommend_resource))
        api_thread_recommend_resource.start()

        api_thread_toplist = RequestApi_multithread(self.api.get_toplist)
        api_thread_toplist.requested.connect(partial(self.fill_toplist, api_thread_toplist))
        api_thread_toplist.start()

        api_thread_personalized = RequestApi_multithread(self.api.get_personalized)
        api_thread_personalized.requested.connect(partial(self.fill_personalized, api_thread_personalized))
        api_thread_personalized.start()

        api_thread_top_playlists = RequestApi_multithread(self.api.get_top_playlists)
        api_thread_top_playlists.requested.connect(partial(self.fill_top_playlists, api_thread_top_playlists))
        api_thread_top_playlists.start()

        api_thread = RequestApi_multithread(self.api.login_status)
        api_thread.requested.connect(partial(self.get_login_info, api_thread))
        api_thread.start()




    def fill_lyric(self, api_thread, data): # 填充播放器页面的歌词(多线程使用)
        api_thread.quit()
        # 清理旧部件
        while self.ui.verticalLayout_lyric.count():
            item = self.ui.verticalLayout_lyric.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()
        # data = self.api.get_lyric(self.musicPlayer.song_id)
        time_sequence, lyrics_sequence = split_lyrics(data)
        time_sequence_offset = time_sequence[1:]
        time_sequence_offset.append(self.musicPlayer.duration/1000)
        for time, lyrics, endTime in zip(time_sequence, lyrics_sequence, time_sequence_offset):
            # print(f"{time}s: {lyrics}")
            lyric = lyricItem(lyrics, time, endTime, self.musicPlayer.player)
            self.ui.verticalLayout_lyric.addWidget(lyric)
            lyric.clicked.connect(partial(self.updatePosition_2, lyric.time))

    def get_login_info(self, api_thread, data): # 储存用户信息
        api_thread.quit()
        self.cache['login_info'] = data
        self.uid = data.get('account').get('id')
        self.api.uid = self.uid
        api_thread = RequestApi_multithread(self.api.get_user_playlist_devided, self.uid)
        api_thread.requested.connect(partial(self.on_requested_get_my_playlists, api_thread))
        api_thread.start()
        api_thread = RequestApi_multithread(self.api.get_likelist, self.uid)
        api_thread.requested.connect(partial(self.api.refresh_likelist, api_thread))
        api_thread.start()
        # print(self.uid)
# ------------------------------槽函数定义--------------------------------------
    def the_myInfo_button_was_clicked(self): # 单击按钮后显示用户信息（待完善）
        self.previous_page.clear()
        data = self.cache['login_info']
        self.ui.label_userName.setText(data.get('profile').get('nickname'))
        self.uid = data.get('account').get('id')
        setPixmap_multithread(self.ui.label_userPic, data.get('profile').get('avatarUrl'), self.cache_folder + '/images')
        self.ui.label_userPic.setScaledContents(True) # 自动调整图片大小
        self.ui.mainStackedWidget.setCurrentWidget(self.ui.myinfo)


    def on_requested_get_my_playlists(self, api_thread, data):
        api_thread.quit()
        self.cache['my_created_playlist'] = data[0]
        self.cache['my_loved_playlist'] = data[1]
        for i in range(0, 6):
            coverImgUrl = data[0][i]['coverImgUrl']
            name = data[0][i]['name']
            item = HomeItemQToolButton(name, coverImgUrl, 6, i, self.ui.horizontalLayout_my_created_playlist, self, self.ui.myinfo)
        more_item_1 = MoreHomeItemQToolButton(self.more_icon, data[0], 6, self.ui.horizontalLayout_my_created_playlist, self, self.ui.myinfo)

        for i in range(0, 6):
            coverImgUrl = data[1][i]['coverImgUrl']
            name = data[1][i]['name']
            item = HomeItemQToolButton(name, coverImgUrl, 7, i, self.ui.horizontalLayout_my_loved_playlist, self, self.ui.myinfo)
        more_item_2 = MoreHomeItemQToolButton(self.more_icon, data[1], 7, self.ui.horizontalLayout_my_loved_playlist, self, self.ui.myinfo)


    def the_frontpage_pushButton_was_clicked(self):
        self.previous_page.clear()
        self.ui.mainStackedWidget.setCurrentWidget(self.ui.main)

    def the_delete_Cookie_PushButton_was_clicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_login)

    def the_captcha_Sent_PushButton_was_clicked(self):
        self.api.captcha_sent(self.ui.phone_Number_by_captcha.text())

    def the_captcha_Verify_PushButton_was_clicked(self):
        if self.api.login_cellphone(self.ui.phone_Number_by_captcha.text(),self.ui.phone_Captcha.text() ):
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            self.fill_home() # 填充首页
            self.init_ui()

    def the_pause_bottom_bar_pushButton_was_clicked(self):
        self.musicPlayer.toggle_playback()

    def the_pushButton_back_in_playlist_was_clicked(self):
        self.ui.mainStackedWidget.setCurrentWidget(self.previous_page.pop())

    def the_pushButton_return_to_home_in_page_home_more_item_was_clicked(self):
        self.ui.mainStackedWidget.setCurrentWidget(self.previous_page.pop())

    def the_previous_music_bottom_bar_pushButton_was_clicked(self):
        self.musicPlayer.play_previous()


    def the_next_music_bottom_bar_pushButton_was_clicked(self):
        self.musicPlayer.play_next()

    def handle_MediaStatus_Changed(self, status): # 切换歌曲
        if status == QMediaPlayer.LoadedMedia:
            # 资源加载完成，可以更新界面等操作
            refresh_thread = threading.Thread(target=refresh_song_detail, args=(self.musicPlayer.song_id, self.api, self.musicPlayer, self.ui, (self.lovedmusic, self.lovemusic)))
            refresh_thread.start() # 调用start方法，启动新的线程
            # self.fill_lyric() # 填充歌词
            api_thread = RequestApi_multithread(self.api.get_lyric, id = f'{self.musicPlayer.song_id}')
            api_thread.requested.connect(partial(self.fill_lyric, api_thread))
            api_thread.start()
            # self.ui.label_playing_singer_name.setText()
        # elif status == QMediaPlayer.InvalidMedia:
        #     # 加载的媒体无效，可能是因为文件不存在或格式不支持
        #     print("Invalid media. Check the file path or format.")
        # # 其他状态...
        return

    def handleStateChanged(self, status):
        # state 是 QMediaPlayer 的状态枚举值，可以通过 QMediaPlayer 的文档查看不同状态的含义
        if status == QMediaPlayer.PlayingState:
            self.ui.pause_pushButton_in_playerpage.setIcon(self.pause_icon)
            self.ui.pause_bottom_bar_pushButton.setIcon(self.pause_icon)
        elif status == QMediaPlayer.PausedState:
            self.ui.pause_pushButton_in_playerpage.setIcon(self.play_icon)
            self.ui.pause_bottom_bar_pushButton.setIcon(self.play_icon)
        elif status == QMediaPlayer.StoppedState:
            self.ui.pause_pushButton_in_playerpage.setIcon(self.play_icon)
            self.ui.pause_bottom_bar_pushButton.setIcon(self.play_icon)

    def the_search_pushButton_was_clicked(self):
        self.previous_page.clear()
        self.ui.mainStackedWidget.setCurrentWidget(self.ui.page_search_song)

    def the_pushButton_confirm_to_search_song_was_clicked(self): # 搜索歌曲页面的搜索键
        keywords = self.ui.lineEdit_search_song.text()
        api_thread = RequestApi_multithread(self.api.get_search_result, keywords)
        api_thread.requested.connect(partial(self.on_requested_the_pushButton_confirm_to_search_song_was_clicked, keywords, api_thread))
        api_thread.start()

    def on_requested_the_pushButton_confirm_to_search_song_was_clicked(self, keywords, api_thread, data):
        api_thread.quit()
        layout = self.ui.verticalLayout_search_song_contents
        # Clear the layout and delete the widgets
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        if data == None:
            pass
        else:
            self.cache[f'search_result_of_{keywords}_song'] = data.get('songs')
            self.fill_search_song_result(layout, keywords + '_song')

    def the_pushButton_confirm_to_search_album_was_clicked(self): # 搜索专辑按键
        keywords = self.ui.lineEdit_search_album.text()
        api_thread = RequestApi_multithread(self.api.get_search_result, keywords, '10')
        api_thread.requested.connect(partial(self.on_requested_the_pushButton_confirm_to_search_album_was_clicked, keywords, api_thread))
        api_thread.start()

    def on_requested_the_pushButton_confirm_to_search_album_was_clicked(self, keywords, api_thread, data):
        api_thread.quit()
        # self.ui.scrollarea_tab_album
        self.ui.scrollarea_tab_album.clean() # 清理重复调用的搜索结果
        data = data.get('albums')
        for i in range(0, len(data)):
            #album_info = data[i]['album']
            picUrl = data[i]['picUrl']
            album_name = data[i]['name']
            #print(f"{playlist_name}, {coverImgUrl}")
            item = HomeItemQToolButton(album_name, picUrl, 100, i, None, self, self.ui.page_search_song, data[i]['id'])
            self.ui.scrollarea_tab_album.addWidget(item)

    def the_pushButton_confirm_to_search_playlists_was_clicked(self):
        keywords = self.ui.lineEdit_search_playlists.text()
        api_thread = RequestApi_multithread(self.api.get_search_result, keywords, '1000')
        api_thread.requested.connect(partial(self.on_requested_the_pushButton_confirm_to_search_playlist_was_clicked, keywords, api_thread))
        api_thread.start()

    def on_requested_the_pushButton_confirm_to_search_playlist_was_clicked(self, keywords, api_thread, data):
        api_thread.quit()
        # self.ui.scrollarea_tab_playlists
        self.ui.scrollarea_tab_playlists.clean() # 清理重复调用的搜索结果
        data = data.get('playlists')
        for i in range(0, len(data)):
            #album_info = data[i]['album']
            coverImgUrl = data[i]['coverImgUrl']
            playlist_name = data[i]['name']
            #print(f"{playlist_name}, {coverImgUrl}")
            item = HomeItemQToolButton(playlist_name, coverImgUrl, 101, i, None, self, self.ui.page_search_song, data[i]['id'])
            self.ui.scrollarea_tab_playlists.addWidget(item)

    def the_pushButton_confirm_to_search_singer_was_clicked(self):
        print('clicked')

    def the_pushButton_player_return_to_main_was_clicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)

    def the_pushButton_music_play_was_clicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_player)

    def the_pushButton_set_volume_was_clicked(self, pushButton): # 创建滑块调节音量大小
        menu = QMenu(self)
        # 创建滑块
        volume_slider = QSlider(Qt.Horizontal)
        volume_slider.setRange(0, 100)  # 设置范围
        volume_slider.setValue(self.musicPlayer.volume*100)      # 设置默认值
        label_volume_value = QLabel(f'{int(self.musicPlayer.volume*100)}')
        # 将滑块的数值改变信号连接到自定义的槽函数
        volume_slider.valueChanged.connect(partial(self.sliderValueChanged, label_volume_value))
        # 在水平布局中添加滑块
        layout = QHBoxLayout()
        layout.addWidget(volume_slider)
        layout.addWidget(label_volume_value)
        # 创建 QWidget 用于承载布局
        widget = QWidget()
        widget.setLayout(layout)
        # 将 QSlider 添加到菜单
        widget_action = QWidgetAction(self)
        widget_action.setDefaultWidget(widget)
        menu.addAction(widget_action)
        # 创建 QAction，并将 QWidgetAction 设置为其部件
        action = menu.addAction("音量")
        action.setMenu(menu)
        # 设置自定义部件
        menu.setActiveAction(action)
        menu.setFixedWidth(widget.width())  # 设置菜单宽度，以防部件不显示
        menu.exec(pushButton.mapToGlobal(pushButton.rect().bottomLeft()))

    def sliderValueChanged(self, label, value):
        label.setText(f'{value}')
        self.musicPlayer.set_volume(value)

    def positionChanged(self, position):
        if position % 1000 <= 50:
            s = int(position/1000) + 1
            text = f'{s // 60}:{s % 60}'
            self.ui.label_time_now_in_playerpage.setText(text) # 更新播放页面时间标签
            self.ui.label_time_in_bottom_bar.setText(text) # 更新下边栏时间标签
            self.musicPlayer.position = position # 更新播放器标识位
            self.ui.horizontalSlider_time_in_bottom_bar.setValue(position/self.musicPlayer.duration*100) # 更新下边栏进度条
            self.ui.horizontalSlider_music_progress_in_playerpage.setValue(position/self.musicPlayer.duration*100) # 更新播放页面进度条

    def durationChanged(self, duration): # 更新进度条旁边歌曲总时间标签
        s = int(duration/1000) + 1
        text = f'{s // 60}:{s % 60}'
        self.ui.label_time_all_in_playerpage.setText(text)
        self.ui.label_full_time_in_bottom_bar.setText(text)
        self.musicPlayer.duration = duration

    def updatePosition(self, value): # 拖动进度条改变播放进度
        position = value * self.musicPlayer.duration / 100
        self.musicPlayer.position = position
        self.musicPlayer.player.setPosition(int(position))

    def updatePosition_2(self, value): # 单击歌词切换播放进度
        position = int(value * 1000)
        self.musicPlayer.position = position
        self.musicPlayer.player.setPosition(position)
        if not self.musicPlayer.playing: # 如果处于暂停状态则开始播放
            self.musicPlayer.start_play()
        return

    def toggle_window(self):
            # 切换窗口的显示和隐藏状态
            if self.isVisible():
                self.hide()
            else:
                self.show()

    def show_window(self):
        # 恢复窗口显示
        self.show()

    def on_the_pushButton_menu_in_bottom_bar_was_clicked(self):
        song_menu = QMenu(self)
        fav_action = song_menu.addAction('收藏到歌单')
        love_action = song_menu.addAction('加入到我喜欢')
        goto_album_action = song_menu.addAction('查看专辑')
        goto_singer_action = song_menu.addAction('查看作者')
        goto_comment_action = song_menu.addAction('查看评论')
        goto_MV_action = song_menu.addAction('查看MV')

        # 将菜单显示在按钮的上方
        button_pos = self.ui.pushButton_menu_in_bottom_bar.mapToGlobal(self.ui.pushButton_menu_in_bottom_bar.pos())
        song_menu.exec(button_pos)

    def on_the_pushButton_play_sequence_was_clicked(self): # 播放顺序切换按钮
        if self.musicPlayer.play_sequence == 0:
            self.musicPlayer.setPlaysequence(1)
            self.ui.pushButton_play_sequence_in_bottom_bar.setIcon(self.suijibofang_icon)
            self.ui.pushButton_play_sequence_in_playerpage.setIcon(self.suijibofang_icon)
        elif self.musicPlayer.play_sequence == 1:
            self.musicPlayer.setPlaysequence(2)
            self.ui.pushButton_play_sequence_in_bottom_bar.setIcon(self.danquxunhuan_icon)
            self.ui.pushButton_play_sequence_in_playerpage.setIcon(self.danquxunhuan_icon)
        elif self.musicPlayer.play_sequence == 2:
            self.musicPlayer.setPlaysequence(0)
            self.ui.pushButton_play_sequence_in_bottom_bar.setIcon(self.gedanxunhuan_icon)
            self.ui.pushButton_play_sequence_in_playerpage.setIcon(self.gedanxunhuan_icon)

    def on_the_favor_music_was_clicked(self): # 收藏歌曲按钮
        if self.musicPlayer.playing:
            if self.musicPlayer.loved_status:
                if self.api.like_song(self.musicPlayer.song_id, 'false'):
                    self.ui.favor_music_bottom_bar_pushButton.setIcon(self.lovemusic)
                    self.ui.favor_music_pushButton_in_playerpage.setIcon(self.lovemusic)
                    self.musicPlayer.loved_status = False
            else:
                if self.api.like_song(self.musicPlayer.song_id, 'true'):
                    self.ui.favor_music_bottom_bar_pushButton.setIcon(self.lovedmusic)
                    self.ui.favor_music_pushButton_in_playerpage.setIcon(self.lovedmusic)
                    self.musicPlayer.loved_status = True
# -------------------------------------------------------------------------
