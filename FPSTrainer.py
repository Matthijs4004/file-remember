import tkinter as tk
import random
from tkinter import font, messagebox

window = tk.Tk()
btntext = tk.StringVar()
time = 20
runTime = tk.StringVar(window, "Time Remaining: {}".format(time))
score = 0
scoreCount = tk.StringVar()
scoreCount.set("Score: {}".format(score))

def ButtonText(btn):
    global btntext
    if btn == "<space>":
        btntext.set("Press space")
    elif btn == "<w>":
        btntext.set("Press w")
    elif btn == "<a>":
        btntext.set("Press a")
    elif btn == "<s>":
        btntext.set("Press s")
    elif btn == "<d>":
        btntext.set("Press d")
    elif btn == "<Button>":
        btntext.set("Single click")
    elif btn == "<Double-Button>":
        btntext.set("Double click")
    elif btn == "<Triple-Button>":
        btntext.set("Triple click")

def newButton():
    global toPress, Num1, Num2, keuzes, btntext
    keuzes = [["<space>", "<w>", "<a>", "<s>", "<d>"],["<Button>", "<Double-Button>", "<Triple-Button>"]]
    Num1 = random.randint(0, 1)
    Num2 = random.randint(0, len(keuzes[Num1]) - 1)
    btn = keuzes[Num1][Num2]
    ButtonText(btn)
    toPress = tk.Label(window, width=15,height=2, textvariable=btntext ,fg="black", bg="white")
    toPress.place(x=random.randint(10,275),y=random.randint(50,250))
    if Num1 == 0:
        window.bind(keuzes[Num1][Num2], destroyBtn)
    else:
        toPress.bind(keuzes[Num1][Num2], destroyBtn)


def destroyBtn(self, endOfGame="no"):
    global score
    toPress.destroy()
    if Num1 == 0:
        window.unbind(keuzes[Num1][Num2])
        score += 1
    else:
        score += 2
    scoreCount.set("Score: {}".format(score))
    if endOfGame != "yes":
        newButton()

def start():
    newButton()
    window.after(1000, timer)

def timer():
    global time
    time -= 1
    runTime.set("Time Remaining: " + str(time))
    timeCount = tk.Label(window,textvariable=runTime,bg="black",fg="white",font=("Calibri Light", 12, font.BOLD))
    timeCount.place(y=5)
    if time != 0:
        window.after(1000, timer)
    else:
        endScreen()

def endScreen():
    global score
    destroyBtn("", "yes")
    answer = messagebox.askyesno("play again?", "Your final score is {}! \nWould you like to try again?".format(score))
    if answer:
        score = 0
        startButton()
    else:
        window.destroy()

def deleteStartButton():
    btn.destroy()
    start()

def startButton():
    global btn, score, time
    score = 0
    time = 20
    btn = tk.Button(window, bg="white", fg="black", text="Click to start game", command=deleteStartButton, justify="center")
    btn.place(x=150,y=125)


window.geometry("400x300")
window["bg"] = "grey"
window.eval('tk::PlaceWindow . center') # optioneel (puur om het scherm in het midden te krijgen)
infoBar = tk.Label(window, bg="black", width=300,height=2)
timeCount = tk.Label(window,textvariable=runTime,bg="black",fg="white",font=("Calibri Light", 12, font.BOLD))
scoreCounter = tk.Label(window,textvariable=scoreCount,bg="black",fg="white",font=("Calibri Light", 12, font.BOLD))
infoBar.pack()
timeCount.place(y=5)
scoreCounter.place(y=5, x=300)

startButton()


window.mainloop()