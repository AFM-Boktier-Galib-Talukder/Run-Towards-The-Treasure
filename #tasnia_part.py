#tasnia_part.py






####Timer Countdown (Level Time Limit screened Top-Left)
import time
start_time = None
countdown_duration = 60  # seconds for countdown
 # seconds

#in the keyboardListener function
if key == b' ':
    Player_running = not Player_running
    D = False
    global start_time
    if Player_running and start_time is None:
        start_time = time.time()


#inside drawdraw_rohit_text() 
    if start_time and Player_running:
        elapsed = int(time.time() - start_time)
        remaining = max(0, countdown_duration - elapsed)
        draw_text(800, 710, f"Time Left: {remaining}s")
        if remaining == 0:
            game_over = True




def draw_timer():
    glColor3f(1,1,1)
    glWindowPos2f(10,600)
    elapsed_time=time.time()-initial_time
    remaining_time=max(0,int(duration-elapsed_time))
    text_screen=f"Time Left: {remaining_time}s"
    print(text_screen)
    for char in text_screen:
        glutBitmapChararacter(GLUT_BITMAP_HELVETICA_18,ord(char))




####HUD: Lives Bar (Top-Right UI Bar)

lives=2
max_life_limit=5

#update_rohit_features() replace with
if abs(px - ox) < 300 and abs(py - oy) < 300 and not cheat_mode:
    lives -= 1
    if lives <= 0:
        game_over = True
    else:
        player_pos[:] = [0, player_pos[1] + 1000, 0]  # knockback
    return

#under draw_rohit_text() 
def draw_lives_bar():
    glColor3f(1, 0, 0)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, 1000, 0, 800)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    # Lives bar background
    glColor3f(0.2, 0.2, 0.2)
    glBegin(GL_QUADS)
    glVertex2f(50, 760)
    glVertex2f(250, 760)
    glVertex2f(250, 730)
    glVertex2f(50, 730)
    glEnd()

    # Filled portion (2 units width per life)
    glColor3f(0, 1, 0)
    bar_width = 200 * (lives / max_lives)
    glBegin(GL_QUADS)
    glVertex2f(50, 760)
    glVertex2f(50 + bar_width, 760)
    glVertex2f(50 + bar_width, 730)
    glVertex2f(50, 730)
    glEnd()

    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

#call this inside showScreen()
draw_lives_bar()


###Distance Tracker

#add global 
distance_travelled = 0

#update idle() function after  player_pos[1] -= dy

distance_travelled = abs(player_pos[1]) // 10

# in draw_rohit_text() after timer text
draw_text(800, 690, f"Distance: {distance_travelled} m")


####Obstacle movement:

obstacle_movement_direction = {}  # index → -1 or 1
obstacle_movement_range = 100     # max offset range
obstacle_movement_speed = 2       # how fast they shift


def generate_obstacles():
    global obstacles, obstacle_movement_direction
    obstacles = []
    obstacle_movement_direction = {}

    y = -500
    y_decrement = 2000

    for i in range(num_obstacles):
        y -= y_decrement
        x = random.choice([-500, 0, 500])
        z = random.choice([0, 500])
        color = (0.36, 0.2, 0.09)

        obstacles.append({
            'id': i,
            'position': [x, y, z],
            'size': obstacle_size,
            'color': color
        })
        obstacle_movement_direction[i] = random.choice([-1, 1])

