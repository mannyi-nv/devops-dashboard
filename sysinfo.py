import os
import socket
import getpass

def show_sysinfo():
        #Docstring:
    """
    Collect info:
        - hostname
        - current_user
        - cwd
    returns via print.       
        
    """
    while True:
        try:
            print(f"\nprinting: hostname, current user, and current working directory")
            # 1. Get Hostname
            hostname = socket.gethostname()
            # 2. Get Current User
            current_user = getpass.getuser()
            # 3. Get Current Working Directory
            cwd = os.getcwd()
  
            print(f"\n- Hostname: {hostname}")
            print(f"- Current User: {current_user}")
            print(f"- Current Working Directory: {cwd}")
            break
          
        except Exception as e:
         print(f"Error! Something went wrong: {e}")
         break
             

     
        

