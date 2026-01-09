import tkinter as tk


class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Dangerous Text Editor")
        self.root.config(padx=100, pady=50)
        self.root.geometry('800x600')

        self.delay = 5000
        self.after_id = None

        self.text = tk.Text(self.root)

        self.text.bind("<Key>", self.clear_text)
        self.text.place(x=0, y=0)

        self.root.mainloop()

    def clear_text(self, event=None):
        if not event:
            self.text.delete("1.0", "end")

        else:
            if self.after_id:
                self.root.after_cancel(self.after_id)
                self.after_id = None

            self.after_id = self.root.after(self.delay, self.clear_text)


app = App()