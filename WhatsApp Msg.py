import pywhatkit
import pyautogui
""" In place of xxxxx enter the phone with country code, then for msg (Enter the text you want to send), 15 is the hour (3 PM) and 15 is the min, 12 is the  seconds delay followed by the boolean to true/false for closing the tab"""
pywhatkit.sendwhatmsg('xxxxxxx', 'Msg', 15, 15, 12, True, 10)
pyautogui.press('enter')
