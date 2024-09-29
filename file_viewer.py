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
import platform
from threading import Thread

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
            parts = full[len(ROOT_DIR) + 1 :]
            files.append(parts)
            print("-", parts)
    files = [f for f in files if f.endswith(".py") or f.endswith(".txt")]  # filter
    files = list(sorted(files))
    return files


def run_program(filename):
    file_dir = os.path.dirname(filename)
    subprocess.run([sys.executable, filename], cwd=file_dir)


def get_selected_file(values):
    files = values["-files-"]
    if len(files) > 0:
        filename = values["-files-"][0]
        fullpath = os.path.join(ROOT_DIR, filename)
        return fullpath
    else:
        return ""


def is_gui_program(fullpath):
    try:
        with open(fullpath, "r", encoding="utf-8") as f:
            text = f.read()
            if "import TkEasyGUI" in text or "import PySimpleGUI" in text:
                return True
    except Exception as e:
        text = str(e)
    return False


# レイアウトを指定
layout = [
    [
        sg.Text("Book samples - TkEasyGUI/PySimpleGUI:"),
        sg.Text(f"(TkEasyGUI v.{sg.__version__})"),
    ],
    [
        # left side listbox
        sg.Listbox(
            values=get_program_files(),
            size=(30, 20),
            key="-files-",
            enable_events=True,
        ),
        sg.VSeparator(pad=5),
        # right side textbox
        sg.Column(
            layout=[
                [
                    sg.Multiline(
                        default_text="画面左側のリストからファイルを選んでください。",
                        size=(60, 20),
                        key="-body-",
                        expand_y=True,
                        expand_x=True,
                    )
                ],
                [sg.Text("-", key="-memo-", expand_x=True)],
            ],
            expand_y=True,
            expand_x=True,
        ),
    ],
    [sg.HSeparator(pad=5)],
    [
        sg.Button("Run Program"),
        sg.Button("閉じる"),
        sg.Button("フォルダを開く"),
        sg.Combo(
            ["src", "src-tkeasygui"],
            default_value="src-tkeasygui",
            key="-filter-",
            enable_events=True,
        ),
        sg.Button("Amazonで書籍を見る", key="-amazon-"),
    ],
]


def show_window():
    window = sg.Window("Book Sample Viewer", layout, font=font)
    # event loop
    while True:
        event, values = window.read()
        print("#", event, values)
        if event in [sg.WINDOW_CLOSED, "閉じる"]:
            break
        if event == "-amazon-":
            url = "https://amzn.to/45R2NSH"
            pf = platform.system()
            print("platform:", pf)
            if pf == "Darwin":
                subprocess.run(["open", url])
            elif pf == "Windows":
                subprocess.run(["start", url], shell=True)
            else:
                sg.popup(f"[URL] {url}")
        if event == "Run Program":
            fullpath = get_selected_file(values)
            if fullpath == "":
                continue
            if fullpath.endswith(".txt"):
                sg.popup("Pythonのプログラムのみ実行できます。")
                continue
            Thread(target=run_program, args=(fullpath,)).start()
        if event == "フォルダを開く":
            fullpath = get_selected_file(values)
            if fullpath == "":
                continue
            fdir = os.path.dirname(fullpath)
            if sg.is_mac():
                subprocess.run(["open", fdir])
            elif sg.is_win():
                subprocess.run(["explorer", fdir])
            else:
                sg.popup("フォルダを開くに未対応のOSです")
        if event == "-files-":
            fullpath = get_selected_file(values)
            if fullpath == "":
                continue
            try:
                # ファイルの内容を開く
                with open(fullpath, "r", encoding="utf-8") as f:
                    text = f.read()
                    window["-body-"].update(text)
                if fullpath.endswith(".py"):
                    window["-memo-"].update(f"Run Programで実行できます。")
                    if "import TkEasyGUI" in text or "import PySimpleGUI" in text:
                        window["-memo-"].update(
                            f"TkEasyGUI/PySimpleGUIを使っています。"
                        )
                    else:
                        window["-memo-"].update(
                            f"IDLEかターミナルで実行して結果を確認してください。"
                        )
                else:
                    window["-memo-"].update(f"テキストファイルです。")
            except Exception as e:
                window["-body-"].update(f"Error: {e}")
        if event == "-filter-":
            TARGET_DIR = os.path.join(ROOT_DIR, values["-filter-"])
            window["-files-"].update(get_program_files(TARGET_DIR))
    window.close()


if __name__ == "__main__":
    show_window()