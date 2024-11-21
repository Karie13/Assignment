import os
import zipfile

def zip_folder(folder_path):
    if not os.path.isdir(folder_path):
        print("Error: Invalid folder path.")
        return

    folder_name = os.path.basename(folder_path.rstrip(os.sep))
    zip_file = os.path.join(os.path.dirname(folder_path), f"{folder_name}.zip")
    
    try:
        with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, folder_path))
        print(f"Folder successfully zipped to: {zip_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    folder = input("Enter the folder path to zip: ").strip()
    zip_folder(folder)

