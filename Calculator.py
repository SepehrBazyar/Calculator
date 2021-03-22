## Calculator
## Produced By Sepehr Bazyar
## Class 3/7

import tkinter as tk, math

string = ""

# Functions
def Sefr():
    global string
    string += str(0)

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)

def Yek():
    global string
    string += str(1)

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)


def Do():
    global string
    string += str(2)

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)


def Se():
    global string
    string += str(3)

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)


def Char():
    global string
    string += str(4)

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)


def Panj():
    global string
    string += str(5)

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)


def Shish():
    global string
    string += str(6)

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)


def Haft():
    global string
    string += str(7)

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)


def Hasht():
    global string
    string += str(8)

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)


def Noh():
    global string
    string += str(9)

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)


def Momayez():
    global string
    string += "."

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)


def Darsad():
    global string
    string += "/100"

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)


def Taghsim():
    global string
    string += "/"

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)


def Zarb():
    global string
    string += "*"

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)


def Menha():
    global string
    string += "-"

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)


def Jam():
    global string
    string += "+"

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)


def Tavan():
    global string
    string += "**"

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)


def Jazr():
    global string
    string += "**0.5"

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)


def Radikal():
    global string
    string += "**(1/3)"

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)  
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)


def PrantezBaz():
    global string
    string += "("

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)


def PrantezBaste():
    global string
    string += ")"

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)


def C():
    global string
    string = ""

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)


def BackSpace():
    global string
    string = list(string)
    string.pop()
    string = "".join(string)

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)


def OutPut():
    global string
    string = str(eval(string))

    R = tk.Label(Window, text="                                                        ")
    R.place(x = 65, y = 160)
    L = tk.Label(Window, text=string)
    L.place(x = 65, y = 160)
    
    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)

def GhadrMotlagh():
    global string
    string = str(abs(eval(string)))

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)


def Pi():
    global string
    string += str(math.pi)

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)


def E():
    global string
    string += str(math.e)

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)

def Factoriel():
    global string
    string = str(math.factorial(eval(string)))

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)

def Time():
    global string
    Array = string.split(":")
    Array[0] = int(Array[0])
    Array[1] = int(Array[1])
    a = Array[1]//60
    Array[0] += a
    Array[1] -= a*60
    Array[0] = str(Array[0])
    Array[1] = str(Array[1])
    string = ":".join(Array)

    R = tk.Label(Window, text="                                                        ")
    R.place(x = 65, y = 160)
    L = tk.Label(Window, text=string)
    L.place(x = 65, y = 160)
    
    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)

def DoNoghte():
    global string
    string += ":"

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)

def Logaritm():
    global string
    string = str(math.degrees(math.log10(eval(string))))

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)

def Radian():
    global string
    string = str(math.radians(eval(string)))

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)

def Darage():
    global string
    string = str(math.degrees(eval(string)))

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)

def Sinos():
    global string
    string = str(math.degrees(math.sin(eval(string))))

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)

def Cosinos():
    global string
    string = str(math.degrees(math.cos(eval(string))))

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)

def Tanzant():
    global string
    string = str(math.degrees(math.tan(eval(string))))

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)

def ArkSinos():
    global string
    string = str(math.degrees(math.asin(eval(string))))

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)

def ArkCosinos():
    global string
    string = str(math.degrees(math.acos(eval(string))))

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)

def ArkTanzant():
    global string
    string = str(math.degrees(math.atan(eval(string))))

    l = tk.Label(Window, text="                                                        ")
    l.place(x = 20, y = 50)
    l = tk.Label(Window, text=string)
    l.place(x = 20, y = 50)


# Program
import tkinter as tk

Window = tk.Tk()
Window.geometry("400x600")
Window.title(" Calculator ")
Window.resizable(0,0)

Rect_A = tk.Canvas(Window, width = 380, height = 150)
Rect_A.pack()
Rect_A.create_rectangle(10, 5, 370, 140)

Rect_N = tk.Canvas(Window, width = 380, height = 100)
Rect_N.pack()
Rect_N.create_rectangle(10, 2, 370, 35)

B = tk.Label(Window, text = " Ans = " )
B.place(x = 25, y = 160)
    
Array = list(range(39))

Array[0] = tk.Button(Window, text = "(", width = 5, command = PrantezBaz)
Array[0].place(x = 15, y = 200)

Array[1] = tk.Button(Window, text = ")", width = 5, command = PrantezBaste)
Array[1].place(x = 95, y = 200)

Array[2] = tk.Button(Window, text = "time", width = 5, command = Time)
Array[2].place(x = 175, y = 200)

Array[3] = tk.Button(Window, text = "←", width = 5, command = BackSpace)
Array[3].place(x = 255, y = 200)

Array[4] = tk.Button(Window, text = "C", width = 5, command = C)
Array[4].place(x = 335, y = 200)

Array[5] = tk.Button(Window, text = "e", width = 5, command = E)
Array[5].place(x = 15, y = 250)

Array[6] = tk.Button(Window, text = "π", width = 5, command = Pi)
Array[6].place(x = 95, y = 250)

Array[7] = tk.Button(Window, text = "!", width = 5, command = Factoriel)
Array[7].place(x = 175, y = 250)

Array[8] = tk.Button(Window, text = "∛", width = 5, command = Radikal)
Array[8].place(x = 255, y = 250)

Array[9] = tk.Button(Window, text = "log", width = 5, command = Logaritm)
Array[9].place(x = 335, y = 250)

Array[10] = tk.Button(Window, text = "asin", width = 5, command = ArkSinos)
Array[10].place(x = 15, y = 300)

Array[11] = tk.Button(Window, text = "acos", width = 5, command = ArkCosinos)
Array[11].place( x = 95, y = 300)

Array[12] = tk.Button(Window, text = "atan", width = 5, command = ArkTanzant)
Array[12].place(x = 175, y = 300)

Array[13] = tk.Button(Window, text = "√", width = 5, command = Jazr)
Array[13].place(x = 255, y = 300)

Array[14] = tk.Button(Window, text = "abs", width = 5, command = GhadrMotlagh)
Array[14].place(x = 335, y = 300)

Array[15] = tk.Button(Window, text = "sin", width = 5, command = Sinos)
Array[15].place(x = 15, y = 350)

Array[16] = tk.Button(Window, text = "cos", width = 5, command = Cosinos)
Array[16].place(x = 95, y = 350)

Array[17] = tk.Button(Window, text = "tan", width = 5, command = Tanzant)
Array[17].place(x = 175, y = 350)

Array[18] = tk.Button(Window, text = "^", width = 5, command = Tavan)
Array[18].place(x = 255, y = 350)

Array[19] = tk.Button(Window, text = "rad", width = 5, command = Radian)
Array[19].place(x = 335, y = 350)

Array[20] = tk.Button(Window, text = "7", width = 5, command = Haft)
Array[20].place(x = 15, y = 400)

Array[21] = tk.Button(Window, text = "8", width = 5, command = Hasht)
Array[21].place(x = 95, y = 400)

Array[22] = tk.Button(Window, text = "9", width = 5, command = Noh)
Array[22].place(x = 175, y = 400)

Array[23] = tk.Button(Window, text = "/", width = 5, command = Taghsim)
Array[23].place(x = 255, y = 400)

Array[24] = tk.Button(Window, text = "deg", width = 5, command = Darage)
Array[24].place(x = 335, y = 400)

Array[25] = tk.Button(Window, text = "4", width = 5, command = Char)
Array[25].place(x = 15, y = 450)

Array[26] = tk.Button(Window, text = "5", width = 5, command = Panj)
Array[26].place(x = 95, y = 450)

Array[27] = tk.Button(Window, text = "6", width = 5, command = Shish)
Array[27].place(x = 175, y = 450)

Array[28] = tk.Button(Window, text = "*", width = 5, command = Zarb)
Array[28].place(x = 255, y = 450)

Array[29] = tk.Button(Window, text = ":", width = 5, command = DoNoghte)
Array[29].place(x = 335, y = 450)

Array[30] = tk.Button(Window, text = "1", width = 5, command = Yek)
Array[30].place(x = 15, y = 500)

Array[31] = tk.Button(Window, text = "2", width = 5, command = Do)
Array[31].place(x = 95, y = 500)

Array[32] = tk.Button(Window, text = "3", width = 5, command = Se)
Array[32].place(x = 175, y = 500)

Array[33] = tk.Button(Window, text = "-", width = 5, command = Menha)
Array[33].place(x = 255, y = 500)

Array[34] = tk.Button(Window, text = "0", width = 5, command = Sefr)
Array[34].place(x = 15, y = 550)

Array[35] = tk.Button(Window, text = ".", width = 5, command = Momayez)
Array[35].place(x = 95, y = 550)

Array[36] = tk.Button(Window, text = "%", width = 5, command = Darsad)
Array[36].place(x = 175, y = 550)

Array[37] = tk.Button(Window, text = "+", width = 5, command = Jam)
Array[37].place(x = 255, y = 550)

Array[37] = tk.Button(Window, text = "=", width = 5, height = 5, command = OutPut)
Array[37].place(x = 335, y = 500)


Window.mainloop()

# The End
