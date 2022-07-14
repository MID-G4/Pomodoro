import time
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
        self.checkmark = 0
        self.mins = 0
        self.total_mins=0

    def welcoming(self):
        pass

    def timer(self,userIn = 25):
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

    def short_Break(self,userIn=3):
        """ set the short break """
        if self.checkmark < 4:
            print('Lets Take a short break.!')
            while self.mins !=userIn:
                time.sleep(60)
                self.mins = self.mins + 1
                print(self.mins, " minutes break completed.")
            print('The Break is over.')

    def settings(self):
        """ Set the breaks """
        print("Enter the settings symbol that you want to change")
        choice = input("Enter your choice:")
        choice = choice.lower()

        if choice == 'sh':
            userIn = int(input("Enter the break time :"))
            self.short_Break(userIn)



        elif choice == 'L':
            userIn = int(input("Enter the break time :"))
            self.long_Break(userIn)



        elif choice == 'P':
            userIn = int(input("Enter the pomodoro time : "))
            self.timer(userIn)


    def quit_app(self):
        pass



class Task:
    def __init__(self):
        self.task_number = 0
        self.task_added = {}

    def add_task(self):
        self.task_number += 1
        task_desc = input("Please enter the task's description")
        self.task_added[self.task_number] = f'{task_desc}'


    def update_task(self, task):
        pass


    def list_tasks(self):
        """ Display  the added task to the user """
        # print("Task Added successfully ! .")
        print (self.task_added)




class Display:
    '''
    To render all the app content
    functionally : root
    '''

    def __init__(self):
        pass

