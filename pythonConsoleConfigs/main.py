from Font import Color, Style, Highlight


def printTesting(msg, color, reset=True):
    print(f'{color}{msg}')
    if reset:
        Style().reset()


if __name__ == '__main__':
    printTesting('This is a test of Python Console Configuration Library', Color.MAGENTA)
    printTesting('This is a test of Python Console Configuration Library', Style.BLINK)
    printTesting('This is a test of Python Console Configuration Library', Highlight.BLUE)
    printTesting('This is a test of Python Console Configuration Library', Color.CYAN)
    printTesting('This is a test of Python Console Configuration Library', Color.LIGHT_CYAN)
    printTesting('This is a test of Python Console Configuration Library', Color.LIGHT_RED)
    print("TEST OF RESET")


    import sys
    for i in range(0, 16):
        for j in range(0, 16):
            code = str(i * 16 + j)
            sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
        print(u"\u001b[0m")
