#passo a passo
import pyautogui
import time

pyautogui.PAUSE = 0.5

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link 
pyautogui.write("https://www.youtube.com/")
pyautogui.press("enter")
time.sleep(3)

#clicar nas inscrições
pyautogui.click(x=67, y=670) # coordenadas do botao de inscricoes

#esperar carregar
time.sleep(3)

#procurar o botao inscrito 

#clicar no botao inscrito
#procurar cancelar inscrição 
#clicr no enter
# repetir para todos
#encerrar quando estiver vazio 