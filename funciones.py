import pickle
import keyboard
import pyautogui
import time


class Funciones():
    def escribirArchivo(obj):
        try:
            with open("data.pickle", "wb") as f:
                pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
        except Exception as ex:
            print("Error during pickling object (Possibly unsupported):", ex)

    def leerArchivo():
        filename = "data.pickle"
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception as ex:
            print("Error during unpickling object (Possibly unsupported):", ex)

    def lanzarMacro(macro):
        pyautogui.keyDown('alt')
        time.sleep(.1)
        pyautogui.press('tab')
        time.sleep(.1)
        pyautogui.keyUp('alt')
        pyautogui.write(str(macro))
        print(macro)
        # Ejemplo:
