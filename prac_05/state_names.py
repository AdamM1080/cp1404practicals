"""
CP1404/CP5632 Practical05
State names in a dictionary
File needs reformatting by LindsayMarkWard
"""

STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
print(STATE_NAMES)

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(f"{state_code:<3} is {STATE_NAMES[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

for state_code, name in STATE_NAMES.items():
    print(f"{state_code:<3} is {name}")
