import base64
def main():
    a = input("""
1. Decoder
2. Encoder
          
Please Select one (1, 2):""")
    if a == "2" or a.lower() == "encoder":
        data = input("Enter anything here: ")
        b = base64.b64encode(data.encode()).decode()
        print(b)
    elif a == "1" or a.lower() == "decoder":
        data = str(input("Enter base64 encoded string here: "))
        b = base64.b64decode(data.encode()).decode()
        print(b)
    else:
        print("Invalid option!")
        main()
    playagain()
def playagain():
    adaw = input("Would you like to run again? (y/n): ")
    if adaw.lower() == "y":
        main()
    elif adaw.lower() == "n":
        print("Goodbye!")
        exit()
    else:
        exit()
main()
