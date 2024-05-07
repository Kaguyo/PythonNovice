# Passo a passo do projeto
  #1. Abrir o sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Após instalar pyautogui (pip install pyautogui_)
  # Importe biblioteca pyautogui
import pyautogui
import time # biblioteca com sistema de timing

pyautogui.PAUSE = 0.7
# Alguns comandos do pyautogui:
    # pyautogui.click -> clicar com o mouse
    # pyautogui.write -> escrever um texto
    # pyautogui.press -> pressionar uma tecla do teclado
    # pyautogui.hoykey -> apertar um conjunto de teclas (Ctrl C, Ctrl V, Alt Tab)
        #Source : https://pyautogui.readthedocs.io/en/latest/quickstart.html
        
# abrir o navegador (Firefox)
pyautogui.press("win")
pyautogui.write("mozila")
pyautogui.press("enter")

# entrar no site do sistema

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

    # Carregamentos podem comprometer o código, prestar atenção nas pausas.
time.sleep(1)

#2. Fazer Login
pyautogui.click(x=594, y=402)
pyautogui.write("gabrieltroop27@gmail.com")
pyautogui.press("tab")

pyautogui.write("XjhzuYsiOPajz")
pyautogui.press("tab")

pyautogui.press("enter")

time.sleep(3)



#3. Abrir/impportar a base de dados de produtos para cadastrar
    # pip install pandas numpy openpyxl
    
import pandas as pd # as/como serve para mudar o nome do item importado para um nome que queira

    #Tip Tabula transforms pdf files into pandas
    
tabela_produtos = pd.read_csv("produtos.csv")
print(tabela_produtos)


#4. Cadastrar um produto

for linha in tabela_produtos.index:
    codigo = str(tabela_produtos.loc[linha, "codigo"])
        # Preencher formulário
            # Passa para proximo campo
    pyautogui.press("tab")
        # Preenche código de produto
    pyautogui.write(codigo)
        # Passa para proximo campo
    pyautogui.press("tab")
        # Preencher marca
    pyautogui.write(str(tabela_produtos.loc[linha, "marca"]))
        # Passa para proximo campo
    pyautogui.press("tab")
        # Preencher tipo
    pyautogui.write(str(tabela_produtos.loc[linha, "tipo"]))
        # Passa para proximo campo
    pyautogui.press("tab")
        # Preencher categoria
    pyautogui.write(str(tabela_produtos.loc[linha, "categoria"]))
        # Passa para proximo campo
    pyautogui.press("tab")
        # Preencher preco
    pyautogui.write(str(tabela_produtos.loc[linha, "preco_unitario"]))
        # Passa para proximo campo
    pyautogui.press("tab")
        # Preencher custo
    pyautogui.write(str(tabela_produtos.loc[linha, "custo"]))
        # Passa para proximo campo
    pyautogui.press("tab")
        # Preencher obs
    obs = str(tabela_produtos.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
        # Passa para proximo campo
    pyautogui.press("tab")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.press("home")

#5. Repetir Isso tudo até acabar a lista de produtos

