import pygame
# 音声を再生する準備を行う --- (*1)
pygame.mixer.init()
# 音声ファイルを読み込む --- (*2)
pygame.mixer.music.load("beep.mp3")
# 音声を再生する --- (*3)
pygame.mixer.music.play()
print("再生開始")
# 再生が完了するのを待つ --- (*4)
while pygame.mixer.music.get_busy():
    pygame.time.wait(100)
print("再生終了")
