from tkinter import *


class test(Tk):
    def __init__(self, width, height):
        super().__init__()
        # Initial Variable Declaration and Assignment

        self.width = width
        self.height = height
        self.wm_geometry(f'{self.width}x{self.height}')
        self.title('Test App')
        self.equation = StringVar()

        # Widgets Creation and Placement
        self.calculation = Label(self, text=self.equation)
        self.calculation.grid(columnspan=4)

        self.equation.set("kfldgi;jrdof;l")


if __name__ == '__main__':
    mainwin = test(250, 120)

    mainwin.mainloop()
