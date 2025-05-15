# 📋 PYSQL version 1.0

A simple and efficient Python application with a graphical interface designed to register and manage clients using a **SQLite** database.

---

## 🚀 Features

- ✅ View all registered clients  
- 🔍 Select and view individual records  
- 📝 Register new clients  
- ✏️ Update existing client data  
- ❌ Delete client records  
- 💾 SQLite database for local storage  
- 🧱 Clean separation of GUI and Backend logic  
- 📦 Executable built with **PyInstaller**

---

## 🧠 Application Structure

```text
📁 project/
│
├── dist/                  # Contains the generated executable (after PyInstaller build)
│   └── app.exe            # Standalone executable (no console window)
│
├── build/                 # Auto-generated build files (can be deleted)
│
├── __pycache__/           # Python cache files
│
├── app.py                 # Entry point for the application
├── gui.py                 # GUI logic (buttons, inputs, layout)
├── backend.py             # Handles all database operations (CRUD)
├── clients.db             # SQLite database file
├── README.md              # This file
└── *.spec                 # PyInstaller spec file
````

---

## ⚙️ How It Works

1. **Import GUI and Backend structure**
2. Declare and load the app variable: `app = None`
3. Define all command functions (`view_command`, `insert_command`, etc.)
4. Define the `getSelectRow` function to retrieve selected entries
5. Instantiate the app: `app = Gui()`
6. Bind message box: `app.listClientes.bind(...)`
7. Configure buttons to trigger functions (`app.btnViewAll.configure(...)`)
8. Launch the app with: `app.run()`

---

## 🛠️ Build Executable (Already Created)

The executable was created using [PyInstaller](https://pyinstaller.org/).
Command used:

```bash
pip install pyinstaller

pyinstaller --onefile --windowed --noconsole app.py
```

✅ The executable can now be found in the `dist/` folder as `app.exe`.

---

## 📌 Notes

* No console window will appear when running the `.exe` (thanks to `--windowed --noconsole`)
* Works completely offline
* Easy to distribute and run on Windows machines without needing Python installed

---

## 📤 License

MIT License © 2025 Rodrigo Yuji Seto Soma