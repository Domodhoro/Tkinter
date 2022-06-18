import tkinter as tkinter


class App(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
        self.entrythingy = tkinter.Entry()
        self.entrythingy.pack()
        self.contents = tkinter.StringVar()
        self.entrythingy["textvariable"] = self.contents
        self.entrythingy.bind('<Key-Return>', self.print_contents)
        pass

    def print_contents(self, event):
        print("Your message is: ", self.contents.get())
        pass


def close(window, e):
    window.quit()
    pass


def main():
    window = tkinter.Tk()

    window.title("Window")
    window.resizable(False, False)
    window.bind('<Escape>', lambda e: close(window, e))

    myapp = App(window)
    myapp.mainloop()
    pass


if __name__ == "__main__":
    main()