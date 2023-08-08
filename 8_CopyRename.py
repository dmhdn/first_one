import os
import shutil

def copy_and_rename_files(source_dir, destination_dir):
    # Create the destination directory if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)

    # Traverse through the entire directory tree using os.walk()
    for root, _, files in os.walk(source_dir):
        for filename in files:
            # Get the full path of the source file
            source_file_path = os.path.join(root, filename)

            # Get the relative path to the source file from the source directory
            relative_path = os.path.relpath(source_file_path, source_dir)

            # Get the folder name (immediate parent folder name)
            folder_name = os.path.basename(root)

            # Create the new filename by combining the folder name and the original filename
            new_filename = f"{folder_name} {filename}"

            # Get the full path of the destination file
            destination_file_path = os.path.join(destination_dir, new_filename)

            # Create the destination directory (if it doesn't exist) for the current file
            os.makedirs(os.path.dirname(destination_file_path), exist_ok=True)

            # Copy the file to the destination directory and rename it
            shutil.copy(source_file_path, destination_file_path)

# Prompt the user for the source and destination directories
source_directory = input("Enter the path of the source directory: ")
#destination_directory = input("Enter the path of the destination directory: ")
destination_directory ="E:/LUU TAM"
copy_and_rename_files(source_directory, destination_directory)
