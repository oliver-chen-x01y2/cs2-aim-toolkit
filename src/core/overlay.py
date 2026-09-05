import win32gui, win32con, win32api

class Overlay:
    def __init__(self):
        self.hwnd = None
        self.create_window()
    def create_window(self):
        self.hwnd = win32gui.CreateWindowEx(
            win32con.WS_EX_TOPMOST | win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT,
            win32con.WC_DIALOG,
            "Overlay",
            win32con.WS_POPUP,
            0, 0, 1920, 1080,
            None, None, None, None
        )
        win32gui.SetLayeredWindowAttributes(self.hwnd, 0, 0, win32con.LWA_ALPHA)
        win32gui.ShowWindow(self.hwnd, win32con.SW_SHOW)
    def draw_crosshair(self):
        pass  # заглушка