import os
import subprocess
from pydub import AudioSegment
from pydub.silence import detect_nonsilent

# FFmpegのパスを指定 --- (*1)
FFMPEG_PATH = 'ffmpeg'
# 無音とみなすパラメータ --- (*2)
min_silence_len = 500 # 無音とみなす最小の長さ（ミリ秒）
silence_thresh = -60  # 無音とみなす音量の閾値（dB）

# 動画を分割して保存する --- (*3)
def split_video(video_path, output_path):
    # 出力フォルダがなければ作成
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    # 動画からWAVを抽出する
    aduio_file = video_path.replace('.mp4', '') + '.wav'
    subprocess.run([
        FFMPEG_PATH, '-y', '-i', video_path, 
        '-vn', aduio_file])
    # 無音部分を検出する --- (*4)
    pos_list = detect_silent(aduio_file)
    # 分割位置に基づいて動画を分割する --- (*5)
    for i, (start, end) in enumerate(pos_list):
        if end == 0: continue
        # 分割した動画を出力ディレクトリに保存 --- (*6)
        print('-', msec_to_time(start), 'to', msec_to_time(end))
        f = os.path.join(output_path, f'video_{i}.mp4')
        cmd = [
            FFMPEG_PATH, '-y', '-i', video_path, 
            '-ss', msec_to_time(start), '-to', msec_to_time(end),
            '-c', 'copy', f]
        subprocess.run(cmd)

# 音声ファイルを走査して無音部分を調べる --- (*7)
def detect_silent(aduio_file):
    # WAVファイルの読み込み --- (*8)
    audio_segment = AudioSegment.from_file(aduio_file)
    # 無音以外の部分を検出 --- (*9)
    nonsilent_parts = detect_nonsilent(
        audio_segment,
        min_silence_len=min_silence_len,
        silence_thresh=silence_thresh)
    # 結果のリストを作成する --- (*10)
    pos_list = []
    pos_end = 0
    for _, p in nonsilent_parts:
        pos_list.append([pos_end, p])
        pos_end = p
    return pos_list

# ミリ秒を hh:mm:ss.ms 形式に変換する
def msec_to_time(milliseconds):
    hours, milliseconds = divmod(milliseconds, 3600000)
    minutes, milliseconds = divmod(milliseconds, 60000)
    seconds = milliseconds / 1000
    return f"{int(hours):02d}:{int(minutes):02d}:{seconds:.03f}"

if __name__ == '__main__':
    # 動画の分割を実行 --- (*11)
    video_path = 'about-python.mp4'
    output_path = './video_split_parts'
    split_video(video_path, output_path)


