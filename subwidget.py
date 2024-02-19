from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QSpacerItem, QSizePolicy, QToolButton, QScrollArea
from PySide6.QtCore import Signal, Qt, QSize, QThreadPool
from PySide6.QtGui import QPainter, QTextOption, QResizeEvent
from functools import partial
from Utils import RequestApi_multithread, LoadImageTask

class CustomScrollArea(QScrollArea):
    widgetAdded = Signal()

    def __init__(self, parent=None):
        super(CustomScrollArea, self).__init__(parent)

        self.scrollContent = QWidget(self)
        self.scrollContent.setGeometry(0, 0, 0, 0)

        self.scrollLayout = QVBoxLayout(self.scrollContent)
        self.scrollLayout.setAlignment(Qt.AlignTop)

        self.setWidgetResizable(True)
        self.setWidget(self.scrollContent)

        self.widgets = []
        self.updateLayout()

    def addWidget(self, widget):
        self.widgets.append(widget)
        self.scrollLayout.addWidget(widget)
        self.updateLayout()
        self.widgetAdded.emit()
        return

    def updateLayout(self):
        # 获取可用的宽度，减去垂直滚动条的宽度
        content_width = self.width() - self.verticalScrollBar().width()

        # 计算当前行的宽度和当前行的 widget 列表
        row_width = 0
        row_widgets = []

        # 额外的间距，用于在 widget 之间添加更多的空间
        extra_spacing = 10

        for widget in self.widgets:
            widget_width = widget.width()

            # 如果当前行加上当前 widget 的宽度超过了可用宽度
            if row_width + widget_width + extra_spacing > content_width:
                # 将当前行的 widget 添加到布局中
                row_layout = self.createRowLayout(row_widgets)
                self.scrollLayout.addLayout(row_layout)

                # 添加spacer以均匀分布widget
                spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
                row_layout.addItem(spacer)

                row_width = 0  # 重置当前行的宽度
                row_widgets = []  # 重置当前行的 widget 列表

            row_widgets.append(widget)
            row_width += widget_width + extra_spacing  # 添加额外的间距

        if row_widgets:
            row_layout = self.createRowLayout(row_widgets)
            self.scrollLayout.addLayout(row_layout)

            # 添加spacer以均匀分布widget
            spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
            row_layout.addItem(spacer)

    def createRowLayout(self, widgets):
        layout = QHBoxLayout()
        layout.addWidget(widgets[0])
        for widget in widgets[1:]:
            layout.addSpacing(5)
            layout.addWidget(widget)
        return layout

    def clean(self):
        for widget in self.widgets:
            widget.setParent(None)
            widget.deleteLater()
        self.widgets = []
        self.scrollLayout.update()
        return

    def resizeEvent(self, event: QResizeEvent):
        super(CustomScrollArea, self).resizeEvent(event)
        self.updateLayout()


class MoreHomeItemQToolButton(QToolButton):
    # 定义一个名为 created 的信号
    created = Signal()
    def __init__(self, icon, data, category, layout, widget, previous_page, parent=None):
        super(MoreHomeItemQToolButton, self).__init__(parent)
        self.setMinimumSize(120, 150)
        self.setMaximumSize(120, 150)
        self.widget = widget
        self.icon = icon
        self.data = data
        self.layout = layout
        self.previous_page = previous_page
        self.setText('更多')
        self.setStyleSheet("border: 0px;")
        self.setIconSize(QSize(120, 120))
        # 设置文本和图标的显示位置
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.setContentsMargins(0, 0, 0, 0)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setAutoRaise(True)

        layout.addWidget(self)
        self.clicked.connect(partial(self.on_select_toolbotton_clicked, category))
        self.created.connect(self.on_created)
        layout.addWidget(self)
        # 在初始化完成后发出 created 信号
        self.created.emit()

    def on_created(self):
        self.setIcon(self.icon)
        return

    def on_select_toolbotton_clicked(self, category , playlist_name=''):
        if category == 1:
            # 清理旧部件
            while self.widget.ui.verticalLayout_playlist.count():
                item = self.widget.ui.verticalLayout_playlist.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
            self.widget.ui.label_in_playlist.setText('新歌速递')
            self.widget.ui.mainStackedWidget.setCurrentWidget(self.widget.ui.music_playlist)
            self.widget.previous_page.append(self.previous_page)
            playlist = []
            index = 0
            cachename = 'top_song_playlist'
            for item in self.data:
                id = item.get('id')
                loved = False
                name = item.get('name')
                ar = item.get('artists')
                singer = ''
                for item_2 in ar:
                    singer = singer + item_2.get('name') + '/'
                singer = singer[:-1]
                album = item.get('album').get('name')
                if id in self.widget.api.likelist_ids:
                    loved = True
                new_song = {"name": name, "id": id, "singer": singer, "album": album, "loved":loved}
                playlist.append(new_song)
                widget = SongItemWidget(self.widget, self.widget.cache, name, singer, album, id, index, self.widget.api, loved, cachename)
                self.widget.ui.verticalLayout_playlist.addWidget(widget)
                index = index + 1
            self.widget.cache[cachename] = playlist

        elif category == 2:
            self.widget.ui.mainStackedWidget.setCurrentWidget(self.widget.ui.page_home_more_item)
            self.widget.ui.label_in_page_home_more_item.setText('热门歌单')
            self.widget.previous_page.append(self.previous_page)
            self.widget.ui.scrollarea_more_item.clean() # 清理已经添加的歌单
            for i in range(0, len(self.data)):
                #album_info = data[i]['album']
                coverImgUrl = self.data[i]['coverImgUrl']
                playlist_name = self.data[i]['name']
                #print(f"{playlist_name}, {coverImgUrl}")
                item = HomeItemQToolButton(playlist_name, coverImgUrl, 2, i, None, self.widget, self.widget.ui.page_home_more_item)
                self.widget.ui.scrollarea_more_item.addWidget(item)

        elif category == 3:
            self.widget.ui.mainStackedWidget.setCurrentWidget(self.widget.ui.page_home_more_item)
            self.widget.ui.label_in_page_home_more_item.setText('推荐歌单')
            self.widget.previous_page.append(self.previous_page)
            self.widget.ui.scrollarea_more_item.clean() # 清理已经添加的歌单
            for i in range(0, len(self.data)):
                #album_info = data[i]['album']
                coverImgUrl = self.data[i]['picUrl']
                playlist_name = self.data[i]['name']
                #print(f"{playlist_name}, {coverImgUrl}")
                item = HomeItemQToolButton(playlist_name, coverImgUrl, 3, i, None, self.widget, self.widget.ui.page_home_more_item)
                self.widget.ui.scrollarea_more_item.addWidget(item)

        elif category == 4:
            self.widget.ui.mainStackedWidget.setCurrentWidget(self.widget.ui.page_home_more_item)
            self.widget.ui.label_in_page_home_more_item.setText('私人推荐')
            self.widget.previous_page.append(self.previous_page)
            self.widget.ui.scrollarea_more_item.clean() # 清理已经添加的歌单
            for i in range(0, len(self.data)):
                #album_info = data[i]['album']
                coverImgUrl = self.data[i]['picUrl']
                playlist_name = self.data[i]['name']
                #print(f"{playlist_name}, {coverImgUrl}")
                # self.create_select_toolbotton(playlist_name, coverImgUrl, 4, i, self.ui.horizontalLayout_recommend_resource)
                item = HomeItemQToolButton(playlist_name, coverImgUrl, 4, i, None, self.widget, self.widget.ui.page_home_more_item)
                self.widget.ui.scrollarea_more_item.addWidget(item)

        elif category == 5:
            self.widget.ui.mainStackedWidget.setCurrentWidget(self.widget.ui.page_home_more_item)
            self.widget.ui.label_in_page_home_more_item.setText('排行榜')
            self.widget.previous_page.append(self.previous_page)
            self.widget.ui.scrollarea_more_item.clean() # 清理已经添加的歌单
            for i in range(0, len(self.data)):
                #album_info = data[i]['album']
                coverImgUrl = self.data[i]['coverImgUrl']
                playlist_name = self.data[i]['name']
                #print(f"{playlist_name}, {coverImgUrl}")
                item = HomeItemQToolButton(playlist_name, coverImgUrl, 5, i, None, self.widget, self.widget.ui.page_home_more_item)
                self.widget.ui.scrollarea_more_item.addWidget(item)

        elif category == 6:
            self.widget.ui.mainStackedWidget.setCurrentWidget(self.widget.ui.page_home_more_item)
            self.widget.previous_page.append(self.widget.ui.myinfo)
            self.widget.ui.label_in_page_home_more_item.setText('我创建的歌单')
            self.widget.previous_page.append(self.previous_page)
            self.widget.ui.scrollarea_more_item.clean() # 清理已经添加的歌单
            for i in range(0, len(self.data)):
                #album_info = data[i]['album']
                coverImgUrl = self.data[i]['coverImgUrl']
                playlist_name = self.data[i]['name']
                #print(f"{playlist_name}, {coverImgUrl}")
                item = HomeItemQToolButton(playlist_name, coverImgUrl, 6, i, None, self.widget, self.widget.ui.page_home_more_item)
                self.widget.ui.scrollarea_more_item.addWidget(item)

        elif category == 7:
            self.widget.ui.mainStackedWidget.setCurrentWidget(self.widget.ui.page_home_more_item)
            self.widget.previous_page.append(self.widget.ui.myinfo)
            self.widget.ui.label_in_page_home_more_item.setText('我收藏的歌单')
            self.widget.previous_page.append(self.previous_page)
            self.widget.ui.scrollarea_more_item.clean() # 清理已经添加的歌单
            for i in range(0, len(self.data)):
                #album_info = data[i]['album']
                coverImgUrl = self.data[i]['coverImgUrl']
                playlist_name = self.data[i]['name']
                #print(f"{playlist_name}, {coverImgUrl}")
                item = HomeItemQToolButton(playlist_name, coverImgUrl, 7, i, None, self.widget, self.widget.ui.page_home_more_item)
                self.widget.ui.scrollarea_more_item.addWidget(item)




class HomeItemQToolButton(QToolButton):
    # 定义一个名为 created 的信号
    created = Signal()
    def __init__(self, name, pic_url, category, index, layout, widget, previous_page, id=None, parent=None):
        super(HomeItemQToolButton, self).__init__(parent)
        self.setMinimumSize(120, 150)
        self.setMaximumSize(120, 150)
        self.id = id # 作为搜索专辑或歌手或歌单项目时专用
        self.index = index
        self.iconURL = pic_url
        self.previous_page = previous_page
        self.task = LoadImageTask(self, self.iconURL, widget.cache_folder)
        self.category = category
        self.setText(name)
        self.widget = widget
        self.setStyleSheet("border: 0px;")
        self.setIconSize(QSize(120, 120))
        # 设置文本和图标的显示位置
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.setContentsMargins(0, 0, 0, 0)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setAutoRaise(True)
        # 设置 QToolButton css样式表（不会）
        # self.setStyleSheet("""
        #             QToolButton {
        #                 background-color: #3498db;
        #                 border: 2px solid #2980b9;
        #                 color: #ecf0f1;
        #                 font-size: 16px;
        #                 padding: 10px;
        #             }

        #             QToolButton:hover {
        #                 background-color: #2980b9;
        #             }

        #             QToolButton:pressed {
        #                 background-color: #21618c;
        #                 border: 2px solid #1a5276;
        #             }
        #         """)
        self.clicked.connect(partial(self.on_select_toolbotton_clicked, category, self.index, name))
        self.created.connect(self.on_created)
        if layout:
            layout.addWidget(self)
        # 在初始化完成后发出 created 信号
        self.created.emit()

    def on_created(self):
        # icon = get_image(self.iconURL, self.widget.cache_folder + '/image')
        QThreadPool.globalInstance().start(self.task) # 开始运行setIcon的task
        # self.setIcon(icon)
        return

    def on_select_toolbotton_clicked(self, category, index, playlist_name=''):
        # print(category)
        #top_song category = 1
        if category == 1 :
            data = self.widget.cache['top_song_cache']
            id = data[index].get('id')
            name = data[index].get('name')
            self.widget.musicPlayer.playmusic_byID(id, name)
        #top_lists category = 2
        elif category == 2 :
            self.widget.previous_page.append(self.previous_page)
            data = self.widget.cache['top_lists_cache']
            id = data[index]['id']
            # self.api.playlist_track_all(id)
            self.widget.fill_playlist(playlist_name, id)
            self.widget.ui.mainStackedWidget.setCurrentWidget(self.widget.ui.music_playlist)
        elif category == 3 :
            self.widget.previous_page.append(self.previous_page)
            data = self.widget.cache['personalized_cache']
            id = data[index]['id']
            self.widget.fill_playlist(playlist_name, id)
            self.widget.ui.mainStackedWidget.setCurrentWidget(self.widget.ui.music_playlist)
        elif category == 4 :
            self.widget.previous_page.append(self.previous_page)
            data = self.widget.cache['recommend_resource_cache']
            id = data[index]['id']
            self.widget.fill_playlist(playlist_name, id)
            self.widget.ui.mainStackedWidget.setCurrentWidget(self.widget.ui.music_playlist);
        elif category == 5 :
            self.widget.previous_page.append(self.previous_page)
            data = self.widget.cache['toplist_cache']
            id = data[index]['id']
            self.widget.fill_playlist(playlist_name, id)
            self.widget.ui.mainStackedWidget.setCurrentWidget(self.widget.ui.music_playlist)
        elif category == 6 :
            self.widget.previous_page.append(self.previous_page)
            data = self.widget.cache['my_created_playlist']
            id = data[index]['id']
            # self.api.playlist_track_all(id)
            self.widget.fill_playlist(playlist_name, id)
            self.widget.ui.mainStackedWidget.setCurrentWidget(self.widget.ui.music_playlist)
        elif category == 7 :
            self.widget.previous_page.append(self.previous_page)
            data = self.widget.cache['my_loved_playlist']
            id = data[index]['id']
            # self.api.playlist_track_all(id)
            self.widget.fill_playlist(playlist_name, id)
            self.widget.ui.mainStackedWidget.setCurrentWidget(self.widget.ui.music_playlist)
        elif category == 100 : # 搜索专辑的页面使用
            self.widget.previous_page.append(self.previous_page)
            self.widget.ui.label_in_playlist.setText('加载中')
            # 清理旧部件
            while self.widget.ui.verticalLayout_playlist.count():
                item = self.widget.ui.verticalLayout_playlist.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()
            self.widget.ui.mainStackedWidget.setCurrentWidget(self.widget.ui.music_playlist)
            api_thread = RequestApi_multithread(self.widget.api.get_album, self.id)
            api_thread.requested.connect(partial(self.on_requested_fill_playlist, api_thread))
            api_thread.start()
            # data = self.widget.api.get_album(self.id)
        elif category == 101:
            self.widget.previous_page.append(self.previous_page)
            self.widget.ui.mainStackedWidget.setCurrentWidget(self.widget.ui.music_playlist)
            self.widget.fill_playlist(playlist_name, self.id)
        return

    def on_requested_fill_playlist(self, api_thread, data):
        api_thread.quit()
        songs = data.get('songs')
        self.widget.ui.label_in_playlist.setText(songs[0].get('al').get('name'))
        self.widget.ui.mainStackedWidget.setCurrentWidget(self.widget.ui.music_playlist)
        self.widget.previous_page.append(self.widget.ui.page_search_song)
        playlist = []
        index = 0
        cachename = f'album_song_{self.id}'
        for item in songs:
            id = item.get('id')
            loved = False
            name = item.get('name')
            ar = item.get('ar')
            singer = ''
            for item_2 in ar:
                singer = singer + item_2.get('name') + '/'
            singer = singer[:-1]
            album = item.get('al').get('name')
            if id in self.widget.api.likelist_ids:
                loved = True
            new_song = {"name": name, "id": id, "singer": singer, "album": album, "loved":loved}
            playlist.append(new_song)
            widget = SongItemWidget(self.widget, self.widget.cache, name, singer, album, id, index, self.widget.api, loved, cachename)
            self.widget.ui.verticalLayout_playlist.addWidget(widget)
            index = index + 1
        spacer_item = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.widget.ui.verticalLayout_playlist.addSpacerItem(spacer_item)
        self.widget.cache[cachename] = playlist
        return


class SongItemWidget(QWidget):
    def __init__(self, widget, diskcache, music_name, singer_name, album_name, music_id, music_index, api, loved_status=0, cachename='', playlist_id='', parent=None):
        super(SongItemWidget, self).__init__(parent)
        self.musicPlayer = widget.musicPlayer
        self.widget = widget
        self.music_id = music_id
        self.cache = diskcache
        self.api = api
        self.index = music_index
        self.loved_status = loved_status
        self.playlist_id = playlist_id
        self.cachename = cachename
        self.button_play = QPushButton('', self)
        self.button_play.setFixedSize(30,30)
        self.button_play.setIcon(self.widget.play_icon)
        self.button_play.setIconSize(self.button_play.size())
        # self.button_play.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: none;")
        self.index_label = QLabel(str(self.index + 1), self)
        self.index_label.setFixedSize(20,20)
        self.label_music_name = QLabel(music_name, self)
        self.label_singer_name = QLabel(singer_name, self) # singername
        self.label_album_name = QLabel(album_name, self) # albumname
        self.horizontal_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.layout_label_singer_name_album_name = QHBoxLayout()
        self.layout_label_singer_name_album_name.addWidget(self.label_singer_name)
        self.layout_label_singer_name_album_name.addWidget(self.label_album_name)
        self.layout_label_singer_name_album_name.addSpacerItem(self.horizontal_spacer)
        self.layout_music_name_singer_album = QVBoxLayout()
        self.layout_music_name_singer_album.addWidget(self.label_music_name)
        self.layout_music_name_singer_album.addLayout(self.layout_label_singer_name_album_name)
        self.button_love = QPushButton('', self)
        self.button_love.setFixedSize(30,30)
        self.button_love.setIconSize(self.button_love.size())
        # self.button_love.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: none;")
        if not loved_status:
            self.button_love.setIcon(self.widget.lovemusic)
        else :
            self.button_love.setIcon(self.widget.lovedmusic)
        self.button_menu = QPushButton('', self)
        self.button_menu.setFixedSize(30,30)
        self.button_menu.setIconSize(self.button_love.size())
        self.button_menu.setIcon(self.widget.menu_icon)
        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.index_label)
        self.layout.addWidget(self.button_play)
        self.layout.addLayout(self.layout_music_name_singer_album)
        self.layout.addWidget(self.button_love)
        self.layout.addWidget(self.button_menu)
        self.button_love.clicked.connect(self.on_button_love_clicked)
        self.button_play.clicked.connect(self.on_button_play_clicked)

    def on_button_play_clicked(self):
        if self.cachename:
            self.musicPlayer.setPlaylist_search_song(self.cachename)
            self.musicPlayer.playmusic_byIndex(self.index)
        elif self.playlist_id:
            self.musicPlayer.setPlaylist(self.playlist_id)
            self.musicPlayer.playmusic_byIndex(self.index)

    def on_button_love_clicked(self):
        if self.loved_status:
            if self.api.like_song(self.music_id, 'false'):
                self.button_love.setIcon(self.widget.lovemusic)
                self.loved_status = False
        else:
            if self.api.like_song(self.music_id, 'true'):
                self.button_love.setIcon(self.widget.lovedmusic)
                self.loved_status = True

class lyricItem(QPushButton):
    def __init__(self, text, time, endTime, player, parent = None):
        super(lyricItem, self).__init__(parent)
        # self.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: none;")
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: none;;font-weight: None; color: None;")
        self.setText(text)
        # self.setMaximumWidth(400)
        # self.setWordWrap(True)
        self.time = time
        self.endTime = endTime
        self.player = player
        player.positionChanged.connect(self.positionChanged)

    # def paintEvent(self, event):
    #         painter = QPainter(self)
    #         painter.setRenderHint(QPainter.Antialiasing)

    #         option = QTextOption()
    #         option.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
    #         option.setWrapMode(QTextOption.WrapAtWordBoundaryOrAnywhere)

    #         # 设置按钮的宽度，如果按钮的宽度小于文本的宽度，则自动换行
    #         button_width = 400

    #         # 获取文本的绘制矩形
    #         text_rect = painter.boundingRect(self.rect(), Qt.AlignLeft, self.text())

    #         # 计算自动换行后的文本绘制矩形，只在 x 方向进行平移
    #         wrapped_text_rect = text_rect.translated(0, 0)
    #         wrapped_text_rect.setWidth(button_width)

    #         # 绘制自动换行的文本
    #         painter.drawText(wrapped_text_rect, self.text(), option)

    def bold(self):
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: none;;font-weight: bold; color: Blue;")

    def default(self):
        self.setStyleSheet("background-color: rgba(0, 0, 0, 0); border: none;;font-weight: None; color: White;")

    def positionChanged(self, value):
        if value % 1000 <= 50:
            if self.player.position()/1000>=self.time and self.player.position()/1000<=self.endTime :
                self.bold()
            else :
                self.default()
        else :
            return
