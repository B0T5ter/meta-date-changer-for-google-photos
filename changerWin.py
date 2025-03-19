import os
import time
import re
from PIL import Image

folder_path = os.getcwd()

pattern = re.compile(r"(\d{4})(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})")

files = [f for f in os.listdir(folder_path) if f.lower().endswith((".jpg", ".jpeg"))]

for i, filename in enumerate(files, 1):
    try:
        match = pattern.search(filename)
        if match:
            year, month, day, hour, minute, second = map(int, match.groups())
            new_date_exif = f"{year}:{month:02d}:{day:02d} {hour:02d}:{minute:02d}:{second:02d}"
            new_timestamp = time.mktime((year, month, day, hour, minute, second, 0, 0, -1))

            file_path = os.path.join(folder_path, filename)
            print(f"{i}/{len(files)}")

            image = Image.open(file_path)
            exif_data = image.getexif()
            if exif_data is not None:
                exif_data[36867] = new_date_exif
                exif_data[306] = new_date_exif
                image.save(file_path, exif=exif_data)

            try:
                os.utime(file_path, (new_timestamp, new_timestamp))

                if os.name == "nt":
                    import pywintypes
                    import win32file
                    import win32con

                    handle = win32file.CreateFile(
                        file_path, win32con.GENERIC_WRITE, win32con.FILE_SHARE_READ, None,
                        win32con.OPEN_EXISTING, win32con.FILE_ATTRIBUTE_NORMAL, None
                    )

                    new_time = pywintypes.Time(new_timestamp)
                    win32file.SetFileTime(handle, new_time, new_time, new_time)
                    handle.Close()

            except Exception as e:
                print(f"Error: {e}")

    except Exception as e:
        print(f"Can't read: {filename}: {e}")
