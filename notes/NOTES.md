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
