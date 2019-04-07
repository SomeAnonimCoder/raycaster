# RAYCASTER
Simple 3d shooter in python based on raycasting
# Idea
look this: https://habr.com/ru/post/439698/
# TL;DR
The main part of this code is GameState.render() - it creates the picture from GameState. 
Gamestate contains state of game: map, player position, etc.
Map is map, no comments.
Image is wrap for PIL(low), python de-facto standart of image processing.
gui.py - main cycle: graphical output, keyboard reading, etc. 
Player is the data class, containing player's position, angles, velociti(in future, maybe).

is a simple 3d render written in python3. It works on classical raycasting algorithm, so there ain`t no suh thing as height or levels. 

# DEPENDENCIES:

*python-keyboard(On Linux you need SUDO to use this!) for reading keyboards 
*PIL(or PILlow - it's much faster!) for image processing 
# NB! you can run this in cpython(default implementation of python) but you`d better use PyPy - it makes this faster and works fine!

# INSTALLATION: 
#cloning git clone https://github.com/someanonimcoder/raycaster 
cd raycaster 
#dependencies sudo pypy3 -m pip install requirements.txt 
#launching sudo pypy3 gui.py
