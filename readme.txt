# Download Organizer

Python script that automatically organizes your Downloads folder files into categorized subfolders by file type.

## About The Project

Organizes the download folder based on the file extension.

**Organizes by type:**
- Photos (jpg, png, gif, svg...)
- Docs (pdf, docx, txt, xlsx...)
- Videos (mp4, avi, mkv...)
- Installers (msi, deb, dmg...)
- Executables (exe)

(May not match with code yet. This will be improved upon in a future update)

Developed as a learning project in Python and automation.

## Getting Started

### Prerequisites
- Python 3.7 or higher

### Installation

```bash
# Clone the repository
git clone https://github.com/5-ter/download-organizer.git
cd download-organizer

# Run the script
python3 main.py
```

### Usage

**Note:** Currently, you need to create the category folders manually before running the script. This will be automated in a future update.

Create the following folders in your Downloads directory:

- Docs
- Photos
- Executables
- Videos
- Installers
- Misc

Then, simply run the script:

```bash
python3 main.py
```

## How It Works

The script scans all files in the Downloads folder and organizes them into subfolders based on file extension. If a file with the same name already exists in the destination folder, it automatically adds a number suffix to prevent overwriting.

**Example:**
```
Downloads/
├── photo.jpg          → Moved to Downloads/Images/
├── document.pdf       → Moved to Downloads/Docs/
└── video.mp4         → Moved to Downloads/Videos/
```

## Built With

- **Python 3** - Core language
- **pathlib** - File path manipulation
- **shutil** - File operations
- **os** - Operating system interface

## What I Learned

This project helped me develop:
- File and directory manipulation in Python
- Dictionary usage and data structures
- Exception handling and edge cases
- Code best practices (docstrings, naming conventions)
- Solving real-world problems with code

## Future Improvements

- [ ] Automatic folder creation
- [ ] Watchdog integration for automatic organization on new downloads
- [ ] Customizable category configuration via config file
- [ ] Undo last organization feature
- [ ] Activity logging system
- [ ] Date-based organization option
- [ ] Cross-platform compatibility testing

## Important Notes

- Backup recommended before first use
- Script moves files, does not delete them
- Use only on your own machine
- Intended for educational purposes

## License

This project is open source and available for educational purposes.

## Author

**Henrique**
- GitHub: [@5-ter](https://github.com/5-ter)

## Contributing

Suggestions and improvements are welcome! Feel free to open an issue or pull request.

---

If you found this project helpful, consider giving it a star!
