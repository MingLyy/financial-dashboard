import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.title("Financial Dashboard")
        self.geometry("1280x720")
        self.after(0, lambda: self.state("zoomed"))  # maximizes window
