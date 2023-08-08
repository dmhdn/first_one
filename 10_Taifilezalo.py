import pyautogui
import time

#import inpdf #import print_pdfs

import os
import glob
import win32api
#import time



def normalize_path(path):
    return path.replace('\\', '/')

def print_pdfs(folder_path):
    # Lay danh sach file pdf
    pdf_files = glob.glob(os.path.join(folder_path, '*.pdf'))
    pdf_files = [normalize_path(file) for file in pdf_files]

    # Vong lap in tung file
    for pdf_file in pdf_files:
        try:
            win32api.ShellExecute(0, "print", pdf_file, None, ".", 0) # None /n:1 in trang 1
            print(f"Dang in file: {pdf_file}")
            time.sleep(5)
            # Xoa file da in
            os.remove(pdf_file)
            print(f"Da xoa file: {pdf_file}")
        except Exception as e:
            print(f"Loi khi in {pdf_file}: {e}")

def wait_for_images(image_actions, action_indexes, wait_time=2, confidence=0.95):
	num_actions = len(image_actions)  # So luong hanh dong
	num_iterations = 30  # So lan lap lai
	
	for _ in range(num_iterations):
		for index in action_indexes:
			if index < 0 or index >= num_actions:
				print(f"Invalid action index: {index}")
				continue
			image_file = list(image_actions.keys())[index]
			action = list(image_actions.values())[index]
			
			while True:
                # Kiem tra hinh anh xuat hien hay khong
				if pyautogui.locateOnScreen(image_file, confidence=confidence) is not None:
                    # Thuc hien hanh dong
					action()

                    # Cho thoi gian thuc hien hanh dong tiep theo
					time.sleep(wait_time)

					break  # Thoat vong lap
				else:
                    # Neu khong tim thay cho thuc hien lai
					time.sleep(wait_time)
		


# Danh sach hanh dong
image_actions = {
    'GroupHD.PNG': lambda: (
        print('Da chon dung group HD'),
    ),
    'hd_moi.PNG': lambda: (
        print('Tim thay hoa don moi gui'),
    ),
    'Taixuong.PNG': lambda: (
        pyautogui.click(pyautogui.locateCenterOnScreen('Taixuong.PNG', confidence=0.95)),
        #pyautogui.typewrite('01319hoa')
    ),
    'ChuaLike.PNG': lambda: (
        pyautogui.click(pyautogui.locateCenterOnScreen('ChuaLike.PNG', confidence=0.95)),
        print_pdfs(folder_path) #pyautogui.typewrite('hoa123')
    ),

 }

action_indexes = [0, 1, 2, 3]
folder_path = 'E:/LUU TAM'
wait_for_images(image_actions, action_indexes)
#print_pdfs(folder_path)
#wait_for_images(image_actions)












'''
time.sleep(10)
x, y = pyautogui.position()
print(f"Current mouse position: ({x}, {y})")
'''