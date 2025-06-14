# 🐍 PytoBash

A lightweight, Python-powered shell interface that mimics basic terminal behavior using `os`, `subprocess`, and native system calls.

---

## 🚀 Features

- `cd <dir>` – Navigate directories
- `ls` / `dir` – List directory contents
- `clear` – Clear the screen (cross-platform)
- `exit` – Exit the shell
- Full system command support (via `os.system`)

---

## 📦 Requirements

- Python 3.7+
- Works on **macOS** and **Linux**

---

## 🧪 Usage

Clone the repository and run:

```bash
python3 main.py
```

---

## 🎯 Example

```bash
PytoBash > ls
main.py
LICENSE
README.md

PytoBash > cd ..
PytoBash > clear
PytoBash > exit
```

---

## 📁 Structure

```text
main.py       # Shell interface
README.md     # This file
LICENSE       # MIT License
```

---

## 📄 License

This project is licensed under the [MIT License](./LICENSE).

---

## 👤 Author

Created by [sudo-hecc](https://github.com/sudo-hecc)

---

> PytoBash is meant to be a learning project, but can evolve into a custom scriptable shell — or even integrate with `tkinter` or `rich` in future versions!
