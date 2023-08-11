from datetime import datetime
import tkinter as tk

class TonyApp:
    def __init__(self, root, feed_data, welcome_msg):
        self.root = root
        self.root.title("TONY")

        self.feed_data = feed_data

        self.welcome_msg = welcome_msg

        # hidden data keeps record of all entries, can't be reset or undone
        self.feed_data_hidden = feed_data.copy()

        self.canvas = tk.Canvas(root)
        self.canvas.pack(side="top", fill="both", expand=True)

        self.y_scrollbar = tk.Scrollbar(root, command=self.canvas.yview)
        self.y_scrollbar.pack(side="right", fill="y")
        self.canvas.config(yscrollcommand=self.y_scrollbar.set)

        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.display_welcome()
        self.display_fed_feed()
        self.create_buttons()

    def display_welcome(self):
        text_label = tk.Label(self.frame, text=self.welcome_msg, justify="left", anchor="s", font=("Comic Sans MS", 14))
        text_label.pack()

    def display_fed_feed(self):
        text = "\n".join(self.feed_data)
        text_label = tk.Label(self.frame, text=text, justify="left", anchor="s", font=("Comic Sans MS", 14))
        text_label.pack()

    def create_buttons(self):
        button_frame_1 = tk.Frame(self.root)
        button_frame_1.pack(side="top")

        button_frame_2 = tk.Frame(self.root)
        button_frame_2.pack(side="bottom")

        fed_button = tk.Button(button_frame_1, text="CAT WAS FED", command=self.fed)
        fed_button.pack(side="top")

        undo_button = tk.Button(button_frame_2, text="Undo", command=self.undo)
        undo_button.pack(side="left")

        reset_button = tk.Button(button_frame_2, text="Reset", command=self.reset)
        reset_button.pack(side="left")

    def fed(self):
        curr_timestamp = datetime.now().strftime('%Y-%m-%d %a %H:%M')
        self.feed_data.append(f'I WAS FED AT: {curr_timestamp}')
        self.feed_data_hidden.append(curr_timestamp)
        self.update_display()

    def undo(self):
        if self.feed_data:
            self.feed_data.pop()
            self.feed_data.append('<removed>')
            self.feed_data_hidden.append('<previous entry was removed>')
            self.update_display()

    def reset(self):
        self.feed_data = ['Feeding data cleared...']
        self.update_display()

    def update_display(self):
        self.frame.destroy()
        self.frame = tk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")
        self.display_welcome()
        self.display_fed_feed()

text_input = [
    # ... add more lines as needed
]

root = tk.Tk()
app = TonyApp(root, text_input, welcome_msg='WELCOME TO TONY APP')
root.mainloop()
