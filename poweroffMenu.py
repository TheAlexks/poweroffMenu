from rich.console import Console
import os
import typer

app = typer.Typer()
console = Console()

@app.command()
def shutdown():
    try:
        console.print("Shutting down the machine...", style="magenta")
        os.system("systemctl poweroff")
    except:
        console.print("There was an error..", style="bold red")

@app.command()
def reboot():
    try:
        console.print("Rebooting the system..", style="magenta")
        os.system("systemctl reboot")
    except:
        console.print("There was an error..", style="bold red")

@app.command()
def suspend():
    try:
        console.print("Suspending the system..", style="magenta")
        os.system("systemctl suspend")
    except:
        console.print("There was an error..", style="bold red")

@app.command()
def help():
    console.print("[red]1. Shutdown[/]")
    console.print("[blue]2. Reboot[/]")
    print("3. Suspend\n")


if __name__ == "__main__":
    app()
