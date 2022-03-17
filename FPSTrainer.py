import tkinter as tk
import random, json
from tkinter import font, messagebox

window = tk.Tk()
filepath = r"C:\Projecten\Software Dev\Mapje 9\file-remember\data\highscores.json"
with open(filepath, "r") as file:
    data = json.load(file)
btntext = tk.StringVar()
highscores = data
time = 20
runTime = tk.StringVar(window, "Time Remaining: {}".format(time))
name = tk.StringVar()
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
    timeCount.configure(textvariable=runTime)
    timeCount.place(y=5)
    if time != 0:
        window.after(1000, timer)
    else:
        scoreBoard()

def scoreBoard():
    global data, scoreboardPlace, name,scoreboardTitle,newHighscore,nameEntry,nextBtn,doneBtn
    highScore = False
    scoreboardPlace = 0
    name.set("")
    i=50
    for x in range(5):
        window.unbind(keuzes[0][x])
    for x in range(3):
        window.unbind(keuzes[1][x])
    timeCount.destroy()
    toPress.destroy()
    scoreboardTitle = tk.Label(window,text="Scoreboard",bg="black",fg="white",font=("Calibri Light", 12, font.BOLD))
    scoreboardTitle.place(y=5)
    for person in data["Highscores"]:
        scoreboard = tk.Label(window, text="{} : {}".format(person["Name"], person["Score"]),bg="grey",fg="white",font=("Calibri Light", 12, font.BOLD))
        scoreboard.place(y=i,x=5)
        i+=20
    for person in data["Highscores"]:
        if score > person["Score"]:
            highScore = True
        if not highScore:
            scoreboardPlace += 1
    if highScore:
        print(scoreboardPlace)
        newHighscore = tk.Label(text="You got a new highscore! \nWhat is your name?",bg="grey",fg="white",font=("Calibri Light", 12, font.BOLD))
        newHighscore.place(y=70,x=140)
        nameEntry = tk.Entry(textvariable=name)
        nameEntry.place(y=120,x=175)
        doneBtn = tk.Button(text="Done", command=HighscoreCheck, bg="white", fg="black",bd=0.5)
        doneBtn.place(y=145,x=220)
    else:
        nextBtn = tk.Button(text="Verder",bg="white", fg="black",bd=0.5,command=endScreen)
        nextBtn.place(y=225,x=225)

def HighscoreCheck():
    for i in range(9, scoreboardPlace, -1):
        data["Highscores"][i]["Name"] = data["Highscores"][i-1]["Name"]
        data["Highscores"][i]["Score"] = data["Highscores"][i-1]["Score"]
    data["Highscores"][scoreboardPlace]["Name"] = name.get()
    data["Highscores"][scoreboardPlace]["Score"] = score
    with open(filepath, "w") as file:
        file.write(json.dumps(data, indent=3))
    window.destroy()

def endScreen():
    global score
    destroyBtn("", "yes")
    answer = messagebox.askyesno("play again?", "Your final score is {}! \nWould you like to try again?".format(score))
    if answer:
        score = 0
        startButton()
        scoreboardTitle.destroy()
        newHighscore.destroy()
        nameEntry.destroy()
        doneBtn.destroy()
        nextBtn.destroy()
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