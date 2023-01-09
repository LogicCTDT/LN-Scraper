import PySimpleGUI as sg
import textwrap
import main
import tkinter as tk
from tkinter import simpledialog
from tkinter import Scrollbar
from tkinter import ttk
from tkinter import *

#Start of Code

sg.theme('DarkAmber')
text = main.string_maker("https://www.webnovelpub.com/novel/supremacy-games-1132/chapter-1128")
for lst in text:
    for string in lst:
        string = textwrap.wrap(string, 70)

#Button size is relative to screen size. Thus, 100 is 100% of x
#coordinate sreensize, and 20% of y screen size.
column = []
for i in range(len(text[0])):
    if i == 0:
        column.append([sg.Text(text[0][0], font='Arial 14', text_color='white')])
    else:
        column.append([sg.Text(text[0][i], font='Arial 14', size=(100, None), text_color='white')])
column.append([sg.Button('Back', size=(20, 3)), sg.Button('Next', size=(20, 3))])
layout = [[sg.Column(column, scrollable=True)]]
window = sg.Window('Gui Sample', layout, size=(1200, 900))



def update_text_column(y: int):
    global window
    column = []
    for j in range(len(text[y])):
        if j == 0:
            column.append([sg.Text(text[y][0], font='Arial 14', text_color='white')])
        else:
            column.append([sg.Text(text[y][j], font='Arial 14', size=(100, None), text_color='white')])
    if y == len(text) - 1:
        column.append([sg.Button('Back', size=(20, 3)), sg.Button('Next', size=(20, 3), visible=False)])
    elif y == 0:
        column.append([sg.Button('Back', size=(20, 3), visible=False), sg.Button('Next', size=(20, 3))])
    else:
        column.append([sg.Button('Back', size=(20, 3)), sg.Button('Next', size=(20, 3))])
    layout = [[sg.Column(column, scrollable=True)]]
    window.close()
    window = sg.Window('Gui Sample', layout, size=(1200, 900))

y = 0
while True:
    update_text_column(y)
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    if event == 'Next':
        if y in range(len(text)- 1):
            y += 1
    if event == 'Back':
        if y in range(len(text)):
            y -= 1






# root = tk.Tk()
# root.title('')
# root.geometry("1920x800")
#
# main_frame = tk.Frame(root)
# main_frame.pack(fill=BOTH, expand=1)
#
# my_canvas = tk.Canvas(main_frame)
# my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
#
# my_scrollbar = ttk.Scrollbar(main_frame,orient=VERTICAL, command=my_canvas.yview)
# my_scrollbar.pack(side=RIGHT, fill=Y)
#
# my_canvas.configure(yscrollcommand=my_scrollbar.set)
# my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
#
# second_frame = tk.Frame(my_canvas)
#
# my_canvas.create_window((0,0), window=second_frame, anchor="nw")
#
# my_canvas.create_text(0, 0, text=text[0][0], fill="black", font=('Arial 14'))
# y=0
# for i in range(len(text[0])):
#     if i == 0:
#         my_canvas.create_text(0, 0, anchor='w', justify=LEFT, text=text[0][0], fill="black", font=('Arial 14'), width=1600)
#     else:
#         my_canvas.create_text(0, y, anchor='w', justify=LEFT, text=text[0][i], fill="black", font=('Arial 14'), width=1600)
#     y += 100
# my_canvas.pack()
#
# root.mainloop()
# Root = tk.Tk()
#
# User_Inp = simpledialog.askstring(title="Input Test", prompt="Type your Name:")
#
# print("Hello", User_Inp)