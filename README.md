# Gradient Maker
![GradientMaker.py](https://cdn.discordapp.com/attachments/1531949987557146695/1551676184792924290/image.png?ex=6ab2d68f&is=6ab1850f&hm=e6be004764a8a7b9810efb98a24cee080a4958389479bda5a61c4f8c68f100b8&)


Simple program to apply gradient to text using as little code as possible
## Usage

Requirements:
- Python 3.6 or higher
- A desire to launch this code

Run the program with:
```bash
  python GradientMaker.py
```

## Usage as a library
![import.py](https://cdn.discordapp.com/attachments/1531949987557146695/1552248352740085871/image.png?ex=6ab4eb6e&is=6ab399ee&hm=0fdb8eb86ae627a586ec021aa3b2130e057224e6927e41e08f089d4b695470b9&)

Import GradientMaker into your code with:
```python
import GradientMaker as gm
```
Functions:

- `gm.check_hex(hex)` - Check hex for validation
- `gm.check_rgb(rgb)` - Check rgb for validation
- `gm.hex_to_rgb(hex)` - Convert hex to rgb
- `gm.rgb_to_hex(rgb)` - Convert rgb to hex
- `gm.interpolate(firstRGB, secondRGB, text)` - Generate colors for each character of text
- `gm.make(colors, text)` - Apply every generated color to text
- `gm.render(colors, text, info, end)` - Output colored text with information for each character if info is set to true

See import.py for details and example
## FAQ

#### Q1. Can I modify `GradientMaker.py`?
Yes. If you commit a modified version, leave `# [MODIFIED]` tag on the first line

#### Q2. Can I use GradientMaker in my own projects?
Yes. You can import `GradientMaker` and use its functions in your own projects

#### Q3. Why does my gradient look different from the expected result?
Make sure your terminal supports ANSI truecolor (24-bit color)