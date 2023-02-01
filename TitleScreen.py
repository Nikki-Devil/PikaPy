# https://www.pythontutorial.net/tkinter/tkinter-label/

# Imports
from tkinter import *
from tkinter import ttk
import os
import shutil


# Variables
language_op = ""
options_file_ = ""
options_Lang = "en"
options_root = ""
bt = ""
len_ = 0
finding = 0


def pikapy():
    # Open Options.ini
    with open("Options.ini", "r") as options_file_o:
        options_file_ = options_file_o.read()
        options_file_o.close()

    # Get the language
    options_file_lang = options_file_.find("Language = ")
    language_op_o = "Language = " + options_file_[options_file_lang + 11: options_file_lang + 13]
    lang_alone = options_file_[options_file_lang + 11: options_file_lang + 13]

    # Get the language values
    def language():
        global bt
        with open(("Data/" + "Lang_" + options_file_[options_file_lang + 11: options_file_lang + 13] +
                   ".txt"), "r") as lang:
            lang_ = lang.read()
            find_lang = 0
            num1, num2, num3, num4 = 0, 0, 0, 1
            pk = [lang_[lang_.find("Pk_000") + 9: lang_.find("Pk_000") + 12], "Pk_"]
            item = [lang_[lang_.find("It_000 = ") + 9: lang_.find("It_000") + 12], "It_"]
            mv = [lang_[lang_.find("Mv_000 = ") + 9: lang_.find("Mv_000") + 12], "Mv_"]
            types = [lang_[lang_.find("Ty_00 = ") + 8: lang_.find("Ty_00") + 10], "Ty_"]
            ab = [lang_[lang_.find("Ab_000 = ") + 9: lang_.find("Ab_000") + 12], "Ab_"]
            lc = [lang_[lang_.find("Lc_000 = ") + 9: lang_.find("Lc_000") + 12], "Lc_"]
            tr = [lang_[lang_.find("Tr_0000 = ") + 10: lang_.find("Tr_0000") + 14], "Tr_"]
            dg = [lang_[lang_.find("Dg_0000 = ") + 10: lang_.find("Dg_0000") + 14], "Dg_"]
            si = [lang_[lang_.find("Si_0000 = ") + 10: lang_.find("Si_0000") + 14], "Si_"]
            bt = [lang_[lang_.find("Bt_0000 = ") + 10: lang_.find("Bt_0000") + 14], "Bt_"]
            dummy = 0
            lang.close()

        # Check the number of the iteration to update it if it's needed (>= 10 : 1, 0)
        def num(num1, num2, num3, num4):
            if num4 == 10:
                num4 = 0
                num3 = num3 + 1
            if num3 == 10:
                num3 = 0
                num2 = num2 + 1
            if num2 == 10:
                num2 = 0
                num1 = num1 + 1

            # In case of a number >= 9999 (5 digits), print an error
            if num1 == 10:
                num4 = 9
                num3 = 9
                num2 = 9
                num1 = 9
                print("Error: Too many items ; out of range")
            return num1, num2, num3, num4

        # Get the language values for a defined variable
        def find_lang_(to_find):
            # Global variables
            global len_
            global finding

            # Variables
            num_ = [0, 0, 0, 1]
            str_to_find = str(to_find[1])
            to_find = [to_find[0]]
            if len(to_find[0]) == 2:
                len_ = 8
            elif len(to_find[0]) == 3:
                len_ = 9
            elif len(to_find[0]) == 4:
                len_ = 10

            # Find the language values for the "to_find" variable
            while (num_[0] * 1000 + num_[1] * 100 + num_[2] * 10 + num_[3]) != (int(to_find[0]) + 1):
                num_ = num(num_[0], num_[1], num_[2], num_[3])
                num_ = [num_[0], num_[1], num_[2], num_[3]]
                find_lang_s = len_

                if len_ == 8:
                    finding = str_to_find + str(num_[2]) + str(num_[3])
                elif len_ == 9:
                    finding = str_to_find + str(num_[1]) + str(num_[2]) + str(num_[3])
                elif len_ == 10:
                    finding = str_to_find + str(num_[0]) + str(num_[1]) + str(num_[2]) + str(num_[3])

                find_lang = lang_.find(str(finding))
                while lang_[find_lang + find_lang_s] != "\n":
                    find_lang_s = find_lang_s + 1
                to_find += [lang_[find_lang + len_: find_lang + find_lang_s]]
                num_[3] += 1
            return to_find

        # Get the language values for each variable from the "find_lang_" function
        pk, item, mv, types = find_lang_(pk), find_lang_(item), find_lang_(mv), find_lang_(types)
        ab, lc, tr, dg, bt = find_lang_(ab), find_lang_(lc), find_lang_(tr), find_lang_(dg), find_lang_(bt)
        si = find_lang_(si)
        return pk, item, mv, types, ab, lc, tr, dg, si, bt

    # Tkinter Window
    root = Tk()
    root.title("PikaPy")
    title = ttk.Frame(root, padding=100)
    title.grid()

    # Options
    def options():
        # Global variables
        global options_file_
        global options_root

        def close_options():
            # noinspection PyUnboundLocalVariable
            options_root.destroy()

            def op():
                global options_root
                options_root = "closed"

            op()

        if options_root == "" or options_root == "closed":
            options_root = "opened"
            # Options Window
            options_root = Tk()
            options_root.title("Options")
            battle_style_win = ttk.Frame(options_root, padding=10)
            language_win = ttk.Frame(options_root, padding=0)
            options_window = ttk.Frame(options_root, padding=15)
            language_win.grid()
            battle_style_win.grid()
            options_window.grid()

            # Change the language to English
            def value_lang_en():
                # Global variables
                global language_op

                language_op = "Language = en"
                language()
                return language_op

            # Change the language to French
            def value_lang_fr():
                # Global variables
                global language_op

                language_op = "Language = fr"
                language()
                return language_op

            # Save the changes
            def save():
                # Global variables
                global language_op

                # noinspection PyShadowingNames
                with open("Options.ini", "r") as options_file_o:
                    # noinspection PyShadowingNames
                    options_file_ = options_file_o.read()
                    options_file_o.close()

                # Backup the file
                with open("Options.ini.bak", "w") as options_file_bak:
                    options_file_bak.write(options_file_)
                    options_file_bak.close()

                # Save the file
                if language_op == "":
                    language_op = "Language = en"
                options_file_s = options_file_
                options_file_s = options_file_s.replace(language_op_o, language_op)
                with open("Options.ini", "w") as options_file_save_s:
                    options_file_save_s.write(str(options_file_s[0: len(options_file_s)]))
                    options_file_save_s.close()

            # Reset Options to default
            def reset():
                # Take the backup file (.bak) in "./Data" and replace the current file
                with open("Data/Options.bak", "r") as options_file_reset:
                    options_file_reset_ = options_file_reset.read()
                    options_file_reset.close()
                with open("Options.ini", "w") as options_file_save_r:
                    options_file_save_r.write(options_file_reset_)
                    options_file_save_r.close()

            # Options Labels
            ttk.Label(battle_style_win, text=bt[12]).grid(column=0, row=0)  # Battle Style
            ttk.Label(language_win, text=bt[13]).grid(column=0, row=0)  # Language
            ttk.Label(options_root, text=bt[14]).grid(column=0, row=101)  # First long text
            # Options Buttons
            ttk.Button(battle_style_win, text=bt[1], command=save).grid(column=1, row=0)  # Set
            ttk.Button(battle_style_win, text=bt[2]).grid(column=2, row=0)  # Switch
            ttk.Button(language_win, text="English", command=value_lang_en).grid(column=1, row=0)
            ttk.Button(language_win, text="Français", command=value_lang_fr).grid(column=2, row=0)

            ttk.Button(options_window, text=bt[4], command=save).grid(column=0, row=1)  # Save
            ttk.Button(options_window, text=bt[3]).grid(column=1, row=1)  # Cancel
            ttk.Button(options_window, text=bt[8], command=reset).grid(column=2, row=1)  # Reset

            ttk.Button(options_root, text=bt[9], command=close_options).grid(column=0, row=100)  # Close

            # Start Options GUI
            options_root.focus_force()
            options_root.protocol("WM_DELETE_WINDOW", close_options)
            options_root.mainloop()

        else:
            # Focus on Options if it's already opened
            options_root.focus_force()

        pass

    # Close everything
    def close_root():
        options_file_o.close()
        exit(print("Bye!"))

    lang = language()
    pk = lang[0]
    item = lang[1]
    mv = lang[2]
    types = lang[3]
    ab = lang[4]
    lc = lang[5]
    tr = lang[6]
    dg = lang[7]
    si = lang[8]
    bt = lang[9]

    def new_game():
        from Scripts import New_Game
        New_Game.new_game(root, bt, lang_alone)

    def debug():
        from Scripts import Map_test
        root.destroy()
        with open("Saves/Save1.sav", "r") as save_file:
            nb_save = 2
            save_file_ = save_file.read()
            save_file.close()
            dummy = save_file_[save_file_.find("Coords = "): save_file_.find("Coords = ") + 9]
            if dummy == "Coords = ":
                coords = save_file_[save_file_.find("Coords = ") + 9: save_file_.find("Coords = ") + 18]
                coords = coords.split(" ")
            else:
                save_file_ = "Null"
            map_name_ = save_file_[save_file_.find("Map = "): save_file_.find("Map = ") + 20]
            if map_name_[0:6] != "Map = ":
                map_name_ = "Corrupted"
            elif len(map_name_) != 17:
                map_name_ = "Corrupted"
            else:
                map_name_ = map_name_[6: len(map_name_)]
        Map_test.move(map_name_, tr, dg, si, coords, lang_alone, nb_save)

    # Buttons
    ttk.Button(title, text=bt[10], command=new_game).grid(column=0, row=0)  # New Game
    ttk.Button(title, text=bt[11]).grid(column=0, row=1)  # Load Game
    ttk.Button(title, text=bt[6], command=options).grid(column=0, row=2)  # Options
    ttk.Button(title, text="Debug", command=debug).grid(column=0, row=3)  # Debug
    ttk.Button(title, text=bt[7], command=close_root).grid(column=0, row=5)  # Quit

    # Start Tkinter GUI
    root.protocol("WM_DELETE_WINDOW", close_root)
    root.mainloop()


# Maybe first time the program is launched
if "Options.ini" in os.listdir():
    pikapy()
else:
    if "Options.ini.bak" in os.listdir():
        shutil.copy("Options.ini.bak", "Options.ini")
        pikapy()
    # Not first time the program is launched
    elif len(os.listdir("Saves")) > 0:
        # Create Options.ini from first save file options
        with open("Saves/Save1.sav", "r") as save_file:
            save_file_ = save_file.read()
            save_file_lang = save_file_.find("Language = ")
            save_file_lang = save_file_[save_file_lang + 11: save_file_lang + 13]
            shutil.copy("Data/Options.bak", "Options.ini")
            with open("Options.ini", "r") as options_file_:
                options_file = options_file_.read()
                options_file = options_file.replace("Language = en", "Language = " + save_file_lang)
                with open("Options.ini", "w") as options_file_save:
                    options_file_save.write(options_file)
                    options_file_save.close()
                options_file_.close()
            save_file.close()
        pikapy()
    else:
        # Create Options.ini from default options (First time)
        shutil.copy("Data/Options.bak", "Options.ini")
        first = Tk()
        first.title("PikaPy")
        first.grid()
        ttk.Label(first, text="Choose Language").grid(column=0, row=0)

        def value_lang_en_f():
            # noinspection PyShadowingNames
            with open("Options.ini", "r") as options_file:
                options_file_o_ = options_file.read()
                options_file_o_ = options_file_o_.replace("Language = en", "Language = en")
                with open("Options.ini", "w") as options_file_save_o:
                    options_file_save_o.write(options_file_o_)
                    options_file_save_o.close()
                options_file.close()
            first.destroy()
            pikapy()
            pass

        def value_lang_fr_f():
            # noinspection PyShadowingNames
            with open("Options.ini", "r") as options_file:
                options_file_o_ = options_file.read()
                options_file_o_ = options_file_o_.replace("Language = en", "Language = fr")
                with open("Options.ini", "w") as options_file_save_o:
                    options_file_save_o.write(options_file_o_)
                    options_file_save_o.close()
                options_file.close()
            first.destroy()
            pikapy()
            pass

        ttk.Button(first, text="English", command=value_lang_en_f).grid(column=1, row=0)
        ttk.Button(first, text="Français", command=value_lang_fr_f).grid(column=2, row=0)
        first.mainloop()
