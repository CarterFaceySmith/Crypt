from re import X


def main():
    testStr = "librarian: test msg"
    print(testStr)
    print(testStr.split())
    print(testStr.split(':', 1))
    print(testStr.strip())
    x, y = testStr.split(':')
    print(x)
    y = y.lstrip()
    print(y)

if __name__ == '__main__':
   main()