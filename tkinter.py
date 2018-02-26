from tkinter import *

from functools import partial

instancia = Tk()

class enviando(object):
    def __init__(self, instancia):

        self.font = ('Verdana', '20', 'bold') #font-family, font-size, text-style
        self.font2 = ('Verdana', '14', 'bold') #font-family, font-size, text-style

        logo = PhotoImage(file = 'img/python.ppm')

        #frame que contem o checkbuttons
        self.frame1 = Frame(instancia)

        #frame que contem o checkbuttons
        self.framec = Frame(instancia)

        #Frame que contem a entrada de texto
        self.frame2 = Frame(instancia)

        #Frame que contem  o botao
        self.frame3 = Frame(instancia)

        #Frame que contem o texto
        self.frame4 = Frame(instancia, pady = 20)

        #Frame que contem botoes especificos
        self.frame5 = Frame(instancia)

        #Empacotando as frames
        self.frame1.pack()
        self.framec.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        self.frame5.pack()

        #logo da aplicação
        self.logo = Label(self.frame1)
        self.logo['image'] = logo
        self.logo.image = logo
        self.logo.pack()

        #checkbutton
        self.bino_s = False
        self.b_binomial = Checkbutton(self.framec, text = 'Modo Preciso', bg = 'blue', font = self.font, command = self.AtivaBinomial)
        self.b_binomial.pack()
        
        #entrada de texto
        self.form = Entry(self.frame2)
        self.form.pack()

        #entrada das matrizes // via user
        lb = {}
        ordem = int(input("Ordem>>"))

        #entrada dos valores da matriz seguindo a ordem

        for o in range(0, ordem*ordem):
            if o % ordem == 0:
                subframe = Frame(self.frame5)
                subframe.pack()
            lb[o] = Entry(subframe, width = 7)
            lb[o].pack(side = LEFT)

        self.send = Button(self.frame3, text = "Enviar Matriz", bg = "#323", command = self.enviarM, font = self.font) #enviando Matriz
        self.send.pack()
        

        #botao
        self.enviar = Button(self.frame3, text = "Enviar", bg = "#323", command = self.enviar, font = self.font)
        self.enviar.pack()

        #texto
        self.texto = Label(self.frame4, text ="Sucesso", fg = "blue", font = self.font2)
        self.texto.pack()

        botoes = ('Matriz Transpostas', 'Matriz Inversa', 'Determinante', 'Produto das Matrizes', 'Precisão Máxima')
        
        for i in range(len(botoes)):
            if i % 3 == 0:
                subframe = Frame(self.frame5)
                subframe.pack()
            a = Button(subframe, text = botoes[i], bg = 'green', width = 25, padx = 5, command = (partial(self.ColocaTexto, botoes[i]))) #classe 'partial' que introduz uma função
            a.pack(side = LEFT) #alinhando a esquerda da linha original*

        self.delete = Button(subframe, text = 'del', bg = 'red', width = 25, padx = 5, command = self.Del)
        self.delete.pack(side = LEFT)

    def Del(self):
        self.form.delete(0 , END)

    def ColocaTexto(self, texto):
        self.form.delete(0 , END)
        self.form.insert(END , texto)
        

    def MSG(self, text, cor = 'red'):
        self.texto['text'] = text
        self.texto['fg'] = cor
        

    def enviar(self):
        self.MSG(self.form.get(), 'green')
        self.form.delete(0, END)

    def enviarM(self):
        self.MSG(self.send.get(), 'green')
        
            
    def AtivaBinomial(self):
        self.bino_s = not self.bino_s
        if self.bino_s:
            self.MSG('Binomial Ativado')
        else:
            self.MSG('Binomial Desativado', cor = 'black')



#instancia da aplicação
enviando(instancia)

instancia.title('Matrizes - §marcos_troia')

instancia.geometry("800x600")



instancia.mainloop()
