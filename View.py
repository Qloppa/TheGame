from tkinter import *
import tkinter as tk
from PIL import ImageTk
from PIL import Image

_GAME_ICON = "resources/THE_GAME_ICON.ico"

root = None
handkartenFrame = None
background = None
up = None
down = None

def createWindow():
    global root
    root = Tk()
    root.title("THE GAME!")
    root.iconbitmap(_GAME_ICON)
    root.geometry("1920x1080")
    root.attributes('-fullscreen', True)
    createMenu()
    return root

# """-----------------------------------MENU---------------------------------------#
def doNothing():
    print("OK, I do Nothing")

def aboutTG(TG_Version, rev):
    newWindow = Toplevel(root)
    newWindow.title("Über The Game")
    newWindow.iconbitmap(_GAME_ICON)
    newWindow.geometry("250x60")
    Label1 = Label(newWindow, text=f"The Game\n" +
                   "by Qloppa & Balboran\n" +
                   "Ver. " + TG_Version + "." + rev)
    Label1.pack()

def createMenu():
    menu = Menu(root)
    subMenu = Menu(menu, tearoff=0)
    root.config(menu=menu)

    menu.add_cascade(label="Spiel", menu=subMenu)
    subMenu.add_command(label="Neue Karten", command=doNothing)
    subMenu.add_command(label='Über The Game', command=aboutTG)
    subMenu.add_separator()
    subMenu.add_command(label="Beenden", command=root.destroy)

    editMenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Einstellungen", menu=editMenu)
    editMenu.add_command(label="1337", command=doNothing)

# """-----------------------------------IMAGE---------------------------------------#
def createImage():
    scale = 0.60
    w = int(439*scale)
    h = int(638*scale)

    backgroundImage = Image.open("resources/Kartengrafiken/Spielkarte_MUSTER_0_unicorn.png") # ohne unicorn
    backgroundImage = backgroundImage.resize((int(w),int(h)), Image.ANTIALIAS)
    global background
    background = ImageTk.PhotoImage(backgroundImage)

    upImage = Image.open("resources/Kartengrafiken/Spielkarte_MUSTER_ARROW_UP.png")
    upImage = upImage.resize((w,h), Image.ANTIALIAS)
    global up
    up = ImageTk.PhotoImage(upImage)

    downImage = Image.open("resources/Kartengrafiken/Spielkarte_MUSTER_ARROW_Down.png")
    downImage = downImage.resize((w,h), Image.ANTIALIAS)
    global down
    down = ImageTk.PhotoImage(downImage)

    ablagestapelFrame = Frame(root)
    ablagestapelFrame.pack(side=TOP)

    ablageKarte = Frame(ablagestapelFrame)
    ablageKarte.pack(side = LEFT)

    canvas1_1 = tk.Canvas(ablageKarte, width=w, height=h)
    canvas1_1.pack(side='top', fill=None, expand=False)

    canvas1_1.create_image(0,0, image=up, anchor=NW)

    canvas1_1.create_text(w/2, 60*scale, text="99", font=f"Chiller 42", fill="white", anchor=CENTER) #mitt oben
    canvas1_1.create_text(w/2, h-100*scale, text="1", font="Chiller 125", fill="white", anchor=CENTER) #mitte unten

    ablageKarte = Frame(ablagestapelFrame)
    ablageKarte.pack(side = LEFT)

    canvas1_2 = tk.Canvas(ablageKarte, width=w, height=h)
    canvas1_2.pack(side='top', fill=None, expand=False)

    canvas1_2.create_image(0,0, image=up, anchor=NW)

    canvas1_2.create_text(w/2, 60*scale, text="99", font="Chiller 42", fill="white", anchor=CENTER) #mitt oben
    canvas1_2.create_text(w/2, h-100*scale, text="1", font="Chiller 125", fill="white", anchor=CENTER) #mitte unten

    ablageKarte = Frame(ablagestapelFrame)
    ablageKarte.pack(side = LEFT)

    canvas100_1 = tk.Canvas(ablageKarte, width=w, height=h)
    canvas100_1.pack(side='top', fill=None, expand=False)

    canvas100_1.create_image(0,0, image=down, anchor=NW)

    canvas100_1.create_text(w/2, 125*scale, text="100", font="Chiller 110", fill="white", anchor=CENTER) #mitt oben
    canvas100_1.create_text(w/2, h-50*scale, text="2", font="Chiller 50", fill="white", anchor=CENTER) #mitte unten

    ablageKarte = Frame(ablagestapelFrame)
    ablageKarte.pack(side = LEFT)

    canvas100_2 = tk.Canvas(ablageKarte, width=w, height=h)
    canvas100_2.pack(side='top', fill=None, expand=False)

    canvas100_2.create_image(0,0, image=down, anchor=NW)

    canvas100_2.create_text(w/2, 125*scale, text="100", font="Chiller 110", fill="white", anchor=CENTER) #mitt oben
    canvas100_2.create_text(w/2, h-50*scale, text="2", font="Chiller 50", fill="white", anchor=CENTER) #mitte unten

    global handkartenFrame
    handkartenFrame = Frame(root)
    handkartenFrame.pack(side=BOTTOM)

def generate(spielKarte):

        cardFrame = Frame(handkartenFrame)
        cardFrame.pack(side=LEFT)

        #Scaling für die Zahlen und die Gesamte Karte
        scale = 0.6
        fontsizecorner = 42
        fontsizemiddle = 137
        font = "Castellar"
        #Alter Font Chiller
        actualfontcorner = f"{font} {str(int(fontsizecorner * scale))}"
        actualfontmiddle = f"{font} {str(int(fontsizemiddle * scale))}"
        w = 439 * scale
        h = 638 * scale

        canvas = tk.Canvas(cardFrame, width=w, height=h)
        canvas.pack(side='top', fill=None, expand=False)

        canvas.create_image(0, 0, image=background, anchor=NW)
                                                                                                            
        canvas.create_text(30 * scale, 20 * scale, text=spielKarte.value, font=actualfontcorner, fill="black",
                           anchor=NW)  # links oben
        canvas.create_text(w - 20 * scale, 20 * scale, text=spielKarte.value, font=actualfontcorner, fill="black",
                           anchor=NE)  # rechts oben
        canvas.create_text(30 * scale, h, text=spielKarte.value, font=actualfontcorner, fill="black", anchor=SW)  # links unten
        canvas.create_text(w - 20 * scale, h, text=spielKarte.value, font=actualfontcorner, fill="black",
                           anchor=SE)  # rechts unten
        canvas.create_text(w / 2, h * 0.6, text=spielKarte.value, font=actualfontmiddle, fill="black",
                           anchor=CENTER)  # mittlere Zahl

# """-----------------------------------BUTTONS---------------------------------------#

def createButtons():
    topFrame = Frame(root)
    topFrame.pack()
    bottomFrame = Frame(root)
    bottomFrame.pack()

    title = Label(topFrame, text="THE GAME")
    title.pack()

    quit = Button(bottomFrame, text="Beenden", command=root.destroy)
    quit.pack()