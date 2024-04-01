import os
import subprocess
from pydub import AudioSegment
from voicevox_api import text2audio
from image2video import gen_images, check_output_dir, generate_video
from image2video import FFMPEG_PATH

# テキストと画像から動画を作成する関数 --- (*1)
def text2video(text, image_file, output_file):
    # 作業用の一時フォルダを準備 --- (*2)
    script_dir = os.path.dirname(__file__)
    temp_dir = os.path.join(script_dir, "temp")
    check_output_dir(temp_dir)
    # テキストから音声を生成 -- (*3)
    audio_file = os.path.join(temp_dir, "voice.wav")
    text2audio(text, audio_file)
    # 音声の長さを調べる --- (*4)
    audio = AudioSegment.from_file(audio_file, format="wav")
    # 画像から動画作成 --- (*5)
    fps = 30
    fps_count = int(audio.duration_seconds * fps)
    gen_images(image_file, temp_dir, fps_count, 0)
    temp_video_file = os.path.join(temp_dir, "temp.mp4")
    generate_video(temp_video_file, temp_dir, 30)
    # 動画に音声を追加 --- (*6)
    video_add_audio(temp_video_file, audio_file, output_file)

# FFmpegを実行して動画に音声を追加する関数 --- (*7)
def video_add_audio(video_file, audio_file, output_file):
    cmd = [
        FFMPEG_PATH, "-y",
        "-i", video_file,
        "-i", audio_file,
        "-c:v", "copy", "-c:a", "aac",
        output_file]
    subprocess.run(cmd)

if __name__ == "__main__": # --- (*8)
    text2video(
        "こんにちは、富士山なのだ。大きいのだ。",
        "fuji.jpeg", "test.mp4")
