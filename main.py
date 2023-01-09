import PySimpleGUI as sg
import textwrap
import lnpub Scraper
import tkinter as tk
from tkinter import simpledialog


#Start of Code

sg.theme('DarkAmber')
text =
new_text = textwrap.wrap(text, 70)
layout = [[sg.Text('Title', font='Arial 14', text_color='white')], [sg.Text(text, font='Arial 14', size =(70, None), text_color='white')],
    [sg.Button('Back', size=(20, 3)), sg.Button('Next', size=(20, 3))]] #Button size is relative to screen size. Thus, 100 is 100% of x
#coordinate sreensize, and 20% of y screen size.

window = sg.Window('Gui Sample', layout, size=(800, 800))

while True:
    event, values = window.read()

    if event == 'Reader Window' or event == sg.WINDOW_CLOSED:
        break
#
# Root = tk.Tk()
#
# User_Inp = simpledialog.askstring(title="Input Test", prompt="Type your Name:")
#
# print("Hello", User_Inp)