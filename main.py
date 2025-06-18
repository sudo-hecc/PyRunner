from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import readline
import os
import shutil
import code

console = Console()

def main():
    #====INPUT====
    console.print("[bold blue]Welcome to your Python 🐍 and Bash terminal. Type `END` to finish[/bold blue]")
    #====LOAD `.zshrc`====
    zshrc_path = os.path.expanduser("~/.zshrc")
    if os.path.exists(zshrc_path):
        with open(zshrc_path, 'r') as file:
            zshrc_content = file.read()
            for cmd in zshrc_content.splitlines():
                cmds = cmd.strip()
    else:
        zshrc_content = "# .zshrc file not found\n"
    os.system(zshrc_content)
    while True:
        #====INPUT====
        try:
            user_input = console.input("[bold green]>>> [/bold green]")
            if user_input.strip().upper() == "END":
                exit(0)
                break
            if user_input.strip() == "":
                continue
            #====CHECK FOR PYTHON CODE====
            try:
                exec(user_input)
            except:
                #====CHECK FOR TERMINAL INPUT====
                if shutil.which(user_input.split()[0]) is not None or user_input in cmds:
                    try:
                        os.system(user_input)
                    except Exception as e:
                        console.print(Panel(f"[bold red]Error: {e}[/bold red]", title="Error"))
                else:
                    try:
                        os.system(user_input)
                    except Exception as e:
                        console.print(Panel(f"[bold red]Error: {e}[/bold red]", title="Error"))
        except KeyboardInterrupt:
            exit(0)
            break

main()
