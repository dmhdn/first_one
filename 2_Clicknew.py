'''
import pyautogui
import time

def click_action(image):
    center = pyautogui.locateCenterOnScreen(image, confidence=0.9)
    if center is not None:
        pyautogui.click(center)

def double_click_action(image):
    center = pyautogui.locateCenterOnScreen(image, confidence=0.9)
    if center is not None:
        pyautogui.doubleClick(center)

def type_action(image, text):
    center = pyautogui.locateCenterOnScreen(image, confidence=0.9)
    if center is not None:
        pyautogui.click(center)
        pyautogui.typewrite(text)

def wait_for_images(image_actions, wait_time=2):
    for image, action_type, action_param in image_actions:
        while True:
            # Kiem tra hinh anh xuat hien
            if pyautogui.locateOnScreen(image) is not None:
                # Thuc hien hanh dong
                if action_type == 'click':
                    click_action(action_param)
                elif action_type == 'double_click':
                    double_click_action(action_param)
                elif action_type == 'type':
                    type_action(action_param[0], action_param[1])
                break  # Thoat khoi vong lap
            else:
                # Neu khong thi cho va kiem tra lai
                time.sleep(wait_time)

# Danh sach hinh anh va hanh dong tuong ung
image_actions = [
    ('bfo.PNG', 'click', None),
    ('userid.PNG', 'type', ('userid.PNG', '01319hoa')),
    ('password.PNG', 'type', ('password.PNG', 'hoa@123')),
    ('signin.PNG', 'click', None),
    ('modules.PNG', 'click', None),
    ('qlbh.png', 'click', None),
    ('khdh.png', 'double_click', None),
    ('dathang.png', 'double_click', None),
    ('modulesmo.png', 'click', None),
    ('qlkcn.png', 'click', None),
    ('dieunoibo.png', 'double_click', None),
    ('dhnbcx.png', 'double_click', None),
]

wait_for_images(image_actions)

'''
import pyautogui
import time
'''
def wait_for_images(image_actions, wait_time=2, confidence=0.9):
    for image_file, action in image_actions.items():
        while True:
            # Kiem tra hinh anh xuat hien hay khong
            if pyautogui.locateOnScreen(image_file) is not None:
                # thuc hien hanh dong tuong ung
                action()
                break  # Thoat vong lap
            else:
                # Neu khong thi cho va kiem tra lai
                time.sleep(wait_time)
'''
def wait_for_images(image_actions, action_indexes, wait_time=2, confidence=0.9):
	num_actions = len(image_actions)  # So luong hanh dong
	num_iterations = 1  # So lan lap lai
	
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
    'bfo.PNG': lambda: (
        pyautogui.click(pyautogui.locateCenterOnScreen('bfo.PNG', confidence=0.9)),
    ),
    'userid.PNG': lambda: (
        pyautogui.click(pyautogui.locateCenterOnScreen('userid.PNG', confidence=0.9)),
        pyautogui.typewrite('01319hoa')
    ),
    'password.PNG': lambda: (
        pyautogui.click(pyautogui.locateCenterOnScreen('password.PNG', confidence=0.9)),
        pyautogui.typewrite('hoa123')
    ),
    'signin.PNG': lambda: (
        pyautogui.click(pyautogui.locateCenterOnScreen('signin.PNG', confidence=0.9)),
    ),
    'modules.PNG': lambda: (
        pyautogui.click(pyautogui.locateCenterOnScreen('modules.PNG', confidence=0.9)),
    ),
    'qlbh.png': lambda: (
        pyautogui.click(pyautogui.locateCenterOnScreen('qlbh.png', confidence=0.9)),
    ),
    'khdh.png': lambda: (
        pyautogui.doubleClick(pyautogui.locateCenterOnScreen('khdh.png', confidence=0.9)),
    ),
    'dathang.png': lambda: (
        pyautogui.doubleClick(pyautogui.locateCenterOnScreen('dathang.png', confidence=0.9)),
    ),
    'modulesmo.png': lambda: (
        pyautogui.click(pyautogui.locateCenterOnScreen('modulesmo.png', confidence=0.9)),
    ),
    'qlkcn.png': lambda: (
        pyautogui.click(pyautogui.locateCenterOnScreen('qlkcn.png', confidence=0.9)),
    ),
    'dieunoibo.png': lambda: (
        pyautogui.doubleClick(pyautogui.locateCenterOnScreen('dieunoibo.png', confidence=0.9)),
    ),
    'dhnbcx.png': lambda: (
        pyautogui.doubleClick(pyautogui.locateCenterOnScreen('dhnbcx.png', confidence=0.9)),
    ),
}

action_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
wait_for_images(image_actions, action_indexes)
#wait_for_images(image_actions)












'''
time.sleep(10)
x, y = pyautogui.position()
print(f"Current mouse position: ({x}, {y})")
'''