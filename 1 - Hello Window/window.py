import tkinter


def centralize(window, width, height):
	x = int((window.winfo_screenwidth() - width) / 2)
	y = int((window.winfo_screenheight() - height) / 2)

	window.geometry("{}x{}+{}+{}".format(width, height, x, y))
	pass


def close(window, e):
	window.quit()
	pass


def main():
	window = tkinter.Tk()
	
	window.title("Window")

	width = 500
	height = 300

	window.resizable(False, False)

	centralize(window, width, height)

	window.bind('<Escape>', lambda e: close(window, e))

	window.mainloop()
	pass


if __name__ == "__main__":
	main()

