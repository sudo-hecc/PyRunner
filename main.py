from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import readline
import os
import shutil
import code
import tempfile

console = Console()
buffer = []

def main():
    console.print("[bold blue]Welcome to your Python 🐍 and Bash terminal.[/bold blue]")
    while True:
        prompt = f"{os.getcwd()} $" if not buffer else "..."
        try:
            user_input = console.input(f"[bold green]{prompt} [/bold green]")
            if user_input.strip().upper() == "END":
                exit(0)
                break
            buffer.append(user_input)
            source = "\n".join(buffer)
            try:
                compiled = code.compile_command(source, "<stdin>", "exec")
                if compiled:
                    exec(compiled, globals())
                    buffer.clear()
                else:
                    continue
            except Exception:
                #====CHECK FOR TERMINAL INPUT====
                stripped_input = user_input.strip()
                if not stripped_input:
                    buffer.clear()
                    continue
                parts = stripped_input.split()
                cmd = parts[0] if parts else ""
                try:
                    # Read .zshrc content
                    zshrc_path = os.path.expanduser("~/.zshrc")
                    with open(zshrc_path, "r") as zshrc_file:
                        zshrc_content = zshrc_file.read()
                    # Create a temp shell script
                    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".sh") as temp_script:
                        temp_script.write(zshrc_content)
                        temp_script.write("\n")
                        temp_script.write(stripped_input)
                        temp_script_path = temp_script.name
                    # Run the temp script
                    os.system(f"zsh {temp_script_path}")
                    # Remove the temp script
                    os.remove(temp_script_path)
                except Exception as e:
                    console.print(Panel(f"[bold red]Error: {e}[/bold red]", title="Error"))
                buffer.clear()
        except KeyboardInterrupt:
            exit(0)
        except Exception as e:
            console.print(Panel(f"[bold red]Error: {e}[/bold red]", title="Error"))
            exit(1)

if __name__ == "__main__":
    main()