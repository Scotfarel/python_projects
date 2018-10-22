import ctypes
import random
 
SPI_SETDESKWALLPAPER = 20
 
path = 'C:\\Users\\scotf\\PycharmProjects\\wallpaper_script\\'
extension = '.jpg'
pic_number = 4
 
current_pic = str(random.randint(1, pic_number))
pic_path = path + current_pic + extension
 
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, pic_path, 0)
