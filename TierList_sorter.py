# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 21:47:39 2020

@author: adXerg
I made this for Altema Tier List. Why? Because I uses Altema Tier List. Feel free to edit it for Other Tier Lists.
"""
import tkinter as tk

def set_text(ent,text):
    ent.delete("1.0",'end')
    ent.insert("1.0",text)
    return

def makeScript():
    newCharacters=newLinesInput.get("1.0",'end').split('\n')
    newCharacters=[i for i in newCharacters if len(i)>0]
    old=oldPageInput.get("1.0",'end')
    starts=old.find("{{Tier")
    ends=old.find("|}")
    header=old[:starts-1]
    footer=old[ends:]
    tosort=old[starts:ends].split('\n')
    tosort=[i for i in tosort if len(i)>0]
    tosort+=newCharacters
    sortedList=[i.split('|') for i in tosort]
    sortedList=sorted(sorted(sortedList, key = lambda x : x[1]), key = lambda x : x[3], reverse = True)
    result=header
    result+='\n'
    for i in sortedList:
        result+='|'.join(i)
        result+='\n'
    result+=footer
    result=result[:-1]
    set_text(resultBox,result)

master = tk.Tk()
master.title("Another Eden Wiki's Altema Tier List Adder/Sorter")

tk.Label(master, text='New lines to add:\n(Leave empty to sort only)', padx=10, pady=5).grid(row=0, column=0)
newLinesInput = tk.Text(master, height=5, width=100)
newLinesInput.grid(row=0, column=1, sticky='W', pady=2.5)

tk.Label(master, text='Old page script:').grid(row=1, column=0)
oldPageInput = tk.Text(master, height=10, width=100)
oldPageInput.grid(row=1, column=1, sticky='W', pady=2.5)

resBtn = tk.Button(master, text='Submit', width=114, height=2)
resBtn.grid(row=2, columnspan=10)
resBtn.bind('<Button-1>', lambda e: makeScript())

tk.Label(master, text='\nResult (Copy-Paste to Edit Page)', padx=10, pady=5).grid(row=3, column=0, columnspan=2)
resultBox = tk.Text(master, width=120, height=20)
resultBox.grid(row=4, column=0, columnspan=2, pady=5)

tk.mainloop() 