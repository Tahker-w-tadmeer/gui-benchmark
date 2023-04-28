import pyautogui
from screeninfo import get_monitors
import glob
from calculate_time import CalculateTime

monitor = get_monitors()[0]
program_icons = glob.glob("./icons/*")

pyautogui.hotkey('win', 'd')
pyautogui.moveTo(1, 1)
pyautogui.click()

for program in program_icons:
    position = pyautogui.locateOnScreen(
        program,
        confidence=0.8,
        region=(0, 0, 600, monitor.height),
        grayscale=True
    )
    if position is not None:
        position = pyautogui.center(position)
        calc = CalculateTime(lambda: open_program_in_location(position))
        time = calc.execute()
        print(program + ": " + time)


def open_program_in_location(location):
    pyautogui.moveTo(location)
    pyautogui.doubleClick(location)
