import os
import shutil

def python_to_bash(line):
    line = line.strip()
    if line.startswith('print("') and line.endswith('")'):
        # Remove print(" and ") correctly
        content = line[7:-2]
        return f'echo "{content}"'
    elif line.startswith("print('") and line.endswith("')"):
        # Remove print(' and ')
        content = line[7:-2]
        return f"echo '{content}'"
    
    else:
        if shutil.which(line):
            return line
        else:
            return f"# {line} is not a recognized command"

def main():
    print("Enter Python code (type END on a new line to finish):")
    lines = []
    while True:
        user_input = input()
        if user_input.strip() == "END":
            break
        lines.append(user_input)
    bash_lines = [python_to_bash(line) for line in lines]
    bash_script = "\n".join(bash_lines)
    print("\nGenerated Bash script:\n")
    print(bash_script)
    run = input("\nRun this Bash script? (y/n): ")
    if run.lower() == 'y':
        with open("temp_script.sh", "w") as f:
            f.write(bash_script)
        os.system("bash temp_script.sh")
        os.remove("temp_script.sh")

if __name__ == "__main__":
    main()
