# Try Not To Crash!

* [1 Summary](#1-summary)  
* [2 How To Play](#2-how-to-play)  
* [3 For Mac OS X / Linux Users](#3-for-mac-os-x--linux-users)   
   * [3.1 Requirements](#31-requirements)

---

## 1 Summary

This personal project is a **Python** (developed in version 3.9) game developed using the **Pygame** library. _Try Not To Crash!_ is a survival game where the player driving a car avoids falling obstacles. The player can drive the vehicle left or right across the screen to dodge the obstacles falling from the sky!

The game features a variety of elements including a _main menu_, a _pause menu_, and _different game modes_. The game modes add to the game's challenge by progressively making the falling blocks _harder to dodge_!

The game also includes _sound effects_ and _background music_, managed using **Pygame**'s mixer module. Its graphics are handled using **Pygame**'s drawing functions and image-loading capabilities!

The game's code is organized and modular, with separate functions for handling different aspects of the game such as _drawing the game objects_, _handling user input_, and _managing the game state_. The code also demonstrates **Pygame**'s event-handling system in response to user actions such as _keyboard inputs_ and _mouse clicks_!

By Quang Hoang

## 2 How To Play

1. Clone the repository (copy the files required to play the game) using a Windows terminal (Command Prompt/Windows PowerShell) or a Mac/Linux terminal:
```
git clone https://github.com/theantigone/Try-Not-To-Crash.git
```
> Alternatively, you could download the files as a ZIP file by clicking the blue **<> Code** Button.

2. Open the `src` folder, then `build` folder inside your new `Try Not To Crash!` folder.
3. Open `exe.win-amd64-3.9`.
4. Open `game.exe`and enjoy!

## 3 For Mac OS X / Linux Users

To run the game on Mac OS X / Linux, navigate to `src`, open your terminal inside that folder, then run:
```bash
python3 game.py
```

You will need to follow section [3.1 Requirements](#31-requirements) to perform the command above.

### 3.1 Requirements

1. **Python** is required. You can download the latest version of Python [here](https://www.python.org/downloads/)!
   - *Pip* should also be installed by default if you installed Python from [python. org](https://www.python.org/)! However, if, for some reason, pip was not installed on your system, refer to [here](https://python.land/virtual-environments/installing-packages-with-pip#Python_Install_Pip) to install pip manually!
2. Python's module **Pygame** is also required. Once you have downloaded Python and pip, install Pygame on your terminal! To do this, run:
   ```bash
   pip3 install pygame
   ```
   Refer to [here](https://www.geeksforgeeks.org/how-to-install-pygame-in-windows/) if you are on Windows, [here](https://www.geeksforgeeks.org/install-pygame-in-linux/) if you are on Linux, or [here](https://www.geeksforgeeks.org/install-pygame-in-macos/) if you are on Mac OS X for more information!
