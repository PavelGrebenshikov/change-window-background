import ctypes
from os import walk
from pathlib import Path
from random import randint

class ChangeBackground():
    SPI_SETDESKWALLPAPER = 20

    def __init__(self, path = None):
        self.path = path

    def get_absolute_path(self):
        if not self.path:
            return Path("images").resolve()

    def get_picture_for_window_background(self):
        if not self.path:
            list_background = sum([file_name for root, dirs, file_name in walk(self.get_absolute_path())], [])
            if not list_background:
                raise FileNotFoundError(f"В папке {self.get_absolute_path()} не найдены обои")
            return list_background
        else:
            list_background = sum([file_name for root, dirs, file_name in walk(self.path)], [])
            if not list_background:
                raise FileNotFoundError(f"В папке {self.path} не найдены обои")
            return list_background

    def change_random_background(self):
        list_window_background = self.get_picture_for_window_background()
        path = self.get_absolute_path()
        if not self.path:
            if len(list_window_background) > 1:
                ctypes.windll.user32.SystemParametersInfoW(self.SPI_SETDESKWALLPAPER, 0, r"{0}\{1}".format(path, list_window_background[randint(0, len(list_window_background) - 1)]), 0)
            elif len(list_window_background) == 1:
                ctypes.windll.user32.SystemParametersInfoW(self.SPI_SETDESKWALLPAPER, 0, r"{0}\{1}".format(path, list_window_background[0]), 0)
        else:
            if len(list_window_background) > 1:
                ctypes.windll.user32.SystemParametersInfoW(self.SPI_SETDESKWALLPAPER, 0, r"{0}\{1}".format(self.path, list_window_background[randint(0, len(list_window_background) - 1)]), 0)
            elif len(list_window_backround) == 1:
                ctypes.windll.user32.SystemParametersInfoW(self.SPI_SETDESKWALLPAPER, 0, r"{0}\{1}".format(self.path, list_window_background[0]), 0)

    def change_backgorund(self):
        if self.path:
            ctypes.windll.user32.SystemParametersInfoW(self.SPI_SETDESKWALLPAPER, 0, r"{0}".format(self.path), 0)
        else:
            raise ValueError("Введите путь до изображения/изображений")
