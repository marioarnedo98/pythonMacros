import pickle
from tkinter import *
from tkinter import ttk


 
class MyClass():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.geometry('300x200+500+50')
        # self.raiz.resizable(0,0)
        self.raiz.title("Ventana de aplicación")
        self.espacioBotones = Frame(self.raiz)
        self.espacioBotones.grid(row=2, column=0, columnspan=2)
        for i in range(11):
            Button(self.espacioBotones, text='Abrir'+str(i)).grid(row=0, column=i, padx=10,pady=10)
        self.raiz.mainloop()
 
def save_object(obj):
    try:
        with open("data.pickle", "wb") as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)
    except Exception as ex:
        print("Error during pickling object (Possibly unsupported):", ex)
 
def load_object(filename):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error during unpickling object (Possibly unsupported):", ex)
 
def main():
    mi_app = MyClass()
    return (0)

if __name__ == '__main__':
    main()
# Insertamos
# obj = ['one', 2, [3, 4, 5]]
# save_object(obj)

# # Leemos y mostramos
# obj = load_object("data.pickle")
# print(obj)