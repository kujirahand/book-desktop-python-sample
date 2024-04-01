import base64
from io import BytesIO
from PIL import Image
from openai import OpenAI

# 画像生成を行う関数 --- (*1)
def text_to_image(savefile, prompt, model="dall-e-3", 
        size="1024x1024", quality="standard", style="vivid"):
    # APIを呼び出す --- (*2)
    client = OpenAI()
    response = client.images.generate(
        prompt=prompt, # プロンプト
        model=model, # モデルを指定(dall-e-2/dall-e-3)
        size=size, # 画像サイズ(1024x1024/1024×1792/1792×1024)
        quality=quality, # 画質(standard/hd)
        style=style, # スタイル(natural/vivid)
        response_format="b64_json", # 応答形式(url/b64_json)
        n=1 # 生成する画像の数
    )
    # Base64で得た画像をファイルに保存 --- (*3)
    image_data = base64.b64decode(response.data[0].b64_json)
    image = Image.open(BytesIO(image_data))
    image.save(savefile)
    # 実際に使われたプロンプトを表示 --- (*4)
    print(response.data[0].revised_prompt)

if __name__ == "__main__":
    # プロンプトを指定して画像を生成 --- (*5)
    text_to_image(
        "text_to_image_test.png", 
        "学校の教室にいるウサギとヒロインをアニメ風に描いてください。",
        quality="hd")
