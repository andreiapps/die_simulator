# Die Simulator
Die Simulator is a mobile app made in Python with the Kivy framework that simulates a die. I might add more features later.

![Die Simulator](fastlane/metadata/android/en-US/images/icon.png)

## Running locally
1. Install [Python](https://python.org/download) and [Git](https://git-scm.com/install)
2. Clone the repo:
   ```bash
   git clone https://github.com/andreiapps/die_simulator
   cd die_simulator
   ```
3. Install Kivy:
   ```bash
   pip install kivy
   ```
   or
   ```bash
   pip3 install kivy
   ```
4. Run the app:
   ```bash
   python main.py
   ```
   or
   ```bash
   python3 main.py
   ```

## Building
Follow the steps above, then also:
1. Install buildozer using the [Installation Guide](https://buildozer.readthedocs.io/en/latest/installation.html)
2. Build the app:
   To build for Android:
   ```bash
   buildozer android debug
   ```
   or to build for iOS:
   ```bash
   buildozer ios debug
   ```

## Planned features
- Ability to customize the number of dice
- Ability to customize the color of the dice
- Ability to customize the color of the dots on the dice

## License
This program is licensed under the GPL-v3 license
