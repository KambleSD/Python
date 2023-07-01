from tkinter import *
import random  

root = Tk()
root.geometry('400x240')
root.title('Love Calculator')

def calculate_love():
    name1 = str(name1_entry.get())
    name2 = str(name2_entry.get())
    love_score = int((len(set(name1.lower() + name2.lower()))) * 7.5)
#add the lengths of the two names (ignoring duplicates),
#multiply the result by 7.5, and convert the result to an integer.

    result.config(text="Love Percentage between " + name1 + " and " + name2 + " is " + str(love_score) + "%")

heading = Label(root, text='Love Calculator - How much is he/she into you')
heading.pack()

slot1 = Label(root, text="Enter Your Name:")
slot1.pack()
name1_entry = Entry(root, border=5)
name1_entry.pack()

slot2 = Label(root, text="Enter Your Partner Name:")
slot2.pack()
name2_entry = Entry(root, border=5)
name2_entry.pack()

bt = Button(root, text="Calculate", height=1, width=7, command=calculate_love)
bt.pack()

result = Label(root, text='Love Percentage between both of You:')
result.pack()

root.mainloop()
