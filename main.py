from Font.Colors import Color
from Font.Highlights import Highlight
from Font.Styles import Style


def printTesting(msg, color, reset=True):
    print(f'{color} {msg}')
    if reset:
        Style().reset()


if __name__ == '__main__':
    printTesting('This is a test of Python Console Configuration Library', Color.MAGENTA)
    printTesting('This is a test of Python Console Configuration Library', Style.ITALIC)
    printTesting('This is a test of Python Console Configuration Library', Highlight.BLUE)

    print("TEST OF RESET")
