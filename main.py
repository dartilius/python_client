import tkinter as tk
from PIL import Image, ImageTk


class VisualFrame(tk.Frame):
    """Класс фрейма с визуальным контентом
    картинки и видеоролики"""

    def __init__(self):
        super().__init__()
        self['background'] = 'green'
        self.put_widgets()

    def put_widgets(self):
        """Отображает контент во фрейме"""
        text = tk.Label(self, text="тут будут картинки")
        text.pack()


class InfoFrame(tk.Frame):
    """Класс фрейма информационной панели"""

    def __init__(self):
        super().__init__()
        self['background'] = 'blue'
        self.put_widgets()

    def put_widgets(self):
        """Отображает контент во фрейме"""
        text = tk.Label(self, text="тут будет инфо-панель")
        text.pack()


class TickerFrame(tk.Frame):
    """Класс фрейма бегущей строки"""

    def __init__(self):
        super().__init__()
        self['background'] = 'black'
        self.put_widgets()

    def put_widgets(self):
        """Отображает контент во фрейме"""
        text = tk.Label(self, text="тут будет бегущая строка")
        text.pack()


class App(tk.Tk):
    """Базовый класс главного экрана приложения"""

    def __init__(self):
        super().__init__()
        self.title("RMC_client")
        self['background'] = 'gray82'
        self.attributes('-fullscreen', True)
        self.put_all_frames()

    def put_all_frames(self):
        """Метод для отображения всех фреймов на главном экране"""
        self.visual_frame = VisualFrame().place(x=0,
                                                y=0,
                                                relwidth=0.9182,
                                                relheight=0.9259)
        self.info_frame = InfoFrame().place(x=1763,
                                            y=0,
                                            relwidth=0.08177,
                                            relheight=0.9259)
        self.ticker_frame = TickerFrame().place(x=0,
                                                y=1000,
                                                relwidth=1,
                                                relheight=0.074)


if __name__ == "__main__":
    window = App()
    window.mainloop()
