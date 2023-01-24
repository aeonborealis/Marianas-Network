import os
import shutil

# Define the desktop directory
desktop = os.path.expanduser("~/Desktop")

# Define the extensions to organize
extensions = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".doc", ".docx", ".pdf", ".txt"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".tar"]
}

# Create the folders if they don't exist
for folder in extensions.keys():
    folder_path = os.path.join(desktop, folder)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

# Organize the files
for file in os.listdir(desktop):
    for folder, exts in extensions.items():
        for ext in exts:
            if file.endswith(ext):
                file_path = os.path.join(desktop, file)
                folder_path = os.path.join(desktop, folder)
                shutil.move(file_path, folder_path)
                break
