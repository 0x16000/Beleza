import subprocess

purple = "\033[35m"
reset = "\033[0m"

def ascii():
    print("""
██████╗ ██╗███╗   ██╗ ██████╗ 
██╔══██╗██║████╗  ██║██╔════╝ 
██████╔╝██║██╔██╗ ██║██║  ███╗
██╔═══╝ ██║██║╚██╗██║██║   ██║
██║     ██║██║ ╚████║╚██████╔╝
╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
    """)

def main():
    ascii()
    target = input(purple + "Target: " + reset)
    print(purple + f"\nPinging {target}...\n" + reset)

    try:
        result = subprocess.run(["ping", "-c", "5", target], capture_output=True, text=True)
        print(purple + result.stdout + reset)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
