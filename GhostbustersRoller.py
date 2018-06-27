from random import randint
from Tkinter import *
from ttk import *


class GhostbustersRPGRoller(object):
    def __init__(self):
        self.dice_list = []
        self.ghost_die = False
        self.root = Tk()
        self.root.wm_title('Ghostbusters RPG Roller')
        self.brains_var = StringVar()
        self.brains_var.set('1')
        self.brains_talent_var = IntVar()
        self.cool_var = StringVar()
        self.cool_var.set('1')
        self.cool_talent_var = IntVar()
        self.moves_var = StringVar()
        self.moves_var.set('1')
        self.moves_talent_var = IntVar()
        self.muscles_var = StringVar()
        self.muscles_var.set('1')
        self.muscles_talent_var = IntVar()
        self.trait_var = StringVar()
        self.trait_var.set('1')
        self.talent_var = IntVar()
        self.brownie_var = StringVar()
        self.brownie_var.set('0')
        self.display_var = StringVar()
        self.total_brownie_var = StringVar()
        self.total_brownie_var.set('0')

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

    def roll_brains(self):
        dice_total = int(self.brains_var.get())
        is_talent = bool(self.brains_talent_var.get())
        self.roll_dice(dice_total, is_talent)

    def roll_cool(self):
        dice_total = int(self.cool_var.get())
        is_talent = bool(self.cool_talent_var.get())
        self.roll_dice(dice_total, is_talent)

    def roll_moves(self):
        dice_total = int(self.moves_var.get())
        is_talent = bool(self.moves_talent_var.get())
        self.roll_dice(dice_total, is_talent)

    def roll_muscles(self):
        dice_total = int(self.muscles_var.get())
        is_talent = bool(self.muscles_talent_var.get())
        self.roll_dice(dice_total, is_talent)

    def update_brownie_points(self):
        points_used = int(self.brownie_var.get())
        points_left = int(self.total_brownie_var.get()) - points_used
        self.total_brownie_var.set(points_left)

    def roll_dice(self, dice_total, is_talent):
        if self.dice_list:
            self.dice_list = []
        try:
            dice_total += int(self.brownie_var.get())
        except ValueError:
            pass
        self.update_brownie_points()
        if is_talent:
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
        self.brownie_var.set('0')

    def make_roller(self):
        page = Frame(self.root)
        brains_dice = Spinbox(page, textvariable=self.brains_var, from_=1, to=10)
        cool_dice = Spinbox(page, textvariable=self.cool_var, from_=1, to=10)
        moves_dice = Spinbox(page, textvariable=self.moves_var, from_=1, to=10)
        muscles_dice = Spinbox(page, textvariable=self.muscles_var, from_=1, to=10)
        brains_talent = Checkbutton(page, text='Talent?', variable=self.brains_talent_var, onvalue=1, offvalue=0)
        cool_talent = Checkbutton(page, text='Talent?', variable=self.cool_talent_var, onvalue=1, offvalue=0)
        moves_talent = Checkbutton(page, text='Talent?', variable=self.moves_talent_var, onvalue=1, offvalue=0)
        muscles_talent = Checkbutton(page, text='Talent?', variable=self.muscles_talent_var, onvalue=1, offvalue=0)
        display = Entry(
            page, textvariable=self.display_var, foreground='black', state=DISABLED, justify=CENTER
        )
        Label(page, text='Brains dice:').grid(row=0, column=0)
        brains_dice.grid(row=0, column=1)
        brains_talent.grid(row=0, column=2)
        Button(page, text='Roll Brains!', command=self.roll_brains).grid(row=0, column=3)
        Label(page, text='Cool dice:').grid(row=1, column=0)
        cool_dice.grid(row=1, column=1)
        cool_talent.grid(row=1, column=2)
        Button(page, text='Roll Cool!', command=self.roll_cool).grid(row=1, column=3)
        Label(page, text='Moves dice:').grid(row=2, column=0)
        moves_dice.grid(row=2, column=1)
        moves_talent.grid(row=2, column=2)
        Button(page, text='Roll Moves!', command=self.roll_moves).grid(row=2, column=3)
        Label(page, text='Muscles dice:').grid(row=3, column=0)
        muscles_dice.grid(row=3, column=1)
        muscles_talent.grid(row=3, column=2)
        Button(page, text='Roll Muscles!', command=self.roll_muscles).grid(row=3, column=3)
        Label(page, text='Total Brownie Points:').grid(row=4, column=0)
        total_brownie = Spinbox(page, textvariable=self.total_brownie_var, from_=0, to=100)
        total_brownie.grid(row=4, column=1)
        Label(page, text='Apply Brownie\npoints to roll:').grid(row=4, column=2)
        brownie_points = Entry(page, textvariable=self.brownie_var)
        brownie_points.grid(row=4, column=3)
        Label(page, text='Your roll: ').grid(row=5, column=0, columnspan=2)
        display.grid(row=5, column=1, columnspan=2)
        page.pack()


GhostbustersRPGRoller().run()
