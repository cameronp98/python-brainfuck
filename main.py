import brainfuck


def main():
    line = input("bf> ")
    print(brainfuck.parse(line))


if __name__ == "__main__":
    main()

