# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QSlider, QSpacerItem,
    QStackedWidget, QTabWidget, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(839, 594)
        Widget.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(Widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.stackedWidget = QStackedWidget(Widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.phone_Number_by_captcha = QLineEdit(self.page_login)
        self.phone_Number_by_captcha.setObjectName(u"phone_Number_by_captcha")
        self.phone_Number_by_captcha.setGeometry(QRect(200, 60, 241, 41))
        self.captcha_Sent_PushButton = QPushButton(self.page_login)
        self.captcha_Sent_PushButton.setObjectName(u"captcha_Sent_PushButton")
        self.captcha_Sent_PushButton.setGeometry(QRect(340, 130, 80, 20))
        self.phone_Captcha = QLineEdit(self.page_login)
        self.phone_Captcha.setObjectName(u"phone_Captcha")
        self.phone_Captcha.setGeometry(QRect(200, 130, 131, 31))
        self.captcha_Verify_PushButton = QPushButton(self.page_login)
        self.captcha_Verify_PushButton.setObjectName(u"captcha_Verify_PushButton")
        self.captcha_Verify_PushButton.setGeometry(QRect(250, 220, 80, 20))
        self.stackedWidget.addWidget(self.page_login)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.horizontalLayout = QHBoxLayout(self.page_home)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.bottomBarStackedWidget = QStackedWidget(self.page_home)
        self.bottomBarStackedWidget.setObjectName(u"bottomBarStackedWidget")
        self.bottomBarStackedWidget.setMinimumSize(QSize(0, 60))
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.bottomBarStackedWidget.addWidget(self.page_3)
        self.landscape_bottom_bar_page = QWidget()
        self.landscape_bottom_bar_page.setObjectName(u"landscape_bottom_bar_page")
        self.verticalLayout_18 = QVBoxLayout(self.landscape_bottom_bar_page)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_time_in_bottom_bar = QLabel(self.landscape_bottom_bar_page)
        self.label_time_in_bottom_bar.setObjectName(u"label_time_in_bottom_bar")

        self.horizontalLayout_16.addWidget(self.label_time_in_bottom_bar)

        self.horizontalSlider_time_in_bottom_bar = QSlider(self.landscape_bottom_bar_page)
        self.horizontalSlider_time_in_bottom_bar.setObjectName(u"horizontalSlider_time_in_bottom_bar")
        self.horizontalSlider_time_in_bottom_bar.setOrientation(Qt.Horizontal)

        self.horizontalLayout_16.addWidget(self.horizontalSlider_time_in_bottom_bar)

        self.label_full_time_in_bottom_bar = QLabel(self.landscape_bottom_bar_page)
        self.label_full_time_in_bottom_bar.setObjectName(u"label_full_time_in_bottom_bar")

        self.horizontalLayout_16.addWidget(self.label_full_time_in_bottom_bar)


        self.verticalLayout_18.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pushButton_music_play = QPushButton(self.landscape_bottom_bar_page)
        self.pushButton_music_play.setObjectName(u"pushButton_music_play")
        self.pushButton_music_play.setMinimumSize(QSize(40, 40))

        self.horizontalLayout_14.addWidget(self.pushButton_music_play)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_playing_music_name = QLabel(self.landscape_bottom_bar_page)
        self.label_playing_music_name.setObjectName(u"label_playing_music_name")

        self.verticalLayout_17.addWidget(self.label_playing_music_name)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_playing_singer_name = QLabel(self.landscape_bottom_bar_page)
        self.label_playing_singer_name.setObjectName(u"label_playing_singer_name")

        self.horizontalLayout_12.addWidget(self.label_playing_singer_name)


        self.verticalLayout_17.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_14.addLayout(self.verticalLayout_17)

        self.horizontalSpacer_18 = QSpacerItem(88, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_18)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.favor_music_bottom_bar_pushButton = QPushButton(self.landscape_bottom_bar_page)
        self.favor_music_bottom_bar_pushButton.setObjectName(u"favor_music_bottom_bar_pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.favor_music_bottom_bar_pushButton.sizePolicy().hasHeightForWidth())
        self.favor_music_bottom_bar_pushButton.setSizePolicy(sizePolicy)
        self.favor_music_bottom_bar_pushButton.setMinimumSize(QSize(20, 20))
        self.favor_music_bottom_bar_pushButton.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_13.addWidget(self.favor_music_bottom_bar_pushButton)

        self.previous_music_bottom_bar_pushButton = QPushButton(self.landscape_bottom_bar_page)
        self.previous_music_bottom_bar_pushButton.setObjectName(u"previous_music_bottom_bar_pushButton")
        sizePolicy.setHeightForWidth(self.previous_music_bottom_bar_pushButton.sizePolicy().hasHeightForWidth())
        self.previous_music_bottom_bar_pushButton.setSizePolicy(sizePolicy)
        self.previous_music_bottom_bar_pushButton.setMinimumSize(QSize(20, 20))
        self.previous_music_bottom_bar_pushButton.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_13.addWidget(self.previous_music_bottom_bar_pushButton)

        self.pause_bottom_bar_pushButton = QPushButton(self.landscape_bottom_bar_page)
        self.pause_bottom_bar_pushButton.setObjectName(u"pause_bottom_bar_pushButton")
        sizePolicy.setHeightForWidth(self.pause_bottom_bar_pushButton.sizePolicy().hasHeightForWidth())
        self.pause_bottom_bar_pushButton.setSizePolicy(sizePolicy)
        self.pause_bottom_bar_pushButton.setMinimumSize(QSize(20, 20))
        self.pause_bottom_bar_pushButton.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_13.addWidget(self.pause_bottom_bar_pushButton)

        self.next_music_bottom_bar_pushButton = QPushButton(self.landscape_bottom_bar_page)
        self.next_music_bottom_bar_pushButton.setObjectName(u"next_music_bottom_bar_pushButton")
        sizePolicy.setHeightForWidth(self.next_music_bottom_bar_pushButton.sizePolicy().hasHeightForWidth())
        self.next_music_bottom_bar_pushButton.setSizePolicy(sizePolicy)
        self.next_music_bottom_bar_pushButton.setMinimumSize(QSize(20, 20))
        self.next_music_bottom_bar_pushButton.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_13.addWidget(self.next_music_bottom_bar_pushButton)

        self.pushButton_play_sequence_in_bottom_bar = QPushButton(self.landscape_bottom_bar_page)
        self.pushButton_play_sequence_in_bottom_bar.setObjectName(u"pushButton_play_sequence_in_bottom_bar")
        sizePolicy.setHeightForWidth(self.pushButton_play_sequence_in_bottom_bar.sizePolicy().hasHeightForWidth())
        self.pushButton_play_sequence_in_bottom_bar.setSizePolicy(sizePolicy)
        self.pushButton_play_sequence_in_bottom_bar.setMinimumSize(QSize(20, 20))
        self.pushButton_play_sequence_in_bottom_bar.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_13.addWidget(self.pushButton_play_sequence_in_bottom_bar)

        self.pushButton_now_playlist_in_bottom_bar = QPushButton(self.landscape_bottom_bar_page)
        self.pushButton_now_playlist_in_bottom_bar.setObjectName(u"pushButton_now_playlist_in_bottom_bar")
        sizePolicy.setHeightForWidth(self.pushButton_now_playlist_in_bottom_bar.sizePolicy().hasHeightForWidth())
        self.pushButton_now_playlist_in_bottom_bar.setSizePolicy(sizePolicy)
        self.pushButton_now_playlist_in_bottom_bar.setMinimumSize(QSize(20, 20))
        self.pushButton_now_playlist_in_bottom_bar.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_13.addWidget(self.pushButton_now_playlist_in_bottom_bar)

        self.pushButton_set_volume_in_bottom_bar = QPushButton(self.landscape_bottom_bar_page)
        self.pushButton_set_volume_in_bottom_bar.setObjectName(u"pushButton_set_volume_in_bottom_bar")
        sizePolicy.setHeightForWidth(self.pushButton_set_volume_in_bottom_bar.sizePolicy().hasHeightForWidth())
        self.pushButton_set_volume_in_bottom_bar.setSizePolicy(sizePolicy)
        self.pushButton_set_volume_in_bottom_bar.setMinimumSize(QSize(20, 20))
        self.pushButton_set_volume_in_bottom_bar.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_13.addWidget(self.pushButton_set_volume_in_bottom_bar)

        self.pushButton_menu_in_bottom_bar = QPushButton(self.landscape_bottom_bar_page)
        self.pushButton_menu_in_bottom_bar.setObjectName(u"pushButton_menu_in_bottom_bar")
        sizePolicy.setHeightForWidth(self.pushButton_menu_in_bottom_bar.sizePolicy().hasHeightForWidth())
        self.pushButton_menu_in_bottom_bar.setSizePolicy(sizePolicy)
        self.pushButton_menu_in_bottom_bar.setMinimumSize(QSize(20, 20))
        self.pushButton_menu_in_bottom_bar.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_13.addWidget(self.pushButton_menu_in_bottom_bar)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_13)


        self.verticalLayout_18.addLayout(self.horizontalLayout_14)

        self.bottomBarStackedWidget.addWidget(self.landscape_bottom_bar_page)

        self.gridLayout.addWidget(self.bottomBarStackedWidget, 1, 1, 1, 1, Qt.AlignBottom)

        self.sideBarStackedWidget = QStackedWidget(self.page_home)
        self.sideBarStackedWidget.setObjectName(u"sideBarStackedWidget")
        self.sideBarStackedWidget.setMinimumSize(QSize(40, 0))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_19 = QVBoxLayout(self.page)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frontpage_pushButton = QPushButton(self.page)
        self.frontpage_pushButton.setObjectName(u"frontpage_pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frontpage_pushButton.sizePolicy().hasHeightForWidth())
        self.frontpage_pushButton.setSizePolicy(sizePolicy1)
        self.frontpage_pushButton.setMinimumSize(QSize(40, 40))
        self.frontpage_pushButton.setMaximumSize(QSize(40, 40))

        self.verticalLayout_14.addWidget(self.frontpage_pushButton)

        self.search_pushButton = QPushButton(self.page)
        self.search_pushButton.setObjectName(u"search_pushButton")
        sizePolicy1.setHeightForWidth(self.search_pushButton.sizePolicy().hasHeightForWidth())
        self.search_pushButton.setSizePolicy(sizePolicy1)
        self.search_pushButton.setMinimumSize(QSize(40, 40))
        self.search_pushButton.setMaximumSize(QSize(40, 40))

        self.verticalLayout_14.addWidget(self.search_pushButton)


        self.verticalLayout_19.addLayout(self.verticalLayout_14)

        self.verticalSpacer_3 = QSpacerItem(20, 373, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_19.addItem(self.verticalSpacer_3)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.myInfo_pushButton = QPushButton(self.page)
        self.myInfo_pushButton.setObjectName(u"myInfo_pushButton")
        sizePolicy1.setHeightForWidth(self.myInfo_pushButton.sizePolicy().hasHeightForWidth())
        self.myInfo_pushButton.setSizePolicy(sizePolicy1)
        self.myInfo_pushButton.setMinimumSize(QSize(40, 40))
        self.myInfo_pushButton.setMaximumSize(QSize(40, 40))

        self.verticalLayout_13.addWidget(self.myInfo_pushButton)

        self.settings_pushButton = QPushButton(self.page)
        self.settings_pushButton.setObjectName(u"settings_pushButton")
        sizePolicy1.setHeightForWidth(self.settings_pushButton.sizePolicy().hasHeightForWidth())
        self.settings_pushButton.setSizePolicy(sizePolicy1)
        self.settings_pushButton.setMinimumSize(QSize(40, 40))
        self.settings_pushButton.setMaximumSize(QSize(40, 40))

        self.verticalLayout_13.addWidget(self.settings_pushButton)


        self.verticalLayout_19.addLayout(self.verticalLayout_13)

        self.sideBarStackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.sideBarStackedWidget.addWidget(self.page_2)

        self.gridLayout.addWidget(self.sideBarStackedWidget, 0, 0, 2, 1, Qt.AlignLeft)

        self.mainStackedWidget = QStackedWidget(self.page_home)
        self.mainStackedWidget.setObjectName(u"mainStackedWidget")
        self.main = QWidget()
        self.main.setObjectName(u"main")
        self.gridLayout_2 = QGridLayout(self.main)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.scrollArea_Main = QScrollArea(self.main)
        self.scrollArea_Main.setObjectName(u"scrollArea_Main")
        self.scrollArea_Main.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_Main.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_Main.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_Main.setWidgetResizable(True)
        self.scrollAreaWidgetContents_Main = QWidget()
        self.scrollAreaWidgetContents_Main.setObjectName(u"scrollAreaWidgetContents_Main")
        self.scrollAreaWidgetContents_Main.setGeometry(QRect(0, 0, 731, 1168))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_Main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_top_song = QVBoxLayout()
        self.verticalLayout_top_song.setObjectName(u"verticalLayout_top_song")
        self.horizontalLayout_top_song_fixed = QHBoxLayout()
        self.horizontalLayout_top_song_fixed.setObjectName(u"horizontalLayout_top_song_fixed")
        self.horizontalLayout_top_song_fixed.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_top_song = QLabel(self.scrollAreaWidgetContents_Main)
        self.label_top_song.setObjectName(u"label_top_song")

        self.horizontalLayout_top_song_fixed.addWidget(self.label_top_song)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_top_song_fixed.addItem(self.horizontalSpacer)


        self.verticalLayout_top_song.addLayout(self.horizontalLayout_top_song_fixed)

        self.scrollArea_top_song = QScrollArea(self.scrollAreaWidgetContents_Main)
        self.scrollArea_top_song.setObjectName(u"scrollArea_top_song")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollArea_top_song.sizePolicy().hasHeightForWidth())
        self.scrollArea_top_song.setSizePolicy(sizePolicy2)
        self.scrollArea_top_song.setMinimumSize(QSize(0, 200))
        self.scrollArea_top_song.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_top_song.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_top_song.setWidgetResizable(True)
        self.scrollAreaWidgetContents_top_song = QWidget()
        self.scrollAreaWidgetContents_top_song.setObjectName(u"scrollAreaWidgetContents_top_song")
        self.scrollAreaWidgetContents_top_song.setGeometry(QRect(0, 0, 715, 198))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents_top_song)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_top_song = QHBoxLayout()
        self.horizontalLayout_top_song.setObjectName(u"horizontalLayout_top_song")

        self.gridLayout_3.addLayout(self.horizontalLayout_top_song, 0, 0, 1, 1)

        self.scrollArea_top_song.setWidget(self.scrollAreaWidgetContents_top_song)

        self.verticalLayout_top_song.addWidget(self.scrollArea_top_song)


        self.verticalLayout.addLayout(self.verticalLayout_top_song)

        self.verticalLayout_top_playlists = QVBoxLayout()
        self.verticalLayout_top_playlists.setObjectName(u"verticalLayout_top_playlists")
        self.horizontalLayout_top_playlists_fixed = QHBoxLayout()
        self.horizontalLayout_top_playlists_fixed.setObjectName(u"horizontalLayout_top_playlists_fixed")
        self.label_top_playlists = QLabel(self.scrollAreaWidgetContents_Main)
        self.label_top_playlists.setObjectName(u"label_top_playlists")

        self.horizontalLayout_top_playlists_fixed.addWidget(self.label_top_playlists)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_top_playlists_fixed.addItem(self.horizontalSpacer_2)


        self.verticalLayout_top_playlists.addLayout(self.horizontalLayout_top_playlists_fixed)

        self.scrollArea_top_playlists = QScrollArea(self.scrollAreaWidgetContents_Main)
        self.scrollArea_top_playlists.setObjectName(u"scrollArea_top_playlists")
        sizePolicy2.setHeightForWidth(self.scrollArea_top_playlists.sizePolicy().hasHeightForWidth())
        self.scrollArea_top_playlists.setSizePolicy(sizePolicy2)
        self.scrollArea_top_playlists.setMinimumSize(QSize(0, 200))
        self.scrollArea_top_playlists.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_top_playlists.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_top_playlists.setWidgetResizable(True)
        self.scrollAreaWidgetContents_top_playlists = QWidget()
        self.scrollAreaWidgetContents_top_playlists.setObjectName(u"scrollAreaWidgetContents_top_playlists")
        self.scrollAreaWidgetContents_top_playlists.setGeometry(QRect(0, 0, 715, 198))
        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents_top_playlists)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalLayout_top_playlists = QHBoxLayout()
        self.horizontalLayout_top_playlists.setObjectName(u"horizontalLayout_top_playlists")
        self.horizontalLayout_top_playlists.setSizeConstraint(QLayout.SetMaximumSize)

        self.gridLayout_4.addLayout(self.horizontalLayout_top_playlists, 0, 0, 1, 1)

        self.scrollArea_top_playlists.setWidget(self.scrollAreaWidgetContents_top_playlists)

        self.verticalLayout_top_playlists.addWidget(self.scrollArea_top_playlists)


        self.verticalLayout.addLayout(self.verticalLayout_top_playlists)

        self.verticalLayout_personalized = QVBoxLayout()
        self.verticalLayout_personalized.setObjectName(u"verticalLayout_personalized")
        self.horizontalLayout_personalized_fixed = QHBoxLayout()
        self.horizontalLayout_personalized_fixed.setObjectName(u"horizontalLayout_personalized_fixed")
        self.label_personalized = QLabel(self.scrollAreaWidgetContents_Main)
        self.label_personalized.setObjectName(u"label_personalized")

        self.horizontalLayout_personalized_fixed.addWidget(self.label_personalized)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_personalized_fixed.addItem(self.horizontalSpacer_3)


        self.verticalLayout_personalized.addLayout(self.horizontalLayout_personalized_fixed)

        self.scrollArea_personalized = QScrollArea(self.scrollAreaWidgetContents_Main)
        self.scrollArea_personalized.setObjectName(u"scrollArea_personalized")
        sizePolicy2.setHeightForWidth(self.scrollArea_personalized.sizePolicy().hasHeightForWidth())
        self.scrollArea_personalized.setSizePolicy(sizePolicy2)
        self.scrollArea_personalized.setMinimumSize(QSize(0, 200))
        self.scrollArea_personalized.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_personalized.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_personalized.setWidgetResizable(True)
        self.scrollAreaWidgetContents_personalized = QWidget()
        self.scrollAreaWidgetContents_personalized.setObjectName(u"scrollAreaWidgetContents_personalized")
        self.scrollAreaWidgetContents_personalized.setGeometry(QRect(0, 0, 715, 198))
        self.gridLayout_5 = QGridLayout(self.scrollAreaWidgetContents_personalized)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_personalized = QHBoxLayout()
        self.horizontalLayout_personalized.setObjectName(u"horizontalLayout_personalized")

        self.gridLayout_5.addLayout(self.horizontalLayout_personalized, 0, 0, 1, 1)

        self.scrollArea_personalized.setWidget(self.scrollAreaWidgetContents_personalized)

        self.verticalLayout_personalized.addWidget(self.scrollArea_personalized)


        self.verticalLayout.addLayout(self.verticalLayout_personalized)

        self.verticalLayout_recommend_resource = QVBoxLayout()
        self.verticalLayout_recommend_resource.setObjectName(u"verticalLayout_recommend_resource")
        self.horizontalLayout_recommend_resource_fixed = QHBoxLayout()
        self.horizontalLayout_recommend_resource_fixed.setObjectName(u"horizontalLayout_recommend_resource_fixed")
        self.label_recommend_resource = QLabel(self.scrollAreaWidgetContents_Main)
        self.label_recommend_resource.setObjectName(u"label_recommend_resource")

        self.horizontalLayout_recommend_resource_fixed.addWidget(self.label_recommend_resource)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_recommend_resource_fixed.addItem(self.horizontalSpacer_5)


        self.verticalLayout_recommend_resource.addLayout(self.horizontalLayout_recommend_resource_fixed)

        self.scrollArea_recommend_resource = QScrollArea(self.scrollAreaWidgetContents_Main)
        self.scrollArea_recommend_resource.setObjectName(u"scrollArea_recommend_resource")
        sizePolicy2.setHeightForWidth(self.scrollArea_recommend_resource.sizePolicy().hasHeightForWidth())
        self.scrollArea_recommend_resource.setSizePolicy(sizePolicy2)
        self.scrollArea_recommend_resource.setMinimumSize(QSize(0, 200))
        self.scrollArea_recommend_resource.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_recommend_resource.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_recommend_resource.setWidgetResizable(True)
        self.scrollAreaWidgetContents_recommend_resource = QWidget()
        self.scrollAreaWidgetContents_recommend_resource.setObjectName(u"scrollAreaWidgetContents_recommend_resource")
        self.scrollAreaWidgetContents_recommend_resource.setGeometry(QRect(0, 0, 715, 198))
        self.gridLayout_7 = QGridLayout(self.scrollAreaWidgetContents_recommend_resource)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalLayout_recommend_resource = QHBoxLayout()
        self.horizontalLayout_recommend_resource.setObjectName(u"horizontalLayout_recommend_resource")

        self.gridLayout_7.addLayout(self.horizontalLayout_recommend_resource, 0, 0, 1, 1)

        self.scrollArea_recommend_resource.setWidget(self.scrollAreaWidgetContents_recommend_resource)

        self.verticalLayout_recommend_resource.addWidget(self.scrollArea_recommend_resource)


        self.verticalLayout.addLayout(self.verticalLayout_recommend_resource)

        self.verticalLayout_toplist = QVBoxLayout()
        self.verticalLayout_toplist.setObjectName(u"verticalLayout_toplist")
        self.horizontalLayout_toplist_fixed = QHBoxLayout()
        self.horizontalLayout_toplist_fixed.setObjectName(u"horizontalLayout_toplist_fixed")
        self.label_toplist = QLabel(self.scrollAreaWidgetContents_Main)
        self.label_toplist.setObjectName(u"label_toplist")

        self.horizontalLayout_toplist_fixed.addWidget(self.label_toplist)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_toplist_fixed.addItem(self.horizontalSpacer_6)


        self.verticalLayout_toplist.addLayout(self.horizontalLayout_toplist_fixed)

        self.scrollArea_toplist = QScrollArea(self.scrollAreaWidgetContents_Main)
        self.scrollArea_toplist.setObjectName(u"scrollArea_toplist")
        sizePolicy2.setHeightForWidth(self.scrollArea_toplist.sizePolicy().hasHeightForWidth())
        self.scrollArea_toplist.setSizePolicy(sizePolicy2)
        self.scrollArea_toplist.setMinimumSize(QSize(0, 200))
        self.scrollArea_toplist.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_toplist.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_toplist.setWidgetResizable(True)
        self.scrollAreaWidgetContents_toplist = QWidget()
        self.scrollAreaWidgetContents_toplist.setObjectName(u"scrollAreaWidgetContents_toplist")
        self.scrollAreaWidgetContents_toplist.setGeometry(QRect(0, 0, 715, 198))
        self.gridLayout_8 = QGridLayout(self.scrollAreaWidgetContents_toplist)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalLayout_toplist = QHBoxLayout()
        self.horizontalLayout_toplist.setObjectName(u"horizontalLayout_toplist")

        self.gridLayout_8.addLayout(self.horizontalLayout_toplist, 0, 0, 1, 1)

        self.scrollArea_toplist.setWidget(self.scrollAreaWidgetContents_toplist)

        self.verticalLayout_toplist.addWidget(self.scrollArea_toplist)


        self.verticalLayout.addLayout(self.verticalLayout_toplist)

        self.scrollArea_Main.setWidget(self.scrollAreaWidgetContents_Main)

        self.gridLayout_2.addWidget(self.scrollArea_Main, 0, 1, 1, 1)

        self.mainStackedWidget.addWidget(self.main)
        self.page_home_more_item = QWidget()
        self.page_home_more_item.setObjectName(u"page_home_more_item")
        self.verticalLayout_21 = QVBoxLayout(self.page_home_more_item)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_page_home_more_item = QVBoxLayout()
        self.verticalLayout_page_home_more_item.setObjectName(u"verticalLayout_page_home_more_item")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.pushButton_return_to_home_in_page_home_more_item = QPushButton(self.page_home_more_item)
        self.pushButton_return_to_home_in_page_home_more_item.setObjectName(u"pushButton_return_to_home_in_page_home_more_item")

        self.horizontalLayout_15.addWidget(self.pushButton_return_to_home_in_page_home_more_item, 0, Qt.AlignLeft)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_19)

        self.label_in_page_home_more_item = QLabel(self.page_home_more_item)
        self.label_in_page_home_more_item.setObjectName(u"label_in_page_home_more_item")
        self.label_in_page_home_more_item.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_in_page_home_more_item)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_14)


        self.verticalLayout_page_home_more_item.addLayout(self.horizontalLayout_15)


        self.verticalLayout_21.addLayout(self.verticalLayout_page_home_more_item)

        self.mainStackedWidget.addWidget(self.page_home_more_item)
        self.page_search_song = QWidget()
        self.page_search_song.setObjectName(u"page_search_song")
        self.verticalLayout_4 = QVBoxLayout(self.page_search_song)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget_search = QTabWidget(self.page_search_song)
        self.tabWidget_search.setObjectName(u"tabWidget_search")
        self.tab_song = QWidget()
        self.tab_song.setObjectName(u"tab_song")
        self.verticalLayout_7 = QVBoxLayout(self.tab_song)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_search_bar_in_search_song_page = QHBoxLayout()
        self.horizontalLayout_search_bar_in_search_song_page.setObjectName(u"horizontalLayout_search_bar_in_search_song_page")
        self.lineEdit_search_song = QLineEdit(self.tab_song)
        self.lineEdit_search_song.setObjectName(u"lineEdit_search_song")

        self.horizontalLayout_search_bar_in_search_song_page.addWidget(self.lineEdit_search_song)

        self.pushButton_confirm_to_search_song = QPushButton(self.tab_song)
        self.pushButton_confirm_to_search_song.setObjectName(u"pushButton_confirm_to_search_song")

        self.horizontalLayout_search_bar_in_search_song_page.addWidget(self.pushButton_confirm_to_search_song, 0, Qt.AlignRight)


        self.verticalLayout_7.addLayout(self.horizontalLayout_search_bar_in_search_song_page)

        self.scrollArea_search_song = QScrollArea(self.tab_song)
        self.scrollArea_search_song.setObjectName(u"scrollArea_search_song")
        self.scrollArea_search_song.setWidgetResizable(True)
        self.scrollAreaWidgetContents_search_song = QWidget()
        self.scrollAreaWidgetContents_search_song.setObjectName(u"scrollAreaWidgetContents_search_song")
        self.scrollAreaWidgetContents_search_song.setGeometry(QRect(0, 0, 725, 411))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_search_song)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_search_song_contents = QVBoxLayout()
        self.verticalLayout_search_song_contents.setObjectName(u"verticalLayout_search_song_contents")

        self.verticalLayout_9.addLayout(self.verticalLayout_search_song_contents)

        self.scrollArea_search_song.setWidget(self.scrollAreaWidgetContents_search_song)

        self.verticalLayout_7.addWidget(self.scrollArea_search_song)

        self.tabWidget_search.addTab(self.tab_song, "")
        self.tab_album = QWidget()
        self.tab_album.setObjectName(u"tab_album")
        self.verticalLayout_10 = QVBoxLayout(self.tab_album)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_tab_album = QVBoxLayout()
        self.verticalLayout_tab_album.setObjectName(u"verticalLayout_tab_album")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.lineEdit_search_album = QLineEdit(self.tab_album)
        self.lineEdit_search_album.setObjectName(u"lineEdit_search_album")

        self.horizontalLayout_17.addWidget(self.lineEdit_search_album)

        self.pushButton_confirm_to_search_album = QPushButton(self.tab_album)
        self.pushButton_confirm_to_search_album.setObjectName(u"pushButton_confirm_to_search_album")

        self.horizontalLayout_17.addWidget(self.pushButton_confirm_to_search_album)


        self.verticalLayout_tab_album.addLayout(self.horizontalLayout_17)


        self.verticalLayout_10.addLayout(self.verticalLayout_tab_album)

        self.tabWidget_search.addTab(self.tab_album, "")
        self.tab_playlists = QWidget()
        self.tab_playlists.setObjectName(u"tab_playlists")
        self.verticalLayout_11 = QVBoxLayout(self.tab_playlists)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_tab_playlists = QVBoxLayout()
        self.verticalLayout_tab_playlists.setObjectName(u"verticalLayout_tab_playlists")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.lineEdit_search_playlists = QLineEdit(self.tab_playlists)
        self.lineEdit_search_playlists.setObjectName(u"lineEdit_search_playlists")

        self.horizontalLayout_18.addWidget(self.lineEdit_search_playlists)

        self.pushButton_confirm_to_search_playlists = QPushButton(self.tab_playlists)
        self.pushButton_confirm_to_search_playlists.setObjectName(u"pushButton_confirm_to_search_playlists")

        self.horizontalLayout_18.addWidget(self.pushButton_confirm_to_search_playlists)


        self.verticalLayout_tab_playlists.addLayout(self.horizontalLayout_18)


        self.verticalLayout_11.addLayout(self.verticalLayout_tab_playlists)

        self.tabWidget_search.addTab(self.tab_playlists, "")
        self.tab_singer = QWidget()
        self.tab_singer.setObjectName(u"tab_singer")
        self.verticalLayout_12 = QVBoxLayout(self.tab_singer)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_tab_singer = QVBoxLayout()
        self.verticalLayout_tab_singer.setObjectName(u"verticalLayout_tab_singer")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.lineEdit_search_singer = QLineEdit(self.tab_singer)
        self.lineEdit_search_singer.setObjectName(u"lineEdit_search_singer")

        self.horizontalLayout_19.addWidget(self.lineEdit_search_singer)

        self.pushButton_confirm_to_search_singer = QPushButton(self.tab_singer)
        self.pushButton_confirm_to_search_singer.setObjectName(u"pushButton_confirm_to_search_singer")

        self.horizontalLayout_19.addWidget(self.pushButton_confirm_to_search_singer)


        self.verticalLayout_tab_singer.addLayout(self.horizontalLayout_19)


        self.verticalLayout_12.addLayout(self.verticalLayout_tab_singer)

        self.tabWidget_search.addTab(self.tab_singer, "")

        self.verticalLayout_4.addWidget(self.tabWidget_search)

        self.mainStackedWidget.addWidget(self.page_search_song)
        self.music_playlist = QWidget()
        self.music_playlist.setObjectName(u"music_playlist")
        self.verticalLayout_3 = QVBoxLayout(self.music_playlist)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_back_in_playlist = QPushButton(self.music_playlist)
        self.pushButton_back_in_playlist.setObjectName(u"pushButton_back_in_playlist")

        self.horizontalLayout_3.addWidget(self.pushButton_back_in_playlist, 0, Qt.AlignLeft)

        self.label_in_playlist = QLabel(self.music_playlist)
        self.label_in_playlist.setObjectName(u"label_in_playlist")

        self.horizontalLayout_3.addWidget(self.label_in_playlist)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.scrollArea_musiclist = QScrollArea(self.music_playlist)
        self.scrollArea_musiclist.setObjectName(u"scrollArea_musiclist")
        self.scrollArea_musiclist.setWidgetResizable(True)
        self.scrollAreaWidgetContents_playlist = QWidget()
        self.scrollAreaWidgetContents_playlist.setObjectName(u"scrollAreaWidgetContents_playlist")
        self.scrollAreaWidgetContents_playlist.setGeometry(QRect(0, 0, 739, 448))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_playlist)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_playlist = QVBoxLayout()
        self.verticalLayout_playlist.setObjectName(u"verticalLayout_playlist")

        self.verticalLayout_5.addLayout(self.verticalLayout_playlist)

        self.scrollArea_musiclist.setWidget(self.scrollAreaWidgetContents_playlist)

        self.verticalLayout_2.addWidget(self.scrollArea_musiclist)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.mainStackedWidget.addWidget(self.music_playlist)
        self.myinfo = QWidget()
        self.myinfo.setObjectName(u"myinfo")
        self.verticalLayout_15 = QVBoxLayout(self.myinfo)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.scrollArea_myinfo = QScrollArea(self.myinfo)
        self.scrollArea_myinfo.setObjectName(u"scrollArea_myinfo")
        self.scrollArea_myinfo.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 731, 531))
        self.verticalLayout_8 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_pic_and_name = QVBoxLayout()
        self.verticalLayout_pic_and_name.setObjectName(u"verticalLayout_pic_and_name")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.label_userPic = QLabel(self.scrollAreaWidgetContents)
        self.label_userPic.setObjectName(u"label_userPic")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_userPic.sizePolicy().hasHeightForWidth())
        self.label_userPic.setSizePolicy(sizePolicy3)
        self.label_userPic.setMinimumSize(QSize(33, 33))

        self.horizontalLayout_4.addWidget(self.label_userPic)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)


        self.verticalLayout_pic_and_name.addLayout(self.horizontalLayout_4)

        self.label_userName = QLabel(self.scrollAreaWidgetContents)
        self.label_userName.setObjectName(u"label_userName")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_userName.sizePolicy().hasHeightForWidth())
        self.label_userName.setSizePolicy(sizePolicy4)
        self.label_userName.setMinimumSize(QSize(0, 18))
        self.label_userName.setAlignment(Qt.AlignCenter)

        self.verticalLayout_pic_and_name.addWidget(self.label_userName)


        self.verticalLayout_8.addLayout(self.verticalLayout_pic_and_name)

        self.verticalLayout_my_created_playlist = QVBoxLayout()
        self.verticalLayout_my_created_playlist.setObjectName(u"verticalLayout_my_created_playlist")
        self.horizontalLayout_my_created_playlist_fixed = QHBoxLayout()
        self.horizontalLayout_my_created_playlist_fixed.setObjectName(u"horizontalLayout_my_created_playlist_fixed")
        self.label_my_created_playlist = QLabel(self.scrollAreaWidgetContents)
        self.label_my_created_playlist.setObjectName(u"label_my_created_playlist")

        self.horizontalLayout_my_created_playlist_fixed.addWidget(self.label_my_created_playlist)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_my_created_playlist_fixed.addItem(self.horizontalSpacer_8)


        self.verticalLayout_my_created_playlist.addLayout(self.horizontalLayout_my_created_playlist_fixed)

        self.scrollArea_my_created_playlist = QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_my_created_playlist.setObjectName(u"scrollArea_my_created_playlist")
        self.scrollArea_my_created_playlist.setMinimumSize(QSize(0, 185))
        self.scrollArea_my_created_playlist.setWidgetResizable(True)
        self.scrollAreaWidgetContents_my_created_playlist = QWidget()
        self.scrollAreaWidgetContents_my_created_playlist.setObjectName(u"scrollAreaWidgetContents_my_created_playlist")
        self.scrollAreaWidgetContents_my_created_playlist.setGeometry(QRect(0, 0, 715, 183))
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents_my_created_playlist)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout_my_created_playlist = QHBoxLayout()
        self.horizontalLayout_my_created_playlist.setObjectName(u"horizontalLayout_my_created_playlist")

        self.gridLayout_6.addLayout(self.horizontalLayout_my_created_playlist, 0, 0, 1, 1)

        self.scrollArea_my_created_playlist.setWidget(self.scrollAreaWidgetContents_my_created_playlist)

        self.verticalLayout_my_created_playlist.addWidget(self.scrollArea_my_created_playlist)


        self.verticalLayout_8.addLayout(self.verticalLayout_my_created_playlist)

        self.verticalLayout_my_loved_playlist = QVBoxLayout()
        self.verticalLayout_my_loved_playlist.setObjectName(u"verticalLayout_my_loved_playlist")
        self.horizontalLayout_my_loved_playlist_fixed = QHBoxLayout()
        self.horizontalLayout_my_loved_playlist_fixed.setObjectName(u"horizontalLayout_my_loved_playlist_fixed")
        self.label_my_loved_playlist = QLabel(self.scrollAreaWidgetContents)
        self.label_my_loved_playlist.setObjectName(u"label_my_loved_playlist")

        self.horizontalLayout_my_loved_playlist_fixed.addWidget(self.label_my_loved_playlist)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_my_loved_playlist_fixed.addItem(self.horizontalSpacer_10)


        self.verticalLayout_my_loved_playlist.addLayout(self.horizontalLayout_my_loved_playlist_fixed)

        self.scrollArea_my_loved_playlist = QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_my_loved_playlist.setObjectName(u"scrollArea_my_loved_playlist")
        self.scrollArea_my_loved_playlist.setMinimumSize(QSize(0, 185))
        self.scrollArea_my_loved_playlist.setWidgetResizable(True)
        self.scrollAreaWidgetContents_my_loved_playlist = QWidget()
        self.scrollAreaWidgetContents_my_loved_playlist.setObjectName(u"scrollAreaWidgetContents_my_loved_playlist")
        self.scrollAreaWidgetContents_my_loved_playlist.setGeometry(QRect(0, 0, 715, 183))
        self.gridLayout_10 = QGridLayout(self.scrollAreaWidgetContents_my_loved_playlist)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalLayout_my_loved_playlist = QHBoxLayout()
        self.horizontalLayout_my_loved_playlist.setObjectName(u"horizontalLayout_my_loved_playlist")

        self.gridLayout_10.addLayout(self.horizontalLayout_my_loved_playlist, 0, 0, 1, 1)

        self.scrollArea_my_loved_playlist.setWidget(self.scrollAreaWidgetContents_my_loved_playlist)

        self.verticalLayout_my_loved_playlist.addWidget(self.scrollArea_my_loved_playlist)


        self.verticalLayout_8.addLayout(self.verticalLayout_my_loved_playlist)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_20)

        self.delete_Cookie_PushButton = QPushButton(self.scrollAreaWidgetContents)
        self.delete_Cookie_PushButton.setObjectName(u"delete_Cookie_PushButton")

        self.horizontalLayout_20.addWidget(self.delete_Cookie_PushButton)


        self.verticalLayout_8.addLayout(self.horizontalLayout_20)

        self.scrollArea_myinfo.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_15.addWidget(self.scrollArea_myinfo)

        self.mainStackedWidget.addWidget(self.myinfo)

        self.gridLayout.addWidget(self.mainStackedWidget, 0, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)

        self.stackedWidget.addWidget(self.page_home)
        self.page_player = QWidget()
        self.page_player.setObjectName(u"page_player")
        self.horizontalLayout_11 = QHBoxLayout(self.page_player)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_player_return_to_main = QPushButton(self.page_player)
        self.pushButton_player_return_to_main.setObjectName(u"pushButton_player_return_to_main")

        self.horizontalLayout_10.addWidget(self.pushButton_player_return_to_main)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_16)


        self.verticalLayout_16.addLayout(self.horizontalLayout_10)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_9)

        self.label_albumPic_in_playerpage = QLabel(self.page_player)
        self.label_albumPic_in_playerpage.setObjectName(u"label_albumPic_in_playerpage")
        self.label_albumPic_in_playerpage.setMinimumSize(QSize(100, 100))
        self.label_albumPic_in_playerpage.setMaximumSize(QSize(300, 300))

        self.horizontalLayout_7.addWidget(self.label_albumPic_in_playerpage)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_11)


        self.verticalLayout_16.addLayout(self.horizontalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_playing_music_name_in_playerpage = QLabel(self.page_player)
        self.label_playing_music_name_in_playerpage.setObjectName(u"label_playing_music_name_in_playerpage")
        self.label_playing_music_name_in_playerpage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_playing_music_name_in_playerpage)

        self.label_playing_singer_name_in_playerpage = QLabel(self.page_player)
        self.label_playing_singer_name_in_playerpage.setObjectName(u"label_playing_singer_name_in_playerpage")
        self.label_playing_singer_name_in_playerpage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_playing_singer_name_in_playerpage)

        self.label_playing_album_name_in_playerpage = QLabel(self.page_player)
        self.label_playing_album_name_in_playerpage.setObjectName(u"label_playing_album_name_in_playerpage")
        self.label_playing_album_name_in_playerpage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_playing_album_name_in_playerpage)


        self.verticalLayout_16.addLayout(self.verticalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_12)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_time_now_in_playerpage = QLabel(self.page_player)
        self.label_time_now_in_playerpage.setObjectName(u"label_time_now_in_playerpage")
        self.label_time_now_in_playerpage.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label_time_now_in_playerpage)

        self.horizontalSlider_music_progress_in_playerpage = QSlider(self.page_player)
        self.horizontalSlider_music_progress_in_playerpage.setObjectName(u"horizontalSlider_music_progress_in_playerpage")
        self.horizontalSlider_music_progress_in_playerpage.setOrientation(Qt.Horizontal)

        self.horizontalLayout_6.addWidget(self.horizontalSlider_music_progress_in_playerpage)

        self.label_time_all_in_playerpage = QLabel(self.page_player)
        self.label_time_all_in_playerpage.setObjectName(u"label_time_all_in_playerpage")

        self.horizontalLayout_6.addWidget(self.label_time_all_in_playerpage)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_6)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_13)


        self.verticalLayout_16.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_17)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.favor_music_pushButton_in_playerpage = QPushButton(self.page_player)
        self.favor_music_pushButton_in_playerpage.setObjectName(u"favor_music_pushButton_in_playerpage")
        sizePolicy3.setHeightForWidth(self.favor_music_pushButton_in_playerpage.sizePolicy().hasHeightForWidth())
        self.favor_music_pushButton_in_playerpage.setSizePolicy(sizePolicy3)
        self.favor_music_pushButton_in_playerpage.setMinimumSize(QSize(20, 20))
        self.favor_music_pushButton_in_playerpage.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_5.addWidget(self.favor_music_pushButton_in_playerpage)

        self.previous_music_pushButton_in_playerpage = QPushButton(self.page_player)
        self.previous_music_pushButton_in_playerpage.setObjectName(u"previous_music_pushButton_in_playerpage")
        sizePolicy3.setHeightForWidth(self.previous_music_pushButton_in_playerpage.sizePolicy().hasHeightForWidth())
        self.previous_music_pushButton_in_playerpage.setSizePolicy(sizePolicy3)
        self.previous_music_pushButton_in_playerpage.setMinimumSize(QSize(20, 20))
        self.previous_music_pushButton_in_playerpage.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_5.addWidget(self.previous_music_pushButton_in_playerpage)

        self.pause_pushButton_in_playerpage = QPushButton(self.page_player)
        self.pause_pushButton_in_playerpage.setObjectName(u"pause_pushButton_in_playerpage")
        self.pause_pushButton_in_playerpage.setMinimumSize(QSize(20, 20))
        self.pause_pushButton_in_playerpage.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_5.addWidget(self.pause_pushButton_in_playerpage)

        self.next_music_pushButton_in_playerpage = QPushButton(self.page_player)
        self.next_music_pushButton_in_playerpage.setObjectName(u"next_music_pushButton_in_playerpage")
        self.next_music_pushButton_in_playerpage.setMinimumSize(QSize(20, 20))
        self.next_music_pushButton_in_playerpage.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_5.addWidget(self.next_music_pushButton_in_playerpage)

        self.pushButton_play_sequence_in_playerpage = QPushButton(self.page_player)
        self.pushButton_play_sequence_in_playerpage.setObjectName(u"pushButton_play_sequence_in_playerpage")
        self.pushButton_play_sequence_in_playerpage.setMinimumSize(QSize(20, 20))
        self.pushButton_play_sequence_in_playerpage.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_5.addWidget(self.pushButton_play_sequence_in_playerpage)

        self.pushButton_now_playlist_in_playerpage = QPushButton(self.page_player)
        self.pushButton_now_playlist_in_playerpage.setObjectName(u"pushButton_now_playlist_in_playerpage")
        self.pushButton_now_playlist_in_playerpage.setMinimumSize(QSize(20, 20))
        self.pushButton_now_playlist_in_playerpage.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_5.addWidget(self.pushButton_now_playlist_in_playerpage)

        self.pushButton_set_volume_in_playerpage = QPushButton(self.page_player)
        self.pushButton_set_volume_in_playerpage.setObjectName(u"pushButton_set_volume_in_playerpage")
        self.pushButton_set_volume_in_playerpage.setMinimumSize(QSize(20, 20))
        self.pushButton_set_volume_in_playerpage.setMaximumSize(QSize(40, 40))

        self.horizontalLayout_5.addWidget(self.pushButton_set_volume_in_playerpage)


        self.horizontalLayout_9.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_15)


        self.verticalLayout_16.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_2)


        self.horizontalLayout_11.addLayout(self.verticalLayout_16)

        self.scrollArea_lyric = QScrollArea(self.page_player)
        self.scrollArea_lyric.setObjectName(u"scrollArea_lyric")
        self.scrollArea_lyric.setMinimumSize(QSize(0, 0))
        self.scrollArea_lyric.setWidgetResizable(True)
        self.scrollAreaWidgetContents_lyric = QWidget()
        self.scrollAreaWidgetContents_lyric.setObjectName(u"scrollAreaWidgetContents_lyric")
        self.scrollAreaWidgetContents_lyric.setGeometry(QRect(0, 0, 403, 568))
        self.verticalLayout_20 = QVBoxLayout(self.scrollAreaWidgetContents_lyric)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_lyric = QVBoxLayout()
        self.verticalLayout_lyric.setObjectName(u"verticalLayout_lyric")

        self.verticalLayout_20.addLayout(self.verticalLayout_lyric)

        self.scrollArea_lyric.setWidget(self.scrollAreaWidgetContents_lyric)

        self.horizontalLayout_11.addWidget(self.scrollArea_lyric)

        self.stackedWidget.addWidget(self.page_player)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.retranslateUi(Widget)

        self.stackedWidget.setCurrentIndex(1)
        self.bottomBarStackedWidget.setCurrentIndex(1)
        self.sideBarStackedWidget.setCurrentIndex(0)
        self.mainStackedWidget.setCurrentIndex(0)
        self.tabWidget_search.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"XixiMusic", None))
        self.captcha_Sent_PushButton.setText(QCoreApplication.translate("Widget", u"\u83b7\u53d6\u9a8c\u8bc1\u7801", None))
        self.captcha_Verify_PushButton.setText(QCoreApplication.translate("Widget", u"\u767b\u5f55", None))
        self.label_time_in_bottom_bar.setText(QCoreApplication.translate("Widget", u"0.00", None))
        self.label_full_time_in_bottom_bar.setText(QCoreApplication.translate("Widget", u"0.00", None))
        self.pushButton_music_play.setText("")
        self.label_playing_music_name.setText("")
        self.label_playing_singer_name.setText("")
        self.favor_music_bottom_bar_pushButton.setText("")
        self.previous_music_bottom_bar_pushButton.setText("")
        self.pause_bottom_bar_pushButton.setText("")
        self.next_music_bottom_bar_pushButton.setText("")
        self.pushButton_play_sequence_in_bottom_bar.setText("")
        self.pushButton_now_playlist_in_bottom_bar.setText("")
        self.pushButton_set_volume_in_bottom_bar.setText("")
        self.pushButton_menu_in_bottom_bar.setText("")
        self.frontpage_pushButton.setText("")
        self.search_pushButton.setText("")
        self.myInfo_pushButton.setText("")
        self.settings_pushButton.setText("")
        self.label_top_song.setText(QCoreApplication.translate("Widget", u"\u65b0\u6b4c\u901f\u9012", None))
        self.label_top_playlists.setText(QCoreApplication.translate("Widget", u"\u70ed\u95e8\u6b4c\u5355", None))
        self.label_personalized.setText(QCoreApplication.translate("Widget", u"\u63a8\u8350\u6b4c\u5355", None))
        self.label_recommend_resource.setText(QCoreApplication.translate("Widget", u" \u79c1\u4eba\u63a8\u8350", None))
        self.label_toplist.setText(QCoreApplication.translate("Widget", u"\u6392\u884c\u699c", None))
        self.pushButton_return_to_home_in_page_home_more_item.setText("")
        self.label_in_page_home_more_item.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.pushButton_confirm_to_search_song.setText(QCoreApplication.translate("Widget", u"\u641c\u7d22", None))
#if QT_CONFIG(shortcut)
        self.pushButton_confirm_to_search_song.setShortcut(QCoreApplication.translate("Widget", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.tabWidget_search.setTabText(self.tabWidget_search.indexOf(self.tab_song), QCoreApplication.translate("Widget", u"\u6b4c\u66f2", None))
        self.pushButton_confirm_to_search_album.setText(QCoreApplication.translate("Widget", u"\u641c\u7d22", None))
#if QT_CONFIG(shortcut)
        self.pushButton_confirm_to_search_album.setShortcut(QCoreApplication.translate("Widget", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.tabWidget_search.setTabText(self.tabWidget_search.indexOf(self.tab_album), QCoreApplication.translate("Widget", u"\u4e13\u8f91", None))
        self.pushButton_confirm_to_search_playlists.setText(QCoreApplication.translate("Widget", u"\u641c\u7d22", None))
#if QT_CONFIG(shortcut)
        self.pushButton_confirm_to_search_playlists.setShortcut(QCoreApplication.translate("Widget", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.tabWidget_search.setTabText(self.tabWidget_search.indexOf(self.tab_playlists), QCoreApplication.translate("Widget", u"\u6b4c\u5355", None))
        self.pushButton_confirm_to_search_singer.setText(QCoreApplication.translate("Widget", u"\u641c\u7d22", None))
#if QT_CONFIG(shortcut)
        self.pushButton_confirm_to_search_singer.setShortcut(QCoreApplication.translate("Widget", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.tabWidget_search.setTabText(self.tabWidget_search.indexOf(self.tab_singer), QCoreApplication.translate("Widget", u"\u6b4c\u624b", None))
        self.pushButton_back_in_playlist.setText("")
        self.label_in_playlist.setText(QCoreApplication.translate("Widget", u"TextLabel", None))
        self.label_userPic.setText(QCoreApplication.translate("Widget", u"UserPic", None))
        self.label_userName.setText(QCoreApplication.translate("Widget", u"UserName", None))
        self.label_my_created_playlist.setText(QCoreApplication.translate("Widget", u"\u6211\u521b\u5efa\u7684\u6b4c\u5355", None))
        self.label_my_loved_playlist.setText(QCoreApplication.translate("Widget", u"\u6211\u6536\u85cf\u7684\u6b4c\u5355", None))
        self.delete_Cookie_PushButton.setText(QCoreApplication.translate("Widget", u"\u9000\u51fa\u767b\u5f55", None))
        self.pushButton_player_return_to_main.setText("")
        self.label_albumPic_in_playerpage.setText(QCoreApplication.translate("Widget", u"albumPic", None))
        self.label_playing_music_name_in_playerpage.setText(QCoreApplication.translate("Widget", u"\u6b4c\u66f2\u540d", None))
        self.label_playing_singer_name_in_playerpage.setText(QCoreApplication.translate("Widget", u"\u6b4c\u624b\u540d", None))
        self.label_playing_album_name_in_playerpage.setText(QCoreApplication.translate("Widget", u"\u4e13\u8f91\u540d", None))
        self.label_time_now_in_playerpage.setText(QCoreApplication.translate("Widget", u"0.00", None))
        self.label_time_all_in_playerpage.setText(QCoreApplication.translate("Widget", u"0.00", None))
        self.favor_music_pushButton_in_playerpage.setText("")
        self.previous_music_pushButton_in_playerpage.setText("")
        self.pause_pushButton_in_playerpage.setText("")
        self.next_music_pushButton_in_playerpage.setText("")
        self.pushButton_play_sequence_in_playerpage.setText("")
        self.pushButton_now_playlist_in_playerpage.setText("")
        self.pushButton_set_volume_in_playerpage.setText("")
    # retranslateUi

