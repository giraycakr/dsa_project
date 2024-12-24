
import tkinter as tk
from gui import CargoSystemGUI

def main():
    root = tk.Tk()
    root.geometry("600x400")
    app = CargoSystemGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()