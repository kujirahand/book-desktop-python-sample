import os
import glob
import subprocess
from PIL import Image, ImageEnhance

FFMPEG_PATH = "ffmpeg"
ZUNDAMON_PATH = "zundamon480.png"
zundamon = Image.open(ZUNDAMON_PATH)

# 静止画を上から下に動かした画像を連続で作成 --- (*1)
def gen_images(image_file, out_dir, count, start_num=0):
    (w, h) = (640, 480) # 動画のサイズ
    # 元画像を読んで画像の幅を合わせてリサイズ --- (*2)
    img = Image.open(image_file)
    img.thumbnail((w * 1.5, w * 1.5))
    iw, ih = img.size
    x = (iw - w) // 2
    zundamon_w, _zundamon_h = zundamon.size
    fade_out = 15
    # Y座標を移動させて画像を連番で保存 --- (*3)
    move_h = (ih - h)
    move_y = move_h / count
    for i in range(count):
        y = i * move_y
        # 新規画像を作成して、部分コピー --- (*4)
        frame_img = Image.new("RGBA", (w, h), (0, 0, 0))
        frame_img.paste(img.crop((x, y, x + w, y + h)), (0, 0))
        # ずんだもんを重ね合わせて前景に描画 --- (*5)
        frame_img.paste(zundamon, (w - zundamon_w, 0), zundamon)
        # フェイドアウトが必要か --- (*6)
        if (count - fade_out) < i:
            fi = i - (count - fade_out)
            fade = ImageEnhance.Brightness(frame_img)
            frame_img = fade.enhance(1.0 + (fi / (fade_out)) * 3.0)
        # 画像を保存 --- (*7)
        num = i + start_num
        save_file = os.path.join(out_dir, f"{num:04d}.png")
        frame_img.save(save_file)
        print(os.path.basename(save_file))

# 出力ディレクトリを作成し空っぽにする --- (*8)
def check_output_dir(output_dir):
    # 出力ディレクトリを作成
    os.makedirs(output_dir, exist_ok=True)
    # 既存ファイルがあれば削除
    for f in glob.glob(os.path.join(output_dir, "*.png")):
        os.remove(f)

# FFmpegを実行して動画を生成する --- (*9)
def generate_video(output_file, input_dir, fps=30):
    cmd = [
        FFMPEG_PATH, "-y", "-r", str(fps),
        "-i", f"{input_dir}/%04d.png",
        "-vcodec", "libx264", "-pix_fmt", "yuv420p",
        "-r", str(fps), output_file]
    subprocess.run(cmd)

if __name__ == "__main__": # 画像から動画作成 --- (*10)
    check_output_dir("./temp")
    # 連続で画像を生成
    gen_images("shop.png", "./temp", 100, 1)
    gen_images("shop.png", "./temp", 100, 101)
    # 画像から動画を作成
    generate_video("test.mp4", "./temp", fps=30)
    print("動画作成完了")
