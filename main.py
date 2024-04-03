import random 
import tkinter as tk

from time import sleep


def zapalka(x, y): 
    canvas.create_line(x, y, x, y+100, width=5, fill='yellow') 
    canvas.create_oval(x-5, y-5, x+5, y+8, fill='brown', outline='brown')


def create(zapalky):
    for i in zapalky:
        zapalka(i*40+40, 40)


def turn(player_id):
    a = input(f'Player {player_id + 1}, how many sticks do you want to take? ')
    if a.isdigit() and int(a) <= 3:
        return int(a)
    else:
        print('Invalid input, try again')
    return turn(player_id)
    

def main():
    zapalky = list(range(15))
    create(zapalky)
    player_id = 0
    while zapalky:
        n = turn(player_id)
        if n > len(zapalky):
            print('Congrats, you have entered more sticks than there are in the pile!')
            sleep(2.5)
            print(f'Player {player_id + 1}, you lose!')
            break

        elif n == len(zapalky):
            print(f'Player {player_id + 1}, you win!')
            break
        else:
            for i in range(n):
                zapalky.pop(random.randint(0, len(zapalky)-1))
            canvas.delete("all")
            create(zapalky)
        player_id = (player_id + 1) % 2
    root.destroy()


root = tk.Tk()
root.geometry("650x200")

canvas = tk.Canvas(width=650, height=200) 
canvas.pack() 



canvas.after(1000, main)


root.mainloop()
