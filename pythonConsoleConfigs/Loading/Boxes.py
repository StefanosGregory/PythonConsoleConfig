from pythonConsoleConfigs.Font import Color as c
from __helper__ import run


class Box:
    def __init__(self, duration, size, color=c.WHITE, reverse=False):
        self.seconds = duration
        self.color = color
        self.reverse = reverse
        self.__emptyBox__ = "□"
        self.__fullBox__ = "■"
        self.__rate__(size)

    def __rate__(self, size):
        animation = []
        accumulator = size - 1
        if self.reverse:
            e, f = self.__fullBox__, self.__emptyBox__
        else:
            f, e = self.__fullBox__, self.__emptyBox__

        for r in range(1, size + 1):
            animation.append(f * r + e * accumulator)
            accumulator -= 1
        self.animation = animation

    def loading(self):
        run(self.color, self.animation, self.seconds)


Box(1, 10, c.BLUE, False).loading()
