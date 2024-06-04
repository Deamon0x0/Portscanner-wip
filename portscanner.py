##### imports libararies ######
import socket
from colorama import Fore, init


########################## Portscanner Python  #####################



ascii_art = '''
        
███████ ██ ███    ███ ██████  ██      ███████               
██      ██ ████  ████ ██   ██ ██      ██                    
███████ ██ ██ ████ ██ ██████  ██      █████                 
     ██ ██ ██  ██  ██ ██      ██      ██                    
███████ ██ ██      ██ ██      ███████ ███████               
                                                            
                                                            
██████   ██████  ██████  ████████                           
██   ██ ██    ██ ██   ██    ██                              
██████  ██    ██ ██████     ██                              
██      ██    ██ ██   ██    ██                              
██       ██████  ██   ██    ██                              
                                                            
                                                            
███████  ██████  █████  ███    ██ ███    ██ ███████ ██████  
██      ██      ██   ██ ████   ██ ████   ██ ██      ██   ██ 
███████ ██      ███████ ██ ██  ██ ██ ██  ██ █████   ██████  
     ██ ██      ██   ██ ██  ██ ██ ██  ██ ██ ██      ██   ██ 
███████  ██████ ██   ██ ██   ████ ██   ████ ███████ ██   ██ 
                                                            
                                                        
'''

####################################### declear colors #######################

init()

RED = Fore.RED
GREEN = Fore.GREEN
BLUE = Fore.BLUE
RESET = Fore.RESET


print(f"{BLUE} {ascii_art} {RESET} ")

####################################### Setup connections ####################

def Scan(host, port):
    #setup connection with socket
    connection = socket.socket()
    try:
        #connecting to host
        connection.connect((host, port))
    except:
        #connect Failed
        return False
    else:
        #connection Success
        return True


################ receive input ###############

host = input("Enter Host to scan: ")
ports = int(input("Enter numbers of ports to scan: "))

################## loop and scan ports ##########

for port in range(1, ports):
    #### if port is open bool=true
    if Scan(host, port):
        print(f"{GREEN} [+] {host}: port {port} is open {RESET} \r")
    else:
        print(f"{RED} [!] {host}: port {port} is closed/filtered! {RESET} \r")


################################ using argument parser to add argument ########################


