# ici on doit mettre l'affichage de notre systeme
import sys
sys.path.insert(0, '../controllers/')

from controller import Controller


class View:
    choices = [
        'Create database',
        'Fetch api and Insert data in DATABASE',
        'Select from DATABASE'
    ]

    @classmethod
    def selection(cls):
        pass


    @classmethod
    def menu(cls):
        menu_choice = cls.choices.copy()
        while len(menu_choice) > 0:
            for ind, choice in enumerate(menu_choice):
                print(f"{ind + 1}.{choice}")
            xchoice = input()

            if xchoice == 3:
                cls.selection()
                cls.menu()
            else:
                if xchoice == 1:
                    menu_choice.remove(menu_choice[xchoice - 1])


# this has to be in the views
# Controller.retrieve_model('users')

View.menu()
