import json
import os
from pprint import pprint
import requests
import diskcache
from functools import partial
from NeteaseCloudMusic import NeteaseCloudMusicApi, api_help, api_list

from Utils import RequestApi_multithread, get_image

class NTCMAPI:
    def __init__(self, cachepath):
        self.netease_cloud_music_api = NeteaseCloudMusicApi()  # 初始化API
        self.cachepath = cachepath
        version_result = self.netease_cloud_music_api.request("inner_version")
        print(f'当前使用NeteaseCloudMusicApi版本号：{version_result["NeteaseCloudMusicApi"]}\n当前使用NeteaseCloudMusicApi_V8版本号：{version_result["NeteaseCloudMusicApi_V8"]}')  # 退出登录
        self.uid = ''
        self.likelist_ids = []

    def login_qr(self): # 获取base64登陆二维码
        key = self.netease_cloud_music_api.request("/login/qr/key")
        qr_base64 = self.netease_cloud_music_api.request("/login/qr/create", {"key": key})
        return qr_base64

    def captcha_sent(self, _phone, ctcode = '86'): # 发送登陆验证码
        # print(_phone)
        _phone = _phone.encode('utf-8').decode('latin-1')
        # print(_phone)
        response = self.netease_cloud_music_api.request("/captcha/sent", {"phone": f"{_phone}", "ctcode": ctcode})
        return response

    def login_cellphone(self, _phone, _captcha): # 验证手机号于验证码
        self.netease_cloud_music_api.cookie
        response = self.netease_cloud_music_api.request("/login/cellphone", {"phone": f"{_phone}", "captcha": f"{_captcha}"})
        if self.netease_cloud_music_api.cookie:
            print("cookie设置成功")
        return response

    def refresh_login(self): # 刷新登陆状态（不支持二维码登陆）
        response = self.netease_cloud_music_api.request("login_refresh")
        pprint(response)
        #if self.netease_cloud_music_api.cookie:
        #    print("cookie设置成功")

    def register_anonimous(self): # 获取游客登陆cookie
        response = self.netease_cloud_music_api.request("/register/anonimous")
        if self.netease_cloud_music_api.cookie:
            print("cookie设置成功")
        return response

    def login_status(self): # 获取登陆状态与账户信息
        response = self.netease_cloud_music_api.request("/login/status")
        # pprint(response)
        return response.get('data').get('data')

    def get_top_song(self,type): # 新歌速递
        response = self.netease_cloud_music_api.request("/top/song", {"type":type})
        #pprint(response)
        #print(len(response.get('data').get('data')))
        return response.get('data').get('data')

    def get_home_page(self, refresh = False, cursor = ""): # 获取首页数据(调用失败）
        response = self.netease_cloud_music_api.request("/homepage/block/page", {"refresh":refresh, "cursor":cursor})
        print(response)

    def get_top_playlists(self, order='hot', cat='全部', limit='50', offset='0'):  #获取网友精选碟
        response = self.netease_cloud_music_api.request("/top/playlist",{"order":order, "cat":cat, "limit":limit, "offset":offset})
        # pprint(len(response.get('data').get('playlists')))
        return response.get('data').get('playlists')

    def get_recommend_resource(self):  #获取每日推荐歌单(私人推荐）
        response = self.netease_cloud_music_api.request("/recommend/resource")
        #pprint(len(response.get('data').get('playlists')))
        #pprint(response)
        return response.get('data').get('recommend')

    def get_personalized(self, limit = ''): # 获取推荐歌单
        response = self.netease_cloud_music_api.request('/personalized', {'limit':limit})
        return response.get('data').get('result')

    def get_song_url(self, id, br=''): # 获取音乐Url(音乐id，码率)
        response = self.netease_cloud_music_api.request('/song/url', {'id':id, 'br':br})
        print(response)

    def get_song_url_v1(self, id, level='standard'): # 新版获取音乐Url(音乐id，码率)
        response = self.netease_cloud_music_api.request('/song/url/v1', {'id':id, 'level':level})
        return response.get('data').get('data')
        # print(response)

    def playlist_track_all(self, id, limit=1000, offset=0): # 获取歌单内全部歌曲
        response = self.netease_cloud_music_api.request('/playlist/track/all', {'id':id, 'limit':limit, 'offset':offset})
        # print(response)
        return response.get('data').get('songs')

    def get_toplist(self): # 排行榜
        response = self.netease_cloud_music_api.request('/toplist', {})
        # print(response)
        return response.get('data').get('list')

    '''type: 搜索类型；默认为 1 即单曲 , 取值意义 : 1: 单曲, 10: 专辑, 100: 歌手, 1000: 歌单, 1002: 用户, 1004: MV, 1006: 歌词, 1009: 电台, 1014: 视频, 1018:综合, 2000:声音'''
    def get_search_result(self, keywords, type = 1, limit = '', offset = 0): # 负责搜索功能
        # print(keywords)
        keywords = keywords.encode('utf-8').decode('latin-1') # 需要转换编码字符集
        response = self.netease_cloud_music_api.request('/cloudsearch', {'keywords':keywords, 'limit':limit, 'offset':offset, 'type':type})
        # print(response)
        if response.get('code') == 200:
            return response.get('data').get('result')
        else:
            return None

    def like_song(self, id, like): # 将歌曲添加进我喜欢
        response = self.netease_cloud_music_api.request('/like', {'id':f'{id}', 'like':like})
        # print(response)
        if response.get('code')==200:
            # print(self.uid)
            api_thread = RequestApi_multithread(self.get_likelist, self.uid)
            api_thread.requested.connect(partial(self.refresh_likelist, api_thread))
            api_thread.start()
            return True
        else:
            return False

    def get_likelist(self, uid): # 获取我喜欢音乐列表(返回列表歌曲的id)
        response = self.netease_cloud_music_api.request('/likelist', {'uid':uid})
        if response.get('code')==200:
            return response.get('data').get('ids')
        else:
            return None

    def get_likelist_detail(self, uid): # 获取我喜欢音乐列表(返回列表歌曲的id)
        response = self.netease_cloud_music_api.request('/likelist', {'uid':uid})
        if response.get('code')==200:
            list = response.get('data').get('ids')
            ids = ','.join(str(item) for item in list)
            return self.get_song_detail(ids) # 通过id获取歌曲信息
        else:
            return None

    def get_song_detail(self, ids):# 可批量获取歌曲信息(ids使用‘’扩起来)
        ids = f'{ids}'
        response = self.netease_cloud_music_api.request('/song/detail', {'ids':ids})
        #print(response)
        if response.get('code')==200:
            return response.get('data').get('songs')
        else:
            return None

    def user_subcount(self): # 只能获取用户收藏等数量
        response = self.netease_cloud_music_api.request('/user/subcount', {})
        if response.get('code')==200:
            return response.get('data')
        else:
            return None

    def get_user_playlist(self, uid): # 可获取用户自己创建的歌单和收藏的歌单
        response = self.netease_cloud_music_api.request('/user/playlist', {'uid':uid})
        # print(response)
        if response.get('code')==200:
            return response.get('data').get('playlist')
        else:
            return None

    def get_user_playlist_devided(self, uid): # 可获取用户自己创建的歌单和收藏的歌单(分开返回)
        countData = self.user_subcount().get('createdPlaylistCount')
        playlistData = self.get_user_playlist(uid)
        return playlistData[:countData], playlistData[countData:]

    def get_albumPic_by_id(self, id): # 返回歌曲专辑封面（和歌手姓名、专辑名称）
        response = self.get_song_detail(id)
        url = response[0].get('al').get('picUrl')
        albumName = response[0].get('al').get('name')
        ar = response[0].get('ar')
        singer = ''
        for item in ar:
            singer = singer + item.get('name') + '/'
        singer = singer[:-1]
        image = get_image(url, self.cachepath + '/image')
        return image, singer, albumName

    def get_lyric(self, id): # 获取歌曲歌词
        response = self.netease_cloud_music_api.request('/lyric', {'id':id})
        # print(response)
        if response.get('code') == 200:
            return response.get('data').get('lrc').get('lyric')
        else :
            return None

    def get_album(self, id): # 获取专辑信息
        response = self.netease_cloud_music_api.request('/album', {'id':id})
        # print(response)
        if response.get('code') == 200:
            return response.get('data')
        else :
            return None

    def refresh_likelist(self,api_thread, data):
        self.likelist_ids = data
