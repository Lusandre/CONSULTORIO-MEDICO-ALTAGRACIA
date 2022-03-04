import tkinter as tk 
import os
from client.gui_app import Frame


def main():
	root = tk.Tk()
	root.title('CONSULTORIO MEDICO ALTAGRACIA')
	root.geometry("600x380")
	app = Frame(root = root)

	root.mainloop()

if __name__ == '__main__':
	main()