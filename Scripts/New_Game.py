# This is the New Game script for the PikaPy Project
import os
# Import modules
from tkinter import *
from tkinter import ttk

sex = ""


# New Game function
def new_game(root, bt, lang_alone):
    root.destroy()
    new_game_info = Tk()
    new_game_info.title("PikaPy - " + bt[15])  # New Game
    new_game_other = ttk.Frame(new_game_info, padding=10)
    new_game_values = ttk.Frame(new_game_info, padding=10)
    new_game_values_s = ttk.Frame(new_game_info, padding=10)
    new_game_values_n = ttk.Frame(new_game_info, padding=10)
    new_game_other.grid()
    new_game_values_n.grid()
    new_game_values_s.grid()

    def close():
        new_game_info.destroy()

    def get_values():
        name = character_name.get()
        save(name, sex, lang_alone)
        pass

    def sex_select_m():
        global sex
        sex = "Male"
        pass

    def sex_select_f():
        global sex
        sex = "Female"
        pass

    def sex_select_h():
        global sex
        sex = "Hermaphrodite"
        pass

    def save(name, sex, lang_alone):
        save_count = 1
        if "Save" + str(save_count) + ".sav" in os.listdir("./Saves"):
            while ("Save" + str(save_count) + ".sav") in os.listdir("./Saves"):
                save_count = save_count + 1
        with open("./Saves/Save" + str(save_count) + ".sav", "w") as save_file:
            save_file.write("Name = " + name + "\n")
            save_file.write("Sex = " + sex + "\n")
            save_file.write("Language = " + lang_alone + "\n")
            save_file.close()
        pass

    # New Game Info
    new_game_values.grid()
    ttk.Label(new_game_other, text=(bt[15] + " " + bt[16].lower())).grid(column=0, row=0)  # New Game Info
    ttk.Label(new_game_values_n, text=bt[17]).grid(column=0, row=1)  # Name
    character_name = ttk.Entry(new_game_values_n, exportselection=False, width=20)
    character_name.grid(column=1, row=1)
    ttk.Label(new_game_values_s, text=bt[19]).grid(column=0, row=2)  # Sex
    ttk.Button(new_game_values_s, text=bt[20], command=sex_select_m).grid(column=1, row=2)  # Male
    ttk.Button(new_game_values_s, text=bt[21], command=sex_select_f).grid(column=2, row=2)  # Female
    ttk.Button(new_game_values_s, text=bt[22], command=sex_select_h).grid(column=3, row=2)  # Hermaphrodite
    ttk.Button(new_game_values, text=bt[18], command=get_values).grid(column=0, row=0)  # Confirm
    ttk.Button(new_game_values, text=bt[7], command=close).grid(column=1, row=0)  # Quit
    new_game_info.protocol("WM_DELETE_WINDOW", close)
    new_game_info.focus_force()
