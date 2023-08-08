import glob
import yagmail

def khaibaomail():
	ten_po=input('Nhap so PO: ')
	folder_path = r"Z:\13. DIEU PHOI HANG\5. BAO TIEU\1 Danh Son\1 DNP-DSG\1 Don hang\2023\Thang 08"  # Duong dan thu muc

	#Liet ke danh sach file dinh kem theo PO
	pdf_files = glob.glob(folder_path + "\\" + ten_po + "\\*.pdf")  # Danh sach file PDF
	jpg_files = glob.glob(folder_path +  "\\" + ten_po + "\\*.jpg")  # Danh sach file JPG
	danhsach_file = []  # List danh sách tệp tin
	danhsach_file.extend(pdf_files)  # Them file PDF vao list
	danhsach_file.extend(jpg_files)  # Them file JPG vao list

	#Danh sach mail nguoi nhan
	#to = ['recipient1@example.com', 'recipient2@example.com']  # Form danh sach nguoi nhan
	DAP_MN=['dungln@daplogistics.vn','duyenntn@daplogistics.vn','sonnh@daplogistics.vn','nghiann@daplogistics.vn','thaclb@daplogistics.vn','nhottb@daplogistics.vn','bichthoa89@gmail.com','tra.vy.danapha@gmail.com','nam.vo@danapha.com']
	DAP_MB=['tra.vy.danapha@gmail.com','nam.vo@danapha.com','thuylb@ds-group.vn','nhungnt@daplogistics.vn']
	DAP_MT=['minhhoavosadn@gmail.com']


	# Thong tin tai khoan
	email = 'hoa.danapha@gmail.com'  # Dia chi email
	password = 'kmtjoloqsxwznfnb'  # Mat khau email

	# Tao doi tuong yagmail
	yag = yagmail.SMTP(email, password)

	# Noi dung cua email
	#Thiet lap nguoi nhan
	nguoinhan=ten_po.split(' ')[-1]
	if nguoinhan == 'DAP.MN':
		to=DAP_MN
	elif nguoinhan =='DAP.MB':
		to=DAP_MB

	elif nguoinhan =='DAP.MT':
		to= DAP_MT

	subject = f'PKN theo PO so {ten_po}'  # Tieu de email
	# Noi dung email
	body = '''Dear All,
	Hoa gui PKN theo file dinh kem

	Tran trong.
	Duong Minh Hoa
	Phone: 0905686872
	'''
	attachments = danhsach_file  # Danh sach file dinh kem
	#print(attachments)

	#Kiem tra file dinh kem 2
	if not attachments:
		print(f'{attachments}. Khong thuc hien gui email khi khong co file dinh kem!')
		SystemExit
	else:
		#sendmail()
		yag.send(to=to, subject=subject, contents=body, attachments=attachments)
		yag.close()
		print(f'Email sent to: {nguoinhan}\n{attachments}')
'''
#Session send mail
def sendmail():
    # Send mail
    yag.send(to=to, subject=subject, contents=body, attachments=attachments)
    # Dong ket noi
    yag.close()
    print(f'Email sent to: {nguoinhan}\n{attachments}')
'''
while True:
	khaibaomail()
	tiep_tuc=input('Nhap Y de tiep tuc gui email, N de thoat: ').lower()
	if tiep_tuc.lower() == 'y':
		continue
	else:
		print('THOAT KHOI CHUONG TRINH !!!')
	break