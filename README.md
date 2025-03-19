# meta-date-changer-for-google-photos

This program allows you to change the creation date of a photo and the EXIF date based on the filename. The program supports `.jpg` and `.jpeg` formats. The filename must include the date in the `YYYYMMDD_HHMMSS` format, e.g., `20250302_153020.jpg`. This date will be used to set both the file's creation date and the EXIF date.

The program works in two versions:
- **Windows**: Changes the creation date of the file using the `pywin32` library.
- **Linux/macOS**: Changes the file's access and modification times.

## Requirements

- **Python 3.x**
- **Python Libraries**:
  - `Pillow` (for working with EXIF data)
  - `pywin32` (only for Windows, optional for Windows version)

### Installing dependencies

#### For Windows

1. Install Python 3 if you don't have it installed.
2. Install the required libraries:
   ```sh
   pip install Pillow
   pip install pywin32

### How to use
Copy the corresponding script to the folder where your photos are located.

For Windows, use changer_windows.py.
For Linux/macOS, use changer_linux_mac.py.
Ensure your photos are named in the format YYYYMMDD_HHMMSS, e.g., 20250302_153020.jpg.

Run the program in the terminal (Windows/Linux/macOS) by typing:
```sh
    python changer_windows.py  
    python changer_linux_mac.py
