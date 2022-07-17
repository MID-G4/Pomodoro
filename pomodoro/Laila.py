import time

class Pomodoro:
  def init(self):
    pass

  def pomodoro(self):
    print("Pomodoro Timer!")
    while True:
      t = input("Enter the time for a task in seconds: ")
      self.countdown(int(t))
      print("Good job! You deserve a break!")
      t = input("Enter the time for a break in seconds: ")
      self.countdown(int(t))
      print("Break is done! Now its work time.")

  def countdown(self, t):
      while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
      # print('Break is done!!!')


if __name__ == '__main__':
  pomo = Pomodoro()
  pomo.pomodoro()
# pomodoro()