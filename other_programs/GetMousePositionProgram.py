import pyautogui

def getMousePosition():
    try:
        while True:
            x,y = pyautogui.position()
            print('X :'+str(x)+'Y :'+str(y))
    except KeyboardInterrupt:
        print('Done')


getMousePosition()
#pyautogui.click(0,5)
pyautogui.middleClick()
print('Middle click operation Done')
