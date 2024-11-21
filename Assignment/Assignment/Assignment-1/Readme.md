

# File Renaming Program
This Python program renames all files in a specified folder sequentially, starting from `1.ext`, `2.ext`, `3.ext`, and so on, while preserving the original file extensions. The program only renames regular files, ignores directories and non-file items, and provides error handling for common issues such as invalid folder paths and permission errors.

# Features
- Renames all regular files in a specified folder sequentially, starting from `1.ext`.
- Retains the original file extensions (e.g., `.jpg`, `.txt`, `.pdf`).
- Supports optional reverse renaming, allowing files to be renamed starting from the highest number.
- Handles common errors such as invalid paths, permission issues, and empty folders.

# Assumptions
- The program assumes that the user provides a valid folder path.
- Only regular files are renamed (directories and non-file items are ignored).
- If the folder is empty, no renaming occurs.
- The program sorts files alphabetically by default, but the user can choose to rename files in reverse order.

# Requirements
- Python 3.x
- No external dependencies are required; the program uses Python's built-in libraries.

# How to Run the Program

1. Clone or Download the Project:
   Download the Python file (`FileRename.py`) to your local system.

2. Run the Program:
   Open a terminal or command prompt and navigate to the folder where the program is saved. Run the following command:

  
   python FileRename.py
   

3. Provide Input:
   The program will prompt you to enter the path to the folder containing the files you want to rename. Enter the full path of the folder.


4. Optional Reverse Renaming:
   The program will then ask whether you want to rename the files in reverse order (starting with the highest number). You can choose `y` for yes or `n` for no.

   Example:
 
   Do you want to rename files in reverse order? (y/n): n
   

5. Program Execution:
   The program will rename the files sequentially. It will display each file's old name and the new name it was renamed to.

   Example output:
  
   Renaming files...
   File 'image1.jpg' renamed to '1.jpg'
   File 'document.txt' renamed to '2.txt'
   File 'report.pdf' renamed to '3.pdf'
   File 'notes.docx' renamed to '4.docx'
   File 'music.mp3' renamed to '5.mp3'
   Renaming completed.
  

# Expected Input and Output

# Input Example:
- Folder path to be provided by the user. For example: `/path/to/folder`.
- Option to rename files in reverse order (y/n).

# Output Example:
If the folder contains the following files:

/path/to/folder/
├── image1.jpg
├── document.txt
├── report.pdf
├── notes.docx
├── music.mp3


The program will rename them as:

/path/to/folder/
├── 1.jpg
├── 2.txt
├── 3.pdf
├── 4.docx
├── 5.mp3


# Error Handling:

- Non-Existing Folder:
   If the provided folder path does not exist, the program will output:
  
   Error: The folder '/path/to/folder' does not exist.
   

- Empty Folder:
   If the folder is empty, the program will output:
   
   The folder is empty. No files to rename.
   

- Permission Issues:
   If the program encounters a file it cannot rename due to permission issues, it will output:
   
   Error: Unable to rename file 'image1.jpg' due to permission issues.
   

# Optional Features

# Reverse Renaming
You can choose to rename files in reverse order, starting from the highest number, by answering `y` when prompted.

# Preview Renaming
While not implemented in this version, you could add an additional feature to display a preview of the new filenames before performing the renaming operation.

# Recursive Renaming
This program currently handles only files in the specified folder. To rename files in subdirectories as well, the script could be modified to traverse directories recursively.

# Known Limitations
- The program does not handle filename conflicts (e.g., if files after renaming would result in the same name). It will simply skip the renaming in case of errors or permission issues.


