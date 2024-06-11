import random
import TkEasyGUI as sg

# ライフゲームのセルの状態 --- (*1)
DEAD = False
ALIVE = True
# ゲーム盤の行と列の数
ROWS = 40
COLS = 50
CELL_W = 14 # セルのサイズ

# メイン関数 --- (*2)
def main():
    # ゲーム盤の初期化
    board = [[random.randint(0, 9) > 7
              for _ in range(COLS)] for _ in range(ROWS)]
    # ウィンドウの作成 --- (*3)
    layout = [
        [sg.Canvas(size=(CELL_W*COLS, CELL_W*ROWS), key='-CANVAS-')],
        [sg.Button('Start', size=(10, 1)),
         sg.Button('Stop', size=(10, 1))]
    ]
    # ウィンドウを作成
    window = sg.Window('Life Game', layout, finalize=True)
    canvas = window['-CANVAS-'].tk_canvas
    paused = True
    # Canvas上のクリックイベントハンドラ --- (*4)
    def canvas_click(event):
        x, y = event.x // CELL_W, event.y // CELL_W
        if 0 <= x < COLS and 0 <= y < ROWS:
            board[y][x] = not board[y][x]
            draw_board(canvas, board)
    # マウスボタンを押した時のイベントを登録 --- (*5)
    window["-CANVAS-"].bind("<ButtonPress>", "press")
    draw_board(canvas, board)
    # イベントループ --- (*6)
    while True:
        event, _ = window.read(timeout=200 if not paused else None)
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Start':
            paused = False
        elif event == 'Stop':
            paused = True
        elif event == '-CANVAS-press': # キャンバスがクリックされた --- (*7)
            canvas_click(window["-CANVAS-"].user_bind_event)
        elif not paused or event == sg.TIMEOUT_KEY: # --- (*8)
            board = calculate_next_generation(board)
            draw_board(canvas, board)
            window.refresh()
    window.close()

# ライフゲームのルールに基づいて次の世代の盤面を計算する関数 --- (*9)
def calculate_next_generation(board):
    new_board = [[DEAD for _ in range(COLS)] for _ in range(ROWS)]
    for i in range(ROWS):
        for j in range(COLS):
            neighbors = count_neighbors(board, i, j)
            if board[i][j] == ALIVE:
                if neighbors < 2 or neighbors > 3:
                    new_board[i][j] = DEAD
                else:
                    new_board[i][j] = ALIVE
            else:
                if neighbors == 3:
                    new_board[i][j] = ALIVE
    return new_board
# 指定されたセルの周囲の生存セルの数を数える関数 --- (*10)
def count_neighbors(board, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 0 <= x + i < ROWS and 0 <= y + j < COLS:
                count += 1 if board[x + i][y + j] else 0
    return count

# 描画関数 --- (*11)
def draw_board(canvas, board):
    canvas.delete('all')
    for i in range(ROWS):
        for j in range(COLS):
            x0, y0 = j * CELL_W, i * CELL_W
            x1, y1 = x0 + CELL_W, y0 + CELL_W
            canvas.create_rectangle(x0, y0, x1, y1, fill='white')
            if board[i][j] == ALIVE:
                canvas.create_oval(x0, y0, x1, y1, fill='red')

if __name__ == "__main__":
    main()
