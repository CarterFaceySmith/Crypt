# Imports
import socket, threading, sys, enCrypt

# Program settings
bufferSize = 1024

# Initialisation
host = '127.0.0.1'
port = 8888
alias = 'librarian'
# host = input('Input host IP to connect to:\n> ')
# print()
# port = int(input('Input host port to connect to:\n> '))
# print()
# cipher = input('Input host cipher key:\n> ')
# print()

# Connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      
client.connect((host, port))
print("Connected to the server successfully.")

# alias = input('Input your alias:\n> ')
# print()
print('Your alias is set to {}.\n', alias)
print("To exit to program, enter \'exit\' at any point.")


# FUNCTIONS
def receive():
    #TODO: Currently vulnerable to segfaults in threading if the server stops whilst user is active
    while True:                                                 
        try:
            message = client.recv(bufferSize).decode('ascii')
            if message == 'NICKNAME':
                client.send(alias.encode('ascii')) 
                #TODO: Vulnerable to people inputting NICKNAME to get the server to spam everyones nicknames
            else:
                print(message)
        except:                                                 
            print("An error occured.\nExiting the program.")
            client.close()
            break

def write():
    while True:  
        message = '{}: {}'.format(alias, input(''))
        name, content = message.split(':')
        content = content.lstrip()
        if content == 'exit':
            print("Thank you for using Crypt.\nGoodbye.")
            exit()
        else:
            client.send(message.encode('ascii'))

# Multithread to monitor send and receive simultaneously
receive_thread = threading.Thread(target=receive)               
receive_thread.start()
write_thread = threading.Thread(target=write)                   
write_thread.start()