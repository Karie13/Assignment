## Collage Creation Program

This program combines four images into a 2x2 grid to create a collage.
Users provide the paths to four image files, and the program resizes and arranges them into a new image saved as collage.jpg (or another format specified by the user).

# Requirements:
- Python 3.6+
- Pillow (Python Imaging Library)

# To install Pillow:

bash

pip install pillow

# How to Use
- Save the program as collage_creator.py.
- Run the program from the terminal:
bash
python collage_creator.py

- Enter the paths to the four images when prompted.
- Specify the output file name (without an extension).
- Choose the desired output format (e.g., jpg or png).

# Input

Path for Image 1: F:\images\image1.jpg
Path for Image 2: F:\images\image2.jpg
Path for Image 3: F:\images\image3.jpg
Path for Image 4: F:\images\image4.jpg
Enter the output file name (without extension): my_collage
Enter the desired output format (jpg, png): jpg

# Output
A file named my_collage.jpg will be created in the working directory.

# Error Handling
- Invalid Paths: Displays an error if the file path does not exist.
- Unsupported Formats: Handles cases where the file is not a valid image.
- Image Corruption: Displays an error if the file cannot be opened.