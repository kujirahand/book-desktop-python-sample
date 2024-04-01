from gui_test import show_window, sg
show_window(layout=[
    [sg.Slider(key="-slider-", 
        range=(0, 100), resolution=1, 
        orientation="horizontal")],
    [sg.Button("終了")] 
])
