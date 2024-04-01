REM バッチファイルのディレクトリを取得
set SCRIPT_DIR=%~dp0
REM Pythonのプログラムを起動
echo %SCRIPT_DIR
python %SCRIPT_DIR%report_aggregation_gui.py
pause
