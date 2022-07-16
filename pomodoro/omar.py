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
        pass

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
            tasks = Task()
            tasks.list_tasks()
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
        self.added_tasks = {}
        self.completed_tasks = {}

    def add_task(self):
        """add a task to the list of tasks"""
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

    def __init__(self):
        pass


if __name__ == '__main__':
    B = Body()
    B.welcoming_main_menu()

