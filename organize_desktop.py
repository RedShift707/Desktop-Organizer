import os
import shutil

def organize_desktop():
    # Define the desktop path
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Create folders if they don't exist
    folders = ["Documents", "Images", "Videos", "Others"]
    for folder in folders:
        folder_path = os.path.join(desktop_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Organize files
    for filename in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Determine file type and move to the corresponding folder
        file_type = filename.split(".")[-1].lower()
        if file_type in ["doc", "docx", "txt", "pdf"]:
            shutil.move(file_path, os.path.join(desktop_path, "Documents", filename))
        elif file_type in ["jpg", "jpeg", "png", "gif"]:
            shutil.move(file_path, os.path.join(desktop_path, "Images", filename))
        elif file_type in ["mp4", "avi", "mkv", "mov"]:
            shutil.move(file_path, os.path.join(desktop_path, "Videos", filename))
        else:
            shutil.move(file_path, os.path.join(desktop_path, "Others", filename))

    print("Desktop organized successfully!")

if __name__ == "__main__":
    organize_desktop()
