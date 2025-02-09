from src.rot13 import rot13
def main():
    while True:
        print(rot13(input("Text: ")))
if __name__ == "__main__":
    main()
