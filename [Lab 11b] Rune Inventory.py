# ETGG1801 Kris Shields Lab 11B



# import all of the things to ever exist
import sys
import pygame
pygame.init()
pygame.font.init()

# Import Rune list
runes = (pygame.image.load("Images\\runeBlack_tile_001.png"), pygame.image.load("Images\\runeBlack_tile_002.png"),
         pygame.image.load("Images\\runeBlack_tile_003.png"), pygame.image.load("Images\\runeBlack_tile_004.png"),
         pygame.image.load("Images\\runeBlack_tile_005.png"), pygame.image.load("Images\\runeBlack_tile_006.png"),
         pygame.image.load("Images\\runeBlack_tile_007.png"), pygame.image.load("Images\\runeBlack_tile_008.png"),
         pygame.image.load("Images\\runeBlack_tile_009.png"), pygame.image.load("Images\\runeBlack_tile_010.png"),
         pygame.image.load("Images\\runeBlack_tile_011.png"), pygame.image.load("Images\\runeBlack_tile_012.png"),
         pygame.image.load("Images\\runeBlack_tile_013.png"), pygame.image.load("Images\\runeBlack_tile_014.png"),
         pygame.image.load("Images\\runeBlack_tile_015.png"), pygame.image.load("Images\\runeBlack_tile_016.png"),
         pygame.image.load("Images\\runeBlack_tile_017.png"), pygame.image.load("Images\\runeBlack_tile_018.png"),
         pygame.image.load("Images\\runeBlack_tile_019.png"), pygame.image.load("Images\\runeBlack_tile_020.png"),
         pygame.image.load("Images\\runeBlack_tile_021.png"), pygame.image.load("Images\\runeBlack_tile_022.png"),
         pygame.image.load("Images\\runeBlack_tile_023.png"), pygame.image.load("Images\\runeBlack_tile_024.png"),
         pygame.image.load("Images\\runeBlack_tile_025.png"), pygame.image.load("Images\\runeBlack_tile_026.png"),
         pygame.image.load("Images\\runeBlack_tile_027.png"), pygame.image.load("Images\\runeBlack_tile_028.png"),
         pygame.image.load("Images\\runeBlack_tile_029.png"), pygame.image.load("Images\\runeBlack_tile_030.png"),
         pygame.image.load("Images\\runeBlack_tile_031.png"), pygame.image.load("Images\\runeBlack_tile_032.png"),
         pygame.image.load("Images\\runeBlack_tile_033.png"), pygame.image.load("Images\\runeBlack_tile_034.png"),
         pygame.image.load("Images\\runeBlack_tile_035.png"), pygame.image.load("Images\\runeBlack_tile_036.png"))

# Declare rescaled runes
resc_ht = (19 + (53 / 63))
resc_wdth = (22 + (2 / 9))
rescale001 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_001.png"), (resc_wdth, resc_ht))
rescale002 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_002.png"), (resc_wdth, resc_ht))
rescale003 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_003.png"), (resc_wdth, resc_ht))
rescale004 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_004.png"), (resc_wdth, resc_ht))
rescale005 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_005.png"), (resc_wdth, resc_ht))
rescale006 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_006.png"), (resc_wdth, resc_ht))
rescale007 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_007.png"), (resc_wdth, resc_ht))
rescale008 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_008.png"), (resc_wdth, resc_ht))
rescale009 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_009.png"), (resc_wdth, resc_ht))
rescale010 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_010.png"), (resc_wdth, resc_ht))
rescale011 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_011.png"), (resc_wdth, resc_ht))
rescale012 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_012.png"), (resc_wdth, resc_ht))
rescale013 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_013.png"), (resc_wdth, resc_ht))
rescale014 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_014.png"), (resc_wdth, resc_ht))
rescale015 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_015.png"), (resc_wdth, resc_ht))
rescale016 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_016.png"), (resc_wdth, resc_ht))
rescale017 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_017.png"), (resc_wdth, resc_ht))
rescale018 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_018.png"), (resc_wdth, resc_ht))
rescale019 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_019.png"), (resc_wdth, resc_ht))
rescale020 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_020.png"), (resc_wdth, resc_ht))
rescale021 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_021.png"), (resc_wdth, resc_ht))
rescale022 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_022.png"), (resc_wdth, resc_ht))
rescale023 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_023.png"), (resc_wdth, resc_ht))
rescale024 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_024.png"), (resc_wdth, resc_ht))
rescale025 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_025.png"), (resc_wdth, resc_ht))
rescale026 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_026.png"), (resc_wdth, resc_ht))
rescale027 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_027.png"), (resc_wdth, resc_ht))
rescale028 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_028.png"), (resc_wdth, resc_ht))
rescale029 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_029.png"), (resc_wdth, resc_ht))
rescale030 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_030.png"), (resc_wdth, resc_ht))
rescale031 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_031.png"), (resc_wdth, resc_ht))
rescale032 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_032.png"), (resc_wdth, resc_ht))
rescale033 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_033.png"), (resc_wdth, resc_ht))
rescale034 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_034.png"), (resc_wdth, resc_ht))
rescale035 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_035.png"), (resc_wdth, resc_ht))
rescale036 = pygame.transform.scale(pygame.image.load("Images\\runeBlack_tile_036.png"), (resc_wdth, resc_ht))
arrow_orig = pygame.image.load("Images\\right_arrow.png")
arrow = pygame.transform.scale(arrow_orig, (55, 50))
font_obj = pygame.font.Font("Fonts\\Roboto-Thin.ttf", 15)

# draw window
pygame.init()
win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))

# variables for each type of rune
A_runes = 0
B_runes = 0
C_runes = 0
D_runes = 0
E_runes = 0
F_runes = 0
G_runes = 0
H_runes = 0
I_runes = 0
J_runes = 0
K_runes = 0
L_runes = 0
M_runes = 0
N_runes = 0
O_runes = 0
P_runes = 0
Q_runes = 0
R_runes = 0
S_runes = 0
T_runes = 0
U_runes = 0
V_runes = 0
W_runes = 0
X_runes = 0
Y_runes = 0
Z_runes = 0
Zero_runes = 0
One_runes = 0
Two_runes = 0
Three_runes = 0
Four_runes = 0
Five_runes = 0
Six_runes = 0
Seven_runes = 0
Eight_runes = 0
Nine_runes = 0
rune_counts = [A_runes, B_runes, C_runes, D_runes, E_runes, F_runes, G_runes, H_runes, I_runes, J_runes, K_runes,
               L_runes, M_runes, N_runes, O_runes, P_runes, Q_runes, R_runes, S_runes, T_runes, U_runes, V_runes,
               W_runes, X_runes, Y_runes, Z_runes, Zero_runes, One_runes, Two_runes, Three_runes, Four_runes,
               Five_runes, Six_runes, Seven_runes, Eight_runes, Nine_runes]

# Main game loop
gameover = False
while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameover = True
            if event.key == pygame.K_a:
                if event.mod & pygame.KMOD_SHIFT:
                    A_runes -= 1
                else:
                    A_runes += 1
            if event.key == pygame.K_b:
                if event.mod & pygame.KMOD_SHIFT:
                    B_runes -= 1
                else:
                    B_runes += 1
            if event.key == pygame.K_c:
                if event.mod & pygame.KMOD_SHIFT:
                    C_runes -= 1
                else:
                    C_runes += 1
            if event.key == pygame.K_d:
                if event.mod & pygame.KMOD_SHIFT:
                    D_runes -= 1
                else:
                    D_runes += 1
            if event.key == pygame.K_e:
                if event.mod & pygame.KMOD_SHIFT:
                    E_runes -= 1
                else:
                    E_runes += 1
            if event.key == pygame.K_f:
                if event.mod & pygame.KMOD_SHIFT:
                    F_runes -= 1
                else:
                    F_runes += 1
            if event.key == pygame.K_g:
                if event.mod & pygame.KMOD_SHIFT:
                    G_runes -= 1
                else:
                    G_runes += 1
            if event.key == pygame.K_h:
                if event.mod & pygame.KMOD_SHIFT:
                    H_runes -= 1
                else:
                    H_runes += 1
            if event.key == pygame.K_i:
                if event.mod & pygame.KMOD_SHIFT:
                    I_runes -= 1
                else:
                    I_runes += 1
            if event.key == pygame.K_j:
                if event.mod & pygame.KMOD_SHIFT:
                    J_runes -= 1
                else:
                    J_runes += 1
            if event.key == pygame.K_k:
                if event.mod & pygame.KMOD_SHIFT:
                    K_runes -= 1
                else:
                    K_runes += 1
            if event.key == pygame.K_l:
                if event.mod & pygame.KMOD_SHIFT:
                    L_runes -= 1
                else:
                    L_runes += 1
            if event.key == pygame.K_m:
                if event.mod & pygame.KMOD_SHIFT:
                    M_runes -= 1
                else:
                    M_runes += 1
            if event.key == pygame.K_n:
                if event.mod & pygame.KMOD_SHIFT:
                    N_runes -= 1
                else:
                    N_runes += 1
            if event.key == pygame.K_o:
                if event.mod & pygame.KMOD_SHIFT:
                    O_runes -= 1
                else:
                    O_runes += 1
            if event.key == pygame.K_p:
                if event.mod & pygame.KMOD_SHIFT:
                    P_runes -= 1
                else:
                    P_runes += 1
            if event.key == pygame.K_q:
                if event.mod & pygame.KMOD_SHIFT:
                    Q_runes -= 1
                else:
                    Q_runes += 1
            if event.key == pygame.K_r:
                if event.mod & pygame.KMOD_SHIFT:
                    R_runes -= 1
                else:
                    R_runes += 1
            if event.key == pygame.K_s:
                if event.mod & pygame.KMOD_SHIFT:
                    S_runes -= 1
                else:
                    S_runes += 1
            if event.key == pygame.K_t:
                if event.mod & pygame.KMOD_SHIFT:
                    T_runes -= 1
                else:
                    T_runes += 1
            if event.key == pygame.K_u:
                if event.mod & pygame.KMOD_SHIFT:
                    U_runes -= 1
                else:
                    U_runes += 1
            if event.key == pygame.K_v:
                if event.mod & pygame.KMOD_SHIFT:
                    V_runes -= 1
                else:
                    V_runes += 1
            if event.key == pygame.K_w:
                if event.mod & pygame.KMOD_SHIFT:
                    W_runes -= 1
                else:
                    W_runes += 1
            if event.key == pygame.K_x:
                if event.mod & pygame.KMOD_SHIFT:
                    X_runes -= 1
                else:
                    X_runes += 1
            if event.key == pygame.K_y:
                if event.mod & pygame.KMOD_SHIFT:
                    Y_runes -= 1
                else:
                    Y_runes += 1
            if event.key == pygame.K_z:
                if event.mod & pygame.KMOD_SHIFT:
                    Z_runes -= 1
                else:
                    Z_runes += 1
            if event.key == pygame.K_0:
                if event.mod & pygame.KMOD_SHIFT:
                    Zero_runes -= 1
                else:
                    Zero_runes += 1
            if event.key == pygame.K_1:
                if event.mod & pygame.KMOD_SHIFT:
                    One_runes -= 1
                else:
                    One_runes += 1
            if event.key == pygame.K_2:
                if event.mod & pygame.KMOD_SHIFT:
                    Two_runes -= 1
                else:
                    Two_runes += 1
            if event.key == pygame.K_3:
                if event.mod & pygame.KMOD_SHIFT:
                    Three_runes -= 1
                else:
                    Three_runes += 1
            if event.key == pygame.K_4:
                if event.mod & pygame.KMOD_SHIFT:
                    Four_runes -= 1
                else:
                    Four_runes += 1
            if event.key == pygame.K_5:
                if event.mod & pygame.KMOD_SHIFT:
                    Five_runes -= 1
                else:
                    Five_runes += 1
            if event.key == pygame.K_6:
                if event.mod & pygame.KMOD_SHIFT:
                    Six_runes -= 1
                else:
                    Six_runes += 1
            if event.key == pygame.K_7:
                if event.mod & pygame.KMOD_SHIFT:
                    Seven_runes -= 1
                else:
                    Seven_runes += 1
            if event.key == pygame.K_8:
                if event.mod & pygame.KMOD_SHIFT:
                    Eight_runes -= 1
                else:
                    Eight_runes += 1
            if event.key == pygame.K_9:
                if event.mod & pygame.KMOD_SHIFT:
                    Nine_runes -= 1
                else:
                    Nine_runes += 1


    # Drawing

    # Redeclare Lists to prepare for drawing
    rune_counts = [A_runes, B_runes, C_runes, D_runes, E_runes, F_runes, G_runes, H_runes, I_runes, J_runes, K_runes,
                   L_runes, M_runes, N_runes, O_runes, P_runes, Q_runes, R_runes, S_runes, T_runes, U_runes, V_runes,
                   W_runes, X_runes, Y_runes, Z_runes, Zero_runes, One_runes, Two_runes, Three_runes, Four_runes,
                   Five_runes, Six_runes, Seven_runes, Eight_runes, Nine_runes]
    rescaled_runes = [rescale001, rescale002, rescale003, rescale004, rescale005, rescale005, rescale006, rescale007,
                      rescale008, rescale009, rescale010, rescale011, rescale012, rescale013, rescale014, rescale015,
                      rescale016, rescale017, rescale018, rescale019, rescale020, rescale021, rescale022, rescale023,
                      rescale024, rescale025, rescale026, rescale026, rescale027, rescale028, rescale029, rescale030,
                      rescale031, rescale032, rescale033, rescale034, rescale025, rescale036]
    win.fill((0, 0, 0))  # Clear the screen

    # Draw inventory bounding box
    pygame.draw.rect(win, (255, 255, 255), (5, 5, 323, 70), 5)

    # set up text spots
    key_text = ("a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  q  x  y  z  0  1  2  3  4  5  6  7  "
                "8  9")
    # NOTE: I wasn't able to get the text for this key (intended to be displayed above or below the rune legend at the
    # bottom of the window, if you can figure out why, I would appreciate it


    # Draw runes

    # do the drawing
    win.fill((0, 0, 0))  # clear the screen
    pygame.draw.rect(win, (255, 255, 255), (5, 5, 323, 70), 5)  # draw inventory bounding box
    legend_done = False
    index = 0
    legendx = 0
    legendy = 550
    while not legend_done:
        while index < len(rescaled_runes):
            win.blit(rescaled_runes[index], (legendx, legendy))
            legendx += (22 + (2 / 9))
            index += 1
        legend_done = True

    # Draw runes
    cur_x = 10
    cur_y = 10
    for i in range(len(runes)):
        if rune_counts[i] > 0:
            # Draw rune_image[i] at (cur_x, cur_y) and add some to cur_x like this:
            win.blit(runes[i], (cur_x, cur_y))
            cur_x += runes[i].get_width() + 3
        if rune_counts[i] < 0:
            rune_counts[i] = 0

    # draw the amount of runes held information onto the screen
    A_rune_info = f"You currently have {A_runes} of the A rune"
    A_rune_surface = font_obj.render(A_rune_info, False, (255, 255, 255))
    win.blit(A_rune_surface, (0, 80))
    if A_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (0, 80, 400, 17))
    B_rune_info = f"You currently have {B_runes} of the B rune"
    B_rune_surface = font_obj.render(B_rune_info, False, (255, 255, 255))
    win.blit(B_rune_surface, (0, 97))
    if B_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (0, 96, 400, 18))
    C_rune_info = f"You currently have {C_runes} of the C rune"
    C_rune_surface = font_obj.render(C_rune_info, False, (255, 255, 255))
    win.blit(C_rune_surface, (0, 114))
    if C_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (0, 113, 400, 19))
    D_rune_info = f"You currently have {D_runes} of the D rune"
    D_rune_surface = font_obj.render(D_rune_info, False, (255, 255, 255))
    win.blit(D_rune_surface, (0, 131))
    if D_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (0, 130, 400, 20))
    E_rune_info = f"You currently have {E_runes} of the E rune"
    E_rune_surface = font_obj.render(E_rune_info, False, (255, 255, 255))
    win.blit(E_rune_surface, (0, 148))
    if E_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (0, 147, 400, 21))
    F_rune_info = f"You currently have {F_runes} of the F rune"
    F_rune_surface = font_obj.render(F_rune_info, False, (255, 255, 255))
    win.blit(F_rune_surface, (0, 165))
    if F_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (0, 164, 400, 22))
    G_rune_info = f"You currently have {G_runes} of the G rune"
    G_rune_surface = font_obj.render(G_rune_info, False, (255, 255, 255))
    win.blit(G_rune_surface, (0, 182))
    if G_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (0, 181, 400, 23))
    H_rune_info = f"You currently have {H_runes} of the H rune"
    H_rune_surface = font_obj.render(H_rune_info, False, (255, 255, 255))
    win.blit(H_rune_surface, (0, 199))
    if H_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (0, 198, 400, 24))
    I_rune_info = f"You currently have {I_runes} of the I rune"
    I_rune_surface = font_obj.render(I_rune_info, False, (255, 255, 255))
    win.blit(I_rune_surface, (0, 216))
    if I_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (0, 215, 400, 25))
    J_rune_info = f"You currently have {J_runes} of the J rune"
    J_rune_surface = font_obj.render(J_rune_info, False, (255, 255, 255))
    win.blit(J_rune_surface, (0, 233))
    if J_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (0, 232, 400, 26))
    K_rune_info = f"You currently have {K_runes} of the K rune"
    K_rune_surface = font_obj.render(K_rune_info, False, (255, 255, 255))
    win.blit(K_rune_surface, (0, 250))
    if K_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (0, 249, 400, 27))
    L_rune_info = f"You currently have {L_runes} of the L rune"
    L_rune_surface = font_obj.render(L_rune_info, False, (255, 255, 255))
    win.blit(L_rune_surface, (0, 267))
    if L_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (0, 266, 400, 28))
    M_rune_info = f"You currently have {M_runes} of the M rune"
    M_rune_surface = font_obj.render(M_rune_info, False, (255, 255, 255))
    win.blit(M_rune_surface, (0, 284))
    if M_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (0, 283, 400, 29))
    N_rune_info = f"You currently have {N_runes} of the N rune"
    N_rune_surface = font_obj.render(N_rune_info, False, (255, 255, 255))
    win.blit(N_rune_surface, (0, 301))
    if N_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (0, 300, 400, 30))
    O_rune_info = f"You currently have {O_runes} of the O rune"
    O_rune_surface = font_obj.render(O_rune_info, False, (255, 255, 255))
    win.blit(O_rune_surface, (0, 318))
    if O_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (0, 317, 400, 31))
    P_rune_info = f"You currently have {P_runes} of the P rune"
    P_rune_surface = font_obj.render(P_rune_info, False, (255, 255, 255))
    win.blit(P_rune_surface, (0, 335))
    if P_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (0, 334, 400, 32))
    Q_rune_info = f"You currently have {Q_runes} of the Q rune"
    Q_rune_surface = font_obj.render(Q_rune_info, False, (255, 255, 255))
    win.blit(Q_rune_surface, (0, 352))
    if Q_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (0, 351, 400, 33))
    R_rune_info = f"You currently have {R_runes} of the R rune"
    R_rune_surface = font_obj.render(R_rune_info, False, (255, 255, 255))
    win.blit(R_rune_surface, (0, 369))
    if R_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (0, 368, 400, 34))
    S_rune_info = f"You currently have {S_runes} of the S rune"
    S_rune_surface = font_obj.render(S_rune_info, False, (255, 255, 255))
    win.blit(S_rune_surface, (0, 386))
    if S_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (0, 385, 400, 35))
    T_rune_info = f"You currently have {T_runes} of the T rune"
    T_rune_surface = font_obj.render(T_rune_info, False, (255, 255, 255))
    win.blit(T_rune_surface, (0, 403))
    if T_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (0, 402, 400, 36))
    U_rune_info = f"You currently have {U_runes} of the U rune"
    U_rune_surface = font_obj.render(U_rune_info, False, (255, 255, 255))
    win.blit(U_rune_surface, (0, 420))
    if U_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (0, 419, 400, 37))
    V_rune_info = f"You currently have {V_runes} of the V rune"
    V_rune_surface = font_obj.render(V_rune_info, False, (255, 255, 255))
    win.blit(V_rune_surface, (0, 437))
    if V_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (0, 436, 400, 38))
    W_rune_info = f"You currently have {W_runes} of the W rune"
    W_rune_surface = font_obj.render(W_rune_info, False, (255, 255, 255))
    win.blit(W_rune_surface, (0, 454))
    if W_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (0, 453, 400, 39))
    X_rune_info = f"You currently have {X_runes} of the X rune"
    X_rune_surface = font_obj.render(X_rune_info, False, (255, 255, 255))
    win.blit(X_rune_surface, (0, 471))
    if X_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (0, 470, 400, 40))
    Y_rune_info = f"You currently have {Y_runes} of the Y rune"
    Y_rune_surface = font_obj.render(Y_rune_info, False, (255, 255, 255))
    win.blit(Y_rune_surface, (0, 488))
    if Y_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (0, 487, 400, 41))
    Z_rune_info = f"You currently have {Z_runes} of the Z Rune"
    Z_rune_surface = font_obj.render(Z_rune_info, False, (255, 255, 255))
    win.blit(Z_rune_surface, (0, 505))
    if Z_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (0, 504, 400, 42))
    zero_info = f"You currently have {Zero_runes} of the 0 rune"
    zero_surface = font_obj.render(zero_info, False, (255, 255, 255))
    win.blit(zero_surface, (300, 80))
    # Numbers
    if Zero_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (300, 80, 400, 17))
    one_info = f"You currently have {One_runes} of the 1 Rune"
    one_surface = font_obj.render(one_info, False, (255, 255, 255))
    win.blit(one_surface, (300, 97))
    if One_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (300, 97, 400, 18))
    two_info = f"You currently have {Two_runes} of the 2 Rune"
    two_surface = font_obj.render(two_info, False, (255, 255, 255))
    win.blit(two_surface, (300, 114))
    if Two_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (300, 114, 400, 19))
    three_info = f"You currently have {Three_runes} of the 3 Rune"
    three_surface = font_obj.render(three_info, False, (255, 255, 255))
    win.blit(three_surface, (300, 131))
    if Three_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (300, 131, 400, 20))
    four_info = f"You currently have {Four_runes} of the 4 Rune"
    four_surface = font_obj.render(four_info, False, (255, 255, 255))
    win.blit(four_surface, (300, 148))
    if Four_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (300, 148, 400, 21))
    five_info = f"You currently have {Five_runes} of the 5 Rune"
    five_surface = font_obj.render(five_info, False, (255, 255, 255))
    win.blit(five_surface, (300, 165))
    if Five_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (300, 165, 400, 22))
    six_info = f"You currently have {Six_runes} of the 6 Rune"
    six_surface = font_obj.render(six_info, False, (255, 255, 255))
    win.blit(six_surface, (300, 182))
    if Six_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (300, 182, 400, 23))
    seven_info = f"You currently have {Seven_runes} of the 7 Rune"
    seven_surface = font_obj.render(seven_info, False, (255, 255, 255))
    win.blit(seven_surface, (300, 199))
    if Seven_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (300, 199, 400, 24))
    eight_info = f"You currently have {Eight_runes} of the 8 Rune"
    eight_surface = font_obj.render(eight_info, False, (255, 255, 255))
    win.blit(eight_surface, (300, 216))
    if Eight_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (300, 216, 400, 25))
    nine_info = f"You currently have {Nine_runes} of the 9 Rune"
    nine_surface = font_obj.render(nine_info, False, (255, 255, 255))
    win.blit(nine_surface, (300, 233))
    if Nine_runes < 2:
        pygame.draw.rect(win, (0, 0, 0), (300, 233, 400, 26))
    # Calculate total amt of unique runes
    ttl_unique = sum(1 for count in rune_counts if count > 0)

    # If more runes than inventory, hide runes and draw arrow
    if ttl_unique > 6:
        pygame.draw.rect(win, (0, 0, 0), (328, 5, 800, 70), 0)
        win.blit(arrow, (350, 15))
    pygame.display.flip()

# Endings
pygame.quit()
sys.exit()
