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
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# Passo 2: Fazer Login
time.sleep(1.5) #dar uma pausa de 1.5 segundos
pyautogui.click(x=722, y=512)
pyautogui.write("pythonimpressionador@gmail.com")

pyautogui.press("tab") #tab sempre passa pra próxima aba do formulário
time.sleep(1)
pyautogui.write("senha123456789")
pyautogui.click(x=942, y=710)
time.sleep(1.5)

# Passo 3: Importar base de dados
#pip install pandas
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)
# Passo 4: cadastrar 1 produto



linha = 0
#para cada linha da tabela executar comandos
for linha in tabela.index: 

    pyautogui.click(x=759, y=369)#selecionar onde


    #código
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    time.sleep(1)

    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    time.sleep(1)

    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    time.sleep(1)

    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    time.sleep(1)

    #preço unitário
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    time.sleep(1)

    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    time.sleep(1)

    #obs
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    time.sleep(1)

    #clicar no enviar
    pyautogui.press("enter")
    pyautogui.scroll(100000)
    #pyautogui.click()

# Passo 5: Repetir o processo de cadastro até acabar os produtos  
