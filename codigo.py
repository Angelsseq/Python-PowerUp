
# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
#pip install 
import pyautogui
import time
#pyautogui.write -> escrever um texto
#pyautogui.click -> clicar com o  mouse
#pyautogui.press -> apertar uma tecla

# abrir o navegador
# apertar a tecla windowns
###pyautogui.PAUSE = 0.5 #da uma pausa de meio segundo depois de cada ação

    
#time.sleep(5) #use esse código caudo queira iniciar o processo apartir da area de trabalho
pyautogui.press("win")
time.sleep(0.4)
pyautogui.write("chrome")
time.sleep(0.5)
pyautogui.press("enter")
pyautogui.sleep(1.5)
pyautogui.click(x=624, y=442, button="left")
#while True:
#    x, y = pyautogui.position() #obtem as cordenadas atuais do mouse
#    print(f"posição do mouse: x={x}, y={y}")
    
    
#entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.sleep(1.5)
pyautogui.write(link)
pyautogui.press("enter")

# Passo 2: Fazer Login
time.sleep(4.5) #dar uma pausa de x(4) segundos
pyautogui.click(x=830, y=473)
pyautogui.write("angelsseq@gmail.com")

pyautogui.press("tab") #tab sempre passa pra próxima aba do formulário
pyautogui.write("senha123456789")
pyautogui.click(x=945, y=655)
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

    
    pyautogui.click(x=882, y=345)#selecionar onde


    #código
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #preço unitário
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")  

    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    #obs  
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
        
    #clicar no enviar
    pyautogui.press("enter")

    #rolar a página para o topo novamente
    pyautogui.scroll(100000)

# Passo 5: Repetir o processo de cadastro até acabar os produtos  
#está acontecendo no if