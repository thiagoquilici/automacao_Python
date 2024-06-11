# importação biblioteca
import pyautogui as auto
# import time

# define espera para cada comando auto
auto.PAUSE = 0.5

# abre o menu iniciar. "win" é a tecla "inciar" do teclado.
auto.press('win')

# abre o "chrome"
auto.write('chrome')
auto.press('enter')

# maximizar tela
auto.hotkey('alt', 'space',)
auto.press('x')

# abre o github
auto.write('github.com')
auto.press('enter')

# abre o classroom em uma nova guia

# atrasa o comando de uma linha específica
# time.sleep(1)

auto.hotkey('ctrl', 't')
auto.write('classroom.google.com')
auto.press('enter')