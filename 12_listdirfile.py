import os
import shutil

# Load configuration from config.txt
config_file = "config_lisdirfile.txt"
config = {}
with open(config_file, "r", encoding="utf-8") as cfg:
    for line in cfg:
        line = line.strip()
        if "=" in line:
            key, value = line.split("=", 1)
            config[key.strip()] = value.strip()

list_dir = config.get("list_dir", "")
copy_file = config.get("copy_file", "")

# Tao file luu tru
list_file = "list_file.txt"

# Tao tap hop de luu tru cac ten file da tai xuong
downloaded_files = set()

# Nap tap hop tu file luu tru (neu co)
if os.path.exists(list_file):
    with open(list_file, "r", encoding="utf-8") as file:
        downloaded_files = set(file.read().splitlines())

# Liet ke cac file trong thu muc list_dir va cap nhat vao list_file.txt neu chua ton tai
updated_files = set()  # Tap hop cac file da cap nhat
with open(list_file, "a", encoding="utf-8") as f:
    for root, _, files in os.walk(list_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path not in downloaded_files:
                f.write(file_path + '\n')
                downloaded_files.add(file_path)
                updated_files.add(file_path)

if updated_files:
    print(f"Da cap nhat {len(updated_files)} duong dan moi vao list_file.txt.")
else:
    print("Khong co duong dan moi de cap nhat.")

# Copy va doi ten cac file vao thu muc
if not os.path.exists(copy_file):
    os.makedirs(copy_file)

for file in updated_files:
    filename = os.path.basename(file)
    parent_folder_name = os.path.basename(os.path.dirname(file))  # Get the parent folder name
    new_filename = f"{parent_folder_name} {filename}"
    dest_file_path = os.path.join(copy_file, new_filename)
    shutil.copy(file, dest_file_path)
    print(f"Da copy va doi ten file {file} thanh {dest_file_path}")
