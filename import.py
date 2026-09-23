# --=[HOW TO USE GRADIENT MAKER AS LIBRARY]=--
# desc: every function needed for code to work

# Import gradient maker first
import GradientMaker as gm

# --=[FUNCTIONS]=--
# desc: interview useful functions for your code

# gm.check_hex(hex: string)
# returns -> hex code (in case, it was changed)
# usage: raises InvalidHexError if check failed
# arguments: hex - Hex code to be checked
# exceptions: InvalidHexError

# gm.check_rgb(rgb: tuple)
# returns -> rgb code (in case, some values were changed)
# usage: raises InvalidRGBError if check failed
# arguments: rgb - RGB code to be checked
# exceptions: InvalidRGBError

# gm.hex_to_rgb(hex: string)
# returns -> rgb code
# usage: converts hex code to rgb
# arguments: hex - hex code to be converted
# exceptions: InvalidHexError

# gm.rgb_to_hex(rgb: tuple)
# returns -> hex code
# usage: converts rgb code to hex
# arguments: rgb - rgb code to be converted
# exceptions: InvalidRGBError

# gm.interpolate(firstColor: string/tuple, secondColor: string/tuple, text: string)
# return -> [(RED1, GREEN1, BLUE1), (RED2, GREEN2, BLUE2), ..., (REDn, GREENn, BLUEn)]
# usage: generate colors for characters between first and last code
# arguments: firstColor - first color for text (can be either rgb, either hex)
#            secondColor - last color for text (can be either rgb, either hex)
#            text - just a text
# exceptions: InvalidRGBError, InvalidHexError, InvalidValueError

# gm.make(colors: list, text: string)
# returns -> result: string
# usage: applies colors to text
# arguments: colors - Should be list of rgb values
#            text - just a text
# exceptions: InvalidRGBValue, InvalidValueError

# gm.render(colors: list, text: string, info: boolean, end="\n":string))
# return -> nothing, prints out colored characters
# usage: output color characters
# arguments: colors - Should be list of rgb values
#            text - just a text
#            info - prints every characters color if True
#            end (DEFAULT) - end argument for print functions
# exceptions: InvalidRGBError, InvalidValueError

# --=[EXAMPLE]=--
colors1 = gm.interpolate("#003d4d", "#00c996", "really cool!")
print("This program is ", end="")
gm.render(colors1, "really cool!", False)
colors2 = gm.interpolate((58, 134, 255), (254, 0, 110), "TheEwonh")
TheEwonh = gm.make(colors2, "TheEwonh")
print("by "+TheEwonh)