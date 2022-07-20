import sys, os
import pandas as pd
import numpy as np
from os.path import exists

from pomodoro_gui import *


def prGreen(skk): print("\033[92m {}\033[00m".format(skk))


def prRed(skk): print("\033[91m {}\033[00m".format(skk))


settings = {"pomo": 25, "long_break": 10, "short_break": 5}


class ErrorHandler:
    '''
    To handle all errors in the whole app
    '''

    def __init__(self):
        pass


class ListOfOptions:
    def __init__(self):
        pass

    def main_menu(self):
        os.system('cls')
        frames = []
        filename = ['welcome.txt']
        for name in filename:
            with open(name, 'r', encoding='utf-8') as f:
                frames.append(f.readlines())
            # for i in range(1):
            for frame in frames:
                prRed("".join(frame))
                time.sleep(0.1)
                os.system('cls')
        print('''
           Please choose from the following:
           S) To start Pomodoro
           A) Add task to your workplace
           V) View all the tasks
           ST) For settings
           Q) To quit the application
           ''')

    def settings(self, l, sh, p):
        '''
        on settings screen to show all available options can the user interact with and take the default values from the
        main class body
        '''
        text = '''
           L) Long break: {} m every 4 running Pomodoro's
           SH) Short break: {} m
           P) Pomodoro's: {} m
           R) To return to main menu

           Enter the setting letter that you want to change.
           '''.format(l, sh, p)

        print(text)

    def settings_selected(self, opt):
        ''''
        on edit selected option
        '''
        print('''
        Enter the new time for the Pomodoro: {} time in minutes
        Press enter to confirm your choice.
        R) To return to main menu
            '''.format(opt))

    def task_add(self):
        ''''
        in add new task screen
        '''
        print('''
            Ad new task:
            R) To return to main menu 
        ''')

    def task_after_added(self):
        prGreen('''Task added successfully''')
        print('''
            V) View all the tasks
            R) To return to starting menu
        ''')

    def view_list_of_tasks(self):
        '''
        in the main screen view all tasks & after add new task and select view all tasks
        '''
        print('''
        > Enter the task number + C to mark the task as completed.
        > Enter the task number to start working on it.
        R) Return to starting menu
        ''')

    def select_existing_task(self):
        print(
            '''
        > Enter the task number to start.
        R) Return to main menu
            '''
        )

    def start_pomodoro(self, opt_func):
        '''
        on the second screen after select Start pomodoro
        '''
        print('''
        To start Pomodoro:''' +
              opt_func +
              '''
              A) Add task to work on
              S) Select an existing task
              R) Return to main menu
              ''')

    def show_default_value(self, p, l, sh):
        '''
        to show the time values in the app
        '''

        text = '''
        Time: Task {} minutes / long break {} minutes / short break {} minutes
        '''.format(p, l, sh)
        return text

    def no_tasks_founded(self):
        print('''
        You don't have an existing task!
        Do you want to add a task?
        Press (A)

        R) To return to main menu
        ''')

    # def break_timer(self):
    #     print(
    #         '''
    #         S) Start working on the task again
    #         LB) Start the long break
    #         M) return main menu
    #         R) return to select task
    #         '''
    #     )

    def task_in_progress(self):
        print(
            '''
            M) Return to main menu
            R) Return to select a task
            C) Select task as complete
            '''
        )


class Body:
    '''
    Implementing all the code functionally in it.
    '''

    def __init__(self):
        self.options_list = ListOfOptions()
        self.choice = ''
        self.task_number = 0
        self.added_tasks = {}
        self.completed_tasks = {}

    def input_messenger(self, msg):
        choice = input(msg)
        return choice

    def welcoming_main_menu(self):
        self.options_list.main_menu()
        self.user_input_main_menu()

    # create new method that will handle the input itself and do the testing

    def user_input_main_menu(self):
        choice = input("Enter your choice: ")
        self.choice = choice.lower()
        InputHandler().main_menu(self.choice)

    def settings(self):
        """ Set the breaks """
        self.options_list.settings(settings["long_break"], settings["short_break"], settings["pomo"])
        choice = input("Enter your choice: ")
        choice = choice.lower()

        if choice == 'sh':
            self.options_list.settings_selected('Short break ')
            user_in = input("Enter the break time: ")
            if user_in == 'r':
                self.settings()
            settings["short_break"] = int(user_in)
            self.settings()
        elif choice == 'l':
            self.options_list.settings_selected('Long break ')
            user_in = input("Enter the break time: ")
            if user_in == 'r':
                self.settings()
            settings["long_break"] = int(user_in)
            self.settings()
        elif choice == 'p':
            self.options_list.settings_selected('Pomodoro break ')
            user_in = input("Enter the pomodoro time: ")
            if user_in == 'r':
                self.settings()
            settings["pomo"] = int(user_in)
            self.settings()
        elif choice == "r":
            self.welcoming_main_menu()

        else:
            prRed("Please make sure you entered a valid input!")
            self.settings()

    def quit_pomodoro(self):
        print('Thanks for using our app, hope to see you again!')
        sys.exit()


class InputHandler(Body):

    def main_menu(self, choice):
        if choice == 's':
            self.start_pomodoro()
        elif choice == 'a':
            self.add_task()
        elif choice == 'v':
            self.view_all_tasks(self.added_tasks)
        elif choice == 'st':
            self.settings()
        elif choice == 'q':
            self.quit_pomodoro()

    def start_pomodoro(self):
        '''select task to work on, to update or to mark it as completed'''

        ListOfOptions().start_pomodoro(ListOfOptions().show_default_value(settings["pomo"], settings["long_break"],
                                                                          settings["short_break"]))
        choice = self.input_messenger('Enter your choice: ')

        if choice.lower() == 'a':
            self.add_task()
        if choice.lower() == 's':
            if self.task_number > 0:
                self.view_all_tasks(self.added_tasks)
            else:
                self.no_tasks_founded()
        if choice.lower() == 'r':
            self.welcoming_main_menu()

        else:
            prRed("Please make sure you entered a valid input!")
            self.start_pomodoro()

    def add_task(self):
        ListOfOptions().task_add()
        task = self.input_task_desc()
        if task == 'r':
            self.start_pomodoro()
        self.task_number += 1
        self.added_tasks[self.task_number] = task
        ListOfOptions().task_after_added()
        self.after_task_added()

    def after_task_added(self):
        file_exists = exists('./tasks.csv')
        if file_exists:
            df = pd.read_csv('tasks.csv', on_bad_lines='skip')

            df = pd.DataFrame(self.added_tasks,index=[0])
            df.to_csv('tasks.csv',header=False)
            print(df,"exists")
        else:
            df = pd.DataFrame(self.added_tasks,index=[0])
            df.to_csv("./tasks.csv",sep='\t')
            print(df)

        choice = self.input_messenger('Enter your choice: ')
        if choice.lower() == 'v':
            self.view_all_tasks(self.added_tasks)

        if choice.lower() == 'r':
            self.start_pomodoro()
        # will be implemented soon for edge cases
        else:
            print('Please make sure you entered a valid input!')
            self.after_task_added()

    def view_all_tasks(self, task1):
        prRed('''To do list''')

        for key, value in self.added_tasks.items():
            print(" " + str(key) + " - " + value)

        ListOfOptions().view_list_of_tasks()
        choice = self.input_messenger('Enter your choice: ')
        if len(choice) > 1:
            # if type(choice[0]) is str:
            #     prRed('Something went wrong!')
            #     self.view_all_tasks(self.added_tasks)
            if (int(choice[0]) in self.added_tasks) and (choice[1].lower() == 'c'):
                self.completed_tasks[self.task_number] = self.added_tasks.get(self.task_number)
                del self.added_tasks[self.task_number]
                prGreen(''' Completed tasks list:''')
                for key, value in self.completed_tasks.items():
                    print(" " + str(key) + " - " + value)
                self.view_all_tasks(self.added_tasks)

            else:
                print('Something went wrong!')
                self.view_all_tasks(self.added_tasks)

        if len(choice) == 1 and choice != 'r':
            if int(choice[0]) in self.added_tasks:
                task = self.added_tasks[int(choice)]
                self.task_in_progress(task, int(choice))
            else:
                prRed(
                    "Something went wrong probably you don't have any available\n tasks or you entered a wrong number.")
                self.view_all_tasks(self.added_tasks)

        if choice.lower() == 'r':
            self.start_pomodoro()

        else:
            # handle wrong input
            prRed("Please make sure you entered a valid input!")
            self.view_all_tasks(self.added_tasks)

    def no_tasks_founded(self):
        ListOfOptions().no_tasks_founded()
        choice = self.input_messenger('Enter your choice: ')
        if choice.lower() == "a":
            self.add_task()
        if choice.lower() == "r":
            self.start_pomodoro()
        else:
            # handle wrong input
            prRed("Please make sure you entered valid input!")
            self.no_tasks_founded()

    def task_in_progress(self, task, task_number):
        print(task)
        pomo_coun = PomodoroTimer(settings)
        ListOfOptions().task_in_progress()
        choice = self.input_messenger('Enter your choice: ')
        if choice.lower() == 'm':
            self.welcoming_main_menu()
        if choice.lower() == 'r':
            self.view_all_tasks(self.added_tasks)
        if choice.lower() == 'c':
            self.completed_tasks[task_number] = self.added_tasks.get(task_number)
            file_exists = exists('./tasks.csv')
            if file_exists:
                df = pd.read_csv('tasks.csv', on_bad_lines='skip')
                df = pd.DataFrame(self.added_tasks, index=[0])
                df.drop([task_number], axis=1, inplace=True)
                print(df)
        # else:
        #     print('no existing tasks plz make sure you add tasks before list them as completed ')
        #
            del self.added_tasks[task_number]
            prGreen(''' Completed tasks list:''')
            for key, value in self.completed_tasks.items():
                print(" " + str(key) + " - " + value)
            self.view_all_tasks(self.added_tasks)

        else:
            prRed("Please make sure you entered valid input!")
            self.view_all_tasks(self.added_tasks)

    def input_task_desc(self):
        task_desc = input("Please enter the task's description: ")
        return task_desc


if __name__ == '__main__':
    B = Body()
    B.welcoming_main_menu()
