from itertools import permutations
from itertools import combinations
from english_words import english_words_set 
import tkinter
from tkinter import *
import tkinter as Tk


def display():
    string = userword.get()
    comb_of_str = [''.join(l) for i in range(len(string)) for l in combinations(string, i+1)]
    total = []
    for i in comb_of_str:
        p = [''.join(x) for x in permutations(i)]
        total = total + p
    s_final = []
    for j in total:
        if j not in s_final:
            s_final.append(j)
    for i in s_final:
        num = 1
        if i in english_words_set:
            if len(i)>1:
                listb.insert(num,i)
                num += 1

#clearing all the text in entry box and listbox
def res():
    userword.delete(0, END)
    listb.delete(0, END)


#creating the window
window = tkinter.Tk()
window.title("All Possible Words")
window.geometry("350x400+400+300")
window.configure(background = "#131212")

#label
lbluserword = Label(window,
                    text = "Enter letters",
                    font = ("Verdana",18),
                    bg = "#131212",
                    fg = "#FFFFFF"
                    )
lbluserword.pack(pady = 30,ipady = 10,ipadx = 10)

#Entry Box
userword = Entry(window,font = ("Verdana",16))
userword.pack(ipady = 5, ipadx = 5)

#Button for getting all the posible words
btncheck = Button(
    window,
    text = "Show All possible words",
    font = ("Comic sans ms",16),
    width = 18,
    bg = "#292424",
    fg = "#11DD30",
    command = display
    )
btncheck.pack(pady = 40)


#List box
listb = Listbox(window,
              font = ("Verdana",18),
              bg = "#4C4B4B",
              fg = "#FFFFFF",
              )
listb.pack()

#Reset button for clearing text in entry box and list box
btnreset = Button(
    window,
    text = "Reset",
    font = ("Comic sans ms",12),
    width = 16,
    bg = "#4C4B4B",
    fg = "#F61919",
    command = res
    )
btnreset.pack(pady = 30)


window.mainloop()


