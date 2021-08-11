import tkinter as Tk
import threading
from gui import GUI


book = ''

def main():
    print("[Starting]: Reader is starting")
    root = Tk.Tk()
    root.title("PDF Reader")
    root.geometry("185x170")
    gui = GUI()
    clear = Tk.Label(root, text=" ")
    clear.grid(row=0, column=0, padx=15, pady=15, columnspan=2)
    selectButton = Tk.Button(root, text="Select a PDF", padx=20, pady=15, command=gui.start)
    selectButton.grid(row=1, column=1)
    endButton = Tk.Button(root, text="Stop", padx=20, pady=15, command=threading.Thread(target=gui.end).start())
    endButton.grid(row=1, column=2)
    clear2 = Tk.Label(root, text=" ")
    clear2.grid(row=2, column=0, padx=15, pady=15, columnspan=2)
    root.mainloop()
    gui.join()
    print("[Finished]: Process Finished")


if __name__ == "__main__":
    main()

