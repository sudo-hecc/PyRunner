import os
import shutil
import re
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import readline

console = Console()

#====DEFINE CONVERSION METHOD====
def python_to_bash(line):
    line = line.strip()
    # Variable assignment
    match = re.match(r"(\w+)\s*=\s*(.+)", line)
    if match:
        var, val = match.groups()
        return f'{var}={val}'
    # If statement
    if line.startswith("if ") and line.endswith(":"):
        condition = line[3:-1].strip()
        # Simple equality check
        condition = condition.replace("==", " -eq ")
        return f'if [ {condition} ]; then'
    # Else statement
    if line == "else:":
        return "else"
    # Elif statement
    if line.startswith("elif ") and line.endswith(":"):
        condition = line[5:-1].strip()
        condition = condition.replace("==", " -eq")
        return f'elif [ {condition} ]; then'
    # For loop (range)
    match = re.match(r"for (\w+) in range\((\d+)\):", line)
    if match:
        var, end = match.groups()
        return f'for {var} in {{0..{int(end)-1}}}; do'
    # While loop
    if line.startswith("while ") and line.endswith(":"):
        condition = line[6:-1].strip()
        condition = condition.replace("==", "-eq")
        return f'while [ {condition} ]; do'
    # End block (dedent)
    if line == "":
        return "fi"  # or "done" depending on context
    # Print statement
    if line.startswith('print("') and line.endswith('")'):
        content = line[7:-2]
        return f'echo "{content}"'
    elif line.startswith("print('") and line.endswith("')"):
        content = line[7:-2]
        return f"echo '{content}'"
    # OS commands
    elif line == "os.pwd()":
        return "pwd"
    elif line == "os.listdir()":
        return "ls"
    elif line.startswith("os.chdir(") and line.endswith(")"):
        content = line[9:-1]
        return f"cd {content}"
    elif line.startswith("os.mkdir(") and line.endswith(")"):
        # Handles os.mkdir("env") and os.mkdir('env')
        content = line[9:-1].strip()
        if (content.startswith('"') and content.endswith('"')) or (content.startswith("'") and content.endswith("'")):
            content = content[1:-1]
        return f'mkdir "{content}"'
    elif line.startswith("os.rmdir(") and line.endswith(")"):
        content = line[9:-1]
        if (content.startswith('"') and content.endswith('"')) or (content.startswith("'") and content.endswith("'")):
            content = content[1:-1]
        return f"rmdir {content}"
    elif line.startswith("os.remove(") and line.endswith(")"):
        content = line[10:-1]
        if (content.startswith('"') and content.endswith('"')) or (content.startswith("'") and content.endswith("'")):
            content = content[1:-1]
        return f"rm -rf {content}"
    elif line.startswith('os.rename("') and line.endswith('")') or line.startswith("os.rename('") and line.endswith("')"):
        parts = line[11:-2].split(',')
        old_name = parts[0].strip().strip('"').strip("'")
        new_name = parts[1].strip().strip('"').strip("'")
        return f"mv {old_name} {new_name}"
    elif line.startswith('open("') and line.endswith('")') or line.startswith("open('") and line.endswith("')"):
        content = line[6:-2]
        return f"cat {content}"
    elif line.startswith('input("') and line.endswith('")') or line.startswith("input('") and line.endswith("')"):
        content = line[7:-2]
        return f'echo "{content}" && read user_input && echo $user_input'
    else:
        if shutil.which(line):
            return line
        else:
            return f"# {line} is not a recognized command"

#====DEFINE `main()` FUNCTION====
def main():
    console.print("[bold cyan]Enter Python code (type /END on a new line to finish):[/bold cyan]")
    lines = []
    while True:
        user_input = console.input("[green]>>> [/green]")
        if user_input.strip() == "/END":
            break
        lines.append(user_input)
    bash_lines = [python_to_bash(line) for line in lines]
    if any(l.strip().startswith("if ") and l.strip().endswith(":") for l in lines):
        bash_lines.append("fi")
    bash_script = "\n".join(bash_lines)
    # Use syntax highlighting for bash
    console.print(Panel(Text(bash_script, style="blue"), title="[bold blue]Generated Bash Script[/bold blue]"))
    run = console.input("\n[bold cyan]Run this Bash script? (y/n): [/bold cyan]")
    if run.lower() == 'y' or run.lower() == '':
        with open("temp_script.sh", "w") as f:
            f.write(bash_script)
        os.system("bash temp_script.sh")
        os.remove("temp_script.sh")

if __name__ == "__main__":
    main()
