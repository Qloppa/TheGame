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
platzhalter = None
TG_Version = None
rev = None
auswahlKarte = None

def init(version, revNumber):
    global TG_Version
    TG_Version = version
    global rev
    rev = revNumber

def createWindow():
    global root
    root = Tk()
    root.title("THE GAME!")
    root.iconbitmap(_GAME_ICON)
    root.geometry("1920x1080")
    root.attributes('-fullscreen', False)
    createMenu()
    return root

# """-----------------------------------MENU---------------------------------------#
def doNothing():
    print("OK, I do Nothing")

def aboutTG():
    newWindow = Toplevel(root)
    newWindow.title("Über The Game")
    newWindow.iconbitmap(_GAME_ICON)
    newWindow.geometry("250x60")
    aboutLabel = Label(newWindow, text=f"The Game\n" +
                   "by Qloppa & Balboran\n" +
                   "Ver. " + TG_Version + "." + rev)
    aboutLabel.pack()

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

    platzhalterImg = Image.open("resources/Kartengrafiken/Spielkarte_platzhalter.png")
    platzhalterImg = platzhalterImg.resize((w,h), Image.ANTIALIAS)
    global platzhalter
    platzhalter = ImageTk.PhotoImage(platzhalterImg)
    
    ablagestapelVorlageFrame = Frame(root)
    ablagestapelVorlageFrame.pack(side=TOP)

    ablagestapelFrame = Frame(root)
    ablagestapelFrame.pack(side=TOP)

    ablageKarte = Frame(ablagestapelFrame)
    ablageKarte.pack(side = LEFT)

    erzeugeAblageKarte(ablageKarte, scale, h, w, platzhalter)

    ablageKarteVorlage = Frame(ablagestapelVorlageFrame)
    ablageKarteVorlage.pack(side = LEFT)

    erzeugeAblageStapelVorlage(ablageKarteVorlage, scale, h, w, up, "1", "99").config(cursor="exchange")

    ablageKarte = Frame(ablagestapelFrame)
    ablageKarte.pack(side = LEFT)

    erzeugeAblageKarte(ablageKarte, scale, h, w, platzhalter)

    ablageKarteVorlage = Frame(ablagestapelVorlageFrame)
    ablageKarteVorlage.pack(side = LEFT)

    erzeugeAblageStapelVorlage(ablageKarteVorlage, scale, h, w, up, "1", "99").config(cursor="exchange")
    
    ablageKarte = Frame(ablagestapelFrame)
    ablageKarte.pack(side = LEFT)

    erzeugeAblageKarte(ablageKarte, scale, h, w, platzhalter)

    ablageKarteVorlage = Frame(ablagestapelVorlageFrame)
    ablageKarteVorlage.pack(side = LEFT)

    erzeugeAblageStapelVorlage(ablageKarteVorlage, scale, h, w, down, "100", "2").config(cursor="exchange")

    ablageKarte = Frame(ablagestapelFrame)
    ablageKarte.pack(side = LEFT)

    erzeugeAblageKarte(ablageKarte, scale, h, w, platzhalter)

    ablageKarteVorlage = Frame(ablagestapelVorlageFrame)
    ablageKarteVorlage.pack(side = LEFT)

    erzeugeAblageStapelVorlage(ablageKarteVorlage, scale, h, w, down, "100", "2").config(cursor="exchange")

    global handkartenFrame
    handkartenFrame = Frame(root)
    handkartenFrame.pack(side=BOTTOM)

def erzeugeAblageStapelVorlage(frame, scale, h, w, img, bigNumber, smallNumber):
    canvas = tk.Canvas(frame, width=w, height=h)
    canvas.pack(side='top', fill=None, expand=False)

    canvas.create_image(0,0, image=img, anchor=NW)

    canvas.create_text(w/2, 60*scale, text=smallNumber, font=f"Chiller 50", fill="white", anchor=CENTER) #mitt oben
    canvas.create_text(w/2, h-100*scale, text=bigNumber, font="Chiller 110", fill="white", anchor=CENTER) #mitte unten
    return canvas

def erzeugeAblageKarte(frame, scale, h, w, img):
    canvas = tk.Canvas(frame, width=w, height=h)
    canvas.pack(side='top', fill=None, expand=False)

    canvas.create_image(0,0, image=img, anchor=NW)
    return canvas

def erzeugeAblageStapel():
    print("moin")

def deleteHandkarten():
    # destroy all widgets from frame
    for widget in handkartenFrame.winfo_children():
       widget.destroy()
    # this will clear frame and frame will be empty

def getClickedValue():
    if auswahlKarte != None:
        auswahl = auswahlKarte
    else:
        auswahl = 0
    return auswahl

def karteAnzeigen(spielKarte):

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

    canvas.config(cursor="exchange")

    
    def buttonPressed(event):
        global auswahlKarte
        auswahlKarte = spielKarte.getValue()
        print(f"Karte angeklickt {auswahlKarte}")

    canvas.bind("<Button-1>", buttonPressed)
    
    return canvas

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