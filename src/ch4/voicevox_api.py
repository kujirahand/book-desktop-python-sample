import json
import requests

# VOICEVOXのサーバーのURL --- (*1)
API_VOICEBOX = "http://127.0.0.1:50021"

# VOICEVOXでテキストを音声ファイルに変換 --- (*2)
def text2audio(text, audio_file):
    # 音声合成用のクエリ作成 --- (*3)
    speaker = 3 # ずんだもん
    query = requests.post(f"{API_VOICEBOX}/audio_query",
                params={"text": text, "speaker": speaker})
    if query.status_code != 200:
        print("失敗: ", r.status_code, r.text)
        return False
    # 音声合成を実行 --- (*4)
    r = requests.post(
        f'{API_VOICEBOX}/synthesis?speaker={speaker}',
        headers = {"Content-Type": "application/json"},
        data = json.dumps(query.json()))
    if r.status_code != 200:
        print("失敗: ", r.status_code, r.text)
        return False
    # WAVファイルを生成 --- (*5)
    with open(audio_file, 'wb') as f:
        f.write(r.content)
    
if __name__ == "__main__":
    # テキストを音声に変換 --- (*6)
    text = "こんにちは。ずんだもんです。楽しいですね。"
    text2audio(text, "./test.wav")
