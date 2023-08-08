import os
from PyPDF2 import PdfMerger

def merge_pdfs_in_folder(folder_path, output_filename):
    # Lay danh sach file
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

    # Tim kiem file_da_noi.pdf trong danh sach file
    file_da_noi_path = os.path.join(folder_path, output_filename)
    if not os.path.exists(file_da_noi_path):
        # Neu file_da_noi.pdf chua ton tai, kiem tra xem co it nhat 1 file PDF trong thu muc
        pdf_files = [pdf_file for pdf_file in pdf_files if pdf_file != output_filename]
        if pdf_files:
            print("Danh sach file PDF trong thu muc:")
            for pdf_file in pdf_files:
                print(pdf_file)

            # Duong dan tuyet doi cua file da noi
            output_file_path = os.path.join(folder_path, output_filename)

            # Noi tung file
            merger = PdfMerger()
            for pdf_file in pdf_files:
                pdf_path = os.path.join(folder_path, pdf_file)
                merger.append(pdf_path)
                print(f"Tien hanh noi file: {pdf_file}")

            # Luu thanh file da noi
            with open(output_file_path, 'wb') as output_file:
                merger.write(output_file_path)
            merger.close()

            print(f"File da noi da duoc luu tai: {output_file_path}")

            # Xoa cac file da duoc noi
            for pdf_file in pdf_files:
                pdf_path = os.path.join(folder_path, pdf_file)
                os.remove(pdf_path)
                print(f"Da xoa file: {pdf_file}")

        else:
            print("Thu muc khong chua file PDF. Khong thuc hien noi.")

    else:
        print(f"File {output_filename} da ton tai. Khong thuc hien noi va khong xoa bat ky file nao.")

if __name__ == "__main__":
    # Duong dan thu muc
    folder_path = r"E:\LUU TAM"
    output_filename = "file_da_noi.pdf"
    merge_pdfs_in_folder(folder_path, output_filename)
