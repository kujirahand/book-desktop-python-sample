import PySimpleGUI as sg
# import TkEasyGUI as sg
import video_split

# ウィンドウを表示する関数を定義 --- (*1)
def show_window():
    # 無音分割に関するオプションを指定 --- (*2)
    options = [
        [
            sg.Text('無音最小長(ミリ秒)'), 
            sg.InputText('500', key='min_silence_len'),
        ],
        [
            sg.Text('無音のしきい値(dB)'),
            sg.InputText('-60', key='silence_thresh'),
        ]
    ]
    # ウィンドウ全体のレイアウトを作成 --- (*3)
    layout = [
        [sg.Text('対象となる動画ファイルを選択してください')],
        [
            sg.InputText(key='infile', enable_events=True), 
            sg.FileBrowse()
        ],
        [sg.Text('保存先フォルダを選択してください')],
        [sg.InputText(key='outpath'), sg.FolderBrowse()],
        # オプションを指定 ---  (*4)
        [sg.Frame('無音認識オプション', options)],
        [sg.Button('実行')]
    ]
    win = sg.Window('無音で動画分割ツール', layout)
    # イベントループ --- (*5)
    while True:
        event, values = win.read()
        if event == sg.WIN_CLOSED: # ウィンドウを閉じた時ループを抜ける
            break 
        if event == '実行':
            # 実行ボタンが押された時の処理 --- (*6)
            video_path = values['infile']
            output_path = values['outpath']
            if output_path == '':
                sg.popup('保存先フォルダを選択してください')
                continue
            # オプションを指定して動画分割実行 --- (*7)
            video_split.min_silence_len = int(values['min_silence_len'])
            video_split.silence_thresh = int(values['silence_thresh'])
            video_split.split_video(video_path, output_path)
        if event == 'infile':
            # 入力ファイルから出力フォルダを自動設定 --- (*8)
            video_path = values['infile']
            output_path = video_path.replace('.mp4', '') + '_parts'
            win['outpath'].update(output_path)
    win.close()

if __name__ == '__main__':
    show_window()


