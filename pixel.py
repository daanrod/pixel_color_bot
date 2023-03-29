import time

import pyautogui

LINE_CLEAR = '\x1b[2K'

while True:
    try:
        posXY = pyautogui.position()
        rgb = pyautogui.pixel(posXY[0], posXY[1])
        to_list = list(rgb)
        to_str = str(rgb).strip("()")
        print(
            f"RGB: {to_str} | "
            +
            "HEX: #%02X%02X%02X" % (to_list[0], to_list[1], to_list[2]),
            end="\r"
        )
        print(end=LINE_CLEAR)
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        exit()
