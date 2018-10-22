import ctypes
import random
 
 
class Wallpaper:
    def __init__(self):
        self._SPI_SETDESKWALLPAPER = 20
        self._path = 'C:\\Users\\scotf\\PycharmProjects\\wallpaper_script\\'
        self._extension = '.jpg'
        self._pic_number = 7
        self.pic_list = []
        self.last_pic = 0
 
    @property
    def spi_setdeskwallpaper(self):
        return self._SPI_SETDESKWALLPAPER
 
    @property
    def path(self):
        return self._path
 
    @property
    def extension(self):
        return self._extension
 
    @property
    def pic_number(self):
        return self._pic_number
 
    def raise_pic_number(self):
        self._pic_number += 1
 
    def set(self):
        config = open(self.path + 'config.txt', 'r')
        self.last_pic = config.readline()
        config.close()
 
        print(self.last_pic)
 
        for x in range(1, self.pic_number + 1):
            self.pic_list.append(x)
 
        # TODO(@me): write last_pic method for not setting the same old wallpaper again
        current_pic = random.choice(self.pic_list)
        if current_pic == self.last_pic:
            self.pic_list.pop(current_pic - 1)
            current_pic = random.choice(self.pic_list)
 
        open(self.path + 'config.txt', 'w').close()
 
        config = open(self.path + 'config.txt', 'w')
        config.write(str(current_pic))
        config.close()
 
        pic_path = self.path + str(current_pic) + self.extension
        ctypes.windll.user32.SystemParametersInfoW(self.spi_setdeskwallpaper, 0, pic_path, 0)
 
 
if __name__ == "__main__":
    wp = Wallpaper()
    wp.set()
