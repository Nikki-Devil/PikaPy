# Open and interpret maps script

# Variables
facing = "u"
tr = []
dg = []
p_line = []
coords_P = [0, 0, "u"]


def move(map_name_, tr, dg, si, coords, lang_alone, nb_save):
    global p_line

    if map_name_ == "Corrupted":
        coords = [0, 0, "u"]
    print(coords)
    map_name = "Data/Maps/" + map_name_
    print("Map name: " + map_name_)

    def open_map(map_name, coords):
        global facing
        # Open the map file
        with open(map_name, "r") as map_file:
            map_o = map_file.read()
            map_file.close()
        with open(map_name, "r") as map_file:
            map_g = map_file.read()
            map_file.close()
        with open(map_name, "r") as map_file:
            map_lines = map_file.readlines()
            map_file.close()
        # Get the map height and width from the map file
        map_height = map_o[map_o.find("Map_Height = ") + 13: map_o.find("Map_Height = ") + 16]
        map_width = map_o[map_o.find("Map_Width = ") + 12: map_o.find("Map_Width = ") + 15]
        map_values = [map_height] + [map_width]
        map_height = list(map_height)
        map_width = list(map_width)
        map_height = int(map_height[0] + map_height[1] + map_height[2])
        map_width = int(map_width[0] + map_width[1] + map_width[2])
        map_values += map_height, map_width
        map_g = map_g.split("#", 1)[0]
        map_g = map_g.replace("a", " ")
        map_o = map_o.replace("a", " ")
        map_lines = map_lines[:- (len(map_lines) - map_height)]
        if str(type(coords)) == "<class 'list'>":
            facing = coords[2]
            map_o = map_o.replace("P", " ")
            map_o = map_o[:((int(coords[0]) * map_values[3]) + int(coords[1]) + int(
                        coords[0]))] + "P" + map_o[(int(coords[0]) * map_values[3]) + int(
                            coords[1]) + int(coords[0]) + 1:]
            map_g = map_g.replace("P", " ")
            map_g = map_g[:((int(coords[0]) * map_values[3]) + int(coords[1]) + int(
                        coords[0]))] + "P" + map_g[(int(coords[0]) * map_values[3] + int(
                            coords[0])) + int(coords[1]) + 1:]
            for j in range(len(map_lines)):
                map_lines[j] = map_lines[j].replace("P", "a")
            map_lines[int(coords[0])] = map_lines[int(coords[0])][:int(coords[1])] + "P" + map_lines[
                                                int(coords[0])][int(coords[1]) + 1:]
        for j in range(len(map_lines)):
            map_lines[j] = map_lines[j].replace("#\n", "")
        return map_o, map_g, map_values, map_lines

    def left(map_g, map_lines):
        # Create variables
        global facing
        facing = "l"
        map_ = map_g
        dummy_variable = 0
        p_line = []

        # Find the player's position
        for line in map_lines:
            if "P" in line:
                p_line += [dummy_variable]
                p_line += [line.find("P")]
            dummy_variable += 1
        p = map_.find("P")
        path = map_.find("P") - 1

        # Check if the player is at the left edge of the map
        if map_.find("P") - 1 == -1 or map_.find("P") - 1 == "\n" or map_.find("P") - 1 == "#":
            return map_g

        # If the player is not at the left edge of the map and the path are clear
        if map_[path] == " ":
            map_lines[p_line[0]] = map_lines[p_line[0]].replace("P", "a")
            map_lines[p_line[0]] = map_lines[p_line[0]][:(p_line[1] - 1)] + "P" + map_lines[p_line[0]][p_line[1]:]
            map_ = map_.replace("P", " ")
            map_ = map_[:p - 1] + "P" + map_[p:]
            return map_

        # If the player is not at the left edge of the map and the path is not clear
        else:
            return map_g
        pass

    def right(map_g, map_lines):
        # Create variables
        global facing
        facing = "r"
        map_ = map_g
        dummy_variable = 0
        p_line = []

        # Find the player's position
        for line in map_lines:
            if "P" in line:
                p_line += [dummy_variable]
                p_line += [line.find("P")]
            dummy_variable += 1
        p = map_.find("P")
        path = map_.find("P") + 1

        # Check if the player is at the right edge of the map
        if map_.find("P") + 1 == -1 or map_.find("P") + 1 == "\n" or map_.find("P") + 1 == "#":
            return map_g

        # If the player is not at the right edge of the map and the path is clear
        if map_[path] == " ":  # If the path is clear
            map_lines[p_line[0]] = map_lines[p_line[0]].replace("P", "a")
            map_lines[p_line[0]] = map_lines[p_line[0]][:(p_line[1] + 1)] + "P" + map_lines[p_line[0]][p_line[1] + 2:]
            map_ = map_.replace("P", " ")
            map_ = map_[:p + 1] + "P" + map_[p + 2:]
            return map_

        # If the player is not at the right edge of the map and the path is not clear
        else:
            return map_g
        pass

    def up(map_g, map_lines, map_values):
        # Create variables
        global facing
        facing = "u"
        map_ = map_g
        map_l = map_lines
        dummy_variable = 0
        p_line = []

        # Find the player's position
        for line in map_l:
            if "P" in line:
                p_line += [dummy_variable]
                p_line += [line.find("P")]
            dummy_variable += 1

        # If the player is at the top of the map
        if p_line[0] - 1 < 0:
            return map_g

        # If the player is not at the top of the map and the path is clear
        elif map_l[p_line[0] - 1][p_line[1]] == "a" or map_l[p_line[0] - 1][p_line[1]] == " ":
            map_l[p_line[0]] = map_l[p_line[0]].replace("P", "a")
            map_l[p_line[0] - 1] = map_l[p_line[0] - 1][:(p_line[1])] + "P" + map_l[
                                       p_line[0] - 1][p_line[1] + 1:]
            map_ = map_.replace("P", " ")
            map_dummy = map_l[p_line[0] - 1].replace("a", " ")
            map_ = map_.replace(map_dummy.replace("P", " "), map_dummy)
            return map_

        # If the player is not at the top of the map and the path is not clear
        else:
            p = (p_line[0] - 1) * map_values[3] + p_line[1] + 1
            return map_g
        pass

    def down(map_g, map_lines, map_values):
        # Create variables
        global facing
        facing = "d"
        map_ = map_g
        map_l = map_lines
        dummy_variable = 0
        p_line = []

        # Find the player's position
        for line in map_l:
            if "P" in line:
                p_line += [dummy_variable]
                p_line += [line.find("P")]
            dummy_variable += 1

        # If the player is at the bottom of the map
        if p_line[0] + 1 > map_values[2]:
            return map_g

        # If the player is not at the bottom of the map and the path is clear
        elif map_l[p_line[0] + 1][p_line[1]] == "a" or map_l[p_line[0] + 1][p_line[1]] == " ":
            map_l[p_line[0]] = map_l[p_line[0]].replace("P", "a")
            map_l[p_line[0] + 1] = map_l[p_line[0] + 1][:(p_line[1])] + "P" + map_l[
                                       p_line[0] + 1][p_line[1] + 1:]
            map_ = map_.replace("P", " ")
            map_dummy = map_l[p_line[0] + 1].replace("a", " ")
            map_ = map_.replace(map_dummy.replace("P", " "), map_dummy)
            return map_

        # If the player is not at the bottom of the map and the path is not clear
        else:
            p = (p_line[0] - 1) * map_values[3] + p_line[1] + 1
            return map_g
        pass

    def interact_(map_o, map_values, map_lines, tr, dg):
        # Create variables
        global facing
        map_ = map_o
        dummy_variable = 0
        p_line = []

        # Instead of having this in every possible direction, I just made it a function
        def dummy_check(npc_location):
            if npc_location[0] > 100:
                dummy_variable = 3
            elif npc_location[0] > 10:
                dummy_variable = 2
            else:
                dummy_variable = 1
            if npc_location[1] > 100:
                dummy_variable += 3
            elif npc_location[1] > 10:
                dummy_variable += 2
            else:
                dummy_variable += 1
            dummy_variable += 10
            return dummy_variable

        # Find the player's position
        for line in map_lines:
            if "P" in line:
                p_line += [dummy_variable]
                p_line += [line.find("P")]
            dummy_variable += 1
        p = map_.find("P")

        # If the player is near a NPC (g)
        if map_lines[p_line[0] - 1][p_line[1]] == "G" and facing == "u":
            print("You interacted with a NPC up")
            npc_location = [(p_line[0] - 1), p_line[1]]
            dummy_variable = dummy_check(npc_location)
            npc = map_[map_.find(str(npc_location)) + dummy_variable:
                       map_.find(str(npc_location)) + (dummy_variable + 4)]
            print(tr[int(npc)], ":")
            print(dg[int(npc)])

        elif map_lines[p_line[0] + 1][p_line[1]] == "G" and facing == "d":
            print("You interacted with a NPC down")
            npc_location = [(p_line[0] + 1), p_line[1]]
            dummy_variable = dummy_check(npc_location)
            npc = map_[map_.find(str(npc_location)) + dummy_variable:
                       map_.find(str(npc_location)) + (dummy_variable + 4)]
            print(tr[int(npc)], ":")
            print(dg[int(npc)])

        elif map_lines[p_line[0]][p_line[1] + 1] == "G" and facing == "r":
            print("You interacted with a NPC right")
            npc_location = [p_line[0], (p_line[1] + 1)]
            dummy_variable = dummy_check(npc_location)
            npc = map_[map_.find(str(npc_location)) + dummy_variable:
                       map_.find(str(npc_location)) + (dummy_variable + 4)]
            print(tr[int(npc)], ":")
            print(dg[int(npc)])

        elif map_lines[p_line[0]][p_line[1] - 1] == "G" and facing == "l":
            print("You interacted with a NPC left")
            npc_location = [p_line[0], (p_line[1] - 1)]
            dummy_variable = dummy_check(npc_location)
            npc = map_[map_.find(str(npc_location)) + dummy_variable:
                       map_.find(str(npc_location)) + (dummy_variable + 4)]
            print(tr[int(npc)], ":")
            print(dg[int(npc)])

        # If the player is not near a NPC
        else:
            print("You are not facing a NPC")
        return map_

    def quit_(map_lines):
        dummy_variable = 0
        p_line = []

        # Find the player's position
        for line in map_lines:
            if "P" in line:
                p_line += [dummy_variable]
                p_line += [line.find("P")]
            dummy_variable += 1

        if p_line[0] >= 100:
            p_line[0] = p_line[0]
        elif p_line[0] >= 10:
            p_line[0] = "0" + str(p_line[0])
        else:
            p_line[0] = "00" + str(p_line[0])
        if p_line[1] >= 100:
            p_line[1] = p_line[1]
        elif p_line[1] >= 10:
            p_line[1] = "0" + str(p_line[1])
        else:
            p_line[1] = "00" + str(p_line[1])

        with open("Saves/Save" + str(nb_save) + ".sav", "w") as save:
            saving = "Coords = " + str(p_line[0]) + " " + str(p_line[1]) + " " + facing + "\n"\
                     + "Language = " + lang_alone + "\n" + "Map = " + map_name_ + "\n"
            save.write(str(saving))
            save.close()
        exit(print("You quit the game"))

    # Map
    def interact(map_o, map_g, map_values, map_lines):
        # Print the map and ask for input
        print(map_g)

        from Scripts import MapGraphic
        MapGraphic.map_graphic(map_values, map_g, facing)

        inp = input("direction (WASD or ZQSD or E): ")

        # If the player wants to interact
        if inp == "E" or inp == "e":
            i = interact_(map_o, map_values, map_lines, tr, dg)
            return interact(i, map_g, map_values, map_lines)

        # If the player wants to go up
        elif inp == "Z" or inp == "z" or inp == "W" or inp == "w":
            u = up(map_g, map_lines, map_values)
            return interact(map_o, u, map_values, map_lines)

        # If the player wants to go left
        elif inp == "Q" or inp == "q" or inp == "A" or inp == "a":
            l = left(map_g, map_lines)
            return interact(map_o, l, map_values, map_lines)

        # If the player wants to go down
        elif inp == "S" or inp == "s":
            d = down(map_g, map_lines, map_values)
            return interact(map_o, d, map_values, map_lines)

        # If the player wants to go right
        elif inp == "D" or inp == "d":
            r = right(map_g, map_lines)
            return interact(map_o, r, map_values, map_lines)

        # If the player wants to quit
        elif inp == "Quit" or inp == "quit":
            quit_(map_lines)

        # If the player didn't enter a valid input
        else:
            return interact(map_o, map_g, map_values, map_lines)

    # Main
    open_map = open_map(map_name, coords)
    interact(open_map[0], open_map[1], open_map[2], open_map[3])
