import time

import pyautogui

while True:
    try:
        posXY = pyautogui.position()
        rgb = pyautogui.pixel(posXY[0], posXY[1])
        to_list = list(rgb)
        to_str = str(rgb).strip("()")
        print(
            f"RGB: {to_str} | "
            + 
             "HEX: #%02X%02X%02X" % (to_list[0], to_list[1], to_list[2])
        )
        time.sleep(0.5)
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        exit()
