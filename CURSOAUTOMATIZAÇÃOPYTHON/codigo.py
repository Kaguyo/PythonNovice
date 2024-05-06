# Passo a passo do projeto
  #1. Abrir o sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Após instalar pyautogui (pip install pyautogui_)
  # Importe biblioteca pyautogui
import pyautogui

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
#2. Fazer Login
#3. Abrir/impportar a base de dados de produtos para cadastrar
#4. Cadastrar um produto
#5. Repetir Isso tudo até acabar a lista de produtos

