import src.server, src.client

def main():
    selection = input("Run program as:\n1. Server\n2. Client\n> ")
    if (selection == "1"):
        src.server.main()
    elif (selection == "2"):
        src.client.main()
    else:
        print("Invalid selection.")
        main()

if __name__ == '__main__':
   main()