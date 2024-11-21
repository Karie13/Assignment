## File zipping Program

This Python program compresses a specified folder into a .zip file, preserving its structure and content.
It handles subdirectories, empty folders, and files gracefully.

# Requirements:
- Python 3.6 or higher.
- os and zipfile libraries (both are part of the Python standard library).


# Run the program:
python FileZipping.py


# Example Input:
Enter the folder path to zip: C:\Users\ASUS\Documents\my_folder

# Example Output:
Processing folder: C:\Users\ASUS\Documents\my_folder
Adding file: C:\Users\ASUS\Documents\my_folder\file1.txt
Adding file: C:\Users\ASUS\Documents\my_folder\subfolder\file2.txt
Zipped successfully to: C:\Users\ASUS\Documents\my_folder.zip

# Error Handling:
- Invalid Folder Path:
The program will display an error message: Error: Invalid folder path.

- Empty Folder:
Creates an empty .zip file without errors.

# Customization
To change the .zip file's location or name, modify the zip_file variable in the code:
zip_file = os.path.join(os.path.dirname(folder_path), f"custom_name.zip")