import customtkinter as CTk
from tkinter import *
from threading import Thread

main = CTk.CTk()
main.title("Cell's life")
main.geometry("800x600")

c = Canvas(main, width=800, height=600, bg='black')
c.pack()
#rules-----------------------------------
rules = [1, 2]

def Check_cell():
    global data_of_cell1
    global data_of_cell2
    global position_first_cell
    global position_second_cell
    
    end = position_second_cell[:] = [i-5 for i in position_second_cell]
    
    while True:
        vision_coords = c.coords(cell1)
        print(vision_coords)

        if vision_coords == end:
            data_of_cell2[1] = 'red'
            c.itemconfig(cell2, outline='red')
            break
     
        else:
            position_first_cell = c.coords(cell1)
        
            data_of_cell1[0] = position_first_cell
        
            c.move(cell1, 1, 1)

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