import sys
sys.path.insert(0, '../controllers/')

from controller import Controller


class View:
    menu_choice = [
        'Fetch api and Insert data in DATABASE',
        'Select from DATABASE'
    ]
    selection_choice = [
        'Select all users',
        'Select all todos',
        'Select all posts',
        'Select all comments',
        'Select all albums',
        'Select all photos',
        'Select them all'
    ]
    @classmethod
    def selection(cls):
        try:
            while len(cls.selection_choice) > 0:
                for ind, choice in enumerate(cls.selection_choice):
                    print(f"                {ind + 1}.{choice}")
                print('                ctrl + c: pour quitter')
                try:
                    schoice = int(input())
                except ValueError:
                    cls.selection()
                if schoice == 0:
                    cls.selection()
                popped = cls.selection_choice[schoice - 1].split()[2]
                Controller.retrieve_model(popped)
                print(100 * '-')
                cls.selection()
        except KeyboardInterrupt:
            print()
            sys.exit('A bientot ..')



    @classmethod
    def menu(cls):
        xchoice = ''
        while xchoice == '' or xchoice is not int:
            for ind, choice in enumerate(cls.menu_choice):
                print(f"{ind + 1}.{choice}")
            try:
                xchoice = int(input())
            except ValueError:
                cls.menu()

            if xchoice == 2:
                cls.selection()
            elif xchoice == 1:
                # cls.menu_choice.remove(cls.menu_choice[xchoice - 1])
                try:
                    print('Fetching information from : jsonplaceholder.typicode.com ...')
                    Controller.prepare_model('all')
                    cls.menu()
                except:
                    print('La base de donnees est deja fournie\n Vous pouvez commencer vos requetes')
                    cls.menu()





# demarrage du programme
View.menu()
