from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import readline
import os
import shutil

console = Console()

def main():
    console.print("[bold blue]Welcome to your Python 🐍 terminal. Type `END` to finish[/bold blue]")
    code = []
    bash = []
    while True:
        user_input = console.input("[green]>>> [/green]")
        if user_input.lower().strip() == "exit()":
            break
        cmd = user_input.strip().split()[0] if user_input.strip() else ""
        if cmd and shutil.which(cmd) is not None:
            bash.append(user_input)
            continue
        code.append(user_input if not "END" in user_input else user_input.replace("END", "").strip())
        lines = ("\n".join(code))
        if user_input == "END":
            try:
                console.print(Panel(Text(lines, style="blue"), title="[bold blue]Code to run[/bold blue]"))
                run = console.input("[bold yellow]Run code? This will affect you system! (Y/n) [/bold yellow]").strip().lower()
                if run.lower() in ["y", ""]:
                    try:
                        with open("temp_script.bash", "w") as bash_file:
                            for cmd in bash:
                                bash_file.write(f"{cmd}\n")
                        os.system("bash temp_script.bash")
                        os.remove("temp_script.bash")
                        exec(lines, globals())
                        exit()
                    except Exception as e:
                        console.print(Panel(Text(str(e), style="bold red")), justify="center")
                        exit()
                else:
                    exit()
            except Exception as e:
                console.print(Panel(Text(str(e), style="bold red")), justify="center")

main()