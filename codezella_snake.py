import random
import curses

s = curses.initscr() #ecran
curses.curs_set(0) # hide mouse curses 
sh, sw = s.getmaxyx() # set window size
w = curses.newwin(sh, sw, 0, 0) # new window into the main window 
w.keypad(1) # active keypad
w.timeout(100) # refresh window each 100 milisecond

snk_x = sw//4
snk_y = sh//2
snake = [
    [snk_y,snk_x],
    [snk_y,snk_x-1],
    [snk_y,snk_x-2]
]

food = [sh//2, sw//2]
w.addch(food[0], food[1], curses.ACS_PI) # display add food

key = curses.KEY_RIGHT

while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1: ]: # collision frame edges and selfit
        curses.endwin() # end curses if collision ok
        quit()
      

    new_head = [snake[0][0], snake[0][1]] # new snake
    #direction
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1

    snake.insert(0, new_head)

    if snake[0] == food: 
        food = None 
        while food is None: # if there isn't food creat it anywhere 
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None # food must not created in snake body else none create and repeat loop.

        w.addch(food[0], food[1], curses.ACS_PI) # display food on screen 
    else: #snake doesn't eat the food
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)