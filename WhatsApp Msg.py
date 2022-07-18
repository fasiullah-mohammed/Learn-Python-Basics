import pywhatkit
import pyautogui
"""Now enter the phone with country code, msg, time with hours and mins in 24 hours format, the delay seconds followed by the boolean
to true/false to close the tab"""
pywhatkit.sendwhatmsg('xxxxxxx', 'Msg', 15, 15, 12, True, 10)
pyautogui.press('enter')