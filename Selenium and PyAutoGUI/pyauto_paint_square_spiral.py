import pyautogui, time
# Gives the user 5 seconds to switch to window where the commands should execute. Here we switch to paint
time.sleep(5)
pyautogui.click()
distance = 400
# Makes a square spiralling inwards
while distance>0:
   pyautogui.dragRel(distance, 0, duration=0.1)
   distance = distance - 10
   pyautogui.dragRel(0, distance, duration=0.1)
   pyautogui.dragRel(-distance, 0, duration=0.1)
   distance = distance - 10
   pyautogui.dragRel(0, -distance, duration=0.1)
