import wx

def show_window():
    app = wx.App()
    frame = wx.Frame(None, wx.ID_ANY, '格言を表示するアプリ')
    panel = wx.Panel(frame, wx.ID_ANY)
    # ラベルを作成
    wx.StaticText(panel, wx.ID_ANY,
        "以下のボタンを押してください。", pos=(10, 10))
    # ボタンを作成
    button = wx.Button(panel, wx.ID_ANY, 
        "格言を表示", pos=(10, 40))
    button.Bind(wx.EVT_BUTTON, show_message)
    frame.Show()
    app.MainLoop()

def show_message(e):
    # メッセージを表示する
    wx.MessageBox("良い言葉によって心が晴れる")

if __name__ == "__main__":
    show_window()
