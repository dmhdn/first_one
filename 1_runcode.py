import os
import pandas as pd
import shutil
from openpyxl import load_workbook
import xlwings as xw
from ctypes import windll
import win32com.client
import win32com.client as win32
excel = win32.gencache.EnsureDispatch('Excel.Application')
xl = win32com.client.Dispatch("Excel.Application")
xlPasteValues = -4163

#Load file excel chi ho tro xls
#------------------------------------------
#excel_file = pd.ExcelFile('file_list.xls')
#df = excel_file.parse('Sheet1')
#print(df.head(5))
#------------------------------------------

#Chuong trinh list tat ca cac file theo thu muc da chi dinh
#Luu list file vao df va luu file ten file_list.xlsx
#Dung de liet ke thu muc PKN
def list_all_file():
	rootdir=input('NHAP DUONG DAN DUYET ALL FILE, DEFAULT:\n')
	if not rootdir:
		rootdir = r'X:\6- PKN- THANH PHAM'
	#rootdir = r'E:\LUU TAM\1. PKN'
	global df
	file_list = []
	for subdir, dirs, files in os.walk(rootdir):
		for file in files:
			file_path = os.path.join(subdir, file)
			file_list.append(file_path)
		df = pd.DataFrame({'Full Path': file_list})
		df[['Path', 'Folder Name', 'File Name']] = df['Full Path'].str.rsplit("\\", 2, expand=True)
	df = pd.DataFrame(df, columns=['Full Path', 'Path', 'Folder Name', 'File Name'])
	df.to_excel(r'E:\WORKING\file_list.xlsx', index=False)
#df['NAM'] = None them cot neu can thiet

#Tim ten san_pham va so_lo
#Copy file tim duoc den duong dan E:\LUU TAM
#Dung de copy file PKN
def tim_kiem_file():
	while True:
		sp_solo=input('Nhap ten SP, LSX tim kiem:\n').lower()
		san_pham=sp_solo[:-6]
		so_lo=sp_solo[-6:]
		result = df[df['Full Path'].str.lower().str.contains(f'{san_pham}.*{so_lo}')]
		if result.empty:
			print("Khong tim thay ket qua, xin vui long nhap lai.")
			with open("notfound.txt", "a") as file:
				file.write(san_pham + " "+so_lo + "\n")
			continue
		else:
			while True:
				print(result['Full Path'].str[-40:])
				print('Da tim thay',len(result), 'ket qua')
				index_file=input('Nhap index ket qua de xu ly:\n')
				if int(index_file)>=len(result):
					print('So index da nhap vuot index ket qua, nhap lai index nho hon',len(result))
					continue
				else:
					row = result.iloc[int(index_file)].tolist()
					end_old=row[0]
					end_dir=r'E:\LUU TAM'
					end_file=row[3]
					end_product=row[2]
					shutil.copy(end_old, f'{end_dir}/{end_product} {end_file}')
					print(f'Da copy xong file den {end_dir}\{end_product} {end_file}')
					break
				break
			break

#Chuong trinh load file excel bang thu vien xlwings
#Luu file excel vao df
#Dung de doc file file_list da luu giam thoi gian liet ke
def load_file_xlwings_xlsx():
	global df
	Path_to_load_file=input('Nhap duong dan day du file excel can load:\n')
	if not Path_to_load_file:
		Path_to_load_file=r'E:\WORKING\file_list.xlsx'
	print('LOADING.........!')
	app = xw.App(visible=False)
	wb_load=app.books.open(Path_to_load_file)
	sh_load=wb_load.sheets
	sh_name=sh_load['Sheet1']
	# Load the first sheet into a dataframe
	df = pd.DataFrame(sh_name.range('A1').options(pd.DataFrame, expand='table').value)
	#df = df.drop(0)
	#df = df.reset_index(drop=True)
	# Close the workbook
	app.quit()

#print(df.head)

#Chuong trinh load file excel bang thu vien openpyxl
#Thu vien nay khong ho tro file .xlsm
#Luu file excel vao df
def load_file_openpyxl_xlsx():
	global df
	#Input path file
	Path_to_load_file=input('Nhap duong dan day du file excel can load:\nDEFAUT VALUE')
	if not Path_to_load_file:
		Path_to_load_file=r'E:\WORKING\file_list.xlsx'
	print('LOADING.........!')
	# Load the workbook
	#wb = load_workbook(filename=Path_to_load_file)

	# Select the first sheet
	#sheet = wb.active

	# Convert the sheet to a dataframe
	#df = pd.DataFrame(sheet.values)

	# Set the column names
	#df.columns = [cell.value for cell in sheet[1]]

	# Drop the first row (assuming it's a header row)
	#df = df.drop(0)

	# Reset the index
	#df = df.reset_index(drop=True)
	df = pd.read_excel(Path_to_load_file, engine='openpyxl')

#Chuong trinh liet ke file trong thu muc
#Dung de tim kiem file PO TAM - HD TAM
def list_file_dir():
	global path_po
	while True:
		path_po = input('Nhap duong dan PO TAM - HD TAM:\n')
		if not path_po:
			path_po=r'E:\LUU TAM'
		key_find=input('Nhap tu khoa ten file tim kiem:\n')
		if not key_find:
			key_find='DSG'
		global otc_files
		files = os.listdir(path_po)
		otc_files = [file for file in files if key_find in file and os.path.isfile(os.path.join(path_po, file))]
        #otc_files = [word.lower() for word in otc_files]
		if len(otc_files)<=0:
			print("Khong tim thay PO TAM - HD TAM")
			print("THOAT KHOI CHUONG TRINH")
			break
		else:
			print(f'Danh sach file co tu khoa: {key_find} \n',otc_files)
			print('Tong so file duyet la: ',len(otc_files))
			make_PO()
			continue
		break

#Chuong trinh tao file BBGH theo mau
def make_PO():
	while True:
		chon_file=input('Nhap index file lam viec, index bat dau tu 0:\n')
		if int(chon_file)>len(otc_files)-1:
			print('Nhap lai index file, SO INDEX NHAP VAO VUOT QUA')
			continue
		else:
			break
	f_po=input('Nhap ten PO:\n')
	
    #Khai bao bien, lay thu muc hien hanh
    #dir_path=r'E:\WORKING'
	dir_path=r'E:\WORKING' #os.getcwd()
    #dir_path=os.path.dirname(os.path.realpath(__file__))

    #Khai bao bien file BBGH origin
	f_to='BBGH.xlsm'
    #Lay duong dan va ten file PO
	f_fr=otc_files[int(chon_file)]
    #Khai bao ten PO moi
	f_po1=f_po+'.xlsm'
	finish_path=r'Z:\13. DIEU PHOI HANG\5. BAO TIEU\1 Danh Son\1 DNP-DSG\1 Don hang\2023\Thang 08'
    #KIEM TRA TEN FILE f_fo1 CO TON TAI HAY KHONG
	if os.path.exists(os.path.join(finish_path,f_po1)):
		print("File PO da ton tai, khong thuc hien di chuyen")
	else:
    #Mo chuong trinh che do an cua so
    #app=xw.App()
		app = xw.App(visible=False)
    # Mo 2 file excel de lam viec
		wb_fr=app.books.open(os.path.join(path_po,f_fr))
		wb_to=app.books.open(os.path.join(dir_path,f_to))
    #Chon 2 sheet lam viec
		sh_names1 = wb_fr.sheets
		sh1=sh_names1['Sheet1']
		sh_names2 = wb_to.sheets
		sh2=sh_names2['BBGH']
	#Xoa image trong file
		#pictures = sh2.pictures
		#for picture in pictures:
		#	if picture.width == 100 and picture.height == 100:
		#		picture.delete()
		#images = sh2._images
		#for image in images:
		#	if image.width == 100 and image.height == 100:
		#		image.anchor._from.delete = True
    #Loc vung chua du lieu
		last_row = sh1.used_range.last_cell.row
		list=[]
		for i in range(1, last_row+1):
			cell=sh1.range('I'+str(i)).value
			if cell is not None:
				list=list+[i]
		d1=min(list)
		d2=max(list)

    #vung copy
		data_range=sh1.range('C'+str(d1)+':I'+str(d2)).api.Copy()
    #data_range=sh1.range('C'+str(d1)+':I'+str(d2)).value
    #data_list=data_range.copy()

    #Ten PO
		sh2.range('A6').value=f_po
    #Vung gan gia tri da copy
		sh2.range('B19').api.PasteSpecial(Paste=xlPasteValues)

		wb_to.save(os.path.join(dir_path,f_po1))
		luu_po=os.path.join(dir_path,f_po1)
		print(' DA LUU PO MOI LA:\n',luu_po)
		app.quit()
		
		#app.close()
	#XOA FILE
		#shutil.rmtree(os.path.join(path_po, f_fr))
		#os.remove(os.path.join(path_po,f_fr))

	#THEM TEN PO VAO LIST
		try:
			wb = excel.Workbooks("Theo doi dieu phoi hang di 2023.xlsm")
			print("The file is currently open.")
			ws = wb.Worksheets("DATA")
			last_row = ws.Range("C" + str(ws.Rows.Count)).End(-4162).Row
			ws.Range("C" + str(last_row + 1)).Value = f_po
			#ws.Save()
			print('DA THEM PO',f_po,'VAO FILE THEO DOI PO')

		except Exception as e:
			if "Cannot access" in str(e):
				print("The file is not open.")
			else:
				print("An unknown error occurred:", e)
	#DI CHUYEN FILE

		print("File PO chua co, thuc hien di chuyen file")
		shutil.move(os.path.join(dir_path,f_po1), os.path.join(finish_path,f_po1))
		print('DI CHUYEN THANH CONG FILE DEN:',finish_path,f_po1)
	#XOA FILE
		#shutil.rmtree(os.path.join(path_po, f_fr))
		os.remove(os.path.join(path_po,f_fr))


while True:
	print('888888888888888888888888-----------------------------------------')
	print('888888888888888888888888|Chon 1 de list HD TAM lam PO            |')
	print('888888888888888888888888-----------------------------------------')
	print('888888888888888888888888|Chon 2 de load list file PKN da luu     |')
	print('888888888888888888888888|Tim san pham va so lo                   |')
	print('888888888888888888888888-----------------------------------------')
	print('888888888888888888888888|Chon 3 de list file PKN                 |')
	print('888888888888888888888888|Tim san pham va so lo                   |')
	print('888888888888888888888888|DOI THOI GIAN LOAD FILE CHAM            |')
	print('888888888888888888888888-----------------------------------------')
	print('888888888888888888888888|Chon 4 de list file PKN luu file!!!     |')
	print('888888888888888888888888|THOAT CHUONG TRINH                      |')
	print('888888888888888888888888|DOI THOI GIAN LOAD FILE CHAM            |')
	print('888888888888888888888888------------------------------------------')
	print('LUU Y TRONG MAKE PO CAN:')
	print('      1. CAI DAT DUONG DAN finish_path')
	print('      2. CAI DAT TEN FILE THEO DOI PO wb')
	all_case=input('Chon 1 2 3 4 DE CHON CTR THUC HIEN\nN DE THOAT CHUONG TRINH: ').lower()
	if all_case.lower() == '1':
		list_file_dir()
		#make_PO()

	elif all_case.lower() == '2':
		print('CTR 2 LOAD DU LIEU DA CO VA TIM SAN PHAM - SO LO')
		#load_file_xlwings_xlsx()
		load_file_openpyxl_xlsx()
		while True:		
			tim_kiem_file()
			tiep_tuc=input('Nhap Y de duyet lai thu muc, N de thoat: ').lower()
			if tiep_tuc.lower() == 'y':
				continue
			else:
				print('THOAT KHOI CHUONG TRINH !!!')
			break
		#continue
	elif all_case.lower() == '3':
		print('CTR 3 LOAD LAI TU DAU PKN VA TIM SAN PHAM - SO LO')
		print('THOI GIAN LOAD HOI CHAM..........................')
		list_all_file()
		while True:
			tim_kiem_file()
			tiep_tuc=input('Nhap Y de duyet lai thu muc, N de thoat: ').lower()
			if tiep_tuc.lower() == 'y':
				continue
			else:
				print('THOAT KHOI CHUONG TRINH !!!')
			break
		#continue
	elif all_case.lower() == '4':
		print('CTR 3 RELOAD PKN LUU VA THOAT CHUONG TRINH')
		print('THOI GIAN LOAD HOI CHAM..........................')
		list_all_file()
		#break
	else: 
		break
#print(df.head)
#Goi cac chuong trinh
#tim_kiem_file()
#df.to_excel('file_list.xlsx', index=False)
#saoke_file()
#load_file_xlsx1()
#list_file_dir()
#while True:
#    tiep_tuc=input('Nhap Y de duyet lai thu muc, N de thoat: ')
#    if tiep_tuc.lower() == 'y':
#        tim_kiem_file()
#    else:
#        print('THOAT KHOI CHUONG TRINH !!!')
#        break

'''
	if all_case.lower() == '1':
		print('CTR 1 LIST PO - HD TAM LAM PO')
		path_po = input('Nhap duong dan PO TAM - HD TAM:\n')
		if not path_po:
			path_po=r'E:\LUU TAM'
		key_find=input('Nhap tu khoa ten file tim kiem:\n')
		if not key_find:
			key_find='HD TAM'
		while True:
			list_file_dir()
			make_PO()
			tiep_tuc=input('Nhap Y de duyet lai thu muc, N de thoat: ').lower()
			if tiep_tuc.lower() == 'y':
				continue
			else:
				print('THOAT KHOI CHUONG TRINH !!!')
			break
'''