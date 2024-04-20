#!/usr/bin/env python
"""
file: file_viewer.py

書籍のサンプルを手軽に実行するランチャーです。
実際には、書籍を読みながら、このプログラムを実行してみてください。
別途モジュールのインストールが必要です。

```
python -m pip install TkEasyGUI PySimpleGUI
```
"""
import os
import subprocess
import sys
from threading import Thread

# import PySimpleGUI as sg
import TkEasyGUI as sg

# set path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
TARGET_DIR = os.path.join(ROOT_DIR, "src-tkeasygui")
# get font
font = ("Arial", 14)

def get_program_files(target_dir=TARGET_DIR):
    # files = os.listdir(ROOT_DIR)
    files = []
    for root, dirs, file_list in os.walk(target_dir):
        for f in file_list:
            full = os.path.join(root, f)
            parts = full[len(ROOT_DIR)+1:]
            files.append(parts)
            print("-", parts)
    files = [f for f in files if f.endswith('.py') or f.endswith('.txt')] # filter
    files = list(sorted(files))
    return files

def run_program(filename):
    file_dir = os.path.dirname(filename)
    subprocess.run([sys.executable, filename], cwd=file_dir)

layout = [
    [sg.Text("Book samples - TkEasyGUI/PySimpleGUI:")],
    [
        # left sizde listbox
        sg.Listbox( 
            values=get_program_files(), 
            size=(30, 20), 
            key="-files-", 
            enable_events=True,
        ),
        sg.VSeparator(pad=5),
        # right side textbox
        sg.Multiline(size=(60, 20), key="-body-", expand_y=True, expand_x=True)
    ],
    [sg.HSeparator(pad=5)],
    [
        sg.Button("Run Program"),
        sg.Button("Close"),
        sg.Combo(["src", "src-tkeasygui"], default_value="src-tkeasygui", key="-filter-", enable_events=True),
    ],
]
window = sg.Window("Book Sample Viewer", layout, font=font)
# event loop
while True:
    event, values = window.read()
    print("#", event, values)
    if event in [sg.WINDOW_CLOSED, "Close"]:
        break
    if event == "Run Program":
        files = values["-files-"]
        if len(files) > 0:
            filename = values["-files-"][0]
            if filename.endswith(".txt"):
                sg.popup("Pythonのプログラムのみ実行できます。")
                continue
            fullpath = os.path.join(ROOT_DIR, filename)
            Thread(target=run_program, args=(fullpath,)).start()
    if event == "-files-":
        files = values["-files-"]
        if len(files) > 0:
            filename = values["-files-"][0]
            fullpath = os.path.join(TARGET_DIR, filename)
            with open(fullpath, "r", encoding="utf-8") as f:
                text = f.read()
                window["-body-"].update(text)
    if event == "-filter-":
        TARGET_DIR = os.path.join(ROOT_DIR, values["-filter-"])
        window["-files-"].update(get_program_files(TARGET_DIR))
window.close()
