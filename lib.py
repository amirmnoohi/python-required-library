import os
import socket
import sys
import time
from multiprocessing import Process

steps = []

HEADER = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
ORANGE = '\033[93m'
RED = '\033[91m'
END = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def check_sudo():
    if os.geteuid() != 0:
        print(RED + "[-] Script is not started as root." + END)


def check_internet(output=False):
    try:
        host = socket.gethostbyname("1.1.1.1")
        s = socket.create_connection((host, 80), 2)
        s.close()
        if output:
            add_steps("[+] Connected To Internet Successfully.")
        return True
    except:
        print(RED + "[-] Failed To Connect To Internet. Please Check your Internet Connectivity." + END)
        return False


def print_steps():
    os.system("clear")
    for step in steps:
        print(GREEN + step + END)


def add_steps(string):
    if len(steps) > 0:
        clean()
    steps.append(string)
    print(GREEN + string + END)
    return string


def wait(length=0.1104):
    try:
        time.sleep(length)
    except KeyboardInterrupt:
        pass


def loading(text, speed):
    try:
        while True:
            print (BLUE + "\r" + "[-] " + text + END)
            sys.stdout.write("\033[F")
            wait(speed)
            print(BLUE + "\r" + "[\\] " + text + END)
            sys.stdout.write("\033[F")
            wait(speed)
            print(BLUE + "\r" + "[|] " + text + END)
            sys.stdout.write("\033[F")
            wait(speed)
            print(BLUE + "\r" + "[/] " + text + END)
            sys.stdout.write("\033[F")
            wait(speed)

    except KeyboardInterrupt:
        exit(0)


def p_start(text, speed):
    p = Process(target=loading, args=(text, speed,))
    p.start()
    return p


def p_stop(p, timeout=3):
    wait(timeout)
    sys.stdout.write("\r")
    p.terminate()


def clean():
    sys.stdout.write("\033[F")
