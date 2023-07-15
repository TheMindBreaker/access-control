import customtkinter as tk

class MyCheckboxFrame(tk.CTkFrame):
    def __ini__(self):
        tk.CTkLabel(self, text="Text1")

class frame2(tk.CTkFrame):
    def __ini__(self):
        tk.CTkLabel(self, text="Text2")

class App(tk.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.attributes("-fullscreen", "True")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.checkbox_frame_1 = MyCheckboxFrame(self)
        self.checkbox_frame_1.grid(row=0, column=0, padx=5, pady=(10, 0), sticky="nsew")
        self.checkbox_frame_2 = frame2(self)
        self.checkbox_frame_2.grid(row=0, column=1, padx=(0, 5), pady=(10, 0), sticky="nsew")


app = App()
app.mainloop()