from gui_test import show_window, sg
def main():
    show_window(layout=[
        [sg.Image(filename="image.png"), # 画像を表示 --- (*1)
         sg.Canvas(key="-canvas-", size=(200,200))], # --- (*2)
        [sg.Button("終了")] 
    ], after_create=draw_canvas)

def draw_canvas(window):
    # キャンバスに図形を描画　--- (*3)
    canvas = window["-canvas-"].tk_canvas
    canvas.create_rectangle((10, 10), (100, 100), fill="red")
    canvas.create_rectangle((30, 30), (50, 50), fill="white")

if __name__ == "__main__": main()
