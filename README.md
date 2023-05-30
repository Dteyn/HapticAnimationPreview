# Haptic Animation Preview
Haptic Animation Preview is a Python script that simulates haptic animations from OpenVrChatHapticFeedback by generating sound representations based on JSON data. The script provides a preview of haptic patterns and allows users to select and play different animations.

For more information on OpenVrChatHapticFeedback, see alextrof94's repository here:
https://github.com/alextrof94/OpenVRChatHapticFeedback/

## Features
- Loads haptic animation data from a JSON file.
- Plays sound representations of haptic patterns based on the animation data.
- Allows users to select an animation from a menu and play a preview.

## How it Works
- The script reads haptic animation data from a JSON file, which provides details about different haptic animations.
- The user is presented with a menu of available animations to choose from.
- Upon selecting an animation, the script generates sound representations that simulate the haptic patterns described in the JSON file.
- The selected animation is played, and the script adjusts volume and duration accordingly.
- After each preview, the user is returned to the menu to select another animation or can choose to exit the script.

## Requirements
- Python 3.x
- Pygame library

# Usage
- Ensure Python 3.x is installed on your system.
- Install the Pygame library by running the following command: pip install pygame.
- Clone or download the Haptic Animation Preview repository.
- Place your haptic animation data in a JSON file following the provided format.
- Update the script with the correct file path of your JSON file.
- Customize the sound files and adjust the script according to your haptic animation requirements.
- Run the script using Python: `python HapticAnimationPreview.py`
- Follow the on-screen instructions to select and preview different haptic animations.
- Press 'q' to exit the script.

## Contributing
Contributions to this project are welcome! If you encounter any issues, have suggestions, or would like to add new features, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
