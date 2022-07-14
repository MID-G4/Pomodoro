class ErrorHandler:
    '''
    To handle all errors in the whole app
    '''

    def __init__(self):
        pass


class Body:
    '''
    Implementing all the code functionally in it.
    '''
    def __init__(self):
        self.c = []

    def welcoming_main_menu(self):
        print('''
        Welcome to Pomodoro
        Please chose from the following:
        S) To start Pomodoro
        A) To add a task
        V) View all tasks
        ST) Settings
        Q) Quit Pomodoro
        ''')
        self.user_input_main_menu()


    def user_input_main_menu(self):
        choice = input("Enter your choice:")
        choice = choice.lower()
        if choice == 's':
            pass
        elif choice == 'a':
            tasks = Task()
            tasks.add_task()
        elif choice == 'v':
            pass
        elif choice == 'st':
            pass
        elif choice == 'q':
            self.quit_pomodoro()


    def timer(self):

        '''
        start the timer and break as SHB or LB
        '''
        pass

    def options(self):
        '''
        display the options in each page instructions
        '''
        pass

    def settings(self):
        pass

    def quit_pomodoro(self):
        pass


class Task:
    def __init__(self):
        self.task_number = 0
        self.task_added = {}
        self.completed_tasks = {}

    def add_task(self):
        self.task_number += 1
        task_desc = input("Please enter the task's description")
        self.task_added[self.task_number] = f'{task_desc}'

        self.list_tasks()

    def update_task(self, task):
        pass

    def task_completed(self):
        pass

    def list_tasks(self):
        """ view the added task to the user """


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

