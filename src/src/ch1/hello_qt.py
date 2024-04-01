import sys
from PySide6 import QtWidgets as qt

def show_window():
    # ウィンドウの初期設定
    app = qt.QApplication(sys.argv)
    win = qt.QWidget()
    win.setGeometry(300, 300, 300, 200)
    win.setWindowTitle('格言を表示するアプリ')
    # ラベルを作成
    l = qt.QLabel("以下のボタンを押してください。", win)
    l.setGeometry(10, 10, 200, 20)
    # ボタンを作成
    b = qt.QPushButton('格言を表示', win)
    b.setGeometry(10, 40, 100, 30)
    b.clicked.connect(show_message)
    win.show()
    app.exec()

def show_message(): # メッセージを表示する
    qt.QMessageBox.information(None,
        '格言','良い言葉によって心が晴れる')

if __name__ == "__main__":
    show_window()
