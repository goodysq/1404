COLOUR_HEX = {"Acid Green": "#b0bf1a",
              "AliceBlue": "#f0f8ff",
              "Alizarin crimson": "#e32636",
              "Amaranth": "#e52b50",
              "Amber": "#ffbf00",
              "Amethyst": "#9966cc",
              "AntiqueWhite": "#faebd7"}
colour_name = input("colour name: ")
while colour_name != "":
    try:
        print(f"{colour_name} : {COLOUR_HEX[colour_name]}")
        colour_name = input("colour name: ")
    except KeyError:
        print("Sorry, no idea")
        colour_name = input("colour name: ")
