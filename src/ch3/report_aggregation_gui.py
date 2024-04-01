import os
import PySimpleGUI as sg
# import TkEasyGUI as sg
import report_aggregation

while True:
    # 処理対象のディレクトリを選択 --- (*1)
    target_dir = sg.popup_get_folder(
        "処理対象のディレクトリを選択してください",
        title="部署ごとのExcelブックのフォルダを選択",
        default_path=os.path.dirname(__file__), # 初期ディレクトリ
        no_window=False # パスの入力ダイアログを表示する
    )
    # キャンセルが押されたらプログラムを終了 --- (*2)
    if target_dir == "" or target_dir is None:
        quit()
    # 集計した売上報告書の保存ファイル名を自動的に決める --- (*3)
    dir_name = os.path.basename(target_dir)
    save_file = os.path.join(os.path.dirname(target_dir), f"{dir_name}-all.xlsx")
    # パスを表示する --- (*4)
    yesno = sg.popup_yes_no(
        "以下のパスで良いですか？\n" +
        f"処理対象ディレクトリ: {target_dir}\n" +
        f"売上報告書の保存先: {save_file}", title="確認")
    if yesno != "Yes":
        continue
    # 集計処理を実行 --- (*5)
    report_aggregation.make_report(target_dir, save_file)
    break
