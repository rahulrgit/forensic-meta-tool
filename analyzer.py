import exifread
import os
from PIL import Image

def get_metadata(file_path):
    try:
        if not os.path.isfile(file_path):
            print("❌ Provided path is not a file.")
            return

        # Open image file for reading (binary mode)
        with open(file_path, 'rb') as f:
            tags = exifread.process_file(f, details=False)

        if not tags:
            if file_path.lower().endswith('.png'):
                print("PNG file does not have exif data.")
            print("❌ No EXIF metadata found.")
            return

        print(f"\n📄 Metadata for: {os.path.basename(file_path)}")
        print("-" * 40)
        for tag in tags:
            print(f"{tag:25}: {tags[tag]}")

        # Optional GPS info
        gps_lat = tags.get('GPS GPSLatitude')
        gps_lon = tags.get('GPS GPSLongitude')
        if gps_lat and gps_lon:
            print(f"\n🌍 Location Info:\nLatitude: {gps_lat}\nLongitude: {gps_lon}")

    except Exception as e:
        print(f"⚠️ Error: {e}")

def main():
    print("=== Metadata Analyzer ===")
    path = input("Enter path to image file: ").strip()
    get_metadata(path)

if __name__ == "__main__":
    main()
