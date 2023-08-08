import os
import openpyxl

def auto_adjust_column_width(excel_file):
    # Mo file
    workbook = openpyxl.load_workbook(excel_file)

    # Cho sheet
    worksheet = workbook.worksheets[0]

    # Dieu chinh cot
    worksheet.column_dimensions['F'].auto_size = True
    worksheet.column_dimensions['G'].auto_size = True
    worksheet.column_dimensions['H'].auto_size = True

    # Luu file
    workbook.save(excel_file)
def auto_adjust_columns_in_directory(folder_path):
    # Lay danh sach file
    excel_files = [file for file in os.listdir(folder_path) if file.endswith('.xlsx')]

    # Duyet qua tung file
    for excel_file in excel_files:
        excel_file_path = os.path.join(folder_path, excel_file)
        auto_adjust_column_width(excel_file_path)

# Duong dan
folder_path = 'E:/LUU TAM'
auto_adjust_columns_in_directory(folder_path)
