from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

#............................................
GRID_LENGTH = 400  
fovY = 80
#...........................................
Player_running=False
player_pos = [0, 0, 0]  
player_rotation = 0    
player_speed = 5 
#...........................................
camera_pos = (0,550,450) 
camera_angle = 0 
camera_distance = 500
fpp_mode = False
tpp_camera_pos = (0,550,450) 
#..................................
Male = True
I=False 
O=True 
P=False 
D=False
#..........................................
obstacles = []
num_obstacles = 20  
obstacle_size = 600  

#.................................................

def draw_text(x, y, text, font=GLUT_BITMAP_HELVETICA_18):
    glColor3f(1,1,1)
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    
    gluOrtho2D(0, 1000, 0, 800) 

    
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()
    

    glRasterPos2f(x, y)
    for ch in text:
        glutBitmapCharacter(font, ord(ch))

    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)


def draw_player():
    if Male:
        glPushMatrix()  
        
        
        glTranslatef(player_pos[0], player_pos[1], player_pos[2])
        glRotatef(-player_rotation, 0, 0, 1)  
    

        # Shoes
        glColor3f(0,0,0)
        glPushMatrix()
        glTranslatef(-50,-50, 0)
        glutSolidCube(50)
        glTranslatef(0, 50, 0)
        glutSolidCube(50)

        glTranslatef(100, 0, 0)
        glutSolidCube(50)
        glTranslatef(0, -50, 0)
        glutSolidCube(50)
        glPopMatrix()

        # Legs
        if O==True:
            glColor3f(0.702,0.71,0.741)
        elif I==True:
            glColor3f(0.541, 0.239, 0.035)
        elif P==True:
            glColor3f(0.659, 0.267, 0)
        glPushMatrix()
        glTranslatef(-50, 0, 25)
        gluCylinder(gluNewQuadric(), 30, 30, 130, 10, 10)
        glTranslatef(100, 0, 0)
        gluCylinder(gluNewQuadric(), 30, 30, 130, 10, 10)
        glPopMatrix()
        
        if P==True:
            glColor3f(0.631, 0.043, 0.043)
            glPushMatrix()
            glTranslatef(-45, 0, 125)
            glutSolidCube(60)
            glTranslatef(45, 0,0)
            glutSolidCube(60)
            glTranslatef(45, 0,0)
            glutSolidCube(60)
            glPopMatrix()
        elif I==True:
            glPushMatrix()
            glColor3f(0.541, 0.239, 0.035)
            glTranslatef(-45, 0,50)
            glutSolidCube(60)
            glTranslatef(45, 0,0)
            glutSolidCube(60)
            glTranslatef(45, 0,0)
            glutSolidCube(60)

            glColor3f(0,0,0)
            glTranslatef(-90, 0, 60) 
            glutSolidCube(60)
            glTranslatef(45, 0,0)
            glutSolidCube(60)
            glTranslatef(45, 0,0)
            glutSolidCube(60)

            glPopMatrix()

        # Pant + Body
        glPushMatrix()
        if P==True:
            glColor3f(0.631, 0.043, 0.043)
        elif I==True:
            glColor3f(0.541, 0.239, 0.035)
        glTranslatef(-45, 0, 175)
        glutSolidCube(60)
        glTranslatef(45, 0,0)
        glutSolidCube(60)
        glTranslatef(45, 0,0)
        glutSolidCube(60)

        if O==True:
            glColor3f(0.929,0.400,0.102)
        elif I==True:
            glColor3f(0.11, 0.839, 0.91)
        elif P==True:
            glColor3f(0.631, 0.043, 0.043)
        
        glTranslatef(-90, 0, 60) 
        glutSolidCube(60)
        glTranslatef(45, 0,0)
        glutSolidCube(60)
        glTranslatef(45, 0,0)
        glutSolidCube(60)

        glTranslatef(-90, 0, 50)
        glutSolidCube(60)
        glTranslatef(45, 0,0)
        glutSolidCube(60)
        glTranslatef(45, 0,0)
        glutSolidCube(60)

        glPopMatrix()

        # Arms + Hands
        glPushMatrix()
        glColor3f(1, 1, 0.8) 
        glTranslatef(-105, 0, 205) 
        gluSphere(gluNewQuadric(), 20, 10, 10)  
        glTranslatef(0, 0,15)  
        if O==True:
            glColor3f(0.929,0.400,0.102)
        elif I==True:
            glColor3f(0.11, 0.839, 0.91)
        elif P==True:
            glColor3f(0.631, 0.043, 0.043) 
        gluCylinder(gluNewQuadric(), 20, 20, 100, 10, 10)

        glTranslatef(210, 0,-15)  
        glColor3f(1, 1, 0.8) 
        gluSphere(gluNewQuadric(), 20, 10, 10) 
        glTranslatef(0, 0, 15) 
        if O==True:
            glColor3f(0.929,0.400,0.102)
        elif I==True:
            glColor3f(0.11, 0.839, 0.91)
        elif P==True:
            glColor3f(0.631, 0.043, 0.043) 
        gluCylinder(gluNewQuadric(), 20, 20, 100, 10, 10)
        glPopMatrix()
        
        # Head 
        glPushMatrix()
        glColor3f(1, 1, 0.8)
        glTranslatef(0, 0, 355)
        glutSolidCube(70)

        glColor3f(0.3,0.3,0.3)
        glTranslatef(0, 10,0)
        glutSolidCube(65)
        glPopMatrix()
        
        glPopMatrix() 

    else:
        glPushMatrix()  
    
        
        glTranslatef(player_pos[0], player_pos[1], player_pos[2])
        glRotatef(-player_rotation, 0, 0, 1) 
        

        # Shoes
        glColor3f(0,0,0)
        glPushMatrix()
        glTranslatef(-50,-50, 0)
        glutSolidCube(50)
        glTranslatef(0, 50, 0)
        glutSolidCube(50)

        glTranslatef(100, 0, 0)
        glutSolidCube(50)
        glTranslatef(0, -50, 0)
        glutSolidCube(50)
        glPopMatrix()

        # skirt
        if I== False:
            if O==True:
                glColor3f(0.929,0.500,0.102)
            elif P==True:
                glColor3f(0.965, 0, 1)
            glPushMatrix()
            glTranslatef(0,0, 30)
            gluCylinder(gluNewQuadric(), 200, 30, 230, 10, 10)
            glPopMatrix()
        elif I ==True:
            glPushMatrix()
            glTranslatef(0,0, 50)
            glColor3f(0,0.78,0.91)
            gluCylinder(gluNewQuadric(),80,80, 30, 10, 10)

            glTranslatef(0,0, 30)
            glColor3f(0.929,0.500,0.102)
            gluCylinder(gluNewQuadric(),80,80, 30, 10, 10)

            glTranslatef(0,0, 30)
            glColor3f(0,0.78,0.91)
            gluCylinder(gluNewQuadric(),80,80, 30, 10, 10)

            glTranslatef(0,0, 30)
            glColor3f(0.929,0.500,0.102)
            gluCylinder(gluNewQuadric(),80,80, 30, 10, 10)

            glTranslatef(0,0, 30)
            glColor3f(0,0.78,0.91)
            gluCylinder(gluNewQuadric(),80,80, 30, 10, 10)

            glTranslatef(0,0, 30)
            glColor3f(0.929,0.500,0.102)
            gluCylinder(gluNewQuadric(),80,80, 40, 10, 10)

            glPopMatrix()

        
        #Body
        if I==True or O==True:
            glPushMatrix()
            glColor3f(0,0.78,0.91)
            if O==True:
                glColor3f(0.929,0.300,0.102)
            glTranslatef(-35, 0, 240) 
            glutSolidCube(60)
            glTranslatef(35, 0,0)
            glutSolidCube(60)
            glTranslatef(35, 0,0)
            glutSolidCube(60)

            glTranslatef(-70, 0, 50)
            glutSolidCube(60)
            glTranslatef(35, 0,0)
            glutSolidCube(60)
            glTranslatef(35, 0,0)
            glutSolidCube(60)
            
            glPopMatrix()
        elif P==True:
            glPushMatrix()
            glTranslatef(0, 0,215)
            glColor3f(1, 0, 0.722)
            gluCylinder(gluNewQuadric(),50,100, 110, 10, 10)
            glPopMatrix()


        if O==True:
            glPushMatrix()
            glTranslatef(0, 0,90)
            glColor3f(0.929,0.400,0.102)
            gluCylinder(gluNewQuadric(),190,25, 160, 10, 10)

            glTranslatef(0, 0,60)
            glColor3f(0.929,0.300,0.102)
            gluCylinder(gluNewQuadric(),180,40, 80, 10, 10)
            glPopMatrix()
        if I == True:
            glPushMatrix()
            glTranslatef(25, 0,250)
            glRotatef(90, 0, 1, 0)
            glColor3f(0.929,0.400,0.102)
            gluCylinder(gluNewQuadric(),75, 75, 40, 10, 10)

            glTranslatef(0,0,-55)
            glRotatef(315, 0, 1, 0)
            glColor3f(0.929,0.400,0.102)
            gluCylinder(gluNewQuadric(),75, 75, 40, 10, 10)
            glPopMatrix()





        # Arms + Hands
        glPushMatrix()
        glColor3f(1, 1, 0.8) 
        glTranslatef(-95, 0, 205) 
        gluSphere(gluNewQuadric(), 20, 10, 10)  
        glTranslatef(0, 0,15)  
        glColor3f(0,0.78,0.91)
        if P== True:
            glColor3f(1, 0, 0.722)  
        elif O==True:
            glColor3f(0.929,0.300,0.102) 
        gluCylinder(gluNewQuadric(), 20, 20, 100, 10, 10)

        glTranslatef(190, 0,-15)  
        glColor3f(1, 1, 0.8) 
        gluSphere(gluNewQuadric(), 20, 10, 10) 
        glTranslatef(0, 0, 15) 
        glColor3f(0,0.78,0.91)  
        if P== True:
            glColor3f(1, 0, 0.722) 
        elif O==True:
            glColor3f(0.929,0.300,0.102)
        gluCylinder(gluNewQuadric(), 20, 20, 100, 10, 10)
        glPopMatrix()
        
        # Head 
        glPushMatrix()
        glColor3f(1, 1, 0.8)
        glTranslatef(0, 0, 355)
        glutSolidCube(60)

        glColor3f(0.3,0.3,0.3)
        glTranslatef(0, 10,0)
        glutSolidCube(55)

        glColor3f(0.2,0.2,0.2)
        glTranslatef(0, 40,0) 
        gluCylinder(gluNewQuadric(), 10, 22,41, 10, 10)


        glPopMatrix()
        
        glPopMatrix()  



def keyboardListener(key, x, y):
    global Player_running, Male, I, O, P, camera_pos, camera_angle, camera_distance, fpp_mode, tpp_camera_pos, player_pos, player_rotation,D
                
    if key == b' ':
        Player_running = not Player_running
        D = False

    key = key.decode('utf-8').lower()
    if key == 'x' and Player_running == False:
        Male = not Male
    if key == 'i' and Player_running == False:
        I=True
        O=False
        P=False
    if key == 'o' and Player_running == False:
        I=False
        O=True
        P=False
    if key == 'p' and Player_running == False:
        I=False
        O=False
        P=True
    if key == 'd' and Player_running == False:
        D = not D

    px, py, pz = player_pos 
    
    if key =='j':
        fpp_mode = not fpp_mode
        if not fpp_mode:
            
            camera_angle = player_rotation  
            rad = math.radians(camera_angle)
            x = px + camera_distance * math.sin(rad)
            y = py + camera_distance * math.cos(rad)
            z = tpp_camera_pos[2]  
            camera_pos = (x, y, z)
            tpp_camera_pos = camera_pos
    
    if fpp_mode==False:
        if key =='h':
            tpp_camera_pos = (tpp_camera_pos[0], tpp_camera_pos[1], tpp_camera_pos[2] + 50)
        if key == 'n':
            tpp_camera_pos = (tpp_camera_pos[0], tpp_camera_pos[1], tpp_camera_pos[2] - 50)
        if key == 'm':
            camera_angle += 5   
        if key == 'b':
            camera_angle -= 5 

        camera_angle %= 360
        rad = math.radians(camera_angle)
        x = px + camera_distance * math.sin(rad)
        y = py + camera_distance * math.cos(rad)
        z = tpp_camera_pos[2]  
        camera_pos = (x, y, z)
        tpp_camera_pos = camera_pos
        
            
       


def setupCamera():
    """
    Configures the camera's projection and view settings.
    Uses a perspective projection and positions the camera to look at the target.
    """
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity()  
    gluPerspective(fovY, 1.25, 0.1, 10000) 
    glMatrixMode(GL_MODELVIEW) 
    glLoadIdentity() 
    
    px, py, pz = player_pos  
    
    if fpp_mode:

        rad = math.radians(player_rotation)
        camera_x = px - 40 * math.sin(rad)  
        camera_y = py - 40 * math.cos(rad)
        camera_z = pz + 350  
        
       
        lookAt_x = px - 500 * math.sin(rad)
        lookAt_y = py - 500 * math.cos(rad)
        lookAt_z = camera_z  
        
        gluLookAt(camera_x, camera_y, camera_z, 
                 lookAt_x, lookAt_y, lookAt_z,     
                 0, 0, 1)                      
    else:
        
        x, y, z = camera_pos
        gluLookAt(x, y, z, 
                 px, py, pz + 200,  
                 0, 0, 1)

def game_floor():
    glBegin(GL_QUADS)
    grid_size = GRID_LENGTH
    
    for i in range(-2,2):
        for j in range(-50, 4):
            if (i + j) % 2 == 0:
                glColor3f(0.65,0.47,0.28)
            else:
                glColor3f(0.79,0.67,0.46)
            
          
            x = i * grid_size
            y = j * grid_size
            glVertex3f(x, y, 0)
            glVertex3f(x + grid_size, y, 0)
            glVertex3f(x + grid_size, y + grid_size, 0)
            glVertex3f(x, y + grid_size, 0)
    glEnd()




def generate_obstacles():
    global obstacles
    obstacles = []
    y =  -500 
    y_decrement = 2000  
    
    for _ in range(num_obstacles):
        
        y -= y_decrement
        
        x = random.choice([-500,0,500])
        
        z = random.choice([0, 500])
        
        # Random color for the obstacles ..... if needed
        #color = (random.uniform(0.1,0.5 ), random.uniform(0.1,0.5), random.uniform(0.1,0.5))
        color = (0.36, 0.2, 0.09)
        
        obstacles.append({
            'position': [x, y, z],
            'size': obstacle_size,
            'color': color
        })

def draw_obstacles():
    for obstacle in obstacles:
        glPushMatrix()
        glTranslatef(*obstacle['position'])
        glColor3f(*obstacle['color'])
        glutSolidCube(obstacle['size'])
        glPopMatrix()


def idle():
    """
    Idle function that runs continuously:
    - Updates player and camera positions when running
    - Triggers screen redraw for real-time updates.
    """
    global player_pos, camera_pos, tpp_camera_pos
    
    if Player_running:
        
        rad = math.radians(player_rotation)
        dx = player_speed * math.sin(rad)
        dy = player_speed * math.cos(rad)
        
       
        player_pos[0] -= dx
        player_pos[1] -= dy
        
        
        if not fpp_mode:  
            cam_x, cam_y, cam_z = camera_pos
            camera_pos = (cam_x - dx, cam_y - dy, cam_z)
            tpp_camera_pos = (tpp_camera_pos[0] - dx, tpp_camera_pos[1] - dy, tpp_camera_pos[2])
    
    glutPostRedisplay()


def showScreen():
    """
    Display function to render the game scene:
    - Clears the screen and sets up the camera.
    - Draws everything of the screen
    """
  
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()  
    glViewport(0, 0, 1000, 800)  

    setupCamera()  


    
    game_floor()
    draw_obstacles()


    if D:
        draw_text(30, 720, f"X =  (Male / Female)")
        draw_text(30, 690, f"For Male, I = Fotua & Lungi , O = Shirt & Pant , P = Panjabi & Payjama")
        draw_text(30, 660, f"For Female, I = Sari , O = Gown , P = Princess dress")
        draw_text(30, 630, f"J =  (TPP / FPP) ")
        draw_text(30, 600, f"H = upper view, N = lower view, M = Right Rotation, B = Left Rotation ")

    if (Player_running == False):
        draw_text(350, 740, f"Press Space Bar to Play The Game")

    else:
        draw_text(370, 740, f"Press Space Bar to Pause")

    draw_player()

    glutSwapBuffers()



def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH) 
    glutInitWindowSize(1000, 800)  
    glutInitWindowPosition(0, 0) 
    wind = glutCreateWindow(b"3D OpenGL Intro") 
    glClearColor(0.7,0.7,0.7, 1.0) 
    generate_obstacles()

    glutDisplayFunc(showScreen)  
    glutKeyboardFunc(keyboardListener)  
    glutSpecialFunc(specialKeyListener)
    #glutMouseFunc(mouseListener)
    glutIdleFunc(idle)  

    glutMainLoop() 

if __name__ == "__main__":
    main()
