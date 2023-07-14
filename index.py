import pickle
from tkinter import *
from tkinter import ttk
from funciones import Funciones


class MyClass():
    def __init__(self):
        self.macros = Funciones.leerArchivo()
        self.raiz = Tk()
        self.raiz.geometry('200x900+0+0')
        # self.raiz.resizable(0,0)
        self.raiz.title("Ventana de aplicación")
        self.raiz.iconbitmap("oveja.ico")
        self.raiz.attributes('-topmost', True)
        self.espacioBotones = Frame(self.raiz)
        self.espacioBotones.grid(row=2, column=0, columnspan=2)
        conteo = 0
        for i in self.macros:
            Button(self.espacioBotones,
                   text=i["macroNombre"],
                   command=lambda codigoMacro=i["macroCodigo"]: Funciones.lanzarMacro(
                       codigoMacro)).grid(row=conteo, column=0, padx=10, pady=10)
            conteo = +1
        self.raiz.mainloop()


def save_object(obj):
    try:
        with open("data.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)


def load_object():
    filename = "data.pickle"
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)


def main():
    # Insertamos datos demo
    # macrosInsertar = [
    #     {
    #         "macroNombre": "Macro 1",
    #         "macroCodigo": "Hola"
    #     },
    #     {
    #         "macroNombre": "Macro 2",
    #         "macroCodigo": "adios"
    #     }
    # ]
    # save_object(macrosInsertar)
    mi_app = MyClass()
    return (0)


if __name__ == '__main__':
    main()

# # Leemos y mostramos
