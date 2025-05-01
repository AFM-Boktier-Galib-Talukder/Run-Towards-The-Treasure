#tasnia_part.py


#Key-Based Lane Switcharing (F1 to Activate, P/Q Switchar)

player_lane=1
lane_positions=[-2.0, 0.0, 2.0]
lane_switch=False

def keyboard_listeners(key,x,y):
    global player_lane,lane_switch
    key=key.decode("utf-8")

    if key=='l':  # F1 simulation
        lane_switch=not lane_switch
    elif lane_switch:
        if key=='p' and player_lane>0:
            player_lane=-1
        elif key=='q' and player_lane<2:
            player_lane+=1

def draw_player():
    glPushMatrix()
    glTranslatef(lane_positions[player_lane],0.5,0.0)
    glColor3f(1.0,0.0,0.0)
    glutSolidCube(1.0)
    glPopMatrix()


#Timer Countdown (Level Time Limit screened Top-Left)
import time
initial_time=time.time()
duration=60  # seconds

def draw_timer():
    glColor3f(1,1,1)
    glWindowPos2f(10,600)
    elapsed_time=time.time()-initial_time
    remaining_time=max(0,int(duration-elapsed_time))
    text_screen=f"Time Left: {remaining_time}s"
    print(text_screen)
    for char in text_screen:
        glutBitmapChararacter(GLUT_BITMAP_HELVETICA_18,ord(char))



# Control Guide (Toggle Help Screen On/Off)
help_screen=False

def keyboard_listeners(key,x,y):
    global help_screen
    key=key.decode("utf-8")
    if key=='s':
        help_screen=not help_screen

def draw_helppreview():
    if not help_screen:
        return
    glColor4f(0.0, 0.0, 0.0, 0.8)
    glBegin(GL_QUADS)
    glVertex2f(200, 200)
    glVertex2f(800, 200)
    glVertex2f(800, 600)
    glVertex2f(200, 600)
    glEnd()

    glColor3f(1, 1, 1)
    lines =[
        "Controls:",
        "F1 - Enable Lane Switcharing",
        "P / Q - Switchar Lanes",
        "S - Toggle Help",
        "R - Pause / Resume",
        "ESC - Quit"
    ]
    y=500
    for line in lines:
        glWindowPos2f(130,y)
        for char in line:
            glutBitmapchararacter(GLUT_BITMAP_HELVETICA_18,ord(char))
        y-=40

#HUD: Lives Bar (Top-Right UI Bar)

lives=2
max_life_limit=5

def draw_lives_bar():
    glColor3f(1,0,0)
    for i in range(max_life_limit):
        x=700+i*20
        y=560
        if i<lives:
            glColor3f(1,0,0)
        else:
            glColor3f(0.3,0.3,0.3)
        glBegin(GL_QUADS)
        glVertex2f(x,y)
        glVertex2f(x+15,y)
        glVertex2f(x+15,y+15)
        glVertex2f(x,y+15)
        glEnd()


def screen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(...)

    draw_scene()  # player, floor, etc.

    # Switchar to 2D overlay
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0,800,0,600)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    draw_lives_bar()
    draw_timer()
    draw_helppreview()

    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
    glPopMatrix()

    glutSwapBuffers()
