import os, datetime, shutil

#helpers
def get_creation_date(path_to_file):
    return datetime.datetime.fromtimestamp(os.path.getctime(path_to_file))




#Step-1: Get all the image files in the current directory
def check_if_images():
    images_list = []
    for images in os.listdir('.'):
        if images.endswith('.jpg') or images.endswith('.png') or images.endswith('.jpeg'):
            images_list.append(images)
    return images_list

files = check_if_images()




#Step-2: Get the date of creation of the image files and sort them
dates = []

for index, file in enumerate(files):
    creation_date = get_creation_date(file).strftime("%d %m %Y")

    if index != 0:
        prev_creation_date = get_creation_date(files[index-1]).strftime("%d %m %Y")
        if prev_creation_date != creation_date:
            dates.append(creation_date)




#Step-3: Create a folder for each date and move the images to the respective folders
print("Total files to move: " + len(files).__str__())
count = 0

#create date directory
for date in dates:
    if not os.path.isdir(date):
        os.mkdir(date)

#move files to respective folders
for index, file in enumerate(files):
    creation_date = get_creation_date(file).strftime("%d %m %Y")
    if(os.path.isdir(creation_date)):
        shutil.move(file, creation_date + '/' + file)
        count += 1
    else:
        print("Error: No such directory named " + creation_date)

print("Files moved: " + count.__str__())
print("Files not moved: " + (len(files) - count).__str__())