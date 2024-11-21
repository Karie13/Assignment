import os

def rename_files_in_folder(folder_path, reverse=False):
    try:
        # Check if the folder exists
        if not os.path.exists(folder_path):
            print(f"Error: The folder does not exist.")
            return
        
        # Check if the folder is indeed a directory
        if not os.path.isdir(folder_path):
            print(f"Error: The provided path is not a valid directory.")
            return
        
        # Get a list of files and sort them
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        if not files:
            print("The folder is empty. No files to rename.")
            return
        
        # Sort files alphabetically by default or in reverse order if specified
        files.sort(reverse=reverse)

        print("Renaming files...")

        # Loop through the files and rename them sequentially
        for index, file in enumerate(files, start=1):
            old_file_path = os.path.join(folder_path, file)
            file_extension = os.path.splitext(file)[1] 
            new_file_name = f"{index}{file_extension}"
            new_file_path = os.path.join(folder_path, new_file_name)

            try:
                os.rename(old_file_path, new_file_path)
                print(f"File '{file}' renamed to '{new_file_name}'")
            except PermissionError:
                print(f"Error: Unable to rename file '{file}' due to permission issues.")
            except Exception as e:
                print(f"Error: Unable to rename file '{file}' due to {e}")

        print("Renaming completed.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Ask the user for the folder path
    folder_path = input("Please enter the path to the folder: ").strip()

    # Optionally, allow reverse renaming
    reverse = input("Do you want to rename files in reverse order? (y/n): ").strip().lower() == 'y'

    rename_files_in_folder(folder_path, reverse)
