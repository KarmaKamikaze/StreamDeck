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

    KEY_Numlock = "53" # Keyboard Num Lock and Clear
    KEY_KPslash = "54" # Keypad /
    KEY_KPasterisk = "55" # Keypad *
    KEY_KPminus = "56" # Keypad -
    KEY_KPplus = "57" # Keypad +
    KEY_KPenter = "58" # Keypad ENTER
    KEY_KP1 = "59" # Keypad 1 and End
    KEY_KP2 = "5a" # Keypad 2 and Down Arrow
    KEY_KP3 = "5b" # Keypad 3 and PageDn
    KEY_KP4 = "5c" # Keypad 4 and Left Arrow
    KEY_KP5 = "5d" # Keypad 5
    KEY_KP6 = "5e" # Keypad 6 and Right Arrow
    KEY_KP7 = "5f" # Keypad 7 and Home
    KEY_KP8 = "60" # Keypad 8 and Up Arrow
    KEY_KP9 = "61" # Keypad 9 and Page Up
    KEY_KP0 = "62" # Keypad 0 and Insert
    KEY_KPdot "63" # Keypad . and Delete

    KEY_102ND = "64" # Keyboard Non-US \ and |
    KEY_Compose = "65" # Keyboard Application
    KEY_Power = "66" # Keyboard Power
    KEY_KPequal = "67" # Keypad =

    KEY_F13 = "68" # Keyboard F13
    KEY_F14 = "69" # Keyboard F14
    KEY_F15 = "6a" # Keyboard F15
    KEY_F16 = "6b" # Keyboard F16
    KEY_F17 = "6c" # Keyboard F17
    KEY_F18 = "6d" # Keyboard F18
    KEY_F19 = "6e" # Keyboard F19
    KEY_F20 = "6f" # Keyboard F20
    KEY_F21 = "70" # Keyboard F21
    KEY_F22 = "71" # Keyboard F22
    KEY_F23 = "72" # Keyboard F23
    KEY_F24 = "73" # Keyboard F24

    KEY_Open = "74" # Keyboard Execute
    KEY_Help = "75" # Keyboard Help
    KEY_Props = "76" # Keyboard Menu
    KEY_Front = "77" # Keyboard Select
    KEY_Stop = "78" # Keyboard Stop
    KEY_Again = "79" # Keyboard Again
    KEY_Undo = "7a" # Keyboard Undo
    KEY_Cut = "7b" # Keyboard Cut
    KEY_Copy = "7c" # Keyboard Copy
    KEY_Paste = "7d" # Keyboard Paste
    KEY_Find = "7e" # Keyboard Find
    KEY_Mute = "7f" # Keyboard Mute
    KEY_Volumeup = "80" # Keyboard Volume Up
    KEY_Volumedown = "81" # Keyboard Volume Down
    KEY_Capslock = "82" # Keyboard Locking Caps Lock
    KEY_Numlock = "83" # Keyboard Locking Num Lock
    KEY_Scrolllock = "84" # Keyboard Locking Scroll Lock
    KEY_KPCOMMA = "85" # Keypad Comma
    KEY_KPequal = "86" # Keypad Equal Sign
    KEY_RO = "87" # Keyboard International1
    KEY_KATAKANAHIRAGANA = "88" # Keyboard International2
    KEY_YEN = "89" # Keyboard International3
    KEY_HENKAN = "8a" # Keyboard International4
    KEY_MUHENKAN = "8b" # Keyboard International5
    KEY_KPJPCOMMA = "8c" # Keyboard International6
    KEY_International17 = "8d" # Keyboard International7
    KEY_International18 = "8e" # Keyboard International8
    KEY_International19 = "8f" # Keyboard International9
    KEY_HANGEUL = "90" # Keyboard LANG1
    KEY_HANJA = "91" # Keyboard LANG2
    KEY_KATAKANA = "92" # Keyboard LANG3
    KEY_HIRAGANA = "93" # Keyboard LANG4
    KEY_ZENKAKUHANKAKU = "94" # Keyboard LANG5
    KEY_Lang6 = "95" # Keyboard LANG6
    KEY_Lang7 = "96" # Keyboard LANG7
    KEY_Lang8 = "97" # Keyboard LANG8
    KEY_Lang9 = "98" # Keyboard LANG9
    KEY_AlternateErase = "99" # Keyboard Alternate Erase
    KEY_Attention = "9a" # Keyboard SysReq/Attention
    KEY_Cancel = "9b" # Keyboard Cancel
    KEY_Clear = "9c" # Keyboard Clear
    KEY_Prior = "9d" # Keyboard Prior
    KEY_Return = "9e" # Keyboard Return
    KEY_Separator = "9f" # Keyboard Separator
    KEY_Out = "a0" # Keyboard Out
    KEY_Oper = "a1" # Keyboard Oper
    KEY_Again = "a2" # Keyboard Clear/Again
    KEY_CrSel = "a3" # Keyboard CrSel/Props
    KEY_ExSel = "a4" # Keyboard ExSel

    '''// = "b0" # Keypad 00
    // = "b1" # Keypad 000
    // = "b2" # Thousands Separator
    // = "b3" # Decimal Separator
    // = "b4" # Currency Unit
    // = "b5" # Currency Sub-unit
    '''
    KEY_KPleftparen = "b6" # Keypad (
    KEY_KPrightparen = "b7" # Keypad )
    '''
    // = "b8" # Keypad {
    // = "b9" # Keypad }
    // = "ba" # Keypad Tab
    // = "bb" # Keypad Backspace
    // = "bc" # Keypad A
    // = "bd" # Keypad B
    // = "be" # Keypad C
    // = "bf" # Keypad D
    // = "c0" # Keypad E
    // = "c1" # Keypad F
    // = "c2" # Keypad XOR
    // = "c3" # Keypad ^
    // = "c4" # Keypad %
    // = "c5" # Keypad <
    // = "c6" # Keypad >
    // = "c7" # Keypad &
    // = "c8" # Keypad &&
    // = "c9" # Keypad |
    // = "ca" # Keypad ||
    // = "cb" # Keypad :
    // = "cc" # Keypad #
    // = "cd" # Keypad Space
    // = "ce" # Keypad @
    // = "cf" # Keypad !
    // = "d0" # Keypad Memory Store
    // = "d1" # Keypad Memory Recall
    // = "d2" # Keypad Memory Clear
    // = "d3" # Keypad Memory Add
    // = "d4" # Keypad Memory Subtract
    // = "d5" # Keypad Memory Multiply
    // = "d6" # Keypad Memory Divide
    // = "d7" # Keypad +/-
    // = "d8" # Keypad Clear
    // = "d9" # Keypad Clear Entry
    // = "da" # Keypad Binary
    // = "db" # Keypad Octal
    // = "dc" # Keypad Decimal
    // = "dd" # Keypad Hexadecimal
    '''
    KEY_LeftCTRL = "e0" # Keyboard Left Control
    KEY_LeftSHIFT = "e1" # Keyboard Left Shift
    KEY_LeftALT = "e2" # Keyboard Left Alt
    KEY_LeftMETA = "e3" # Keyboard Left GUI
    KEY_RightCTRL = "e4" # Keyboard Right Control
    KEY_RightSHIFT = "e5" # Keyboard Right Shift
    KEY_RightALT = "e6" # Keyboard Right Alt
    KEY_RightMETA = "e7" # Keyboard Right GUI
