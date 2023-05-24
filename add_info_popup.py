from tkinter import *
import main_config
from parent_interface import Parent


class OpenPopUp:
    """ Initialises the popup window that holds all of the additional information widgets """
    def __init__(self, parent: Parent, art_title=None, add_info=None):
        self.parent = parent
        self.info_pop = Toplevel()
        self.info_pop.geometry("390x300")
        self.info_pop.title("Additional Info")
        self.info_pop.lift()
        self.info_pop.config(bg=main_config.THEME_COLOR)
        self.info_pop.transient(self.parent.window)
        self.info_pop.grab_set()

        self.add_info = add_info
        self.art_title = art_title

        self.label1 = Label(self.info_pop, text="Here is some more information on the piece titled:", font="Helvetica 13",
                            fg="black", bg=main_config.THEME_COLOR, padx=50, pady=10)
        self.label1.grid(column=1, row=1)

        self.label2 = Label(self.info_pop, text=f"'{art_title}'", font="Helvetica 13 italic",
                            fg=main_config.DEFAULT_FONT_COLOUR, bg=main_config.THEME_COLOR, padx=50, pady=10,
                            wraplength=300)
        self.label2.grid(column=1, row=2)

        self.label3 = Label(self.info_pop, text=f"{'*' * 50}", font="Helvetica 13 bold",
                            fg="black", bg=main_config.THEME_COLOR, padx=50, pady=10,
                            wraplength=300)
        self.label3.grid(column=1, row=3)

        self.label4 = Label(self.info_pop, text=f"{add_info}", font="Helvetica 16 bold",
                            fg=main_config.DEFAULT_FONT_COLOUR, bg=main_config.THEME_COLOR, padx=50, pady=20, wraplength=300)
        self.label4.grid(column=1, row=4)

        self.button = Button(self.info_pop, text="Close", highlightthickness=0,highlightbackground=main_config.THEME_COLOR,
                             command=lambda: self.close_popup())
        self.button.grid(column=1, row=6)

    """ Function to close the popup window """
    def close_popup(self):
        self.info_pop.destroy()