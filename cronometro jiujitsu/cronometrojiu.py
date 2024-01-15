from tkinter import *
import time
from tkinter import messagebox
from tkinter import END
from tkinter import font as tkFont
from PIL import Image, ImageTk 
root = Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.title("cronometro jiujitsu")
root.overrideredirect(True)
pausado = False
pausadobt = False
root.configure(background = '#d3d3d3')


canvas123 = Canvas(root, width=root.winfo_screenwidth(), height=200, background='#add8e6' )
canvas123.place(x = 0, y = 150)

def sair():
    root.destroy()
def maxime():
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.overrideredirect(True)
def abas():
    root.overrideredirect(False)

def corkimono1():
    global cor1
    global canvas123
    cor_digitada = cor1.get().lower()

    if cor_digitada == "azul":
        canvas123.configure(background="#add8e6")
    elif cor_digitada == "preto":
        canvas123.configure(background="black")
    elif cor_digitada == "branco":
        canvas123.configure(background="white")
    root.after(1000, corkimono1)  
root.after(1000, corkimono1)


def submit():
    
    try:
        temp = int(minute.get()) * 60 + int(second.get())
    except ValueError:
        messagebox.showerror("Erro", "Insira um tempo válido.")
        print("Valor inválido")
        return
    while temp > -1 and not pausado:
        mins, secs = divmod(temp, 60)
        if mins > 60:
            mins = divmod(mins, 60)
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
        root.update()
        root.after(1000)  
        if temp == 0:
            messagebox.showinfo("Tempo Concluído")
        temp -= 1
def definir():

    global pausado
    pausado = False
def reset_tempo():
    global minute
    global pausado
    global pausadobt
    pausado = True
    time.sleep(1)
    minute.set(6)
    time.sleep(1)
    pausado = False
    btpausar.config(text = "Pausar")
def pausarplusdespausar():
    global pausado
    global pausadobt

    if pausadobt == False:
        pausado = True
        pausadobt = True
        btpausar.config(text = "Despausar")
    else:
        pausado = False
        pausadobt = False
        btpausar.config(text = "Pausar")
        submit()


def kimonoigual():
    global cor1, cor2
    global canvask
    if cor1.get() == cor2.get():
        canvask.configure(height=10)
    else:
        canvask.configure(height=0)
    root.after(1000, kimonoigual)  
root.after(1000, kimonoigual)

def reset_placar():
    global pontos
    global punirt
    pontos.set(0)
    punirt.set(0)
    pontose.set(0)
    punirte.set(0)
    vantagem.set(0)
    vantageme.set(0)
def reset_tempo():
    global minute
    minute.set(6)
    second.set(0)
    global pausado
    pausado = False
    

    if not pausado:
        btpausar.config(text="Pausar")

def botaoponto(valor):
    global pontos
    pontos_antigos =int(pontos.get())
    novo_valor = pontos_antigos + valor
    pontos.set(str(novo_valor))

def punir():
    punicao_atual = int(punirt.get())
    punicao_atual += 1
    punirt.set(str(punicao_atual))


def despunir():
    punicao_atual = int(punirt.get())
    punicao_atual -= 1
    punirt.set(str(punicao_atual))

def vantagemr():
    vantagem_atual = int(vantagem.get())
    vantagem_atual += 1
    vantagem.set(str(vantagem_atual))
def desvantagemr():
    vantagem_atual = int(vantagem.get())
    vantagem_atual -= 1
    vantagem.set(str(vantagem_atual))

def botaopont(valor2):
    global pontose
    pontose_antigos =int(pontose.get())
    novo_valor2 = pontose_antigos + valor2
    pontose.set(str(novo_valor2))

def puni():
    punicaoe_atual = int(punirte.get())
    punicaoe_atual += 1
    punirte.set(str(punicaoe_atual))

def despuni():
    punicaoe_atual = int(punirte.get())
    punicaoe_atual -= 1
    punirte.set(str(punicaoe_atual))
def vantagemre():
    vantageme_atual = int(vantageme.get())
    vantageme_atual += 1
    vantageme.set(str(vantageme_atual))
def desvantagemre():
    vantageme_atual = int(vantageme.get())
    vantageme_atual -= 1
    vantageme.set(str(vantageme_atual))
def corkimono2():
    global cor2
    global canvas12
    cor_digitada1 = cor2.get().lower()

    if cor_digitada1 == "azul":
        canvas12.configure(background="#add8e6")
    elif cor_digitada1 == "preto":
        canvas12.configure(background="black")
    elif cor_digitada1 == "branco":
        canvas12.configure(background="white")
    root.after(1000, corkimono2)  
root.after(1000, corkimono2)



bt1 = Button(width=2,bd=0, bg='gray',font='roboto',text='◱', command=abas)
bt1.place(x=1450, y=0)
bt2 = Button(width=2, bg='gray',bd=0,font='roboto',text='□', command=maxime)
bt2.place(x=1475, y=0)
bt3 = Button(width=3, bg='gray', bd=0 ,font='roboto',text='X', command=sair)
bt3.place(x=1500, y=0)

minute = StringVar()
second = StringVar()
minute.set("6")
second.set("0")

pontos = StringVar()
pontos.set("0")
pontose = StringVar()
pontose.set("0")

minuteEntry = Entry(root, bd='0',width=2, font=("Arial", 66, ""), textvariable=minute, justify = 'center')
minuteEntry.place(x=530, y=30)
secondEntry = Entry(root, bd='0',width=2, font=("Arial", 66, ""), textvariable=second, justify = 'center')
secondEntry.place(x=660, y=30)

btpausar = Button(root,  width = 13,bd = 0,text ="Pausar", font=("arial", 18, "bold"), bg='gray', command=lambda:pausarplusdespausar(), justify='center')
btpausar.place(x = 900, y = 85)

btn = Button(root, text='Iniciar Tempo', bg='#00008B',fg = 'white', font=("arial", 22, ""), bd='1', command=lambda: [submit(), definir])
btn.place(x=900, y=30)

btnqd = Button(root, text="queda/raspagem", bd='5', command=lambda: botaoponto(2))
btnqd.place(x=300, y=300)
btnqd = Button(root, text="passagem de guarda", bd='5', command=lambda: botaoponto(3))
btnqd.place(x=430, y=300)
btnqd = Button(root, text="Costas/montada", bd='5', command=lambda: botaoponto(4))
btnqd.place(x=570, y=300)
btnqd = Button(root, text="joelho na barriga", bd='5', command=lambda: botaoponto(2))
btnqd.place(x=700, y=300)
btnqd = Button(root, text="ponto", bd='5', command=lambda: botaoponto(1))
btnqd.place(x=825, y=300)


pontosentry = Entry(root, width=2, font=("arial", 96,"",), textvariable=pontos, justify = 'center')
pontosentry.place(x= 1390, y=150)

btreset = Button(root, text="resetar placar", bd=5, command=lambda: reset_placar())
btreset.place(x= 1385, y=353)


btresettempo = Button(root, font=("arial", 10, "bold"),text="resetar tempo", bd=0, command=reset_tempo)
btresettempo.place(x=1101, y=85)

btpunicao = Button(root, text="PUNIÇÃO", bd=1, font=("arial", 14,"bold"), bg= 'red', command=lambda:punir())
btpunicao.place(x= 900, y=300)
btremoverpunicao = Button(root, bd=1,text="Retroceder punição", font=("arial", 10,"bold"), bg='gray', command=lambda:despunir())
btremoverpunicao.place(x=903, y=375)
punirt = StringVar()
punirt.set("0")
punirte = StringVar()
punirte.set("0")
vantagem = StringVar()
vantagem.set("0")
vantageme = StringVar()
vantageme.set("0")
punirentry = Entry(root,bd=0, width=2, font=("arial", 32, "bold"), bg='red',textvariable=punirt, justify = 'center')
punirentry.place(x=1391, y=297)

vantagementry = Entry(root, bd=0, width = 2, font=("arial", 32,"bold"), bg="lightgreen",textvariable=vantagem, justify='center')
vantagementry.place(x= 1490, y=297)
btvantagem = Button(root, text= "VANTAGEM", bd=1, font=("arial", 14,"bold"), bg='lightgreen', command=lambda:vantagemr())
btvantagem.place(x= 1000, y=300)
btvantagem = Button(root, text= "Retroceder vantagem", bd=1, font=("arial", 10,"bold"), bg='gray', command=lambda:desvantagemr())
btvantagem.place(x= 1037, y=375)
btvantagem = Button(root, text= "Retroceder pontuação", bd=1, font=("arial", 10,"bold"), bg='gray', command=lambda:botaoponto(-1))
btvantagem.place(x= 755, y=375)
canvask = Canvas(root, width=root.winfo_screenwidth(), height =10, bg= 'green')
canvask.place(x=0, y=650)
canvas12 = Canvas(root, width=root.winfo_screenwidth(), height=200, background='#add8e6' )
canvas12.place(x = 0, y = 450)

btnqd = Button(root, text="queda/raspagem", bd='5', command=lambda: botaopont(2))
btnqd.place(x=300, y=600)
btnqd = Button(root, text="passagem de guarda", bd='5', command=lambda: botaopont(3))
btnqd.place(x=430, y=600)
btnqd = Button(root, text="Costas/montada", bd='5', command=lambda: botaopont(4))
btnqd.place(x=570, y=600)
btnqd = Button(root, text="joelho na barriga", bd='5', command=lambda: botaopont(2))
btnqd.place(x=700, y=600)
btnqd = Button(root, text="ponto", bd='5', command=lambda: botaoponto(1))
btnqd.place(x=825, y=600)


pontosentry = Entry(root, width=2, font=("arial", 96,"",), textvariable=pontose, justify = 'center')
pontosentry.place(x= 1390, y=450)

btpunicao = Button(root, text="PUNIÇÃO", bd=1, font=("arial", 14,"bold"), bg= 'red', command=lambda:puni())
btpunicao.place(x= 900, y=600)

punirentry = Entry(root,bd=0, width=2, font=("arial", 32, "bold"), bg='red',textvariable=punirte, justify = 'center')
punirentry.place(x=1391, y=597)
btvantagem = Button(root, text= "Retroceder vantagem", bd=1, font=("arial", 10,"bold"), bg='gray', command=lambda:desvantagemre())
btvantagem.place(x= 1037, y=675)
btremoverpunicao = Button(root, bd=1,text="Retroceder punição", font=("arial", 10,"bold"), bg='gray', command=lambda:despuni())
btremoverpunicao.place(x=903, y=675)
btvantagem = Button(root, text= "Retroceder pontuação", bd=1, font=("arial", 10,"bold"), bg='gray', command=lambda:botaopont(-1))
btvantagem.place(x= 755, y=675)
vantagementry = Entry(root, bd=0, width = 2, font=("arial", 32,"bold"), bg="lightgreen",textvariable=vantageme, justify='center')
vantagementry.place(x= 1490, y=597)
btvantagem = Button(root, text= "VANTAGEM", bd=1, font=("arial", 14,"bold"), bg='lightgreen', command=lambda:vantagemre())
btvantagem.place(x= 1000, y=600)

cor1 = StringVar()
cor2 = StringVar()
cor1.set("azul")  
cor2.set("azul")
entryteste1 = Entry(root, bd=2, width=7, font=("arial", 18, "bold"), bg='gray', textvariable=cor1)
entryteste1.place(x=200, y=700)

entryteste2 = Entry(root, bd=2, width=7, font=("arial", 18, "bold"), bg='gray', textvariable=cor2)
entryteste2.place(x=600, y=700)


Label1 = Label(root,width =30, text="Cor do kimono 2", font=("arial", 8, "bold"), bg="#d3d3d3") 
Label1.place(x=600, y=680)

Label = Label(root, text="Cor do kimono 1", font=("arial", 8, "bold"), bg="#d3d3d3") 
Label.place(x=200, y=680)



root.mainloop()
