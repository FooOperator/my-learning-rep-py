from playsound import playsound
import os
import tkinter as tk
from tkinter import StringVar

cuts = 0
ranks = {
    0: ['Dismal', 'blue'],
    3: ['Crazy', 'darkblue'],
    5: ['Badass', 'lightblue'],
    10: ['Apocalyptic', 'lightblue'],
    15: ['Savage', 'yellow'],
    20: ['Sick Skills', 'gold'],
    25: ['Smokin\' Sexy Style!', '#dea403']
}

window = tk.Tk()

update_counter = lambda : counter.set('Cuts So Far: {}'.format(cuts))

def cut():
    global cuts
    playsound('assets\\jc.mp3', False)
    cuts += 1
    update_counter()
    
def show_rank():
    global cuts
    global ranks
    rank_index = min(ranks.keys(), key=lambda k : abs(k-cuts))
    if cuts in ranks:
        rank_change.set('Rank\n{}\nMax Cuts: {}'.format(ranks[cuts][0], cuts))
        rank_label.config(fg=ranks[cuts][1])
    else:
        rank_change.set('Rank\n{}\nMax Cuts: {}'.format(ranks[rank_index][0], cuts))
        rank_label.config(fg=ranks[rank_index][1])
    cuts = 0
    rank_label.config(bg='grey')
    update_counter()
    playsound('assets\\jc end.mp3', False)
    

counter = tk.StringVar()
counter_label = tk.Label(textvariable=counter)
update_counter()
rank_change = tk.StringVar()
rank_label = tk.Label(textvariable=rank_change)
 
end_button = tk.Button(
    text='END',
    width=40,
    height=3,
    bg='blue',
    fg='darkblue',
    command=show_rank
) 
    
cut_button = tk.Button(
    text='Judgement Cut',
    width=25,
    height=2,
    bg='blue',
    fg='magenta',
    command= cut
)

window.geometry('300x200')
window.resizable(0, 0)
counter_label.pack()
cut_button.pack()
end_button.pack()
rank_label.pack()

window.mainloop()