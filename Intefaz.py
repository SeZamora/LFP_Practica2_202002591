import imp
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from analizador import AnalizadorLexico
import subprocess
class Inicio:
    def CargarArchivo(self):
        root = Tk()
        root.withdraw()
        root.update()
        pathString = askopenfilename(filetypes=[("Text files","*.gpw")])
        if pathString:
            openFile = open(pathString,'r')
            ArchivoEntrada = openFile.read()
        root.destroy()
        self.inputtxt.delete(1.0,END)
        self.inputtxt.insert(1.0,ArchivoEntrada)
    
    def Analizar(self):
        lexico = AnalizadorLexico()
        ArchivoAnalizar= self.inputtxt.get("1.0",END)
        lexico.AnalizadorLexico(ArchivoAnalizar)
        lexico.Html()
        lexico.css()
    
    def manual_tecnico(self):
        path = ("C:\\Users\\SEBASTIAN ZAMORA\\Desktop\\[LFP]PROYECTO2_A-_202002591\\Manual Tecnico.pdf")
        subprocess.Popen([path], shell=True)
  
    def manual_usuario(self):
        path = ("C:\\Users\\SEBASTIAN ZAMORA\\Desktop\\[LFP]PROYECTO2_A-_202002591\\Manual de usuario.pdf")
        subprocess.Popen([path], shell=True)
        
    def abrir(self):
        inicio = tk.Tk()
        inicio.geometry("1800x900")
        inicio.title('Pagina Principal')

        frame_derecha = tk.Frame(inicio, bd=0,
        relief=tk.SOLID, bg='#fcfcfc')
        frame_derecha.pack(side="right", expand=tk.YES, fill=tk.BOTH)

        frame_izquierda = tk.Frame(inicio, bd=0,
        relief=tk.SOLID, bg='#fcfcfc')
        frame_izquierda.pack(side="left", expand=tk.YES, fill=tk.BOTH)
        #Archivo
        la = tk.Label( frame_izquierda,text="Archivo")
        la.pack(fill=tk.X, padx=20, pady=50)
        btn = tk.Button(frame_izquierda,text="Abrir", command=self.CargarArchivo)
        btn.pack(fill=tk.X, padx=20, pady=1)


        btn = tk.Button(frame_izquierda,text="Analizar", command=self.Analizar)
        btn.pack(fill=tk.X, padx=20, pady=15)

        btn = tk.Button(frame_izquierda,text="Salir", command=inicio.destroy)
        btn.pack(fill=tk.X, padx=20, pady=15)

        #Ayuda
        la = tk.Label( frame_izquierda,text="Ayuda")
        la.pack(fill=tk.X, padx=25, pady=35)
        btn = tk.Button(frame_izquierda,text="Manual de usuario", command=self.manual_usuario)
        btn.pack(fill=tk.X, padx=20, pady=1)

        btn = tk.Button(frame_izquierda,text="Manual Técnico", command=self.manual_tecnico)
        btn.pack(fill=tk.X, padx=20, pady=15)

        btn = tk.Button(frame_izquierda,text="Temas Ayudas")
        btn.pack(fill=tk.X, padx=20, pady=15)

        #text
        self.inputtxt = tk.Text(frame_derecha, height = 35, width = 85,
                bg = "light yellow")
        self.inputtxt.pack(fill=tk.X, padx=20, pady=50)
        
        inicio.mainloop()  
