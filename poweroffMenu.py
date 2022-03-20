from rich.console import Console
import os

console = Console()

def shutdown():
    try:
        console.print("Shutting down the machine...", style="magenta")
        os.system("systemctl poweroff")
    except:
        console.print("There was an error..", style="bold red")

def reboot():
    try:
        console.print("Rebooting the system..", style="magenta")
        os.system("systemctl reboot")
    except:
        console.print("There was an error..", style="bold red")

def suspend():
    try:
        console.print("Suspending the system..", style="magenta")
        os.system("systemctl suspend")
    except:
        console.print("There was an error..", style="bold red")

def menu():
    console.print("[red]1. Shutdown[/]")
    console.print("[blue]2. Reboot[/]")
    print("3. Suspend\n")

    op = int(input("Choose an option: "))

    if op == 1:
        shutdown()
    elif op == 2:
        reboot()
    elif op == 3:
        suspend()
    else:
        console.print("Invalid option.", style="bold red")

menu()
