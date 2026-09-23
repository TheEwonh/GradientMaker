# Gradient Maker (or printer) by TheEwonh
# desc: Makes gradient text by simple code
# Algorithm: Get needed data -> Check if values are correct ->
#            -> convert hex-code to rgb -> apply every generated color
#            to text

# --=[VALUES]=--
# desc: assigns values needed for program to run

# HEXVALUES - number for every letter used in conversion (CONSTANT)
HEXVALUES = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}

# --=[EXCEPTIONS]=--
# desc: custom error codes if code crashes

class InvalidHexError(ValueError):
    # summons if invalid hex code was passed
    pass

class InvalidRGBError(ValueError):
    # summons if invalid rgb value was passed in
    pass

class InvalidValueError(ValueError):
    # summons if invalid value was given
    pass

# --=[FUNCTIONS]=--
# desc: reusable functions or separated blocks of code

# check_hex() - checks if given hex code is valid
def check_hex(hex):
    # Checking if hex is string
    if not isinstance(hex, str):
        print(f"\033[31m✖\033[0m Hex code should be string. Not {type(hex)}")
        raise InvalidHexError("Hex code should be string")
    # Is length of hex code is 7 and first character is #?
    # If yes - fix hex code being EXACTLY 6 characters without number symbol
    # If not - continue...
    if len(hex) == 7 and hex[0] == "#":
        hex = hex[1:7]
    # Checking if hex code is strictly 6 digits long:
    # If yes - return true, which causes program exit
    # If not - continue...
    if len(hex) != 6:
        print("\033[31m✖\033[0m Hex code should be strictly 6 characters long! (ex.: 00FFFF, 234fca)")
        raise InvalidHexError("Should be 6 characters long")
    # Checking for every character to be exactly in hexadecimal system:
    # If unknown character - return true, which causes program exit
    # If not - continue...
    for char in hex:
        if not char.lower() in "0123456789abcdef":
            print("\033[31m✖\033[0m Invalid hex code was given. Unrecognized "+char.upper())
            raise InvalidHexError("Should contain characters from hexadecimal system")
    # return hex code in case it was changed
    return hex

# check_rgb() - checks if given rgb is valid
def check_rgb(rgb):
    # is length of tuple is not 3?
    # if yes - Invalid rgb, raise InvalidRGBError
    # if not - continue...
    if len(rgb) != 3:
        print(f"\033[31m✖\033[0m Incorrect {rgb} rgb value. Should be strictly (red, green, blue)")
        raise InvalidRGBError("Incorrect RGB format")
    # check for validation of every color
    for index, color in enumerate(rgb):
        # is color an integer?
        # if yes - continue...
        # if not - check if it is float
        if not isinstance(color, int):
            # is color a float?
            # if yes - convert every color into an integer, in case why not
            # if not - value is not a number, raise InvalidValueError
            if isinstance(color, float):
                rgb = tuple(int(channel) for channel in rgb)
                color = rgb[index]
                print("\033[33m⚠\033[0m One of your values was changed, because it was float (should be strictly int)")
            else:
                print("\033[31m✖\033[0m One of your channels is not a number. Should be strictly an integer")
                raise InvalidRGBError("Not a number detected")
        # is color in between 0 and 255?
        # if yes - continue...
        # if not - raise InvalidRGBError
        if color < 0 or color > 255:
            print("\033[31m✖\033[0m One of your channels is out of range. Only 0-255 number allowed")
            raise InvalidRGBError("Out of range value")
    return rgb

# hex_to_rgb() - converts hex code to rgb
def hex_to_rgb(hex):
    # Check hex code for validation
    hex = check_hex(hex)
    # color - list which is being returned with rgb value
    color = []
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
        color.append(color_tens*16 + color_ones)
    # return: (RED, GREEN, BLUE)
    return tuple(color)

# rgb_to_hex() - converts rgb to hex code
def rgb_to_hex(rgb):
    # check if rgb is valid
    rgb = check_rgb(rgb)
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
    # is first a string? (meaning it could be possibly be hex code)
    # if yes - probably hex code, checking if hex code is valid
    # if not - check if it is tuple
    # if not tuple - raise InvalidValueError
    if isinstance(first, str):
        # check if hex code is valid
        first = check_hex(first)
        # if hex code is valid, then convert it to rgb
        first = hex_to_rgb(first)
    elif isinstance(first, tuple):
        # check if rgb code is valid
        first = check_rgb(first)
    else:
        print("\033[31m✖\033[0m Incorrect first hex/rgb code was given. Should be either integer, either tuple")
        raise InvalidValueError("Incorrect hex/rgb code")

    # is last a string? (meaning it could be possibly be hex code)
    # if yes - probably hex code, checking if hex code is valid
    # if not - check if it is tuple
    # if not tuple - raise InvalidValueError
    if isinstance(last, str):
        last = check_hex(last)
        # if hex code is valid, then convert it to rgb
        last = hex_to_rgb(last)
    elif isinstance(last, tuple):
        last = check_rgb(last)
    else:
        print("\033[31m✖\033[0m Incorrect last hex/rgb code was given. Should be either integer, either tuple")
        raise InvalidValueError("Incorrect hex/rgb code")

    # Checking if text is a string
    if not isinstance(text, str):
        print(f"\033[31m✖\033[0m Text requires string to be given, not {type(text)}")
        raise InvalidValueError("Text should be string")

    # Checking if it's length is greater or equal to 2 characters (Might cause ZeroDivisionError/unknown behavior if less than 2)
    if len(text) < 2:
        print(f"\033[31m✖\033[0m Text cannot be less than 2 characters long")
        raise InvalidValueError("Text should be at least 2 characters long")
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
def render(colors, text, info, end="\n"):
    # Checking if colors is list
    if not isinstance(colors, list):
        print(f"\033[31m✖\033[0m colors should be strictly list, not {type(colors)}")
        raise InvalidValueError("colors should be list")
    # Checking if text is string
    if not isinstance(text, str):
        print(f"\033[31m✖\033[0m Text requires string to be given, not {type(text)}")
        raise InvalidValueError("Text should be string")
    # Checking if end is string, if not -> convert it to string
    if not isinstance(end, str):
        end = str(end)
    # Checking if colors length are equal to text length
    if len(colors) != len(text):
        print("\033[31m✖\033[0m Colors list and text have different length. Should be equal to each other")
        raise InvalidValueError("Cannot apply colors to text, because colors is shorter/longer than text")
    # Checking every rgb color in colors
    for index, color in enumerate(colors):
        rgb = check_rgb(color)
        if rgb != color:
            colors[index] = rgb
    # Iterate through text length
    for count in range(len(text)):
        # Apply color to character (it is complicated written, I know)
        print(f"\033[38;2;{colors[count][0]};{colors[count][1]};{colors[count][2]}m"+text[count]+"\033[0m", end="")
    # Create space between gradient text and color for each character
    print(end=end)
    if info:
        # Do the same loop
        for count in range(len(text)):
            # Print colored character
            print(f"\033[38;2;{colors[count][0]};{colors[count][1]};{colors[count][2]}m"+text[count]+"\033[0m", end="")
            # Convert rgb color to hexadecimal code
            hex = rgb_to_hex((colors[count][0], colors[count][1], colors[count][2]))
            # Print color as hex and rgb
            print(f" -> #{hex} / ({colors[count][0]}, {colors[count][1]}, {colors[count][2]})")

# make() - apply colors to text
def make(colors, text):
    # Checking if colors is list
    if not isinstance(colors, list):
        print(f"\033[31m✖\033[0m colors should be strictly list, not {type(colors)}")
        raise InvalidValueError("colors should be list")
    # Checking if text is string
    if not isinstance(text, str):
        print(f"\033[31m✖\033[0m Text requires string to be given, not {type(text)}")
        raise InvalidValueError("Text should be string")
    # Checking if colors length is equal to text length
    if len(colors) != len(text):
        print("\033[31m✖\033[0m Colors list and text have different length. Should be equal to each other")
        raise InvalidValueError("Cannot apply colors to text, because colors is shorter/longer than text")
    # Checking if colors length are equal to text length
    for index, color in enumerate(colors):
        rgb = check_rgb(color)
        if rgb != color:
            colors[index] = rgb
    result = ""
    # Add every colored character to result
    for count in range(len(text)):
        result += f"\033[38;2;{colors[count][0]};{colors[count][1]};{colors[count][2]}m"+text[count]+"\033[0m"
    return result

# --=[MAIN]=--
# desc: main functions for program to run

def main():
    if __name__ != "__main__":
        print("\033[33m⚠\033[0m main() function is not recommended to call with another script")
    # Asking for hex-code's and checking for their validation
    firstHex = input("Enter first hex code: #")
    # If check returns true:
    # exit program, else continue
    check_hex(firstHex)
    secondHex = input("Enter last hex code: #")
    check_hex(secondHex)
    text = input("Enter text:\n")

    # Create space between text input field and output
    print()
    # Converting hex to rgb for further usage in code
    colors = (hex_to_rgb(firstHex), hex_to_rgb(secondHex))
    # Generate colors for each character in text
    interColors = interpolate(colors[0], colors[1], text)
    # Rendering gradient
    render(interColors, text, True)

if __name__ == "__main__":
    main()