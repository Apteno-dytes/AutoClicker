import keyboard, pyautogui

# 連打間隔
pyautogui.PAUSE = 0

def clk():
    while True:
        try:
            pyautogui.click()
        except:
            pass
        if keyboard.is_pressed("z"):
            break
keyboard.add_hotkey("x", clk)
keyboard.wait()