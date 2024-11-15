# MasterCode Hacking Tool (Cracker_of_Smart_Phone_Parttens)
The MasterCode Hacking Tool is a GUI-based Python application for exploring and visualizing all possible Android-style lock screen patterns. This tool helps users understand the intricacies and variations in lock patterns by cycling through 389,112 unique patterns. Each pattern is visualized on a customizable canvas, and users can navigate between patterns to see all possible combinations.

## Features
- **Pattern Visualization:** The tool draws Android-style lock screen patterns on a grid of nine dots.
- **Complete Pattern Set:** Displays all possible lock patterns, which range from four to nine connected dots.
- **Pattern Navigation:** Includes "Next" and "Previous" buttons for easy navigation between patterns.
- **Customizable Canvas Size:** Users can set the canvas size to their preference, providing flexibility in how patterns are displayed.
- **Pattern Logging:** Each pattern viewed by the user is logged in a patterns_log.txt file for future reference.
- **Pattern Counter:** Displays the current pattern number out of the total patterns, so users can track progress through the set.
- **Large Header Title:** The application window displays a bold title, "MasterCode Hacking Tool," for a professional and identifiable look.

## Installation
This tool is built with Python and requires `tkinter` for the GUI. `tkinter` is included in most Python installations, but if you’re using a lightweight Python installation, you may need to install it separately.

## Requirements:
- Python 3.6+
- `tkinter` library
To check if tkinter is installed, run:

```
python -m tkinter
```

If no errors appear, you’re ready to go! If tkinter is not installed, refer to your operating system's documentation for instructions.

## Usage
1. Clone or download this repository.
2. Run the MasterCode Hacking Tool script:
```
python mastercode_hacking_tool.py
```
3. Upon launching, the tool will prompt you to enter a canvas size (e.g., 600 for a 600x600 window). This controls the size of the lock pattern display.
4. Use the Next and Previous buttons to navigate through patterns. The pattern count at the bottom displays your current position out of 389,112 possible patterns.
5. Each viewed pattern is automatically logged to patterns_log.txt in the script’s directory.
   
## How It Works
This tool uses the `itertools.permutations` method to generate all valid lock screen patterns. Each pattern connects dots on a 3x3 grid without revisiting dots in the same pattern. The generated patterns follow Android’s lock pattern rules, with a minimum length of four and a maximum of nine dots.

The graphical display uses `tkinter.Canvas` to render each pattern by drawing dots and lines connecting them according to each unique sequence.

## License
This project is licensed under the MIT License, allowing for free use, distribution, and modification with proper attribution.

## Contributions
Contributions are welcome! If you'd like to add more features or improve the code, please feel free to open a pull request.

