import os

def main():
    user_input = input(">>> ")
    if user_input.startswith('print("') and user_input.endswith('")') or user_input.startswith("print('") and user_input.endswith("')"):
        os.system(f'echo "{user_input[7:-2]}"')
    else:
        print("Not a command")

main()