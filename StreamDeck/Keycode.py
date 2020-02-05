# USB HID Keyboard scan codes as per USB spec 1.11
# plus some additional codes
#
# Created by KarmaKamikaze, 2020
# Public domain
#
# Adapted from:
# https://source.android.com/devices/input/keyboard-devices.html

class Keycode:
    
    # comments are for danish layout

    KEY_A = "\0\0\04\0\0\0\0\0" # a and A
    KEY_B = "\0\0\05\0\0\0\0\0" # b and B
    KEY_C = "\0\0\06\0\0\0\0\0" # c and C
    KEY_D = "\0\0\07\0\0\0\0\0" # d and D
    KEY_E = "\0\0\08\0\0\0\0\0" # e and E
    KEY_F = "\0\0\09\0\0\0\0\0" # f and F
    KEY_G = "\0\0\0a\0\0\0\0\0" # g and G
    KEY_H = "\0\0\0b\0\0\0\0\0" # h and H
    KEY_I = "\0\0\0c\0\0\0\0\0" # i and I
    KEY_J = "\0\0\0d\0\0\0\0\0" # j and J
    KEY_K = "\0\0\0e\0\0\0\0\0" # k and K
    KEY_L = "\0\0\0f\0\0\0\0\0" # l and L
    KEY_M = "\0\0\10\0\0\0\0\0" # m and M
    KEY_N = "\0\0\11\0\0\0\0\0" # n and N
    KEY_O = "\0\0\12\0\0\0\0\0" # o and O
    KEY_P = "\0\0\13\0\0\0\0\0" # p and P
    KEY_Q = "\0\0\14\0\0\0\0\0" # q and Q
    KEY_R = "\0\0\15\0\0\0\0\0" # r and R
    KEY_S = "\0\0\16\0\0\0\0\0" # s and S
    KEY_T = "\0\0\17\0\0\0\0\0" # t and T
    KEY_U = "\0\0\18\0\0\0\0\0" # u and U 
    KEY_V = "\0\0\19\0\0\0\0\0" # v and V
    KEY_W = "\0\0\1a\0\0\0\0\0" # w and W
    KEY_X = "\0\0\1b\0\0\0\0\0" # x and X
    KEY_Y = "\0\0\1c\0\0\0\0\0" # y and Y
    KEY_Z = "\0\0\1d\0\0\0\0\0" # z and Z

    KEY_1 = "\0\0\1e\0\0\0\0\0" # 1 and !
    KEY_2 = "\0\0\1f\0\0\0\0\0" # 2 and "
    KEY_3 = "\0\0\20\0\0\0\0\0" # 3 and #
    KEY_4 = "\0\0\21\0\0\0\0\0" # 4 and ¤
    KEY_5 = "\0\0\22\0\0\0\0\0" # 5 and %
    KEY_6 = "\0\0\23\0\0\0\0\0" # 6 and &
    KEY_7 = "\0\0\24\0\0\0\0\0" # 7 and /
    KEY_8 = "\0\0\25\0\0\0\0\0" # 8 and (
    KEY_9 = "\0\0\26\0\0\0\0\0" # 9 and )
    KEY_0 = "\0\0\27\0\0\0\0\0" # 0 and =

    KEY_Enter = "\0\0\28\0\0\0\0\0" # Return (Enter)
    KEY_ESC = "\0\0\29\0\0\0\0\0" # Escape
    KEY_Backspace = "\0\0\2a\0\0\0\0\0" # Delete (Backspace)
    KEY_Tab = "\0\0\2b\0\0\0\0\0" # Tab
    KEY_Space = "\0\0\2c\0\0\0\0\0" # Spacebar
    KEY_Minus = "\0\0\2d\0\0\0\0\0" # + and ?
    KEY_Equal = "\0\0\2e\0\0\0\0\0" # ´ and `
    KEY_Leftbrace = "\0\0\2f\0\0\0\0\0" # å and Å
    KEY_Rightbrace = "\0\0\30\0\0\0\0\0" # ¨ and ^
    KEY_Backslash = "\0\0\31\0\0\0\0\0" # < and >
    KEY_Hashtilde = "\0\0\32\0\0\0\0\0" # ' and *
    KEY_Semicolon = "\0\0\33\0\0\0\0\0" # æ and Æ
    KEY_Apostrophe = "\0\0\34\0\0\0\0\0" # ø and Ø
    KEY_Grave = "\0\0\35\0\0\0\0\0" # ½ and §
    KEY_Comma = "\0\0\36\0\0\0\0\0" # , and ;
    KEY_Dot = "\0\0\37\0\0\0\0\0" # . and :
    KEY_Slash = "\0\0\38\0\0\0\0\0" # - and _
    KEY_Capslock = "\0\0\39\0\0\0\0\0" # Capslock

    KEY_F1 = "\0\0\3a\0\0\0\0\0" # F1
    KEY_F2 = "\0\0\3b\0\0\0\0\0" # F2
    KEY_F3 = "\0\0\3c\0\0\0\0\0" # F3
    KEY_F4 = "\0\0\3d\0\0\0\0\0" # F4
    KEY_F5 = "\0\0\3e\0\0\0\0\0" # F5
    KEY_F6 = "\0\0\3f\0\0\0\0\0" # F6
    KEY_F7 = "\0\0\40\0\0\0\0\0" # F7
    KEY_F8 = "\0\0\41\0\0\0\0\0" # F8
    KEY_F9 = "\0\0\42\0\0\0\0\0" # F9
    KEY_F10 = "\0\0\43\0\0\0\0\0" # F10
    KEY_F11 = "\0\0\44\0\0\0\0\0" # F11
    KEY_F12 = "\0\0\45\0\0\0\0\0" # F12

    KEY_Sysrq = "\0\0\46\0\0\0\0\0" # Print screen
    KEY_Scrolllock = "\0\0\47\0\0\0\0\0" # Scroll Lock
    KEY_Pause = "\0\0\48\0\0\0\0\0" # Pause
    KEY_Insert = "\0\0\49\0\0\0\0\0" # Insert
    KEY_Home = "\0\0\4a\0\0\0\0\0" # Home
    KEY_Pageup = "\0\0\4b\0\0\0\0\0" # Page up
    KEY_Delete = "\0\0\4c\0\0\0\0\0" # Delete
    KET_End = "\0\0\4d\0\0\0\0\0" # End
    KEY_Pagedown = "\0\0\4e\0\0\0\0\0" # Page down
    KEY_Right = "\0\0\4f\0\0\0\0\0" # Right arrow
    KEY_Left = "\0\0\50\0\0\0\0\0" # Left arrow
    KEY_Down = "\0\0\51\0\0\0\0\0" # Down arrow
    KEY_Up = "\0\0\52\0\0\0\0\0" # Up arrow
