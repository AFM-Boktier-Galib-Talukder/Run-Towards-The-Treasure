# ---------- START: ROHIT'S PART (MY FEATURES) ----------
score = 0
paused = False
game_over = False
cheat_mode = False
treasures = [(0, -3000, 0)]  # initial treasure to avoid empty list crash
treasure_spawn_timer = 0


def draw_treasures():
    glColor3f(1, 1, 0)
    for (x, y, z) in treasures:
        glPushMatrix()
        glTranslatef(x, y, z)
        gluSphere(gluNewQuadric(), 50, 10, 10)
        glPopMatrix()


def update_rohit_features():
    global score, game_over, treasures, treasure_spawn_timer

    if not Player_running or paused or game_over:
        return

    if not obstacles:
        return  # Avoid crash if obstacles are not yet generated

    px, py, _ = player_pos

    for obs in obstacles:
        ox, oy, _ = obs['position']
        if abs(px - ox) < 300 and abs(py - oy) < 300 and not cheat_mode:
            game_over = True
            return

    new_treasures = []
    for (tx, ty, tz) in treasures:
        if abs(px - tx) < 300 and abs(py - ty) < 300:
            score += 100
        else:
            new_treasures.append((tx, ty, tz))
    treasures[:] = new_treasures

    treasure_spawn_timer += 1
    if treasure_spawn_timer >= 200:
        treasures.append((random.choice([-500, 0, 500]), py - 3000, 0))
        treasure_spawn_timer = 0


def handle_rohit_keys(key):
    global paused, game_over, cheat_mode, score, treasures, player_pos, treasure_spawn_timer
    if key == b'p':
        paused = not paused
    if key == b'r':
        score = 0
        paused = False
        game_over = False
        treasure_spawn_timer = 0
        treasures.clear()
        treasures.append((0, -3000, 0))
        generate_obstacles()
        player_pos[:] = [0, 0, 0]
    if key == b'c':
        cheat_mode = not cheat_mode


def draw_rohit_text():
    if not Player_running:
        draw_text(350, 740, f"Press Space Bar to Play The Game")
    else:
        draw_text(370, 740, f"Press Space Bar to Pause")
    draw_text(800, 770, f"Score: {score}")
    if paused:
        draw_text(400, 400, "PAUSED")
    if game_over:
        draw_text(350, 380, "GAME OVER - Press 'R' to Restart")
    if cheat_mode:
        draw_text(800, 740, "Cheat Mode ON")
    draw_text(30, 570, "Controls: P = Pause | R = Restart | C = Cheat | Space = Start")
# ---------- END: ROHIT'S PART ----------
