from tkinter import *
from PIL import ImageTk
from PIL import Image

class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="Lade Werker...", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        Button(self, text="Gehe zu nächstem Werker",
                  command=lambda: master.switch_frame(StartPage)).pack()

_GAME_ICON = "resources/THE_GAME_ICON.ico"

root = None
handkartenFrame = None
background = None
up = None
down = None
platzhalter = None
nachziehStapel = None
TG_Version = None
rev = None
auswahlKarte = None
ablagestapelFrame = None
check_FS = None
scale = None
font = "Chiller"  # Fonts: Chiller, Castellar
ablagestapelVorlageFrame = None
check_state = False
player1name = None
settingswindow = None
skinchoice = None
skin = None
skinversion = None

def init(version, revNumber):
    global TG_Version
    TG_Version = version
    global rev
    rev = revNumber


def createWindow():
    global root
    global player1name
    global check_state
    root = Tk()
    root.title("THE GAME!")
    root.iconbitmap(_GAME_ICON)
    root.attributes
    root.attributes('-fullscreen', True)
    windowScaling(root.winfo_screenwidth(), root.winfo_screenheight())
    print(f"scale: {scale}")
    global check_FS
    check_FS = False
    createMenu()

    return root


def windowScaling(width, height):
    global scale
    if (round((width / height), 2) == round((1920 / 1080), 2) or round((width / height), 2) == round((1360 / 768), 2)):
        scalePerPixel = 0.40 / 1080
        scale = scalePerPixel * height
    if (round((width / height), 2) == round((1600 / 1200), 2)):
        scalePerPixel = 0.35 / 1200
        scale = scalePerPixel * height
    if (round((width / height), 2) == round((1920 / 1200), 2) or round((width / height), 2) == round((1280 / 768), 2)):
        scalePerPixel = 0.42 / 1200
        scale = scalePerPixel * height
    if (round((width / height), 2) == round((1280 / 1024), 2)):
        scalePerPixel = 0.28 / 1024
        scale = scalePerPixel * height
    if (round((width / height), 2) == round((1600 / 1024), 2)):
        scalePerPixel = 0.36 / 1024
        scale = scalePerPixel * height


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

def settings():
    global settingswindow
    global player1name
    settingswindow = Toplevel(root)
    settingswindow.overrideredirect(1)
    settingswindow.title("Einstellungen")
    settingswindow.iconbitmap(_GAME_ICON)
    settingswindow.configure(pady=10)
    bind_esc()
    #x = root.winfo_width()
    #y = root.winfo_height()
    #size = str(str(x) + "x" + str(y))
    getplayername()
    skinchoose()


def fullscreen():
    global check_FS
    global actualwidth
    global actualheight

    if not check_FS:
        actualwidth = root.winfo_width()
        actualheight = root.winfo_height()
        print("Kein Vollbild")
        root.attributes('-fullscreen', True)
        # global screenmode
        # screenmode = "Vollbild"
        check_FS = True
    else:
        print("Vollbild")
        print(actualwidth, actualheight)
        root.attributes('-fullscreen', False)
        root.geometry(f"" + str(actualwidth) + "x" + str(actualheight))
        # screenmode = "Kein Vollbild"
        check_FS = False


def createMenu():
    menu = Menu(root)
    subMenu = Menu(menu, tearoff=0)
    root.config(menu=menu)

    menu.add_cascade(label="Spiel", menu=subMenu)
    subMenu.add_command(label="Neue Spiel", command=doNothing)
    subMenu.add_command(label="Spiel Laden", command=doNothing)
    subMenu.add_command(label="Spiel Speichern", command=doNothing)
    subMenu.add_separator()
    subMenu.add_command(label="Beenden", command=root.destroy)
    editMenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Optionen", menu=editMenu)
    editMenu.add_command(label="Einstellungen", command=settings)
    editMenu.add_command(label="Screenmode", command=fullscreen)
    editMenu.add_command(label='Über The Game', command=aboutTG)
    #editMenu.add_command(label='Namenswahl', command=getplayername)


# """-----------------------------------IMAGE---------------------------------------#
def getplayername():
    print("Wir sind hier")
    global group
    group = LabelFrame(settingswindow, text="Name:", padx=5, pady=5)
    group.pack(side="left")
    getnameLabel = Label(group, text="Gib deinen Namen ein: ")
    getnameLabel.pack()
    global player1getname
    player1getname = Entry(group)
    player1getname.pack()
    player1getname.bind('<Return>', entername)

def entername(event):
    global check_state
    global player1name
    global group
    player1name = str(player1getname.get())
    check_state = True
    player1NL.configure(text=player1name)
    settingswindow.destroy()

def bind_esc():
    def close(event):
        settingswindow.destroy()  # if you want to exit the entire thing

    settingswindow.bind('<Escape>', close)

def chooseskin():
    global skinchoice
    global skin
    global skinversion

    if skinchoice == "Death":
        chosenskin = "resources/Kartengrafiken/Spielkarte_MUSTER_0.png"
        return chosenskin

    if skinchoice == "Unicorn":
        chosenskin = "resources/Kartengrafiken/Spielkarte_MUSTER_0_unicorn.png"
        return chosenskin


def skinchoose():
    skin = LabelFrame(settingswindow, text="Skins:", padx=5, pady=5)
    skin.pack(side="right")
    getskinlabel = Label(skin, text="Wähle deinen Kartentheme: ")
    getskinlabel.pack()
    # data
    data = {
        'Death': "don't dead open inside",
        'Unicorn': "Pink fluffy unicorns...",
        'Comming Soon': "What would you do with...",
    }

    # updates text
    def useskin(new_value):
        global skinchoice
        display.config(text=data[new_value])

        skinchoice = data[new_value]
        #chooseskin()
        #createImage()
        root.update_idletasks()
        print("Skinupdate")
        # create a dropdown list

    var = StringVar()
    var.set(str(skinchoice))
    p = OptionMenu(skin, var, *data, command=useskin)
    p.pack()

    display = Label(skin)
    display.pack()

def createImage():
    global scale
    global font
    w = int(439 * scale)
    h = int(638 * scale)

    backgroundImage = Image.open("resources/Kartengrafiken/Spielkarte_MUSTER_0.png")  # ohne unicorn
    backgroundImage = backgroundImage.resize((w, h), Image.ANTIALIAS)
    global background
    background = ImageTk.PhotoImage(backgroundImage)

    upImage = Image.open("resources/Kartengrafiken/Spielkarte_MUSTER_ARROW_UP.png")
    upImage = upImage.resize((w, h), Image.ANTIALIAS)
    global up
    up = ImageTk.PhotoImage(upImage)

    downImage = Image.open("resources/Kartengrafiken/Spielkarte_MUSTER_ARROW_Down.png")
    downImage = downImage.resize((w, h), Image.ANTIALIAS)
    global down
    down = ImageTk.PhotoImage(downImage)

    platzhalterImg = Image.open("resources/Kartengrafiken/Spielkarte_platzhalter.png")
    platzhalterImg = platzhalterImg.resize((w, h), Image.ANTIALIAS)
    global platzhalter
    platzhalter = ImageTk.PhotoImage(platzhalterImg)

    nachziehStapelImg = Image.open("resources/Kartengrafiken/Spielkarte_MUSTER_0_Kartenstapel.png")
    nachziehStapelImg = nachziehStapelImg.resize((w, h), Image.ANTIALIAS)
    global nachziehStapel
    nachziehStapel = ImageTk.PhotoImage(nachziehStapelImg)

    sideFrameleft = Frame(root, bg="blue")
    sideFrameleft.pack(side='left', fill=Y)

    player1NF = Frame(sideFrameleft)
    player1NF.pack(side="top")

    global player1NL
    player1NL = Label(player1NF, text="Spieler1", bg="red")
    player1NL.pack()
    player1NL.configure(text=player1name)

    nachziehStapelFrame = Frame(sideFrameleft)
    nachziehStapelFrame.pack(side='bottom')

    if font == "Chiller":
        fontsizecorner = 55
    else:
        fontsizecorner = 23
    actualfontcorner = f"{font} {str(int(fontsizecorner * scale))}"

    canvasLabel = Label(nachziehStapelFrame, text="Verbleibende Karten:", font=actualfontcorner)
    canvasLabel.pack(side='top')

    canvas = Canvas(nachziehStapelFrame, width=w, height=h)
    canvas.pack(side='top', fill=None, expand=False)

    canvas.create_image(0, 0, image=nachziehStapel, anchor=NW)

    nachziehStapelFrame.update()
    leftframewidth = nachziehStapelFrame.winfo_width()
    leftframeheight = nachziehStapelFrame.winfo_height()

    sideFrameright = Frame(root, bg="blue", width=leftframewidth)
    sideFrameright.pack_propagate(0)
    sideFrameright.pack(side="right", fill=Y)

    player2NF = Frame(sideFrameright)
    player2NF.pack(side="top")

    player2NL = Label(player2NF, text="Spieler2", bg="red")
    player2NL.pack(side="top")

    global ablagestapelVorlageFrame
    ablagestapelVorlageFrame = Frame(root)
    ablagestapelVorlageFrame.pack(side="top")

    global ablagestapelFrame
    ablagestapelFrame = Frame(root)
    ablagestapelFrame.pack(side=TOP)

    ablageKarteVorlage = Frame(ablagestapelVorlageFrame)
    ablageKarteVorlage.pack(side=LEFT)

    erzeugeAblageStapelVorlage(ablageKarteVorlage, scale, h, w, up, "1", "99").config(cursor="exchange")

    ablageKarteVorlage = Frame(ablagestapelVorlageFrame)
    ablageKarteVorlage.pack(side=LEFT)

    erzeugeAblageStapelVorlage(ablageKarteVorlage, scale, h, w, up, "1", "99").config(cursor="exchange")

    ablageKarteVorlage = Frame(ablagestapelVorlageFrame)
    ablageKarteVorlage.pack(side=LEFT)

    erzeugeAblageStapelVorlage(ablageKarteVorlage, scale, h, w, down, "100", "2").config(cursor="exchange")

    ablageKarteVorlage = Frame(ablagestapelVorlageFrame)
    ablageKarteVorlage.pack(side=LEFT)

    erzeugeAblageStapelVorlage(ablageKarteVorlage, scale, h, w, down, "100", "2").config(cursor="exchange")

    global handkartenFrame
    handkartenFrame = Frame(root)
    handkartenFrame.pack(side='bottom')


def erzeugeAblageStapelVorlage(frame, scale, h, w, img, bigNumber, smallNumber):
    global font
    fontsizesmall = 50
    fontsizebig = 110
    # Alter Font Castellar
    smallNumberFont = f"{font} {str(int(fontsizesmall * scale))}"
    bigNumberFont = f"{font} {str(int(fontsizebig * scale))}"

    canvas = Canvas(frame, width=w, height=h)
    canvas.pack(side='top', fill=None, expand=False)

    canvas.create_image(0, 0, image=img, anchor=NW)

    canvas.create_text(w / 2, 60 * scale, text=smallNumber, font=smallNumberFont, fill="white",
                       anchor=CENTER)  # mitt oben
    canvas.create_text(w / 2, h - 100 * scale, text=bigNumber, font=bigNumberFont, fill="white",
                       anchor=CENTER)  # mitte unten
    return canvas


def erzeugeAblageKarte(frame, scale, h, w, index):
    print(f"erzeugeAblageKarte {index}")
    canvas = Canvas(frame, width=w, height=h)
    canvas.pack(side='top', fill=None, expand=False)

    canvas.create_image(0, 0, image=platzhalter, anchor=NW)

    def stapelGewaehlt(event):
        global auswahlKarte
        auswahlKarte = index - 4

    canvas.bind("<Button-1>", stapelGewaehlt)

    return canvas


def aktuelisiereAblageKarte(frame, index, value):
    global scale
    global font
    w = int(439 * scale)
    h = int(638 * scale)

    if value >= 1:
        fontsizecorner = 42
        fontsizemiddle = 137
        # Alter Font Chiller
        actualfontcorner = f"{font} {str(int(fontsizecorner * scale))}"
        actualfontmiddle = f"{font} {str(int(fontsizemiddle * scale))}"

        canvas = Canvas(frame, width=w, height=h)
        canvas.pack(side='top', fill=None, expand=False)

        canvas.create_image(0, 0, image=background, anchor=NW)

        canvas.create_text(30 * scale, 20 * scale, text=value, font=actualfontcorner, fill="black",
                           anchor=NW)  # links oben
        canvas.create_text(w - 20 * scale, 20 * scale, text=value, font=actualfontcorner, fill="black",
                           anchor=NE)  # rechts oben
        canvas.create_text(30 * scale, h, text=value, font=actualfontcorner, fill="black", anchor=SW)  # links unten
        canvas.create_text(w - 20 * scale, h, text=value, font=actualfontcorner, fill="black",
                           anchor=SE)  # rechts unten
        canvas.create_text(w / 2, h * 0.6, text=value, font=actualfontmiddle, fill="black",
                           anchor=CENTER)  # mittlere Zahl

        def karteGewaehlt(event):
            global auswahlKarte
            auswahlKarte = index - 4

        canvas.bind("<Button-1>", karteGewaehlt)
    else:
        erzeugeAblageKarte(frame, scale, h, w, index)


def aktualisiereAblageStapel(ablageStapel):
    index = 0
    for spielKarte in ablageStapel:
        ablageKarte = Frame(ablagestapelFrame)
        ablageKarte.pack(side=LEFT)
        print(f"spielkarten: {spielKarte.value}")
        aktuelisiereAblageKarte(ablageKarte, index, spielKarte.value)
        index = index + 1


def deleteHandkarten():
    # destroy all widgets from frame
    for widget in handkartenFrame.winfo_children():
        widget.destroy()
    # this will clear frame and frame will be empty


def deleteAblagestapel():
    for widget in ablagestapelFrame.winfo_children():
        widget.destroy()


def getClickedValue():
    if auswahlKarte != None:
        auswahl = auswahlKarte
    else:
        auswahl = 0
    return auswahl


def setClickedValue(value):
    global auswahlKarte
    auswahlKarte = value


def handKarteAnzeigen(spielKarte):
    cardFrame = Frame(handkartenFrame)
    cardFrame.pack(side=LEFT)

    # Scaling für die Zahlen und die Gesamte Karte
    global scale
    global font
    fontsizecorner = 42
    fontsizemiddle = 137
    # Alter Font Chiller/Castellar
    actualfontcorner = f"{font} {str(int(fontsizecorner * scale))}"
    actualfontmiddle = f"{font} {str(int(fontsizemiddle * scale))}"
    w = 439 * scale
    h = 638 * scale

    canvas = Canvas(cardFrame, width=w, height=h)
    canvas.pack(side='top', fill=None, expand=False)

    canvas.create_image(0, 0, image=background, anchor=NW)

    canvas.create_text(30 * scale, 20 * scale, text=spielKarte.value, font=actualfontcorner, fill="black",
                       anchor=NW)  # links oben
    canvas.create_text(w - 20 * scale, 20 * scale, text=spielKarte.value, font=actualfontcorner, fill="black",
                       anchor=NE)  # rechts oben
    canvas.create_text(30 * scale, h, text=spielKarte.value, font=actualfontcorner, fill="black",
                       anchor=SW)  # links unten
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

    """
    title = Label(topFrame, text="THE GAME")
    title.pack()

    quit = Button(bottomFrame, text="Beenden", command=root.destroy)
    quit.pack()
    """