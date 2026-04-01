import pyautogui
from time import sleep

pyautogui.click(1273,203, duration=1)
pyautogui.press("enter")
sleep(3)
pyautogui.click(966,622, duration=2)
pyautogui.write("123")
pyautogui.press("enter")
sleep(2)
pyautogui.press('enter')
#clicar novo produto
pyautogui.click(30,40, duration= 1)
#add produto
with open('produtos_itens.txt' , 'r') as arquivo:
    for linha in arquivo:
        id_prod = linha.split(",")[0]
        nome = linha.split(",")[1]
        qntd = linha.split(",")[2]
        preco = linha.split(",")[3]


        pyautogui.click(223,88, duration= 1)
        pyautogui.write(id_prod)
        pyautogui.click(215,150, duration= 1)
        pyautogui.write(nome)
        pyautogui.click(205,220, duration= 1)
        pyautogui.write(qntd)
        pyautogui.click(208,274, duration= 1)
        pyautogui.write(preco)
        pyautogui.click(233,326, duration=1)
        sleep(1)
        pyautogui.press('enter')
        


       



