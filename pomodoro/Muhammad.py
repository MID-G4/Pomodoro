import time
import sys

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
        print('''
           Welcome to Pomodoro
           Please chose from the following:
           S) To start Pomodoro
           A) To add a task
           V) View all tasks
           ST) Settings
           Q) Quit Pomodoro
           ''')

    def settings(self, l, sh, p):
        '''
        on settings screen to show all available options can the user interact with and take the default values from the
        main class body
        '''
        text = '''
           L ) Long Break : {} m every 4 running Pomodoro's
           SH ) Short Break : {} m
           P ) Pomodoro's:  {} m
           R ) To return to main menu

           Enter the settings symbol that you want to change .
           '''.format(l, sh, p)

        print(text)

    def settings_selected(self, opt):
        ''''
        on edit selected option
        '''
        print('''
        Enter the new time for the Pomodoro section :  {} time in minutes
        press Enter to confirm your choice
        R ) To return to main menu
            '''.format(opt))

    def task_add(self):
        ''''
        in add new task screen
        '''
        print('''
            ADD New Task:
            R ) To return to main menu 
        ''')

    def task_after_added(self):
        print('''

            Task Added Successfully

            V) View all the Tasks
            R ) To return to previse menu

        ''')

    def view_list_of_tasks(self):
        '''
        in the main screen view all tasks & after add new task and select view all tasks
        '''
        print('''
        )> Enter the task number + C to mark the task as complete
        )> Enter task number to start working on it
        R) Return to main menu
        ''')

    def select_existing_task(self):
        print(
            '''
        )> Enter the task number to start.
        R)> Return to main menu.
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
              A) add task to work on
              S) select existing task
              R) return to main menu
              ''')

    def show_default_value(self, l, sh, p):
        '''
        to show the time values in the app
        '''
        text = '''
        Time: {} minutes / long break {} minutes /short break {} minutes
        '''.format(p, l, sh)
        return text

    def no_tasks_founded(self):
        print('''
        You Don't have an existing tasks !
        Do you want to add Task
        Press (A)

        R ) to return to main menu
        ''')

    def break_timer(self):
        print(
            '''
            P) to Pause the timer
            S) Start working on the task again
            LB) Start the long break
            M) return main menu
            R) return to select task
            '''
        )

    def task_in_progress(self):
        print(
            '''

            P) to Pause the timer
            LB) Start the long break
            SB) Start the short break
            M) return main menu
            R) return to select task
            C) select task as complete
            '''
        )


class Body:
    '''
    Implementing all the code functionally in it.
    '''

    def __init__(self):
        self.checkmark = 0
        self.mins = 0
        self.total_mins = 0
        # self.pomo = 25
        # self.short_break = 5
        # self.long_break = 10
        self.options_list = ListOfOptions()
        self.choice = ''
        self.task_number = 0
        self.added_tasks = {}
        self.completed_tasks = {}
        # self.input_handles = InputHandler()

    def input_messenger(self, msg):
        choice = input(msg)
        return choice

    def welcoming_main_menu(self):
        self.options_list.main_menu()
        self.user_input_main_menu()

    # create new method that will handle the input itself and do the testing

    def user_input_main_menu(self):
        choice = input("Enter your choice:")
        self.choice = choice.lower()
        InputHandler().main_menu(self.choice)

    def timer(self, userIn=25):
        '''
        start the timer for pomodoro
        '''
        start = input('Press Enter to start the timer.')
        while self.mins <= userIn:
            time.sleep(60)
            self.mins = self.mins + 1
            self.total_mins += 1
            print(self.mins, " minutes work completed.")
        print('End of this  Pomodoro')
        self.checkmark += 1
        # print('Total check mark is ', self.checkmark)

    def long_Break(self, userIn=10):
        """ set the long break """

        if self.checkmark >= 4:
            print('Lets Take a long break.!')
            while self.mins != userIn:
                time.sleep(60)
                self.mins = self.mins + 1
                print(self.mins, " minutes break completed.")
            self.checkmark = 0
            print('The Break is over.')

    def short_Break(self, userIn=3):
        """ set the short break """
        if self.checkmark < 4:
            print('Lets Take a short break.!')
            while self.mins != userIn:
                time.sleep(60)
                self.mins = self.mins + 1
                print(self.mins, " minutes break completed.")
            print('The Break is over.')

    def settings(self):
        """ Set the breaks """
        self.options_list.settings(settings["long_break"], settings["short_break"], settings["pomo"])
        # print("Enter the set/tings symbol that you want to change")
        choice = input("Enter your choice:")
        choice = choice.lower()

        if choice == 'sh':
            self.options_list.settings_selected('Short break ')

            userIn = int(input("Enter the break time :"))
            self.short_break = userIn
            settings["short_break"] = userIn
            self.settings()
        elif choice == 'l':
            self.options_list.settings_selected('Long break ')
            userIn = int(input("Enter the break time :"))
            # self.long_break = userIn
            settings["long_break"] = userIn
            self.settings()


        elif choice == 'p':
            self.options_list.settings_selected('Pomodoro break ')
            userIn = int(input("Enter the pomodoro time : "))
            # self.timer(userIn)
            # self.pomo = userIn
            settings["pomo"] = userIn
            self.settings()

        elif choice == "r":
            self.welcoming_main_menu()

    def quit_pomodoro(self):
        print('Thanks for using our app, hope to see you again ')
        sys.exit()


class InputHandler(Body):

    def main_menu(self, choice):
        tasks = Task()
        if choice == 's':
            self.start_pomodoro()
        elif choice == 'a':
            self.add_task()
            # tasks.add_task()
        elif choice == 'v':
            # tasks.list_tasks()
            self.view_all_tasks(self.added_tasks)
        elif choice == 'st':
            self.settings()
        elif choice == 'q':
            self.quit_pomodoro()

    def start_pomodoro(self):
        '''select task to work on, to update or to mark it as completed'''

        # default_values = ListOfOptions().show_default_value(self.pomo, self.long_break, self.short_break)
        ListOfOptions().start_pomodoro(
            ListOfOptions().show_default_value(settings["long_break"], settings["short_break"], settings["pomo"]))
        choice = self.input_messenger('Enter your choice: ')

        # flag = True
        # while flag:
        if choice.lower() == 'a':
            # flag = False
            # Task().add_task()
            self.add_task()
        if choice.lower() == 's':
            # flag = False
            if Task().task_number > 0:
                # Task().list_tasks()
                self.view_all_tasks(self.added_tasks)
            else:
                self.no_tasks_founded()
            # Task().select_task(choice)
        if choice.lower() == 'r':
            # flag = False
            self.welcoming_main_menu()
            # else:
            #     choice = self.input_messenger('Please make sure you entered valid input: Enter your choice: ')

            if choice.lower() == 'r':
                self.welcoming_main_menu()
            else:
                choice = self.input_messenger('Please make sure you entered valid input: Enter your choice: ')
            if choice.lower() == 'r':
                self.welcoming_main_menu()
            else:
                choice = self.input_messenger('Please make sure you entered valid input: Enter your choice: ')

    def add_task(self):
        ListOfOptions().task_add()
        # Task().add_task()
        task = Task().add_task()
        self.task_number += 1
        self.added_tasks[self.task_number] = task
        ListOfOptions().task_after_added()
        self.after_task_added()

    def after_task_added(self):
        choice = self.input_messenger('Enter your choice: ')
        if choice.lower() == 'v':
            self.view_all_tasks(self.added_tasks)

        if choice.lower() == 'r':
            self.welcoming_main_menu()
        # will be implemented soon for edge cases
        # else:
        #     choice = self.input_messenger('Please make sure you entered valid input: Enter your choice: ')
        #

    def view_all_tasks(self, task1):
        # ListOfOptions().show_default_value()

        # Task().list_tasks()
        print(self.added_tasks)
        ListOfOptions().view_list_of_tasks()
        choice = self.input_messenger('Enter your choice: >')
        # print(len(choice))
        if len(choice) > 1:
            if (int(choice[0]) in self.added_tasks) and (choice[1].lower() == 'c'):
                self.completed_tasks[self.task_number] = self.added_tasks.get(self.task_number)
                print(self.completed_tasks)
                self.view_all_tasks(self.added_tasks)
            else:
                print('something went wrong')
                self.view_all_tasks(self.added_tasks)
                # self.completed_tasks[self.task_number] = self.added_tasks.get(self.task_number)
        if len(choice) == 1 and choice != 'r':
            if int(choice[0]) in self.added_tasks:
                # start the timer
                # timer
                task = self.added_tasks[int(choice)]
                self.task_in_progress(task)
            else:
                print("something went wrong probably you don't have any available\n tasks or you entered wrong number")
                self.view_all_tasks(self.added_tasks)



        elif choice.lower() == 'r':
            self.welcoming_main_menu()

    # def select_task(self):
    #     ListOfOptions().show_default_value()
    #     Task().list_tasks()
    #     choice = self.input_messenger('Enter your choice: >')
    #     if choice in Task().added_tasks:
    #         Task().select_task(choice)
    #         ListOfOptions().select_existing_task()

    def no_tasks_founded(self):
        ListOfOptions().no_tasks_founded()
        choice = self.input_messenger('Enter your choice: ')
        if choice.lower() == "a":
            self.add_task()

    def task_in_progress(self, task):
        print(task)

        # timer progress
        ListOfOptions().task_in_progress()
        choice = self.input_messenger('Enter your choice: ')
        if choice.lower() == 'p':
            # pause timer
            pass
        if choice.lower() == 'lb':
            self.short_Break()
            self.break_in_progress(task)

        if choice.lower() == 'sb':
            self.short_Break()
            self.break_in_progress(task)
        if choice.lower() == 'm':
            self.welcoming_main_menu()
        if choice.lower() == 'r':
            self.view_all_tasks(self.added_tasks)
        if choice.lower() == 'c':
            # mark task as complete
            # Task().update_added_tasks(task)
            Task().update_added_tasks('1')

    def break_in_progress(self, task):
        print(task)
        # timer progress
        ListOfOptions().task_in_progress()
        choice = self.input_messenger('Enter your choice: ')

        if choice.lower() == 'p':
            # pause
            pass
        if choice.lower() == 's':
            self.task_in_progress(task)
        if choice.lower() == 'lb':
            self.break_in_progress(task)
            self.long_Break()
        if choice.lower() == 'm':
            self.welcoming_main_menu()
        if choice.lower() == 'r':
            self.view_all_tasks(self.added_tasks)


class Task:
    def __init__(self):
        self.task_number = 0
        self.added_tasks = {}
        self.completed_tasks = {}
        # pass

    def add_task(self):
        """add a task to the list of tasks"""
        self.task_number += 1
        task_desc = input("Please enter the task's description: >")
        task = self.added_tasks[self.task_number] = f'{task_desc}'
        # Body().added_tasks[Body().task_number] = f'{task_desc}'

        self.list_tasks()
        return task

    # def complete_task(self):
    #     """add a task to the completed list of tasks"""
    #     self.completed_tasks[self.task_number] = self.added_tasks.get(self.task_number)
    #     return self.completed_tasks

    def delete_task(self):
        """delete a task for the list of added tasks"""
        del self.added_tasks[self.task_number]

    def update_added_tasks(self, task):
        """add a task to the completed list and delete it from the added list"""
        self.complete_task()
        self.delete_task()

    def list_tasks(self):
        """ view the added task to the user """
        print(self.added_tasks)
        return self.added_tasks


class Display:
    '''
    To render all the app content
    functionally : root
    '''

    def __init__(self):
        pass


if __name__ == '__main__':
    B = Body()
    B.welcoming_main_menu()
