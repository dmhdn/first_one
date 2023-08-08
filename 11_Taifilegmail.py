import imaplib
import email
import os

# Load configuration from config.txt
config_file = "config.txt"
with open(config_file, "r", encoding="utf-8") as cfg:
    config = dict(line.strip().split("=") for line in cfg)

username = config.get("username", "")
password = config.get("password", "")
sender_emails_input = config.get("sender_emails", "")
sender_emails = [email.strip() for email in sender_emails_input.split(",")]
path_to_your_directory = config.get("path_to_your_directory", "").strip()

# Rest of the code remains unchanged...

# Tao file luu tru
downloaded_files_file = "downloaded_files.txt"

# Tao tap hop de luu tru cac ten file da tai xuong
downloaded_files = set()

# Nap tap hop tu file luu tru (neu co)
if os.path.exists(downloaded_files_file):
    with open(downloaded_files_file, "r", encoding="utf-8") as file:
        downloaded_files = set(file.read().splitlines())

# Ket noi den Gmail
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(username, password)

# Chon thu muc inbox
mail.select("inbox")

# Tao danh sach cac dieu kien tim kiem cho tung nguoi gui
search_queries = [f'(FROM "{sender}")' for sender in sender_emails]

# Ket hop ket qua tu cac dieu kien tim kiem
all_messages = set()
for search_query in search_queries:
    status, messages = mail.search(None, search_query)
    all_messages.update(messages[0].split())

# Duyet qua tung email va lay file dinh kem
for message_id in all_messages:
    # Lay noi dung email
    res, msg = mail.fetch(message_id, "(RFC822)")
    email_msg = email.message_from_bytes(msg[0][1])
    
    # Kiem tra email co file dinh kem khong
    if email_msg.get_content_maintype() != "multipart":
        continue
    
    # Duyet qua tung phan tu trong email
    for part in email_msg.walk():
        if part.get_content_maintype() == "multipart":
            continue
        if part.get("Content-Disposition") is None:
            continue
        
        # Lay ten file dinh kem
        filename = part.get_filename()
        
        # Kiem tra co ten file khong
        if filename:
            # Kiem tra xem ten file da duoc tai truoc do chua
            if filename in downloaded_files:
                print("File {} da duoc tai truoc do, bo qua.".format(filename))
                continue

            # Xac dinh duong dan de luu tru file dinh kem
            save_path = os.path.join(path_to_your_directory, filename)
            
            # Tao thu muc
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            
            # Ghi file dinh kem vao o cung
            with open(save_path, "wb") as f:
                f.write(part.get_payload(decode=True))
                print("Da tai file dinh kem tu {}: {}".format(email_msg['From'], filename))
            
            # Them ten file vao tap hop cac ten file da tai xuong
            downloaded_files.add(filename)

# Dong ket noi
mail.logout()

# Luu trang thai da tai xuong vao file
with open(downloaded_files_file, "w", encoding="utf-8") as file:
    file.write("\n".join(downloaded_files))
