import os
from pydub import AudioSegment
from pydub.silence import detect_nonsilent

# MP3ファイルの無音部分で分割する関数 --- (*1)
def segment_audio_by_silence(audio_file, save_dir):
    # 音声ファイルの読み込み -- (*2)
    audio_segment = AudioSegment.from_file(audio_file)
    # 無音部分の検出 --- (*3)
    min_silence_len = 500  # 無音とみなす最小の長さ（ミリ秒）
    silence_thresh = -60  # 無音とみなす音量の閾値（dB）
    nonsilent_parts = detect_nonsilent(
        audio_segment,
        min_silence_len=min_silence_len,
        silence_thresh=silence_thresh)
    # 検出結果の表示 --- (*4)
    for p1, p2 in nonsilent_parts:
        print(f'[parts] {msec_to_time(p1)} - {msec_to_time(p2)}')
    # 音声ファイルを分割して保存 --- (*5)
    if not os.path.exists(save_dir): os.mkdir(save_dir)
    last_pos = 0 # 前回の終了位置
    for i, (p1, p2) in enumerate(nonsilent_parts):
        # 部分データを音声ファイルに保存 --- (*6)
        part = audio_segment[last_pos: p2]
        part.export(f'{save_dir}/part_{i:02}.mp3', format="mp3")
        last_pos = p2

# ミリ秒を hh:mm:ss.ms 形式に変換する関数を定義 --- (*7)
def msec_to_time(milliseconds):
    hours, milliseconds = divmod(milliseconds, 3600000)
    minutes, milliseconds = divmod(milliseconds, 60000)
    seconds = milliseconds / 1000
    return f"{int(hours):02d}:{int(minutes):02d}:{seconds:.03f}"

if __name__ == "__main__": # --- (*8)
    mp3_file = "about-python.mp3" # MP3ファイルのパス
    save_dir = "about-python_parts" # 分割したオーディオのパス
    segment_audio_by_silence(mp3_file, save_dir)

