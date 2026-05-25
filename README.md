📚 ComicInfo XML Generator
-
A modern, lightweight Windows application designed to help digital comic book collectors and archivists create ComicInfo.xml files. This tool provides a user-friendly graphical interface to input comic metadata and export it into a standardized XML format.

✨ Features
-
- Modern Interface: Built with CustomTkinter for a sleek, Windows 11-style dark mode appearance.  
- Comprehensive Fields: Includes all standard ComicInfo fields (Title, Series, Writer, Artist, etc.).  
- Pretty-Print XML: Generates neatly indented XML files that are easy to read and compatible with most comic management software.  
- Scrollable Layout: Easily navigate through a large number of metadata fields.

🛠️ Installation & Usage
-
Prerequisites:  
You will need Python 3.x installed on your system.

1. Clone the Repository:
```
git clone https://github.com/YOUR_USERNAME/ComicInfo-Generator.git
```
```
cd ComicInfo-Generator
```
2. Install Dependencies:   
This application uses customtkinter for the modern GUI.  
Install it via pip:
```
pip install customtkinter
```
3. Run the Application
```
python comic_info_gen.py
```

📦 Creating a Windows Executable (.exe)
-
If you want to use this application without running the Python script every time, you can compile it into a standalone .exe file using PyInstaller.

1. Install PyInstaller:
```
pip install pyinstaller
```
2. Build the EXE: Run the following command in your terminal.  
(Optional: If you have an icon file, include the --icon flag):
```
pyinstaller --noconsole --onefile --icon=app_icon.ico comic_app.py
```
3. Locate your App: Once the process finishes, your ready-to-use application will be located in the dist/ folder.

🤖 AI Disclosure
-
This project was developed with the assistance of a Gemini4:31b. The AI was used to architect the GUI layout, implement the XML generation logic, and optimize the user interface for a modern experience. The code was then reviewed and refined for functionality and usability.

📄 License
-
This project is licensed under the MIT License - see the LICENSE [blocked] file for details.
