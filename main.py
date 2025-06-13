import os
import shutil
import readline

#====DEFINE CONVERSION METHOD====
def python_to_bash(line):
    line = line.strip()
    if line.startswith('print("') and line.endswith('")'):
        content = line[7:-2]
        return f'echo "{content}"'
    elif line.startswith("print('") and line.endswith("')"):
        content = line[7:-2]
        return f"echo '{content}'"
    elif line == "os.pwd()":
        return "pwd"
    elif line == "os.listdir()":
        return "ls"
    elif line.startswith("os.chdir(") and line.endswith(")"):
        content = line[9:-1]
        return f"cd {content}"
    elif line.startswith("mkdir('") and line.endswith("')"):
        content = line[7:-2]
        return f"mkdir {content}"
    elif line.startswith("os.mkdir(") and line.endswith(")"):
        # Handles os.mkdir("env") and os.mkdir('env')
        content = line[9:-1]
        if (content.startswith('"') and content.endswith('"')) or (content.startswith("'") and content.endswith("'")):
            content = content[1:-1]
        return f"mkdir {content}"
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
    else:
        if shutil.which(line):
            return line
        else:
            return f"# {line} is not a recognized command"

#====DEFINE `main()` FUNCTION====
def main():
    print("Enter Python code (type END on a new line to finish):")
    lines = []
    while True:
        user_input = input(">>> ")
        if user_input.strip() == "END":
            break
        lines.append(user_input)
    bash_lines = [python_to_bash(line) for line in lines]
    bash_script = "\n".join(bash_lines)
    print("\nGenerated Bash script:\n")
    print(bash_script)
    run = input("\nRun this Bash script? (y/n): ")
    if run.lower() == 'y' or run.lower() == '':
        with open("temp_script.sh", "w") as f:
            f.write(bash_script)
        os.system("bash temp_script.sh")
        os.remove("temp_script.sh")

if __name__ == "__main__":
    main()
