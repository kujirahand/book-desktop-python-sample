#!/bin/bash

# スクリプトのディレクトリを取得
SCRIPT_DIR=$( cd $( dirname "$0" ) && pwd)
# プログラムを実行
python3 $SCRIPT_DIR/report_aggregation_gui.py



