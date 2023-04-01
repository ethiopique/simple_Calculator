import tkinter as tk

class Calculator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Calculator")
        self.pack()

        # create the calculator display
        self.create_display()

        # create the calculator buttons
        self.create_buttons()

    def create_display(self):
        # create the display label
        self.display = tk.Label(self, width=20, height=2, anchor="e", text="0")
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    def create_buttons(self):
        # define button labels and positions
        button_labels = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "C", "+",
            "=",  # add "=" button
        ]
        positions = [
            (1, 0), (1, 1), (1, 2), (1, 3),
            (2, 0), (2, 1), (2, 2), (2, 3),
            (3, 0), (3, 1), (3, 2), (3, 3),
            (4, 0), (4, 1), (4, 2), (4, 3),
            (5, 0), (5, 1), (5, 2), (5, 3),  # position "=" button
        ]

        # create the buttons and add them to the calculator
        for label, position in zip(button_labels, positions):
            # set the background color of the button based on its label
            bg_color = "gray"
            if label in {"C", "=", "+", "-", "*", "/"}:
                bg_color = "orange"

            button = tk.Button(self, text=label, width=5, height=2, bg=bg_color, fg="white")
            button.grid(row=position[0], column=position[1])
            button.bind("<Button-1>", self.button_click)

    def button_click(self, event):
        # handle button clicks
        button = event.widget
        text = button["text"]

        if text == "C":
            self.display["text"] = "0"
        elif text == "=":
            try:
                result = eval(self.display["text"])
                self.display["text"] = str(result)
            except:
                self.display["text"] = "Error"
        else:
            if self.display["text"] == "0":
                self.display["text"] = text
            else:
                self.display["text"] += text

root = tk.Tk()
app = Calculator(master=root)
app.mainloop()
