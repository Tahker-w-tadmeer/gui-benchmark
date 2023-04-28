import pyautogui
from screeninfo import get_monitors
import glob
import time


def open_program_in_location(location):
    pyautogui.moveTo(location)
    pyautogui.doubleClick(location)


def go_to_desktop():
    time.sleep(1)
    pyautogui.hotkey('win', 'd')
    pyautogui.moveTo(1, 1)
    pyautogui.click()


def get_pixel_in_center():
    pyautogui.moveTo(monitor.width // 2, monitor.height // 2)
    return pyautogui.screenshot().getpixel((monitor.width // 2, monitor.height // 2))


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
        color_before = get_pixel_in_center()
        start = time.time_ns()
        open_program_in_location(position)
        while get_pixel_in_center() == color_before:
            pass
        end = time.time_ns()
        exec_time = end - start
        name = program.split("\\")[1].split(".")[0]
        print(name + ": " + str(exec_time) + " ns")
