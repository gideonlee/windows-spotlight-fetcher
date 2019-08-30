# The OS module in Python provides a way of using operating system dependent functionality
# shutil - Python's standard utility modules. This module helps in automating the process of copying and removal of files and directories
# Python Imaging Library is a free library for the Python programming language that adds support for opening, manipulating, and saving many different image file formats
# The imghdr module determines the type of image contained in a file or byte stream.
import os
import shutil
from PIL import Image
import imghdr


# This is the folder that Windows keeps the spotlight photos.
appdata = os.getenv('APPDATA')[:-7]
windows_spotlight_folder = appdata + "Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets\\"

# This is where the spotlight photos will be saved. 
wallpaper_path = "C:\Users\Gideon\Pictures\Wallpapers\\"

# Checks all the spotlight photos and runs the copy_file function on anything bigger than 721 x 720 (ideally 1280 x 720, 1980 x 1080). 
def transfer_files():
	# Valid photo types
	image_types = ('jpeg', 'jpg', 'png', 'gif')

	# Loops through all the files in this spotlight folder. 
	for file_name in os.listdir(windows_spotlight_folder): 
		# Append the current path and file name(s) togethers
		# "C:\Users\name\AppData\Local\Packages\Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy\LocalState\Assets\xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
		file_path = '%s%s' % (windows_spotlight_folder, file_name)

		# gets files .png, .jpeg, jpg
		file_type = imghdr.what(file_path) 

		if image_types.count(file_type) == 1:
			im = Image.open(file_path)
			(width, height) = im.size

			if height >= 720 and width > height: 
				copy_file(file_name, file_type, width, height, file_path)


# Copies the spotlight photos
def copy_file(file_name, file_type, width, height, file_path):
	# Appends the file_name.file_type (e.g. we87gf1f22ef1221wnflr3l2k.jpeg)
	picture_name = '%s.%s' % (file_name, file_type)

	new_picture_path = wallpaper_path + picture_name
	shutil.copyfile(file_path, new_picture_path)

transfer_files()
