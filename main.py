import pyautogui
from screeninfo import get_monitors
import glob
from calculate_time import CalculateTime
import time


def open_program_in_location(location):
    pyautogui.moveTo(location)
    pyautogui.doubleClick(location)


def go_to_desktop():
    time.sleep(1)
    pyautogui.hotkey('win', 'd')
    pyautogui.moveTo(1, 1)
    pyautogui.click()


monitor = get_monitors()[0]
program_icons = glob.glob("./icons/*")

for program in program_icons:
    go_to_desktop()

    position = pyautogui.locateOnScreen(
        program,
        confidence=0.6,
        region=(0, 0, 600, monitor.height),
        grayscale=False
    )
    if position is not None:
        position = pyautogui.center(position)
        calc = CalculateTime(lambda: open_program_in_location(position))
        exec_time = calc.execute()
        name = program.split("\\")[1].split(".")[0]
        print(name + ": " + str(exec_time) + "ns")
