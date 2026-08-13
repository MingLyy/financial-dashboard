import customtkinter as ctk

from financial_dashboard.app import App


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

def main() -> None:
    App().mainloop()
