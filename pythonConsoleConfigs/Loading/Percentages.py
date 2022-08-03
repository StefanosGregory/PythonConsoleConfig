import sys
import time
from pythonConsoleConfigs.Font import Color as c
from pythonConsoleConfigs.Font import Style as s


class Percentage:
    def __init__(self, duration, rate, color=c.WHITE):
        self.seconds = duration
        self.color = color
        self.__rate__(rate)

    def __rate__(self, rate):
        if rate == 10:
            self.animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]
        elif rate == 5:
            self.animation = ["5%", "10%", "15%", "20%", "25%", "30%", "35%", "40%", "45%", "50%", "55%", "60%", "65%",
                              "70%", "75%", "80%", "85%", "90%", "95%", "100%"]

    def loading(self):
        print(self.color, end="")
        for i in range(len(self.animation)):
            time.sleep(self.seconds)
            sys.stdout.write("\r" + self.animation[i % len(self.animation)])
            sys.stdout.flush()
        s().reset()


Percentage(1, 5, c.BLUE).loading()
