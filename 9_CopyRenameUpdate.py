import os
import shutil
import pandas as pd

def list_all_files(source_dir):
    file_list = []
    for root, _, files in os.walk(source_dir):
        for filename in files:
            file_list.append(os.path.join(root, filename))
    return file_list

def save_to_excel(file_list, excel_file):
    df = pd.DataFrame({"Directory": file_list})
    df.to_excel(excel_file, index=False, engine="openpyxl")

def copy_and_rename_files(source_dir, destination_dir, excel_file):
    # Create the destination directory if it doesn't exist
    os.makedirs(destination_dir, exist_ok=True)

    # List all file paths in the source directory and its subdirectories
    file_list = list_all_files(source_dir)

    # Save the file paths to the Excel file (filedir.xlsx)
    save_to_excel(file_list, excel_file)

    # Copy and rename files for each directory path in the Excel file
    for source_file_path in file_list:
        # Get the relative path to the source file from the source directory
        relative_path = os.path.relpath(source_file_path, source_dir)

        # Get the parent folder name (source_directory)
        parent_folder_name = os.path.basename(source_dir)

        # Get the filename without the extension
        filename, file_extension = os.path.splitext(os.path.basename(relative_path))

        # Create the new filename by combining the parent folder name and the original filename
        new_filename = f"{parent_folder_name}_{filename}{file_extension}"

        # Get the full path of the destination file
        destination_file_path = os.path.join(destination_dir, new_filename)

        # Create the destination directory (if it doesn't exist) for the current file
        os.makedirs(os.path.dirname(destination_file_path), exist_ok=True)

        # Copy the file to the destination directory and rename it
        shutil.copy(source_file_path, destination_file_path)

# Prompt the user for the source directory and the Excel file name
source_directory = input("Enter the path of the source directory: ")
#destination_directory = input("Enter the path of the destination directory: ")
destination_directory = "E:/LUU TAM"
excel_file = "E:/LUU TAM/filedir.xlsx"

copy_and_rename_files(source_directory, destination_directory, excel_file)
