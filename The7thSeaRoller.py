from copy import deepcopy
from random import randint
from Tkinter import *
from ttk import *


class The7thSeaRoller(object):
    def __init__(self):
        self.dice_list = []

    def run(self):
        self.make_root()
        self.make_roller()
        self.root.mainloop()

    def make_root(self):
        self.root = Tk()
        self.root.wm_title('7th Sea Raise Roller')

    def roll_dice(self):
        if self.dice_list:
            self.dice_list = []
        trait = int(self.trait_dice.get())
        skill = int(self.skill_dice.get())
        bonus = int(self.bonus_dice.get())
        explode = self.explode_var.get() or skill == 5
        legendary = self.legendary_var.get()
        for i in range(trait + skill + bonus - legendary):
            self.dice_list.append(randint(1, 10))
            while explode and self.dice_list[-1] == 10:
                    self.dice_list.append(randint(1, 10))
        if legendary:
            self.dice_list.append(10)
            while explode and self.dice_list[-1] == 10:
                self.dice_list.append(randint(1, 10))
        self.dice_list.sort()
        if self.add_one_var.get():
            for i in range(len(self.dice_list)):
                self.dice_list[i] += 1
        str_dice_list = []
        for die in self.dice_list:
            str_dice_list.append(str(die))
        self.dice_var.set(', '.join(str_dice_list))
        if len(self.dice_var.get()) > 20:
            self.dice_field.config(width=len(self.dice_var.get()))
        self.dice_field.grid(row=5, column=0, columnspan=3)

    def calculate_raises(self):
        dice_copy = deepcopy(self.dice_list)
        raise_target = 10
        double_raises = False
        if int(self.skill_dice.get()) > 4:
            double_raises = True
        if self.gm_var:
            raise_target += 5
        if double_raises:
            self.group_raises(dice_copy, raise_target + 5, 2)
        # self.group_raises(dice_copy, raise_target, 1)

    def group_raises(self, rolls, target, raises_per_set):
        raises = []
        initial = 10
        # If target is 10, all 10s count as a single Raise
        if target == 10:
            while rolls[-1] == 10:
                raises.append((rolls.pop()))
            initial = 9
        while sum(rolls) > target:
            for h in range(min(initial, target), 0, -1):
                l = min(target - h, h)

    def make_roller(self):
        page = Frame(self.root)
        self.trait_dice = Spinbox(page, from_=2, to=6)
        self.skill_dice = Spinbox(page, from_=0, to=6)
        self.bonus_dice = Spinbox(page, from_=0, to=10)
        self.add_one_var = IntVar()
        self.explode_var = IntVar()
        self.legendary_var = IntVar()
        add_one = Checkbutton(page, text='Add one to each die', variable=self.add_one_var, onvalue=1, offvalue=0)
        explode = Checkbutton(page, text='Force exploding 10s', variable=self.explode_var, onvalue=1, offvalue=0)
        legendary = Checkbutton(page, text='Legendary trait', variable=self.legendary_var, onvalue=1, offvalue=0)
        roll_button = Button(page, text='Roll dice', command=self.roll_dice)
        Label(page, text='Trait dice:').grid(row=0, column=0)
        self.trait_dice.grid(row=0, column=1)
        Label(page, text='Skill dice:').grid(row=1, column=0)
        self.skill_dice.grid(row=1, column=1)
        Label(page, text='Bonus dice').grid(row=2, column=0)
        self.bonus_dice.grid(row=2, column=1)
        add_one.grid(row=3, column=0)
        explode.grid(row=3, column=1)
        legendary.grid(row=3, column=2)
        roll_button.grid(row=4, column=0, columnspan=3)
        self.dice_var = StringVar()
        self.dice_field = Entry(page, textvariable=self.dice_var, foreground='black', state=DISABLED, justify=CENTER)
        self.dice_field.grid(row=5, column=0, columnspan=3)
        self.gm_var = IntVar()
        Checkbutton(page, text='GM increases difficulty', variable=self.gm_var, onvalue=1, offvalue=0).grid(row=6, column=0)
        self.raise_var = StringVar()
        self.raise_field = Entry(page, textvariable=self.raise_var, foreground='black', state=DISABLED)
        raise_button = Button(page, text='Calculate raises', command=self.calculate_raises)
        raise_button.grid(row=6, column=1, columnspan=2)
        self.raise_field.grid(row=7, column=0, columnspan=3)
        page.pack()
