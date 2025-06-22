# 🐍 PyRunner

A lightweight, Python-powered shell-like interface for entering and executing Python code interactively, powered by [rich](https://github.com/Textualize/rich).

---

## 🚀 Features

- Interactive prompt for entering multi-line Python code
- Executes Python code interactively (multi-line supported)
- If input is not valid Python, attempts to run it as a shell command
- Shell commands are executed in a zsh environment with your `.zshrc` sourced (aliases and functions work)
- Syntax-highlighted output and prompts via rich
- Handles keyboard interrupts gracefully

---

## 📦 Requirements

- Python 3.7+
- rich library

---

## 🧪 Usage

Clone the repository and run:
```
python3 main.py
```
---

## 🎯 Example
```
Welcome to your Python 🐍 and Bash terminal.
/Users/<yourname> $ print("Hello, world!")
Hello, world!
/Users/<yourname> $ pip --version
pip 23.2.1 from /usr/local/lib/python3.11/site-packages/pip (python 3.11)
/Users/<yourname> $ echo $HOME
/Users/<yourname>
/Users/<yourname> $ exit() # Can also be `END` or `quit()`
```

---

## 📁 Structure
- main.py          --> Shell interface
- README.md        --> This file
- LICENSE          --> MIT License
- SECURITY.md      --> Security policy
- requirements.txt --> Requirements list

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

Created by sudo-hecc

---

> PyRunner is a learning project and may evolve into a more advanced shell or scripting environment in the future!
