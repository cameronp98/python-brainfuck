from brainfuck import execute

def main():
    try:
        execute(input("bf> "))
    except Exception as e:
        print(f"Error: {e}")
       

if __name__ == "__main__":
    main()

