from Game import *

g = Game.Instance()
g.start_screen()

while g.__game_playing__:
    g.new()
    g.run()
    g.__game_playing__ = True
