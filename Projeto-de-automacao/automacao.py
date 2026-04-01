import pyautogui 
import time

pyautogui.PAUSE= 0.5 # Não causar conflito no codigo, rodando tudo de vez


pyautogui.press("win")
pyautogui.write("whatsapp")
pyautogui.press("enter")
time.sleep(20) #Tempo pro programa carregar 
pyautogui.click (x=196, y=125)
pyautogui.write("Nome do contato")
pyautogui.press("enter")
pyautogui.write("Mensagem a ser enviada")
pyautogui.press("enter")
