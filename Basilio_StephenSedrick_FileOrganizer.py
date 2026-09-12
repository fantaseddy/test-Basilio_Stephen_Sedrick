# Basilio, Stephen Sedrick File Organizer

import os
import shutil

folder_path = input("Enter folder path: ")

if not os.path.exists(folder):
    print("Error. Does not exist.")
else:
    files = os.listdir(folder)

    images = 0
    documents = 0
    videos = 0
    others = 0

    image_folder =  os.path.join(folder, "Images")
    documents_folder = os.path.join(folder, "Documents")
    videos_folder = os.path.join(folder, "Videos")
    others_folder = os.path.join(folder, "Others")

    if not os.path.exists(image_folder):
        os.mkdir(image_folder)
    if not os.path.exists(documents_folder):
        os.mkdir(documents_folder)
    if not os.path.exists(videos_folder):
        os.mkdir(videos_folder)
    if not os.path.exists(others_folder):
        os.mkdir(others_folder)

    for file in files: 
        if file == "Images" or file == "Documents" or file == "Videos" or file == "Others":
            continue

        file_path = os.path.join(folder, file)

        if os.path.isdir(file_path):
            continue

        file_lower = file.lower()

        if file_lower.endswith((".jpg", ".jpeg", ".png", ".gif")):
            destination = os.path.join(image_folder, file)
            shutil.move(file_path, destination)
            images += 1
            print("Moved: ", file, "->  Images")

        elif file_lower.endswith((".pdf", ".docx", ".txt", ".pptx")):
            destination = os.path.join(documents_folder, file)
            shutil.move(file_path, destination)
            documents += 1
            print("Moved: ", file, "-> Documents")

        elif file_lower.endswith((".mp4", ".mov", ".avi")):
            destination = os.path.join(videos_folder, file)
            shutil.move(file_path, destination)
            videos += 1
            print("Moved: ", file. "-> Videos")

        else:
            destination = os.path.join(others_folder, file):
            shutil.move(file_path, destination)
            others += 1
            print("Moved: ", file, "-> Others")

        total = images + documents + videos + others

print()
print("----- Folder Summary -----")
print("Images moved: ", images)
print("Documents moved: ", documents)
print("Videos moved: ", videos)
print("Others moved: ", others)
print("Total files organized: ", total)