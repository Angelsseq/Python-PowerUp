# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
#pip install pyautogui
import pyautogui
import time
#pyautogui.write -> escrever um texto
#pyautogui.click -> clicar com o  mouse
#pyautogui.press -> apertar uma tecla

# abrir o navegador
# apertar a tecla windowns
pyautogui.PAUSE = 0.5 #da uma pausa de meio segundo depois de cada ação

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.sleep(1)
pyautogui.click(x=624, y=442, button="left")
#while True:
#    x, y = pyautogui.position() #obtem as cordenadas atuais do mouse
#    print(f"posição do mouse: x={x}, y={y}")
    

#entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Passo 2: Fazer Login
time.sleep(1.5) #dar uma pausa de 1.5 segundos
pyautogui.click(x=722, y=512)
pyautogui.write("pythonimpressionador@gmail.com")

pyautogui.press("tab") #tab sempre passa pra próxima aba do formulário
time.sleep(1)
pyautogui.write("senha")
pyautogui.click(x=942, y=710)
time.sleep(1.5)

# Passo 3: Importar base de dados
#pip install pandas
import pandas

produtos.csv

# Passo 4: cadastrar 1 produto
# Passo 5: Repetir o processo de cadastro até acabar os produtos  
