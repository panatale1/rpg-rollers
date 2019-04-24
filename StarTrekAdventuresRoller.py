from random import randint
from tkinter import *
from tkinter.ttk import *


ATTRIBUTES = ['Control', 'Fitness', 'Presence', 'Daring', 'Insight', 'Reason']
DISCIPLINES = ['Command', 'Conn', 'Security', 'Engineering', 'Science', 'Medicine']


class StarTrekAdventuresRoller(object):
    def __init__(self):
        self.dice_list = []
        self.root = Tk()
        self.root.wm_title('Star Trek Adventures Roller')
        self.control_var = StringVar()
        self.control_var.set('7')
        self.fitness_var = StringVar()
        self.fitness_var.set('7')
        self.presence_var = StringVar()
        self.presence_var.set('7')
        self.daring_var = StringVar()
        self.daring_var.set('7')
        self.insight_var = StringVar()
        self.insight_var.set('7')
        self.reason_var = StringVar()
        self.reason_var.set('7')
        self.command_var = StringVar()
        self.command_var.set('1')
        self.conn_var = StringVar()
        self.conn_var.set('1')
        self.security_var = StringVar()
        self.security_var.set('1')
        self.engineering_var = StringVar()
        self.engineering_var.set('1')
        self.science_var = StringVar()
        self.science_var.set('1')
        self.medicine_var = StringVar()
        self.medicine_var.set('1')
        self.d20_pool = StringVar()
        self.d20_pool.set('2')
        self.d6_pool = StringVar()
        self.d6_pool.set('1')
        self.challenge_pool = StringVar()
        self.challenge_pool.set('1')
        self.display_var = StringVar()
        self.attribute_select = StringVar()
        self.attribute_select.set('Control')
        self.discipline_select = StringVar()
        self.discipline_select.set('Command')
        self.success_var = StringVar()
        self.focus_var = IntVar()

    def run(self):
        self.make_roller()
        self.root.mainloop()

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

    def roll_d20(self):
        target_number = 0
        if self.attribute_select.get() == 'Control':
            target_number += int(self.control_var.get())
        elif self.attribute_select.get() == 'Fitness':
            target_number += int(self.fitness_var.get())
        elif self.attribute_select.get() == 'Presence':
            target_number += int(self.presence_var.get())
        elif self.attribute_select.get() == 'Daring':
            target_number += int(self.daring_var.get())
        elif self.attribute_select.get() == 'Reason':
            target_number += int(self.reason_var.get())
        else:
            target_number += int(self.insight_var.get())

        if self.discipline_select.get() == 'Conn':
            target_number += int(self.conn_var.get())
        elif self.discipline_select.get() == 'Command':
            target_number += int(self.command_var.get())
        elif self.discipline_select.get() == 'Engineering':
            target_number = int(self.engineering_var.get())
        elif self.discipline_select.get() == 'Security':
            target_number = int(self.security_var.get())
        elif self.discipline_select.get() == 'Science':
            target_number = int(self.science_var.get())
        else:
            target_number = int(self.medicine_var.get())

        consequences = 0
        successes = 0
        for i in range(int(self.d20_pool.get())):
            roll = randint(1, 20)
            if int(self.focus_var.get()):
                # All successes are 2 successes
                if roll <= target_number:
                    successes += 2
                elif roll == 20:
                    consequences += 1
            else:
                # 1s are 2 successes, otherwise 1 success
                if roll == 1:
                    successes += 2
                elif roll <= target_number:
                    successes += 1
                elif roll == 20:
                    consequences += 1
        total = str(successes) + ' successe(s)'
        if consequences:
            total += ' and {} consequence(s)'.format(consequences)
        self.success_var.set(total)

    def make_attributes(self, page):
        attribute_frame = LabelFrame(page, text='Attributes:')
        attribute_frame.grid(row=0, column=0, columnspan=4)
        control_dice = Spinbox(attribute_frame, textvariable=self.control_var, from_=7, to=12)
        fitness_dice = Spinbox(attribute_frame, textvariable=self.fitness_var, from_=7, to=12)
        presence_dice = Spinbox(attribute_frame, textvariable=self.presence_var, from_=7, to=12)
        daring_dice = Spinbox(attribute_frame, textvariable=self.daring_var, from_=7, to=12)
        insight_dice = Spinbox(attribute_frame, textvariable=self.insight_var, from_=7, to=12)
        reason_dice = Spinbox(attribute_frame, textvariable=self.reason_var, from_=7, to=12)
        Label(attribute_frame, text='Control dice:').grid(row=0, column=1)
        control_dice.grid(row=0, column=2)
        control_select = Radiobutton(attribute_frame, variable=self.attribute_select, value='Control')
        control_select.grid(row=0, column=0)
        Label(attribute_frame, text='Fitness dice:').grid(row=0, column=4)
        fitness_dice.grid(row=0, column=5)
        fitness_select = Radiobutton(attribute_frame, variable=self.attribute_select, value='Fitness')
        fitness_select.grid(row=0, column=3)
        Label(attribute_frame, text='Presence dice:').grid(row=0, column=7)
        presence_dice.grid(row=0, column=8)
        presence_select = Radiobutton(attribute_frame, variable=self.attribute_select, value='Presence')
        presence_select.grid(row=0, column=6)
        Label(attribute_frame, text='Daring dice:').grid(row=1, column=1)
        daring_dice.grid(row=1, column=2)
        daring_select = Radiobutton(attribute_frame, variable=self.attribute_select, value='Daring')
        daring_select.grid(row=1, column=0)
        Label(attribute_frame, text='Reason dice:').grid(row=1, column=4)
        reason_dice.grid(row=1, column=5)
        reason_select = Radiobutton(attribute_frame, variable=self.attribute_select, value='Reason')
        reason_select.grid(row=1, column=3)
        Label(attribute_frame, text='Insight dice:').grid(row=1, column=7)
        insight_dice.grid(row=1, column=8)
        insight_select = Radiobutton(attribute_frame, variable=self.attribute_select, value='Insight')
        insight_select.grid(row=1, column=6)
    
    def make_disciplines(self, page):
        discipline_frame = LabelFrame(page, text="Disciplines:")
        discipline_frame.grid(row=1, column=0, columnspan=4)
        command_dice = Spinbox(discipline_frame, textvariable=self.command_var, from_=1, to=5)
        conn_dice = Spinbox(discipline_frame, textvariable=self.conn_var, from_=1, to=5)
        security_dice = Spinbox(discipline_frame, textvariable=self.security_var, from_=1, to=5)
        engineering_dice = Spinbox(discipline_frame, textvariable=self.engineering_var, from_=1, to=5)
        science_dice = Spinbox(discipline_frame, textvariable=self.science_var, from_=1, to=5)
        medicine_dice = Spinbox(discipline_frame, textvariable=self.medicine_var, from_=1, to=5)
        Label(discipline_frame, text='Command dice:').grid(row=0, column=1)
        command_dice.grid(row=0, column=2)
        command_select = Radiobutton(discipline_frame, variable=self.discipline_select, value='Command')
        command_select.grid(row=0, column=0)
        Label(discipline_frame, text='Conn dice:').grid(row=0, column=4)
        conn_dice.grid(row=0, column=5)
        conn_select = Radiobutton(discipline_frame, variable=self.discipline_select, value='Conn')
        conn_select.grid(row=0, column=3)
        Label(discipline_frame, text='Security dice:').grid(row=0, column=7)
        security_dice.grid(row=0, column=8)
        security_select = Radiobutton(discipline_frame, variable=self.discipline_select, value='Security')
        security_select.grid(row=0, column=6)
        Label(discipline_frame, text='Engineering dice:').grid(row=1, column=1)
        engineering_dice.grid(row=1, column=2)
        engineering_select = Radiobutton(discipline_frame, variable=self.discipline_select, value='Engineering')
        engineering_select.grid(row=1, column=0)
        Label(discipline_frame, text='Science dice:').grid(row=1, column=4)
        science_dice.grid(row=1, column=5)
        science_select = Radiobutton(discipline_frame, variable=self.discipline_select, value='Science')
        science_select.grid(row=1, column=3)
        Label(discipline_frame, text='Medicine dice:').grid(row=1, column=7)
        medicine_dice.grid(row=1, column=8)
        medicine_select = Radiobutton(discipline_frame, variable=self.discipline_select, value='Medicine')
        medicine_select.grid(row=1, column=6)

    def make_success_roller(self, page):
        d20_frame = LabelFrame(page, text='Task Rolls:')
        d20_frame.grid(row=0, column=0)
        self.make_attributes(d20_frame)
        self.make_disciplines(d20_frame)
        d20_dice = Spinbox(d20_frame, textvariable=self.d20_pool, from_=1, to=10)
        d20_dice.grid(row=2, column=0)
        Checkbutton(d20_frame, text='Applicable Focus?', variable=self.focus_var, onvalue=1, offvalue=0).grid(row=2, column=1)
        Button(d20_frame, text='Roll Task', command=self.roll_d20).grid(row=3, column=0, columnspan=3)
        Label(d20_frame, text='Your roll: ').grid(row=2, column=2)
        Entry(d20_frame, textvariable=self.success_var, foreground='black', state=DISABLED, justify=CENTER).grid(row=2, column=3)

    def make_roller(self):
        page = Frame(self.root)
        self.make_success_roller(page)
        command_dice = Spinbox(page, textvariable=self.command_var, from_=1, to=5)
        conn_dice = Spinbox(page, textvariable=self.conn_var, from_=1, to=5)
        security_dice = Spinbox(page, textvariable=self.security_var, from_=1, to=5)
        engineering_dice = Spinbox(page, textvariable=self.engineering_var, from_=1, to=5)
        science_dice = Spinbox(page, textvariable=self.science_var, from_=1, to=5)
        medicine_dice = Spinbox(page, textvariable=self.medicine_var, from_=1, to=5)
        page.pack()

StarTrekAdventuresRoller().run()
