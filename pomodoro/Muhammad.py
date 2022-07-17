import time


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

    def settings(self, p, sh, l):
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
            ADD New Task:
            R ) To return to main menu
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

    def start_pomodoro(self):
        '''
        on the second screen after select Start pomodoro
        '''
        print('''
        To start Pomodoro:
        Time: {} minutes / long break {} minutes /short break {} minutes
        A) add task to work on
        S) select existing task
        R) return to main menu
        ''')

    def show_default_value(self, p, l, sh):
        '''
        to show the time values in the app
        '''
        print('''
        Time: {} minutes / long break {} minutes /short break {} minutes
        '''.format(p, l, sh))

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
            SL) Start the long break
            M) return main menu
            Q) return to select task
            '''
        )

    def started_timer(self):
            print(
                '''
                P) to Pause the timer
                SL) Start the long break
                SH) Start the short break
                M) return main menu
                Q) return to select tasks
                S) mark task as complete
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
        self.pomo = 25
        self.short_break = 5
        self.long_break = 10
        self.options_list = ListOfOptions()
        # self.input_handles = InputHandler()

    def welcoming_main_menu(self):
        self.options_list.main_menu()
        self.user_input_main_menu()

    def user_input_main_menu(self):
        choice = input("Enter your choice:")
        choice = choice.lower()
        # self.O.main_menu()
        if choice == 's':
            pass
        elif choice == 'a':
            tasks = Task()
            tasks.add_task()
        elif choice == 'v':
            pass
        elif choice == 'st':
            self.settings()
        elif choice == 'q':
            self.quit_pomodoro()

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

    def options(self):
        '''
        display the options in each page instructions
        '''
        pass

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
        self.options_list.settings(self.pomo, self.short_break, self.long_break)
        # print("Enter the set/tings symbol that you want to change")
        choice = input("Enter your choice:")
        choice = choice.lower()

        if choice == 'sh':
            self.options_list.settings_selected('Short break ')
            userIn = int(input("Enter the break time :"))
            self.short_break = int(userIn)
            self.settings()
        elif choice == 'l':
            self.options_list.settings_selected('Long break ')
            userIn = int(input("Enter the break time :"))
            self.long_break = int(userIn)
            self.settings()


        elif choice == 'p':
            self.options_list.settings_selected('Pomodoro break ')
            userIn = int(input("Enter the pomodoro time : "))
            # self.timer(userIn)
            self.pomo = int(userIn)
            self.settings()

    def quit_pomodoro(self):
        pass


class InputHandler(Body):
    def main_menu(self, choice):
        if choice == 's':
            pass
        elif choice == 'a':
            tasks = Task()
            tasks.add_task()
        elif choice == 'v':
            pass
        elif choice == 'st':
            self.settings()
        elif choice == 'q':
            self.quit_pomodoro()

    def select_task(self, task_number):
        "select task to work on, to update or to mark it as completed"
        pass


class Task:
    def __init__(self):
        self.task_number = 0
        self.added_tasks = {}
        self.completed_tasks = {}
        # self.options_list = ListOfOptions().task_added()

    def add_task(self):
        """add a task to the list of tasks"""
        # self.options_list.task_added()
        self.task_number += 1
        task_desc = input("Please enter the task's description")
        self.added_tasks[self.task_number] = f'{task_desc}'

        self.list_tasks()

    def complete_task(self):
        """add a task to the completed list of tasks"""
        self.completed_tasks[self.task_number] = self.added_tasks.get(self.task_number)

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


class Display:
    '''
    To render all the app content
    functionally : root
    '''

    # list_of_options = ListOfOptions()

    def __init__(self):
        # self.list_of_options = list_of_options()
        self.body = Body()
        # self.tasks = Task()
        pass

    def run_app(self):
        '''
        This the main method responsible for runing the hole app
        '''
        self.body.welcoming_main_menu()


if __name__ == '__main__':
    x = Display()
    x.run_app()
