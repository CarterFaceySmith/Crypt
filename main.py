import lib, sys

def main():
    match sys.argv[1]:
        case "server":
            exec('lib/server.py')
        case "client":
            exec('lib/client.py')

if __name__ == '__main__':
   main()