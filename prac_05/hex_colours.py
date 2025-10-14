"""
CP1404/CP5632 Practical05
Look up different hexadecimal colour codes
"""


def main():
    colour_names = {"absolute zero": "#0048ba",
                    "acid green": "#b0bf1a",
                    "aliceblue": "#f0f8ff",
                    "alizarin crimson": "#e32636",
                    "amaranth": "#e52b50",
                    "amber": "#ffbf00",
                    "amethyst": "#9966cc",
                    "antiquewhite": "#faebd7",
                    "antiquewhite2": "#ffefdb",
                    "antiquewhite3": "#cdc0b0"
                    }
    print(colour_names)
    colour_name = input("Enter colour name: ").lower()
    while colour_name != "":
        try:
            print(f"{colour_name} is {colour_names[colour_name]}")
        except KeyError:
            print("Invalid colour name")
        colour_name = input("Enter colour name: ").lower()


main()
