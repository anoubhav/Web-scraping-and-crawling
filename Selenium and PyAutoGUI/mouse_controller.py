import pyautogui, time

## Depending on your program pyautogui may 'go rogue'. As a failsafe, we may
## move the mouse to the upper left corner of the screen to halt
pyautogui.FAILSAFE = True

## The location of the mouse is provided by an (x, y) pair. This is determined by
## the resolution of the monitor

## You can obtain the size of screen by below command
# print(pyautogui.size())

## Moving the mouse to specific position
# pyautogui.moveTo(100, 100, duration=0.2)

## Move the mouse to a specific location (in a loop)
# for i in range(10):
#    pyautogui.moveTo(100, 100, duration=0.1)
#    pyautogui.moveTo(200, 100, duration=0.1)
#    pyautogui.moveTo(200, 200, duration=0.1)
#    pyautogui.moveTo(100, 200, duration=0.1)

## Move the mouse relative to the starting position of mouse
# pyautogui.moveRel(100, 0, duration=0.2)

## Getting the mouse position
# loc = pyautogui.position()
# print(loc)

## Clicking the mouse
# pyautogui.click(loc)

## Dragging the mouse (moving the mouse while simultaneously clicking). drageTo and dragRel
# pyautogui.dragRel(500, 0, duration=0.3)

## Scrolling the mouse
# time.sleep(5)
# pyautogui.scroll(2000)
time.sleep(5)

# pyautogui.typewrite('Hello')
pyautogui.dragRel(700, 0, duration=0.2)
pyautogui.hotkey('ctrl','c')
pyautogui.moveRel(0,100,duration=0.2)
pyautogui.click()
pyautogui.hotkey('ctrl','v')