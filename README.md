# 🧹 Downloads Organizer Script
**Author:** Built by someone who got tired of the digital landfill that is ~/Downloads.

This Python script helps you **automatically organize and clean your Downloads folder** by:

- Categorizing files into folders based on their extensions
- Deleting files that haven't been accessed in a while
- Generating a JSON recap with statistics on the operation

---

## 📁 Folder Structure

When run, it creates an `Organized` folder inside your Downloads directory, with subfolders for each file category:
Downloads/ ├── Organized/ │ ├── Archives/ │ ├── Code/ │ ├── Documents/ │ ├── Images/ │ ├── Installers/ │ ├── Music/ │ ├── Others/ │ ├── Scripts/ │ ├── Videos/ │ └── recap.json ├── your_unorganized_files...


---

## 🚀 Features

- ✅ File categorization based on extensions
- 🧼 Automatic deletion of old files (default: 180 days)
- 📦 JSON summary (`recap.json`) with moved & deleted files
- 🧠 Customizable source and target directories
- 🔧 Command-line interface or default fallback

---

## 📌 File Categories

The script supports these default file types:

| Category   | Extensions                                            |
|------------|--------------------------------------------------------|
| Images     | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`       |
| Documents  | `.pdf`, `.docx`, `.doc`, `.txt`, `.odt`               |
| Archives   | `.zip`, `.tar`, `.gz`, `.rar`, `.7z`                  |
| Scripts    | `.sh`, `.py`, `.js`, `.go`, `.rb`                     |
| Installers | `.deb`, `.AppImage`, `.exe`, `.msi`                   |
| Videos     | `.mp4`, `.mkv`, `.avi`                                |
| Music      | `.mp3`, `.wav`, `.flac`                               |
| Code       | `.c`, `.cpp`, `.h`, `.py`                             |
| Others     | Everything else                                       |

---

## 🛠️ Installation

Make sure you have Python 3 installed. No external dependencies are needed.

```bash
python3 --version
```
---
## 💡 Usage
### Run with default values (clean Downloads folder)
```bash
python3 organize_downloads.py
```
This will:
* Organize ~/Downloads
* Create folders inside ~/Downloads/Organized
* Delete files older than 180 days

### Run with custom arguments
```bash
python3 organize_downloads.py <source_path> <target_path> <age_limit_days>
```

Example:
```bash
python3 organize_downloads.py ~/Downloads /tmp/OrganizedDownloads 90
```

## 📄 Output
The script will print logs of moved and deleted files and save a recap.json in the target directory containing:
```bash
{
  "moved": [
    {"file": "screenshot1.png", "category": "Images"},
    {"file": "document.pdf", "category": "Documents"}
  ],
  "deleted": [
    "/home/user/Downloads/oldfile.zip"
  ],
  "total_moved": 2,
  "total_deleted": 1,
  "timestamp": "2025-04-13T18:41:07.123456"
}
```

## Further Development 
* Weekly scheduling with crontab
* Extend the Extension table, maybe with the help of AI ?
