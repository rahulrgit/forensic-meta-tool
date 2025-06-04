# 🧠 Metadata Analyzer

A simple Python-based tool to extract **EXIF metadata** (like GPS location, camera model, date, time, etc.) from image files. Helpful in **digital forensics**, photography, and data analysis.

---

## 🚀 Features

- 📷 Extract metadata from JPEG images
- 📍 Get GPS coordinates if available
- 🕒 See original creation timestamp
- ❌ Detect unsupported files like PNG
- 🖥️ Easy-to-use CLI interface

---

## 📦 Tech Stack

- Python 3.x
- [ExifRead](https://pypi.org/project/ExifRead/) – to read EXIF metadata
- [Pillow](https://pillow.readthedocs.io/en/stable/) – optional image handling
- OS module for path & file handling

---

## 📁 Project Structure

```
metadata_analyzer/
├── analyzer.py           # Main script
├── sample/               # Place sample images here
└── README.md
```

---

## 📥 Installation

```bash
pip install exifread pillow
```

---

## 🔧 Usage

```bash
python3 analyzer.py
```

📂 Enter the **full path** of your `.jpg` file (example):

```
/home/user/metadata_analyzer/sample/photo.jpg
```

---

## 📌 Notes

- Only **.jpg / .jpeg** files contain detailed EXIF metadata
- **.png / .webp / .bmp** do not support EXIF
- Many social media platforms **strip metadata** before upload

---

## 📈 Future Enhancements

- [ ] Batch process all images in a folder
- [ ] Export metadata to CSV
- [ ] Add GUI using Tkinter

---

## 👨‍💻 Author

**Rahul Rathod**  
🔗 GitHub: [@rahulrgit](https://github.com/rahulrgit)

---

## 🪪 License

MIT License. Feel free to use, modify, and share.
