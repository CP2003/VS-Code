import pyautogui, time
time.sleep(5)
f = open("text.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("numlock")
    time.sleep(0)
    pyautogui.press("numlock")
    pyautogui.press("enter")
    time.sleep(0)
