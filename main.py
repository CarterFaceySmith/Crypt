import src, sys

def main():
    args = sys.argv
    if len(args) > 1:
        if args[1] == "server":
                exec(open("./src/server.py").read())
        elif args[1] == "client":
                exec(open("./src/client.py").read())
    else:
        print("No program flag specified, exiting.")
        exit()

if __name__ == '__main__':
   main()