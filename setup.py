import cx_Freeze

executables = [cx_Freeze.Executable('game.py')]

cx_Freeze.setup(
    name='Try Not To Crash!',
    options={'build_exe': {'packages': ['pygame'],
                           'include_files': ['car.png', 'car_icon.png', 'instructions_background.jpg',
                                             'main_menu_background.jpg', 'crash.mp3', 'music.mp3', 'background.jpg'],
                           'excludes': ['tkinter', 'numpy', 'pandas', 'matplotlib', 'scipy', 'sklearn', 'seaborn',
                                       'statsmodels']}},
    executables=executables
)
