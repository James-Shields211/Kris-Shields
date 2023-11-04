import pygame
import time
import random
import math

# Initialize pygame
pygame.init()
win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()

# Load the assets (later, when we get into game loops, make sure this is all done
#   before the game loop starts if at all possible)
bg_img = pygame.image.load("Images\\Wood.jpg")
player_ssheet = pygame.image.load("Images\\Princess.jpg")
debug_font = pygame.font.SysFont("Fonts\\Roboto-Thin.ttf", 16)
coin_img = pygame.image.load("Images\\Coin.png")
# From https://opengameart.org/content/16x16-spinning-coin-pickup-animation
font_obj = pygame.font.Font("fonts/Notable-Regular.ttf", 16)

# Some useful constants and intermediate variables
player_ssheet_cell_width = 96
player_ssheet_cell_height = 96
player_speed = 100  # How many pixels do we move if holding down a movement key for one second?
player_frame_delay = 0.05  # How many seconds to pause between steps?
player_animation_time = 0.0  # This "ticks up" each frame.  Once it reaches player_frame_delay, we change the
# player's animation frame (and set this back close to 0.0)
player_diag_speed = (player_speed ** 2 / 2) ** 0.5  # The speed in the horizontal AND vertical direction the player
# moves when moving on a diagonal.  This is so we don't move faster on diagonals.
player_horizontal_speed = 0  # The current speed at which we're moving (in pixels/s) horizontally.  This and...
player_vertical_speed = 0  # are reset every frame, but then set to either player_speed or player_diag_speed
#    if the user is moving the player.
player_bound_radius = 25  # The radius of a bounding circle around player_x, player_y that we use for hits
# with the wall and collectibles


# Some variables that will change over the lifetime of the "game"
player_x = 400
player_y = 400
player_hearts = 0
player_frame = 0
player_direction = 0
player_segment_length = 10  # How many steps do we take before changing directions?
player_segment_length_increment = 1  # Each time we change directions, increase player_segment_length by
#    this amount (giving us the spiral movement we're looking for)
player_steps_so_far = 0  # Once this reaches player_segment_length, we'll change directions
done = False  # When this becomes True (because the princess when outside of the bounds of the screen
#    we'll end the program
debug = True  # Are we in "debug" mode (showing some extra developer-only "stuff")
paused = True
player_score = 0
player_time = 0.0

coin_x = None  # I have the code to set the initial coin position in the game loop (so I can
coin_y = None  # re-use the respawning code when a coin is collected)
coin_frame = None
coin_horizontal_speed = None  # Speed at which the coin is moving horizontally (will be +/- coin_speed)
coin_respawn = True  # If True, respawn the coin
coin_speed = 20  # Speed at which coin moves horizontally without regard to direction
coin_frame_delay = 0.1  # Time in seconds to wait until the coin changes animation frames
coin_animation_time = 0  # Will count up in a similar way to player_animation_time
coin_radius = 8

control_mode = "keyboard"  # Either "keyboard" or "mouse"

# This is the beginnings of a GAME LOOP (the next lecture, covering input and frame rate will make it complete)
while not done:
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # @ UPDATE VARIABLES         @
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # ... this is used for many update operations and input operations.  It indicates the amount of time (in seconds
    #          since I'm dividing by 1000) since the last time we were here (or since the clock was created the first
    #          time we get here)
    delta_time = clock.tick() / 1000.0
    if paused:
        delta_time = 0.0

    # ... add to player time-alive
    player_time += delta_time

    # ... adjust the player speed if they are moving on the diagonal.
    if abs(player_horizontal_speed) > 0 and abs(player_vertical_speed) > 0:
        # player is moving on the diagonal.  We want the sign (positive / negative) for each
        # to remain the same, but use player_diag_speed for the two parts rather than player_speed
        # The math.copysign function works like this: it returns the absolute value of the first
        #     thing multiplied by the sign of the second thing.
        #        math.copy_sign(-213, 50) -> 213
        #        math.copy_sign(118, -13) -> -118
        # I'm using it here to get the sign of the vertical / horizontal speed but multiply it by the diagonal speed
        player_horizontal_speed = math.copysign(player_diag_speed, player_horizontal_speed)
        player_vertical_speed = math.copysign(player_diag_speed, player_vertical_speed)

    # ... use player velocity VECTOR (ask about this term...) to adjust player position
    player_x += player_horizontal_speed * delta_time
    player_y += player_vertical_speed * delta_time

    # ... adjust player direction variable to match movement velocity (do you see why I need to check for
    # diagonals first?)
    if player_horizontal_speed > 0 and player_vertical_speed < 0:
        player_direction = 1
    elif player_horizontal_speed < 0 and player_vertical_speed < 0:
        player_direction = 3
    elif player_horizontal_speed < 0 and player_vertical_speed > 0:
        player_direction = 5
    elif player_horizontal_speed > 0 and player_vertical_speed > 0:
        player_direction = 7
    elif player_horizontal_speed > 0:
        player_direction = 0
    elif player_horizontal_speed < 0:
        player_direction = 4
    elif player_vertical_speed < 0:
        player_direction = 2
    elif player_vertical_speed > 0:
        player_direction = 6

    # ... update the player frame if the player is moving.  Note the clever technique for "wrapping" around
    if abs(player_horizontal_speed) > 0 or abs(player_vertical_speed) > 0:
        player_animation_time += delta_time
        if player_animation_time >= player_frame_delay:
            # (nearly) zero out the timer so we wait roughly another player_frame_delay seconds before
            # changing frames again
            player_animation_time -= player_frame_delay

            # Actually change the frame
            player_frame = (player_frame + 1) % 8

    # ... reset the player velocity.  It may very well be un-reset if the player is still holding down a movement key
    player_horizontal_speed = 0.0
    player_vertical_speed = 0.0

    # ... keep the player on-screen
    if player_x > win_width - player_bound_radius:
        player_x = win_width - player_bound_radius
    if player_x < player_bound_radius:
        player_x = player_bound_radius
    if player_y > win_height - player_bound_radius:
        player_y = win_height - player_bound_radius
    if player_y < player_bound_radius:
        player_y = player_bound_radius

    # ... respawn the coin, if necessary
    if coin_respawn:
        side = random.randint(0, 1)
        if side == 0:
            coin_x = coin_radius
            coin_horizontal_speed = coin_speed
        else:
            coin_x = win_width - coin_radius
            coin_horizontal_speed = -coin_speed
        coin_y = random.randint(coin_radius * 2, win_height - coin_radius * 2)
        coin_frame = 0
        coin_respawn = False

    # ... move the coin
    coin_x += coin_horizontal_speed * delta_time
    if coin_x < coin_radius:
        coin_x = coin_radius
        coin_horizontal_speed = -coin_horizontal_speed
    elif coin_x > win_width - coin_radius:
        coin_x = win_width - coin_radius
        coin_horizontal_speed = -coin_horizontal_speed

    # ... change coin_frames
    coin_animation_time += delta_time
    if coin_animation_time >= coin_frame_delay:
        coin_animation_time -= coin_frame_delay
        coin_frame = (coin_frame + 1) % 7

    # ... check for hits with the player
    coin_player_xdist = player_x - coin_x
    coin_player_ydist = player_y - coin_y
    coin_player_dist = (coin_player_xdist ** 2 + coin_player_ydist ** 2) ** 0.5
    if coin_player_dist <= coin_radius + player_bound_radius:
        coin_respawn = True  # Trigger a respawn next frame
        player_score += 100

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@
    # @ INPUT                   @
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@
    # ... input-handling always starts with this (or one of a few alternatives).  Make sure to only call it once!!
    event = pygame.event.poll()
    # ... do EVENT-HANDLING by looking at the event object
    if event.type == pygame.QUIT:
        done = True
    elif event.type == pygame.KEYDOWN:
        control_mode = "keyboard"
        if event.key == pygame.K_ESCAPE:
            done = True
        elif event.key == pygame.K_F1:
            debug = not debug
        elif event.key == pygame.K_p:
            paused = not paused
    elif event.type == pygame.MOUSEMOTION:
        control_mode = "mouse"
    # ... do DEVICE-POLLING by calling some/all of these functions EVERY FRAME
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    keys_pressed = pygame.key.get_pressed()
    # ...player-movement.  Note: these speed values are adjusted in the update section
    #     if the player is moving on a diagonal.  Also note: player_vertical_speed and player_horizontal_speed
    #     are always zero coming into this code.
    if control_mode == "keyboard":
        if keys_pressed[pygame.K_d] or keys_pressed[pygame.K_RIGHT]:
            player_horizontal_speed += player_speed
        if keys_pressed[pygame.K_a] or keys_pressed[pygame.K_LEFT]:
            player_horizontal_speed -= player_speed
        if keys_pressed[pygame.K_w] or keys_pressed[pygame.K_UP]:
            player_vertical_speed -= player_speed
        if keys_pressed[pygame.K_s] or keys_pressed[pygame.K_DOWN]:
            player_vertical_speed += player_speed
    elif control_mode == "mouse" and mouse_pressed[0]:
        mouse_buffer = 10  # Mouse has to be more than this many pixels from the player
        #   to trigger any movement
        if mouse_pos[0] < player_x - mouse_buffer:
            player_horizontal_speed -= player_speed
        if mouse_pos[0] > player_x + mouse_buffer:
            player_horizontal_speed += player_speed
        if mouse_pos[1] < player_y - mouse_buffer:
            player_vertical_speed -= player_speed
        if mouse_pos[1] > player_y + mouse_buffer:
            player_vertical_speed += player_speed

    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@
    # @ DRAWING                  @
    # @@@@@@@@@@@@@@@@@@@@@@@@@@@@

    # Draw the scene
    # ... background
    win.blit(bg_img, (0, 0))

    # This was optional, but I'm drawing whichever of the coin and player is lower, last.
    if coin_y > player_y:
        # ... player
        win.blit(player_ssheet, (player_x - player_ssheet_cell_width / 2, player_y - player_ssheet_cell_height / 2),
                 (player_frame * player_ssheet_cell_width, player_direction * player_ssheet_cell_height,
                  player_ssheet_cell_width, player_ssheet_cell_height))

        # ... coin
        win.blit(coin_img, (coin_x - coin_radius, coin_y - coin_radius), (coin_frame * 16, 0, 16, 16))
    else:
        # ... coin
        win.blit(coin_img, (coin_x - coin_radius, coin_y - coin_radius), (coin_frame * 16, 0, 16, 16))

        # ... player
        win.blit(player_ssheet, (player_x - player_ssheet_cell_width / 2, player_y - player_ssheet_cell_height / 2),
                 (player_frame * player_ssheet_cell_width, player_direction * player_ssheet_cell_height,
                  player_ssheet_cell_width, player_ssheet_cell_height))

    # ... draw the mark to the screen AND the background
    pygame.draw.rect(win, (0, 255, 0), (player_x - 3, player_y - 3, 6, 6))  # screen
    pygame.draw.rect(bg_img, (0, 255, 0), (player_x - 3, player_y - 3, 6, 6))  # background

    # ... draw the score
    game_text_color = (25, 25, 120)
    text_surf = font_obj.render("Score: " + str(player_score), False, game_text_color)
    win.blit(text_surf, (win_width / 2 - 80, 0))

    # ... draw the time-played
    text_surf = font_obj.render(f"Time played: {player_time:.2f}", False, game_text_color)
    win.blit(text_surf, (win_width / 2 - 130, 20))

    # ... draw the "instructions"
    if control_mode == "keyboard":
        text_surf = font_obj.render("WASD or arrow keys to move", False, game_text_color)
    else:
        text_surf = font_obj.render("hold Left mouse button to move", False, game_text_color)
    win.blit(text_surf, (win_width / 2 - text_surf.get_width() / 2, 40))

    # ... paused
    if paused:
        text_surf = font_obj.render("PAUSED (p to toggle)", False, game_text_color)
        win.blit(text_surf, (win_width / 2 - text_surf.get_width() / 2, 60))

    # ... draw debug items
    if debug:
        # bounding circles
        pygame.draw.circle(win, (0, 255, 0), (player_x, player_y), player_bound_radius, 1)
        pygame.draw.circle(win, (0, 255, 0), (coin_x, coin_y), coin_radius, 1)

        # ... text
        text_x = 0
        text_y = 0
        text_color = (255, 255, 0)
        text_surf = debug_font.render("Player X: " + str(int(player_x)), False, text_color, (0, 0, 0))
        win.blit(text_surf, (text_x, text_y))
        text_y += text_surf.get_height() + 2
        text_surf = debug_font.render("Player Y: " + str(int(player_y)), False, text_color, (0, 0, 0))
        win.blit(text_surf, (text_x, text_y))
        text_y += text_surf.get_height() + 2
        text_surf = debug_font.render(f"Steps: {player_steps_so_far + 1}/{player_segment_length}", False, text_color,
                                      (0, 0, 0))
        win.blit(text_surf, (text_x, text_y))
        text_y += text_surf.get_height() + 2
        text_surf = debug_font.render(f"AnimationFrame: {player_frame}", False, text_color, (0, 0, 0))
        win.blit(text_surf, (text_x, text_y))
        text_y += text_surf.get_height() + 2
        text_surf = debug_font.render(f"Direction: {player_direction}", False, text_color, (0, 0, 0))
        win.blit(text_surf, (text_x, text_y))
        text_y += text_surf.get_height() + 2
        text_surf = debug_font.render(f"Player-Coin Distance: {coin_player_dist:.1f}", False, text_color, (0, 0, 0))
        win.blit(text_surf, (text_x, text_y))
        text_y += text_surf.get_height() + 2

        # ... frame-rate
        text_surf = debug_font.render(f"FPS: {int(clock.get_fps())}", False, (255, 0, 0), (0, 0, 0))
        win.blit(text_surf, (win_width - 200, 0))

    # Show the result.  Note how the time.sleep isn't necessary anymore!
    # time.sleep(player_frame_delay)
    pygame.display.flip()

# Shutdown pygame
pygame.quit()
