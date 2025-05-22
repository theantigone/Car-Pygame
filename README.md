# Racing Car Pygame

* [1 Synopsis](#1-synopsis)  
* [2 How To Play](#2-how-to-play)  
* [3 For Mac OS X / Linux Users](#3-for-mac-os-x--linux-users)   
   * [3.1 Requirements](#31-requirements)

---

## 1 Synopsis

This personal project is a Python (developed in version 3.9) game developed using the Pygame library. "Try Not To Crash!" is a survival game where the player driving a car avoids falling obstacles. The player can drive the vehicle left or right across the screen to dodge the obstacles falling from the sky!

The game features a variety of elements including a main menu, a pause menu, and different game modes. The game modes add to the game's challenge by progressively making the falling blocks harder to dodge!

The game also includes sound effects and background music, managed using Pygame's mixer module. Its graphics are handled using Pygame's drawing functions and image-loading capabilities!

The game's code is organized and modular, with separate functions for handling different aspects of the game such as drawing the game objects, handling user input, and managing the game state. The code also demonstrates Pygame's event-handling system in response to user actions such as keyboard inputs and mouse clicks!

By Quang Hoang

## 2 How To Play

1. Clone the repository (copy the files required to play the game) using a Windows terminal (Command Prompt/Windows PowerShell) or a Mac/Linux terminal:
```
git clone https://github.com/theantigone/Car-Pygame.git
```
   - Alternatively, you could download the files as a ZIP file by clicking the blue **<> Code** Button.
2. Open the **src**, then **build** folder inside your new **Car-Pygame** folder.
3. Open **exe.win-amd64-3.9**.
4. Open **game.exe**, and enjoy!

## 3 For Mac OS X / Linux Users

To run the game on Mac OS X / Linux, navigate to `src`, open your terminal inside that folder, then run:
```bash
python3 game.py
```

You will need to follow section **3.1 Requirements** to perform the command above.

### 3.1 Requirements

1. **Python** is required. You can download the latest version of Python [here](https://www.python.org/downloads/)!
   - *Pip* should also be installed by default if you installed Python from [python. org](https://www.python.org/)! However, if, for some reason, pip was not installed on your system, refer to [here](https://python.land/virtual-environments/installing-packages-with-pip#Python_Install_Pip) to install pip manually!
2. Python's module **Pygame** is also required. Once you have downloaded Python and pip, install Pygame on your terminal! To do this, run:
   ```bash
   pip3 install pygame
   ```
   Refer to [here](https://www.geeksforgeeks.org/how-to-install-pygame-in-windows/) if you are on Windows, [here](https://www.geeksforgeeks.org/install-pygame-in-linux/) if you are on Linux, or [here](https://www.geeksforgeeks.org/install-pygame-in-macos/) if you are on Mac OS X for more information!
