from PIL import Image  
import os  

# Function to create a collage
def create_collage(image_paths, output_path, output_format):
    try:
        # Step 1: Load the images and verify their paths
        images = []
        for path in image_paths:
            if not os.path.isfile(path):  
                print(f"Error: File not found - {path}")
                return
            try:
                img = Image.open(path)  
                images.append(img)
            except Exception as e:
                print(f"Error: Unable to open file {path} - {e}")
                return

        # Step 2: Resize images to the same size (smallest image dimensions)
        min_width = min(img.size[0] for img in images)  
        min_height = min(img.size[1] for img in images) 
        resized_images = [img.resize((min_width, min_height)) for img in images] 

        # Step 3: Create a blank canvas for the collage
        collage_width = min_width * 2  
        collage_height = min_height * 2  
        collage = Image.new("RGB", (collage_width, collage_height))  

        # Step 4: Arrange the images in a 2x2 grid
        collage.paste(resized_images[0], (0, 0))  
        collage.paste(resized_images[1], (min_width, 0))  
        collage.paste(resized_images[2], (0, min_height))  
        collage.paste(resized_images[3], (min_width, min_height))  

        # Step 5: Save the collage to a file
        output_file = f"{output_path}.{output_format}"  
        collage.save(output_file)  
        print(f"Collage saved as {output_file}")  

    except Exception as e:
        
        print(f"Error: {e}")


# Main program: Collect input from the user
if __name__ == "__main__":
    print("Enter the paths for the 4 images to create a collage:")
    image_paths = [
        input("Path for Image 1: ").strip(),  
        input("Path for Image 2: ").strip(),  
        input("Path for Image 3: ").strip(),  
        input("Path for Image 4: ").strip()   
    ]
    output_path = input("Enter the output file name (without extension): ").strip()  
    output_format = input("Enter the desired output format (jpg, png): ").strip() 

    # Call the function to create the collage
    create_collage(image_paths, output_path, output_format)
