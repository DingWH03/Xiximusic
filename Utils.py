# This Python file uses the following encoding: utf-8
import base64
from PySide6.QtCore import QByteArray, Qt, QThread, Signal, QRunnable
from PySide6.QtGui import QImage, QPixmap, QColor
from PySide6.QtWidgets import QLabel, QToolButton
import heapq
import time
import os
from PIL import Image
from io import BytesIO
import requests
import platform
from datetime import datetime
from functools import partial
import re

class LoadImageTask(QRunnable):
    def __init__(self, button, icon_url, cache_folder):
        super(LoadImageTask, self).__init__()
        self.button = button
        self.icon_url = icon_url
        self.cache_folder = cache_folder

    def run(self):
        icon = get_thumbnail(self.icon_url, self.cache_folder + '/image', 240, 240) # 加载尺寸为240x240的缩略图
        if getattr(self, 'button', None):
            self.button.setIcon(icon)
            del(icon)
            del(self)

class DownLoadThread(QThread): # 下载的多线程类，下载完成后发送信号downloaded
    downloaded = Signal()
    def __init__(self, url, save_path):
        super().__init__()
        self.url = url
        self.save_path = save_path

    def run(self):
        try:
            response = requests.get(self.url, stream=True)
            response.raise_for_status()

            with open(self.save_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            # print(response)
            self.downloaded.emit()
        except Exception as e:
            print(f"Download failed: {e}")

class RequestApi_multithread(QThread): # 调用函数（网易云api）多线程类
    requested = Signal(object)
    def __init__(self, request_function, *args, **kwargs):
        super().__init__()
        self.request_function = request_function
        self.args = args
        self.kwargs = kwargs

    def run(self):
        try:
            result = self.request_function(*self.args, **self.kwargs)
            # print('线程运行')
            self.requested.emit(result)
        except Exception as e:
            print(f"Requests failed: {e}")

def on_downloaded_setPixmap(object, image_filename, download_thread):
    download_thread.quit()
    pixmap = QPixmap(image_filename)
    # print(isinstance(object, QLabel))
    if isinstance(object, QLabel) :
        object.setPixmap(pixmap)
    elif isinstance(object, QToolButton):
        object.setIcon(pixmap)

def setPixmap_multithread(object, URL, save_path):
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    image_filename = os.path.join(save_path, os.path.basename(URL))
    if os.path.exists(image_filename):
        # 使用 PySide6 的 QPixmap 加载保存的图片
        pixmap = QPixmap(image_filename)
        # object.setPixmap(pixmap)
        if isinstance(object, QLabel) :
            object.setPixmap(pixmap)
        elif isinstance(object, QToolButton):
            object.setIcon(pixmap)
    else:
        download_thread = DownLoadThread(URL, image_filename)
        download_thread.downloaded.connect(partial(on_downloaded_setPixmap, object, image_filename, download_thread))
        download_thread.start()

def refresh_song_detail(song_id, api, musicPlayer, ui, icon): # 多线程调用函数
    ui.label_playing_music_name.setText(musicPlayer.music_name) # 更新歌曲名
    ui.label_playing_music_name_in_playerpage.setText(musicPlayer.music_name) # 更新播放页面歌曲名
    albumPic, singer_name, album_name = api.get_albumPic_by_id(song_id) # 通过api获取专辑图片，歌手与专辑名
    musicPlayer.singer_name = singer_name
    musicPlayer.album_name = album_name
    ui.label_playing_singer_name.setText(singer_name)
    ui.label_playing_singer_name_in_playerpage.setText(singer_name) # 更新歌手名
    ui.label_playing_album_name_in_playerpage.setText(album_name) # 更新专辑名
    ui.pushButton_music_play.setIcon(albumPic) # 更新下边栏播放页面图片
    ui.label_albumPic_in_playerpage.setPixmap(albumPic) # 设置图片
    if musicPlayer.loved_status == False:
        ui.favor_music_bottom_bar_pushButton.setIcon(icon[1])
        ui.favor_music_pushButton_in_playerpage.setIcon(icon[1])
    else:
        ui.favor_music_bottom_bar_pushButton.setIcon(icon[0])
        ui.favor_music_pushButton_in_playerpage.setIcon(icon[0])
    return

def get_cache_folder(): # 根据操作系统获取缓存目录
    system = platform.system()
    if system == 'Windows':
        # On Windows, use the personal folder and create a 'xiximusic/cache' directory
        cache_folder = os.path.expanduser('~/xiximusic/cache')
    else:
        # On other systems, use the default '.cache/xiximusic' directory
        cache_folder = os.path.expanduser('~/.cache/xiximusic')
    return cache_folder



class MyUtils:
    def __init__(self):
        pass

    def base64_to_qimage(self, base64_string):
        # Decode base64 string to bytes
        image_data = base64.b64decode(base64_string)
        # Convert bytes to QByteArray
        qbyte_array = QByteArray(image_data)
        # Create QImage from QByteArray
        qimage = QImage()
        qimage.loadFromData(qbyte_array)

        return qimage

def check_and_clean_cache(cache_dir, max_size):
    # 使用os.scandir来获取文件名和文件属性
    cache_files = list(os.scandir(cache_dir))

    # 计算文件总大小
    cache_size = sum(f.stat().st_size for f in cache_files)

    # 如果文件总大小超过最大值，删除最早的文件
    while cache_size > max_size and cache_files:
        # 找到最早的文件
        oldest_file = min(cache_files, key=lambda f: f.stat().st_mtime)

        file_path = os.path.join(cache_dir, oldest_file.name)

        # 检查文件是否存在
        if os.path.exists(file_path):
            os.remove(file_path)
            cache_size -= oldest_file.stat().st_size
        else:
            print(f"File not found: {file_path}")

        # 删除已处理的文件
        cache_files.remove(oldest_file)

    return cache_size

def clean_cache(cache_dir, max_size):
    check_and_clean_cache(cache_dir, max_size)

# 加载图片到缓存目录并返回QPixmap
def get_image(image_url, save_path, max_retries=2):
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    image_filename = os.path.join(save_path, os.path.basename(image_url))
    if os.path.exists(image_filename):
        # 使用 PySide6 的 QPixmap 加载保存的图片
        pixmap = QPixmap(image_filename)
        return pixmap
    else:
        retries = 0
        while retries < max_retries:
            try:
                response = requests.get(image_url)
                response.raise_for_status()  # 如果请求失败会抛出异常
                image_filename = os.path.join(save_path, os.path.basename(image_url[:255]))  # 避免文件名过长
                with open(image_filename, 'wb') as file:
                    file.write(response.content)
                pixmap = QPixmap(image_filename)
                return pixmap
            except requests.RequestException:
                # print(f"Error downloading image from {image_url}: {e}")
                retries += 1
        print(f"get_image: Failed to download image from {image_url} after {max_retries} retries")
        return None

# 加载缩略图
def get_thumbnail(image_url, save_path, thumbnail_width, thumbnail_height, max_retries=2):
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    thumbnail_filename = os.path.join(save_path, f"thumbnail_{thumbnail_width}x{thumbnail_height}_{os.path.basename(image_url[:200])}")

    if os.path.exists(thumbnail_filename):
        # 如果缩略图已存在，直接加载
        pixmap = QPixmap(thumbnail_filename)
        return pixmap
    else:
        retries = 0
        while retries < max_retries:
            try:
                # 下载原始图片
                response = requests.get(image_url)
                response.raise_for_status()  # 如果请求失败会抛出异常
                image = Image.open(BytesIO(response.content))
                image = image.convert("RGB")

                # 生成缩略图
                thumbnail = image.resize((thumbnail_width, thumbnail_height), Image.ANTIALIAS)
                try:
                    thumbnail.save(thumbnail_filename)
                    pixmap = QPixmap(thumbnail_filename)
                except BaseException:
                    image_data = thumbnail.tobytes()
                    qimage = QImage(image_data, thumbnail.width, thumbnail.height, QImage.Format_RGB888)
                    pixmap = QPixmap.fromImage(qimage)

                return pixmap
            except requests.RequestException as e:
                # print(f"Error downloading image from {image_url}: {e}")
                retries += 1
        print(f"get_thumbnail: Failed to download image from {image_url} after {max_retries} retries")
        return None



# 清理图片缓存
def cleanup_old_images(image_folder, days_threshold=7):
    now = datetime.now()
    # 使用 os.scandir 替代 os.walk
    with os.scandir(image_folder) as entries:
        for entry in entries:
            if entry.is_file():
                file_path = entry.path
                # 获取文件的最后修改时间
                if platform.system() == 'Windows':
                    # 对于 Windows，使用 entry.stat().st_mtime
                    modified_time = datetime.fromtimestamp(entry.stat().st_mtime)
                else:
                    # 对于其他系统，使用 os.stat().st_mtime
                    modified_time = datetime.fromtimestamp(os.stat(file_path).st_mtime)

                # 计算文件保存的天数
                days_difference = (now - modified_time).days

                if days_difference > days_threshold:
                    # 删除超过指定天数的文件
                    os.remove(file_path)
                    print(f"Deleted old image: {file_path}")
    return 1

def split_lyrics(input_data):
    time_sequence = []
    lyrics_sequence = []
    pattern = re.compile(r'\[(\d+:\d+\.\d+)\]\s*(.*)') # 匹配[12:34.567]

    for line in input_data.split('\n'):
        match = pattern.match(line)
        if match:
            time = match.group(1)
            lyrics = match.group(2)

            # 将时间转换成秒
            minutes, seconds_with_ms = map(float, time.split(':'))
            seconds, milliseconds = divmod(seconds_with_ms * 1000, 1000)
            time_in_seconds = minutes * 60 + seconds + milliseconds / 1000

            time_sequence.append(time_in_seconds)
            lyrics_sequence.append(lyrics)

    return time_sequence, lyrics_sequence

def get_typical_color_hex(qpixmap):
    # 提取图像中的颜色
    colors = get_image_colors(qpixmap)

    # 计算典型色调
    typical_color = calculate_typical_color(colors)

    # 返回典型色调的十六进制代码
    return typical_color.name()

def get_image_colors(qpixmap):
    # 获取图像中的所有像素颜色
    image = qpixmap.toImage()
    width, height = qpixmap.width(), qpixmap.height()

    # 存储颜色
    colors = []

    for x in range(width):
        for y in range(height):
            color = QColor(image.pixel(x, y))
            colors.append(color)

    return colors

def calculate_typical_color(colors):
    # 计算颜色平均值作为典型色调
    total_red = sum(color.red() for color in colors)
    total_green = sum(color.green() for color in colors)
    total_blue = sum(color.blue() for color in colors)

    average_red = total_red // len(colors)
    average_green = total_green // len(colors)
    average_blue = total_blue // len(colors)

    return QColor(average_red, average_green, average_blue)
