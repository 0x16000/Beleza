import sys
import subprocess
import os
import platform

purple = "\033[35m"
reset = "\033[0m"

def help():
    print(purple + """
    We trust you have received the usual lecture from the Software's creator.
    It usually boils down to these three things:

        1) Respect the privacy of others.
        2) Think before you type.
        3) With great power comes great responsibility.
        4) Don't share your output of this software to anyone, for your own safety.

    Usage: [-h] [-p <ip>] [-q] [-i] [-d <ip or domain>] [-a]
    -h : -help
    -p : -ping <ip>
    -q : -quiet [suppress output]
    -i : -ipconfig / -ifconfig
    -d : -dig / -nslookup
    -a : -arp [show ARP table]

""" + reset)

def ascii():
    print(r"""
██████╗ ███████╗██╗     ███████╗███████╗ █████╗
██╔══██╗██╔════╝██║     ██╔════╝╚══███╔╝██╔══██╗
██████╔╝█████╗  ██║     █████╗    ███╔╝ ███████║
██╔══██╗██╔══╝  ██║     ██╔══╝   ███╔╝  ██╔══██║
██████╔╝███████╗███████╗███████╗███████╗██║  ██║
╚═════╝ ╚══════╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
""")

def main():
    quiet = "-q" in sys.argv

    if "-h" in sys.argv:
        help()
        sys.exit(0)

    if "-i" in sys.argv:
        if not quiet:
            system = platform.system()
            if system in ("Linux", "Darwin"):
                result = subprocess.run(["ifconfig"], capture_output=True, text=True)
                print(purple + result.stdout + reset)
            elif system == "Windows":
                result = subprocess.run(["ipconfig"], capture_output=True, text=True)
                print(purple + result.stdout + reset)
            else:
                print("Unsupported OS for -i flag.")
        sys.exit(0)

    if "-p" in sys.argv:
        if not quiet:
            print("Opening ping.py...\n")
        subprocess.run(["python3", os.path.join(os.path.dirname(__file__), "ping.py")])
        sys.exit(0)

    if "-d" in sys.argv:
        d_index = sys.argv.index("-d")
        if d_index + 1 < len(sys.argv):
            domain = sys.argv[d_index + 1]
            if not quiet:
                system = platform.system()
                if system in ("Linux", "Darwin"):
                    result = subprocess.run(["dig", domain], capture_output=True, text=True)
                    print(purple + result.stdout + reset)
                elif system == "Windows":
                    result = subprocess.run(["nslookup", domain], capture_output=True, text=True)
                    print(purple + result.stdout + reset)
                else:
                    print("Unsupported OS for -d flag.")
            sys.exit(0)
        else:
            print("Error: -d flag requires a domain or IP address")
            sys.exit(1)

    if "-a" in sys.argv:
        if not quiet:
            system = platform.system()
            if system in ("Linux", "Darwin"):
                result = subprocess.run(["arp", "-a"], capture_output=True, text=True)
                print(purple + result.stdout + reset)
            elif system == "Windows":
                result = subprocess.run(["arp", "-a"], capture_output=True, text=True)
                print(purple + result.stdout + reset)
            else:
                print("Unsupported OS for -a flag.")
        sys.exit(0)

    if not quiet:
        ascii()
        print(purple + """
    @0x16000 Beleza

    We trust you have received the usual lecture from the Software's creator.
    It usually boils down to these three things:

        1) Respect the privacy of others.
        2) Think before you type.
        3) With great power comes great responsibility.
        4) Don't share your output of this software to anyone, for your own safety.

    Usage: [-h] [-p <ip>] [-q] [-i] [-d <ip or domain>] [-a]
    -h : -help
    -p : -ping <ip>
    -q : -quiet [suppress output]
    -i : -ipconfig / -ifconfig
    -d : -dig / -nslookup
    -a : -arp [show ARP table]

""" + reset)

if __name__ == "__main__":
    main()
