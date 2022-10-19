import os

#Step-1: Get all the image files in the current directory
def check_if_images():
    images_list = []
    for images in os.listdir('.'):
        if images.endswith('.jpg') or images.endswith('.png') or images.endswith('.jpeg'):
            images_list.append(images)
    return images_list

files = check_if_images()

#Mid step: rename the files to the index number

images_list = files.copy()
def rename_files():
    for index, file in enumerate(images_list):
        extension = os.path.splitext(file)[1]

        try:
            #naming convention 1
            #os.rename(file, str(index+1) + '-image' + extension)

            #naming convention 2
            os.rename(file, 'image-' + str(index+1) + extension)
        except FileExistsError:
            print("Error renaming file: " + file + ". File already exixts")

rename_files()