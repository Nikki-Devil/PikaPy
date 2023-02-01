# Can I tkinter out a 16x16 image from a 32x32 image?

test = [1, 1]
test2 = [2, 1]
test3 = [1, 2]
test4 = [2, 2]
num = '0000'
num_case = 0
coords_tile = [0, 0]
tile_type = '0001'
tile = [" "]


def map_graphic(map_values, map_g, facing):
    import os
    from tkinter import Tk, Canvas, PhotoImage
    from Scripts.PIL import Image
    global num
    global coords_tile

    def map_tile_finder(map_g, coords_tile):
        global tile_type
        global num_case
        num_case += 1
        print("num_case :", num_case)
        if map_g[num_case] == "-":
            tile_type = "0001"
            coords_tile = [coords_tile[1] + 1, coords_tile[1]]
        elif map_g[num_case] == "a" or map_g[num_case] == " ":
            tile_type = '0002'
            coords_tile = [coords_tile[1] + 1, coords_tile[1]]
        elif map_g[num_case] == "G":
            tile_type = '0003'
            coords_tile = [coords_tile[1] + 1, coords_tile[1]]
        elif map_g[num_case] == "P":
            tile_type = '0004'
            coords_tile = [coords_tile[1] + 1, coords_tile[1]]
        elif map_g[num_case] == "\n" or (num_case * coords_tile[1] + 1) == map_values[4]:
            num_case += 1
            coords_tile = [0, coords_tile[1] + 1]
        elif (num_case * coords_tile[0] + 1) == map_values[3]:
            print("Map Graphic Error Out of Bounds height")
            tile_type = '0001'
        else:
            tile_type = '0001'
            coords_tile = [coords_tile[1] + 1, coords_tile[1]]
        return tile_type, coords_tile[0], coords_tile[1]

    def num_check():
        global num
        if num == '9999' or len(num) > 4 or num == 'error':
            num = 'error'
            return print("Error: Too many images")
        else:
            num = str(int(num) + 1)
        if len(num) == 4:
            num = int(num)
        elif len(num) == 3:
            num = "0" + str(int(num))
        elif len(num) == 2:
            num = "00" + str(int(num))
        elif len(num) == 1:
            num = "000" + str(int(num))
        return num

    if ".Temp" in os.listdir():
        for file in os.listdir(".Temp"):
            os.remove(".Temp/" + file)
        pass
    else:
        os.mkdir(".Temp")
        pass

    # Tkinter
    root = Tk()
    root.title("Map Graphic")
    root.geometry("800x600")
    root.resizable(False, False)

    # Canvas
    canvas = Canvas(root, width=800, height=600, bg="white")
    canvas.pack()

    # Image
    image = "data/tileset/012_0123456.jpg"

    def num_0():
        global num
        num = '0000'
        return num

    # Tile
    im = Image.open(image)
    size = str(im.size)
    size = size.replace("(", "")
    size = size.replace(")", "")
    size = size.split(",")
    size = [int(size[0]), int(size[1])]
    print(size)
    num_0()
    for i in range(0, size[0], 16):
        for j in range(0, size[1], 16):
            print(i), print(j)
            num_check()
            print(num)
            crop = (i, j, i + 16, j + 16)
            crop_im = im.crop(crop)
            crop_im = crop_im.resize((32, 32), Image.Resampling.LANCZOS)
            file = ".Temp/Tile_" + str(num) + ".png"
            crop_im.save(file)

    # Grid
    for x in range(0, 800, 33):
        canvas.create_line(x, 0, x, 600, fill="black")
    for y in range(0, 600, 33):
        canvas.create_line(0, y, 800, y, fill="black")

    # Mapping Graphic
    def tile_g(*coords):
        global tile
        num_check()
        if len(coords) == 3:
            tile_type = coords[0]
            x = coords[1]
            y = coords[2]
        else:
            tile_type = "0001"
            x = 0
            y = 0
        file = ".Temp/Tile_" + tile_type + ".png"
        tile = PhotoImage(file=file)
        print(tile)
        canvas.create_image((32 * int(x) - 16 + int(x)), (32 * int(y) - 16 + int(y)), image=tile,
                            tags=("Tile_" + str(num)))
    num_0()
    for g in range(0, (len(map_g) - map_values[3])):
        tile_g_values = map_tile_finder(map_g, coords_tile)
        tile_g(tile_g_values[0], tile_g_values[1], tile_g_values[2])

    for file in os.listdir(".Temp"):
        os.remove(".Temp/" + file)
    os.rmdir(".Temp")
    print("Exited and .Temp and Pycache cleaned")


# for file in os.listdir("PIL/__pycache__"):
#     os.remove("PIL/__pycache__/" + file)
# os.rmdir("PIL/__pycache__")
