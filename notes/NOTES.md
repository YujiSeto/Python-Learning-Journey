# 📝 Notes & Observations

Welcome!  
This document contains various notes, observations, and quick references collected during my learning journey.

The goal is to keep useful information in one place — whether it’s a quick reminder, a deeper insight, or something interesting I came across 💡

## ⚙️ VS Code Settings for Python + Terminal Style

This is a custom configuration for Visual Studio Code to improve the experience when running Python code.  
It enables terminal execution, clears the screen before running, and applies a PyCharm-like appearance to the terminal and editor.

```json
{
    "code-runner.runInTerminal": true,
    "code-runner.executorMap": {
        "python": "powershell -Command \"Clear-Host; python -u\""
    },
    "terminal.integrated.defaultEncoding": "utf8",

    // Aparência do terminal
    "terminal.integrated.fontFamily": "monospace",
    "terminal.integrated.fontSize": 14,
    "terminal.integrated.lineHeight": 1.4,
    "terminal.integrated.cursorStyle": "block",
    "terminal.integrated.cursorBlinking": true,

    // Aparência geral do editor
    "editor.fontFamily": "'JetBrains Mono', Consolas, 'Courier New', monospace",
    "editor.fontLigatures": true,
    "git.autofetch": true,
    "json.schemas": [],

    "workbench.colorCustomizations": {
        "terminal.ansiBrightGreen": "#AAAA00",
        "terminal.foreground": "#00AA00",
        "terminalCursor.foreground": "#00AA00",
        "terminal.background": "#000000"
    }
}

```

## 📊 Format Specifiers Table (with Examples)

| Mask        | Data Type         | Description                                            | Example                      |
|-------------|-------------------|--------------------------------------------------------|------------------------------|
| `%d` / `%i` | Int (integer)     | Displays an integer value.                            | `print("%d" % 10)` → `10`    |
| `%f`        | Float or double   | Displays a decimal (floating-point) number.           | `print("%.2f" % 3.14159)` → `3.14` |
| `%ld`       | Long Int          | Displays a long integer.                              | `print("%ld" % 1234567890)` → `1234567890` |
| `%e` / `%E` | Float or double   | Displays a number in exponential format.              | `print("%e" % 1500)` → `1.500000e+03` |
| `%c`        | Char (character)  | Displays a single character.                          | `print("%c" % 65)` → `A`     |
| `%o`        | Int               | Displays an integer in octal format.                  | `print("%o" % 10)` → `12`    |
| `%x` / `%X` | Int               | Displays an integer in hexadecimal format.            | `print("%x" % 255)` → `ff`   |
| `%s`        | Char              | Displays a string of characters.                      | `print("%s" % "Hello")` → `Hello` |
| `%r`        | Boolean           | Displays `true` or `false` (boolean values).          | `print("%r" % True)` → `True` |

## 🔠 Escape Sequences in Python

| Sequence | Description                                                                 |
|----------|-----------------------------------------------------------------------------|
| `\n`     | Inserts a **new line**.                                                     |
| `\t`     | Inserts a **horizontal tab**.                                               |
| `\v`     | Inserts a **vertical tab**.                                                 |
| `\r`     | **Carriage return** — moves the cursor to the beginning of the line.        |
| `\'`     | Inserts a **single quote**.                                                 |
| `\"`     | Inserts a **double quote**.                                                 |
| `\\`     | Inserts a **backslash** (`\`).                                              |
| `\a`     | **System bell (beep)** — triggers a sound if supported.                     |
| `\b`     | **Backspace** — deletes the previous character.                             |
| `\f`     | **Form feed** — inserts a page break (mostly symbolic).                     |
| `\u`     | Inserts a **Unicode character** (requires 4-digit hex code, e.g., `\u2764`).|

## 🧪 Escape Sequences Examples in Python

Here are practical examples of how each escape sequence behaves:

```python
# New line
print("Hello\nWorld")      # Output:
                           # Hello
                           # World

# Horizontal tab
print("Name:\tYuji")       # Output: Name:    Yuji

# Vertical tab
print("Line1\vLine2")      # Output: Line1
                           #         Line2  (may render oddly depending on the terminal)

# Carriage return
print("Hello\rWorld")      # Output: World (overwrites "Hello" with "World")

# Single quote
print('It\'s fine.')       # Output: It's fine.

# Double quote
print("She said \"Hi\".")  # Output: She said "Hi".

# Backslash
print("C:\\Users\\Yuji")   # Output: C:\Users\Yuji

# System bell
print("\a")                # Output: Triggers a system beep (if supported)

# Backspace
print("Helloo\b!")         # Output: Hello! (removes extra 'o')

# Form feed
print("Page 1\fPage 2")    # Output: Page 1
                           #         Page 2  (acts like a soft page break)

# Unicode character
print("\u2764")            # Output: ❤
```

## ➕ Arithmetic Operators in Python (with Examples)

| Operation             | Symbol | Example             | Result     |
|-----------------------|--------|---------------------|------------|
| Addition              | `+`    | `3 + 2`             | `5`        |
| Subtraction           | `-`    | `5 - 1`             | `4`        |
| Multiplication        | `*`    | `4 * 2`             | `8`        |
| Real Division         | `/`    | `10 / 3`            | `3.3333...`|
| Integer Division      | `//`   | `10 // 3`           | `3`        |
| Exponentiation        | `**`   | `2 ** 3`            | `8`        |
| Modulus (Remainder)   | `%`    | `10 % 3`            | `1`        |

## 🧮 Comparison Operators in Python

| Description             | Symbol | Example        | Result     |
|-------------------------|--------|----------------|------------|
| Equal to                | `==`   | `5 == 5`       | `True`     |
| Not equal to            | `!=`   | `5 != 3`       | `True`     |
| Greater than            | `>`    | `7 > 2`        | `True`     |
| Less than               | `<`    | `3 < 1`        | `False`    |
| Greater than or equal to| `>=`   | `6 >= 6`       | `True`     |
| Less than or equal to   | `<=`   | `4 <= 5`       | `True`     |

## 🔗 Logical Operators in Python

| Algorithm Keyword | Python Keyword | Example              | Result     |
|-------------------|----------------|----------------------|------------|
| AND               | `and`          | `True and False`     | `False`    |
| OR                | `or`           | `True or False`      | `True`     |
| NOT               | `not`          | `not True`           | `False`    |

## ⚠️ Important

Python requires standardized **indentation** to define code blocks.

In other programming languages, indentation is just a good practice — but in Python, it's **mandatory**.  
That's because Python doesn't use symbols like `{}` or keywords like `begin/end` to define blocks of code.

## 📁 File Opening Modes in Python

| Mode | Description                                                                 |
|------|-----------------------------------------------------------------------------|
| `r`  | Opens the file **for reading only**. The file **must already exist**.       |
| `r+` | Opens the file for **reading and writing**. The file **must already exist**. Writing starts at the beginning and **overwrites** existing content. |
| `w`  | Opens the file **for writing only**. Existing content is **deleted**. Creates a new file if it doesn't exist. |
| `w+` | Opens the file for **reading and writing**. **Deletes existing content**.   |
| `a`  | Opens the file **for appending** at the end. **Preserves existing content**.|
| `a+` | Opens the file for **reading and appending**. Content is added to the end.  |


# 🖥️ Setting Up a Kivy GUI Project with VSCode in Python

This guide walks you through creating a basic graphical interface using **Kivy** in Python, with proper environment setup and code structure.

---

## 📁 1. Create and Open the Project Folder

- Create a folder for your project, e.g., `meu_kivy_app`.
- Open **VS Code** and go to `File > Open Folder…` and select your project folder.

---


## 🐍 2. Set Up a Python Virtual Environment

Open the integrated terminal in VS Code:
- Shortcut: <kbd>Ctrl</kbd> + <kbd>`</kbd> or go to `Terminal > New Terminal`

Create a virtual environment in the project folder:

```bash
python -m venv .venv
````

### ✅ Activate the Virtual Environment

#### Windows (PowerShell)

First, set PowerShell execution policy for your user:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

#### Windows (cmd.exe)

```bat
.\.venv\Scripts\activate.bat
```

#### macOS / Linux

```bash
source .venv/bin/activate
```

Your terminal prompt should change to something like: `(.venv) C:\...`

---

## 📦 3. Install Kivy

Upgrade pip and install Kivy:

```bash
python -m pip install --upgrade pip
python -m pip install kivy
```

### Optional: Add KivyMD

Create a `requirements.txt`:

```txt
kivy
kivymd
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 🧾 4. Create the Main File

Create a file named `main.py` with the following content:

```python
from kivy.app import App
from kivy.uix.label import Label

class MainApp(App):
    def build(self):
        return Label(text='Hello World!')

if __name__ == '__main__':
    MainApp().run()
```

> 📝 Optionally, create a `main.kv` file to define the UI using KV language.

---

With these steps, your Kivy app is ready to run inside a virtual environment using **VS Code**. 🚀

> 🧠 **Did you know?**  
The **KV language** also supports importing Python modules, creating **dynamic classes**, and much more.  
For full details, refer to the official Kivy documentation:  
🔗 [https://kivy.org/doc/stable/](https://kivy.org/doc/stable/)


## ✅ How to Create, Activate, and Deactivate a Virtual Environment with `venv`

Setting up a virtual environment is a great way to manage dependencies for your Python project 🐍. Here's how you can do it using PowerShell:

### 🛠 Create and Activate

```powershell
# 1. Create the virtual environment
python -m venv venv

# 2. Activate the virtual environment
.\venv\Scripts\Activate
````

Once activated, your terminal prompt will change to show the virtual environment name (e.g., `(venv)`).

### 🔚 Deactivate

To deactivate the virtual environment and return to your system's global Python environment, simply run:

```powershell
deactivate
```

✨ *This keeps your Python workspace clean and avoids conflicts between packages from different projects.*

# 🔁 Managing Different Django Versions (Windows - PowerShell)

You can manage different versions of Django for clients using isolated virtual environments.

---

### 🧱 Client 1 – Django 2.2.26

1. **Create the folder for client 1 and navigate to it**:
   ```powershell
   mkdir client-1
   cd client-1
   ```

2. **Create the virtual environment with the prompt "client-1"**:

   ```powershell
   python -m venv venv --prompt="client-1"
   ```

3. **Activate the virtual environment**:

   ```powershell
   .\venv\Scripts\Activate
   ```

4. **Install Django version 2.2.26**:

   ```powershell
   python -m pip install django==2.2.26
   ```

5. **List installed packages**:

   ```powershell
   python -m pip list
   ```

   Example output:

   ```text
   Package Version
   ---------- -------
   Django 2.2.26
   pip 22.0.4
   pytz 2022.1
   setuptools 58.1.0
   sqlparse 0.4.2
   ```

6. **Deactivate the virtual environment**:

   ```powershell
   deactivate
   ```

---

### 🧱 Client 2 – Django 4.0.3

1. **Go back and repeat the process for client 2**:

   ```powershell
   cd ..
   mkdir client-2
   cd client-2
   ```

2. **Create the virtual environment with the prompt "client-2"**:

   ```powershell
   python -m venv venv --prompt="client-2"
   ```

3. **Activate the virtual environment**:

   ```powershell
   .\venv\Scripts\Activate
   ```

4. **Install Django version 4.0.3**:

   ```powershell
   python -m pip install django==4.0.3
   ```

5. **List installed packages**:

   ```powershell
   python -m pip list
   ```

   Example output:

   ```text
   Package Version
   ---------- -------
   asgiref 3.5.0
   Django 4.0.3
   pip 22.0.4
   setuptools 58.1.0
   sqlparse 0.4.2
   ```

6. **Deactivate the virtual environment**:

   ```powershell
   deactivate
   ```

---

### ✅ Notes:

* Each virtual environment is **isolated**, containing only the specific Django version and dependencies for that client.
* You can **switch** between projects by activating the corresponding virtual environment.
* Using `--prompt` helps **identify** which environment is active, making it easier to manage multiple projects.

Now you have a well-organized process to install and manage different Django versions in virtual environments on Windows using PowerShell.