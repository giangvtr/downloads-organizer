import os                           #to work with operating system
import json                         #to work with json file
import shutil                       #for copy and overwrite operation
from subprocess import PIPE, run    #to run terminal command
import sys                          #to use CL arguments
from datetime import datetime, timedelta


DOWNLOADS_PATH = os.path.expanduser("~/Downloads")
ORGANIZED_PATH = os.path.join(DOWNLOADS_PATH, "Organized")
AGE_LIMIT_DAYS = 180

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".odt", ".csv"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Scripts": [".sh", ".js", ".go", ".rb"],  
    "Installers": [".deb", ".AppImage", ".exe", ".msi"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav", ".flac"],
    "Code": [".c", ".cpp", ".h", ".py"],
    "Others": []
}

# STEP 1: Get file category
def get_file_category(file_ext):
    for category, extensions in FILE_CATEGORIES.items():
        if file_ext.lower() in extensions:
            return category
    return "Others"

# STEP 2: Create a new target directory
def create_dir(target_folder_path):
    if not os.path.exists(target_folder_path):
        os.makedirs(target_folder_path)

def create_dir_from_dict(base_path):
    for category in FILE_CATEGORIES.keys():
        folder_path = os.path.join(base_path, category)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

# STEP 3: Delete old files
def delete_old_files(base_path, days):
    deleted_files = []
    now = datetime.now()
    age_limit = timedelta(days=days)

    for root, _, files in os.walk(base_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                last_accessed = datetime.fromtimestamp(os.path.getatime(file_path))
                if now - last_accessed > age_limit:
                    os.remove(file_path)
                    deleted_files.append(file_path)
            except Exception as e:
                print(f"Error processing {file_path}: {e}")
    return deleted_files

# STEP 4: Move files to respective folders
def move_files(source_path, target_path):
    moved_files = []

    for item in os.listdir(source_path):
        item_path = os.path.join(source_path, item)
        if os.path.isdir(item_path):
            continue

        _, ext = os.path.splitext(item)
        category = get_file_category(ext)
        category_folder = os.path.join(target_path, category)
        create_dir(category_folder)  # Ensure category folder exists

        dest_path = os.path.join(category_folder, item)

        try:
            shutil.move(item_path, dest_path)
            moved_files.append((item, category))
            print(f"Moved: {item} -> {category}/")
        except Exception as e:
            print(f"Failed to move {item}: {e}")
    
    return moved_files

# STEP 5: Write a JSON File to recap
def write_recap_json(organized_path, moved_files, deleted_files):
    recap = {
        "moved": [{"file": name, "category": category} for name, category in moved_files],
        "deleted": deleted_files,
        "total_moved": len(moved_files),
        "total_deleted": len(deleted_files),
        "timestamp": datetime.now().isoformat()
    }

    json_path = os.path.join(organized_path, "recap.json")
    with open(json_path, "w") as f:
        json.dump(recap, f, indent=4)
    print(f"Recap written to {json_path}")

# ========== MAIN =============
def main(src=DOWNLOADS_PATH, dest=ORGANIZED_PATH, age=AGE_LIMIT_DAYS):
    print(f"Organizing files in {src}")

    create_dir(dest)
    create_dir_from_dict(dest)

    deleted_files = delete_old_files(src, age)
    moved_files = move_files(src, dest)

    write_recap_json(dest, moved_files, deleted_files)
    print("Done organizing.")

# Run only if called directly
if __name__ == "__main__":
    args = sys.argv
    if len(args) == 4:
        source, target, days = args[1:]
        main(os.path.expanduser(source), os.path.expanduser(target), int(days))
    else:
        print("Default values are chosen: Clean ~/Downloads and move into ~/Downloads/Organized with age limit = 180 days")
        main()
    
    
    