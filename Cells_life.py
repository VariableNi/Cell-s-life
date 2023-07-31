import customtkinter as CTk
from tkinter import *
from threading import Thread
import random

main = CTk.CTk()
main.title("Cell's life")
main.geometry("800x600")
lis = ["x", "y"]

c = Canvas(main, width=800, height=600, bg='black')
c.pack()
#rules-----------------------------------
rules = [1, 2]

def Check_cell():
    global data_of_cell1
    global data_of_cell2
    global position_first_cell
    global position_second_cell
    
    
    while True:
        # coords cells
        position_first_cell = c.coords(cell1)
        position_second_cell = c.coords(cell2)

        # vision cells
        vision_cell1 = [position_first_cell[0] - 5, position_first_cell[1] - 5,
                        position_first_cell[2] - 5, position_first_cell[3] - 5]
        
        vision_cell2 = [position_second_cell[0] - 5, position_second_cell[1] - 5,
                        position_second_cell[2] - 5, position_second_cell[3] - 5]

        # run out red

        if position_first_cell[0] == vision_cell2[0] or position_first_cell[1] == vision_cell2[1] or position_first_cell[2] == vision_cell2[2] or position_first_cell[3] == vision_cell2[3]:
            kp = random.choice(lis)

            if kp == "x":
                if position_first_cell[0] + position_second_cell[2] >= position_second_cell[0] + position_second_cell[2]:
                    c.move(cell2, -1, 0)
                
                if position_first_cell[0] + position_second_cell[2] >= position_second_cell[0] + position_second_cell[2]:
                    c.move(cell2, -1, 0)
                
            elif kp == "y":
                if position_first_cell[1] + position_second_cell[3] >= position_second_cell[1] + position_second_cell[3]:
                    c.move(cell2, 0, -1)
                
                elif position_first_cell[1] + position_second_cell[3] <= position_second_cell[1] + position_second_cell[3]:
                    c.move(cell2, 0, 1)
        
        # detect of green cell
        if position_second_cell[0] == vision_cell1[0] or position_second_cell[1] == vision_cell1[1] or position_second_cell[2] == vision_cell1[2] or position_second_cell[3] == vision_cell1[3]:
            pass

        else:
            kp = random.choice(lis)
            zn = random.choice(["+", "-"])

            if kp == "x":

                if position_first_cell[0] <= 0:

                    c.move(cell1, 1, 0)
                
                elif position_first_cell[2] >= 800:
                        
                    c.move(cell1, -1, 0)

                else:

                    if zn == "+":
                        c.move(cell1, 1, 0)
                    
                    elif zn == "-":
                        c.move(cell1, -1, 0)
                    
            elif kp == "y":

                if position_first_cell[1] <= 0:

                    c.move(cell1, 0, 1)
                
                elif position_first_cell[3] >= 800:
                        
                    c.move(cell1, 0, -1)

                else:
                    if zn == "+":
                        c.move(cell1, 0, 1)
                    
                    elif zn == "-":
                        c.move(cell1, 0, -1)

position_first_cell = [30, 30, 35, 35]
position_second_cell = [200, 200, 205, 205]

data_of_cell1 = [position_first_cell, 'red', rules[0]]
data_of_cell2 = [position_second_cell, 'green', rules[1]]

cell1 = c.create_rectangle(position_first_cell[0], position_first_cell[1], 
                          position_first_cell[2], position_first_cell[3], 
                          fill='white', outline=data_of_cell1[1], width=5)

cell2 = c.create_rectangle(position_second_cell[0], position_second_cell[1], 
                          position_second_cell[2], position_second_cell[3], 
                          fill='white', outline=data_of_cell2[1], width=5)

t1 = Thread(target=Check_cell)
t1.start()

main.mainloop()