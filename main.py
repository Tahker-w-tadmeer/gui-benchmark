import pyautogui
from screeninfo import get_monitors

monitor = get_monitors()[0]
program_icons = [
    'someButton.png',
]

for program in program_icons:
    position_of_program = pyautogui.locateOnScreen(program, region=(0, 0, 400, monitor.height))
    if position_of_program is not None:
        pyautogui.doubleClick(position_of_program)

