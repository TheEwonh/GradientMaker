# Gradient Maker (or printer) by TheEwonh
# desc: Makes gradient text by simple code
# Algorithm: Get needed data -> Check if values are correct ->
#            -> convert hex-code to rgb -> apply every generated color
#            to text

# --=[VALUES]=--
# desc: assigns values needed for program to run

# HEXVALUES - number for every letter used in conversion (CONSTANT)
HEXVALUES = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}

# --=[FUNCTIONS]=--
# desc: reusable functions or separated blocks of code

# check() - checks if given hex code is valid
def check(hex):
    # Checking if hex code is strictly 6 digits long:
    # If yes - return true, which causes program exit
    # If not - continue...
    if len(hex) != 6:
        print("Hex code should be strictly 6 characters long! (ex.: 00FFFF, 234fca)")
        return 1
    # Checking for every character to be exactly in hexadecimal system:
    # If unknown character - return true, which causes program exit
    # If not - continue...
    for char in hex:
        if not char.lower() in "0123456789abcdef":
            print("Invalid hex code was given. Unrecognized "+char)
            return 1

# hex_to_rgb() - converts hex code to rgb
def hex_to_rgb(first, last):
    # colors - list which is being returned with rgb values
    colors = []
    # Iterating through each hex code
    for hex in [first, last]:
        # temp_colors - temporary list of [Red, Green, Blue]
        temp_colors = []
        # Take every color separately
        # First iteration - 1, 2 (RED)
        # Second iteration - 3, 4 (GREEN)
        # Third iteration - 5, 6 (BLUE)
        for pair in range(0, 5, 2):
            # color_tens - takes first character of each hex color (aka: tens)
            # color_ones - takes second character of each hex color (aka: ones)
            color_tens = hex[pair].lower()
            color_ones = hex[pair+1].lower()
            # Is color_tens an integer?
            # If yes - converts str to int
            # If not - applies number from hexValues for that letter
            try:
                color_tens = int(color_tens)
            except:
                color_tens = HEXVALUES[color_tens]
            # Is color_ones an integer?
            # If yes - converts str to int
            # If not - applies number from hexValues for that letter
            try:
                color_ones = int(color_ones)
            except:
                color_ones = HEXVALUES[color_ones]
            temp_colors.append(color_tens*16 + color_ones)
        # Converts temp_colors to tuple and adds it to colors to separate it from other color
        colors.append(tuple(temp_colors))
    # return: [(RED, GREEN, BLUE), (RED, GREEN, BLUE)]
    return colors

# rgb_to_hex() - converts rgb to hex code
def rgb_to_hex(rgb):
    # converted - variable of final hex code
    converted = ""
    # Iterating through Red, Green, Blue colors
    for color in rgb:
        # Get tens by dividing color to 16 without remainder
        tens = color // 16
        # Is tens greater or equal to 10?
        # If yes - get value from HEXVALUES and paste in letter
        # If not - convert tens to string and add it to converted
        if tens >= 10:
            for k, v in HEXVALUES.items():
                if tens == v:
                    converted += k.upper()
        else:
            converted += str(tens)
        # Get ones by subtracting near number to color dividable by 16 from color
        ones = color - (tens*16)
        # Is ones greater or equal to 10?
        # If yes - get value from HEXVALUES and paste in letter
        # If not - convert ones to string and add it to converted
        if ones >= 10:
            for k, v in HEXVALUES.items():
                if ones == v:
                    converted += k.upper()
        else:
            converted += str(ones)
    # returns hex code
    return converted

# interpolate() - generates colors in between
def interpolate(first, last, text):
    # colors - list for interpolated colors
    colors = []
    # amp (amplifier) - how much gradient should change per character
    amp = 1/(len(text)-1)
    # first_amp (first_amplifier) - amplifier for first color (decreases each character)
    first_amp = 1
    # last_amp (last_amplifier) - amplifier for last color (increases each character)
    last_amp = 0

    # iterate through text characters (Iteration is not used)
    for Iteration in range(len(text)):
        # color - list for interpolated color
        color = []
        # interpolating color
        for _ in range(3):
            # FORMULA: (first_color * first_amplifier) + (last_color * last_amplifier)
            # Converting result to integer, in case result will be float (Yeah, that's why we only have 16777216 colors)
            # Adding interpolated color to color list
            color.append(int((first[_] * first_amp) + (last[_] * last_amp)))
        # Decreasing first amplifier to weaken effect of first effect
        # And increasing last amplifier for stronger effect of last color
        first_amp -= amp
        last_amp += amp
        # Adding color to colors
        colors.append(tuple(color))
    # return: [(RED1, GREEN1, BLUE1), (RED2, GREEN2, BLUE2), ..., (REDn, GREENn, BLUEn)]
    return colors

# render() - prints text and colors for each character
def render(colors, text):
    # Create space between text input field and output
    print()
    # Iterate through text length
    for count in range(len(text)):
        # Apply color to character (it is complicated written, I know)
        print(f"\033[38;2;{colors[count][0]};{colors[count][1]};{colors[count][2]}m"+text[count]+"\033[0m", end="")
    # Create space between gradient text and color for each character
    print()
    # Do the same loop
    for count in range(len(text)):
        # Print colored character
        print(f"\033[38;2;{colors[count][0]};{colors[count][1]};{colors[count][2]}m"+text[count]+"\033[0m", end="")
        # Convert rgb color to hexadecimal code
        hex = rgb_to_hex((colors[count][0], colors[count][1], colors[count][2]))
        # Print color as hex and rgb
        print(f" -> #{hex} / ({colors[count][0]}, {colors[count][1]}, {colors[count][2]})")

# --=[MAIN]=--
# desc: main functions for program to run

def main():
    # Asking for hex-code's and checking for their validation
    firstHex = input("Enter first hex code: #")
    # If check returns true:
    # exit program, else continue
    if check(firstHex):
        return
    secondHex = input("Enter last hex code: #")
    if check(secondHex):
        return
    text = input("Enter text:\n")

    # Converting hex to rgb for further usage in code
    colors = hex_to_rgb(firstHex, secondHex)
    # Generate colors for each character in text
    interColors = interpolate(colors[0], colors[1], text)
    # Rendering gradient
    render(interColors, text)

# --=[EXECUTE]=--
# desc: in case why not

if __name__ == "__main__":
    main()
else:
    print("Run script directly")