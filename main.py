from datetime import datetime
import tkinter.font as tkFont
import tkinter as tk


class Clock(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_label()
        self.update_time()
        self.pack()

    def create_label(self):
        font_style = tkFont.Font(family="Consolas", size=60)
        self.datetime_text = tk.StringVar()
        datetime_label = tk.Label(self, textvariable=self.datetime_text, font=font_style, foreground="#3AED3A", background="black")
        datetime_label.pack(side="top")

    def update_time(self):
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        date = now.strftime("%d-%m-%Y")
        text = f"{time}\n{date}"

        self.datetime_text.set(text)

        self.after(1000, self.update_time)


if __name__ == "__main__":
    root = tk.Tk()
    app = Clock(master=root)
    app.mainloop()
    