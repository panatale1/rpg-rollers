from random import randint
from Tkinter import *
from ttk import *


class GhostbustersRPGRoller(object):
    def __init__(self):
        self.dice_list = []
        self.ghost_die = False
        self.root = Tk()
        self.root.wm_title('Ghostbusters RPG Roller')
        self.trait_var = StringVar()
        self.trait_var.set('1')
        self.talent_var = IntVar()
        self.brownie_var = StringVar()
        self.brownie_var.set('0')
        self.display_var = StringVar()

    def run(self):
        self.make_roller()
        self.root.mainloop()

    def roll_ghost(self):
        ghost = randint(1, 6)
        if ghost == 6:
            self.ghost_die = True
        else:
            self.ghost_die = False
            self.dice_list.append(ghost)

    def roll_dice(self):
        if self.dice_list:
            self.dice_list = []
        dice_total = int(self.trait_var.get())
        try:
            dice_total += int(self.brownie_var.get())
        except ValueError:
            pass
        if self.talent_var.get():
            dice_total += 3
        self.roll_ghost()
        for i in range(dice_total - 1):
            self.dice_list.append(randint(1, 6))
        total = str(sum(self.dice_list))
        if self.ghost_die and self.dice_list:
            total += ' and a Ghost!'
        elif self.ghost_die:
            total = 'Ghost!'
        self.display_var.set(total)

    def make_roller(self):
        page = Frame(self.root)
        trait_dice = Entry(page, textvariable=self.trait_var)
        talent = Checkbutton(page, text='Talent?', variable=self.talent_var, onvalue=1, offvalue=0)
        brownie_points = Entry(page, textvariable=self.brownie_var)
        display = Entry(
            page, textvariable=self.display_var, foreground='black', state=DISABLED, justify=CENTER
        )
        Label(page, text='Trait dice:').grid(row=0, column=0)
        trait_dice.grid(row=0, column=1)
        talent.grid(row=0, column=2)
        Label(page, text='Brownie points:').grid(row=1, column=0)
        brownie_points.grid(row=1, column=1)
        Button(page, text='Roll!', command=self.roll_dice).grid(row=2, column=0, columnspan=3)
        Label(page, text='Your roll: ').grid(row=3, column=0)
        display.grid(row=3, column=1)
        page.pack()


GhostbustersRPGRoller().run()
