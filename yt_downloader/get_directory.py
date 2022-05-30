from tkinter import *
from tkinter import filedialog


def get_dir():
    root = Tk()
    root.withdraw()

    selectedFolder = filedialog.askdirectory()

    while selectedFolder == "":
        selectedFolder = filedialog.askdirectory()
    return selectedFolder
