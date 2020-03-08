# Keyboard report format:
# Byte 0: Keyboard modifier bits (SHIFT, ALT, CTRL etc)
# Byte 1: reserved
# Byte 2-7: Up to six keyboard usage indexes representing the keys that are 
#           currently "pressed". 
#           Order is not important, a key is either pressed (present in the 
#           buffer) or not pressed.
#
# USB HID Keyboard scan codes as per USB spec 1.12
# plus some additional codes
#
# Created by KarmaKamikaze, 2020
# Public domain
#
# Adapted from:
# https://source.android.com/devices/input/keyboard-devices.html
# https://www.usb.org/document-library/hid-usage-tables-112

class Keycode:
    
    # Comments are for danish layout

    # Modifier masks - used for the first byte in the HID report.
    # NOTE: The second byte in the report is reserved, 0x00

    # Modifier keys can be added (+) together to represent multiple modifier presses at once.

    KEY_MOD_LCTRL = chr(1)
    KEY_MOD_LSHIFT = chr(2)
    KEY_MOD_LALT = chr(4)
    KEY_MOD_LMETA = chr(8)
    KEY_MOD_RCTRL = chr(16)
    KEY_MOD_RSHIFT = chr(32)
    KEY_MOD_RALT = chr(64)
    KEY_MOD_RMETA = chr(128)

    KEY_A = chr(4) # a and A
    KEY_B = chr(5) # b and B
    KEY_C = chr(6) # c and C
    KEY_D = chr(7) # d and D
    KEY_E = chr(8) # e and E
    KEY_F = chr(9) # f and F
    KEY_G = chr(10) # g and G
    KEY_H = chr(11) # h and H
    KEY_I = chr(12) # i and I
    KEY_J = chr(13) # j and J
    KEY_K = chr(14) # k and K
    KEY_L = chr(15) # l and L
    KEY_M = chr(16) # m and M
    KEY_N = chr(17) # n and N
    KEY_O = chr(18) # o and O
    KEY_P = chr(19) # p and P
    KEY_Q = chr(20) # q and Q
    KEY_R = chr(21) # r and R
    KEY_S = chr(22) # s and S
    KEY_T = chr(23) # t and T
    KEY_U = chr(24) # u and U 
    KEY_V = chr(25) # v and V
    KEY_W = chr(26) # w and W
    KEY_X = chr(27) # x and X
    KEY_Y = chr(28) # y and Y
    KEY_Z = chr(29) # z and Z

    KEY_1 = chr(30) # 1 and !
    KEY_2 = chr(31) # 2 and "
    KEY_3 = chr(32) # 3 and #
    KEY_4 = chr(33) # 4 and ¤
    KEY_5 = chr(34) # 5 and %
    KEY_6 = chr(35) # 6 and &
    KEY_7 = chr(36) # 7 and /
    KEY_8 = chr(37) # 8 and (
    KEY_9 = chr(38) # 9 and )
    KEY_0 = chr(39) # 0 and =

    KEY_Enter = chr(40) # Return (Enter)
    KEY_ESC = chr(41) # Escape
    KEY_Backspace = chr(42) # Delete (Backspace)
    KEY_Tab = chr(43) # Tab
    KEY_Space = chr(44) # Spacebar
    KEY_Minus = chr(45) # + and ?
    KEY_Equal = chr(46) # ´ and `
    KEY_Leftbrace = chr(47) # å and Å
    KEY_Rightbrace = chr(48) # ¨ and ^
    KEY_Backslash = chr(49) # < and >
    KEY_Hashtilde = chr(50) # ' and *
    KEY_Semicolon = chr(51) # æ and Æ
    KEY_Apostrophe = chr(52) # ø and Ø
    KEY_Grave = chr(53) # ½ and §
    KEY_Comma = chr(54) # , and ;
    KEY_Dot = chr(55) # . and :
    KEY_Slash = chr(56) # - and _
    KEY_Capslock = chr(57) # Capslock

    KEY_F1 = chr(58) # F1
    KEY_F2 = chr(59) # F2
    KEY_F3 = chr(60) # F3
    KEY_F4 = chr(61) # F4
    KEY_F5 = chr(62) # F5
    KEY_F6 = chr(63) # F6
    KEY_F7 = chr(64) # F7
    KEY_F8 = chr(65) # F8
    KEY_F9 = chr(66) # F9
    KEY_F10 = chr(67) # F10
    KEY_F11 = chr(68) # F11
    KEY_F12 = chr(69) # F12

    KEY_Sysrq = chr(70) # Print screen
    KEY_Scrolllock = chr(71) # Scroll Lock
    KEY_Pause = chr(72) # Pause
    KEY_Insert = chr(73) # Insert
    KEY_Home = chr(74) # Home
    KEY_Pageup = chr(75) # Page up
    KEY_Delete = chr(76) # Delete
    KET_End = chr(77) # End
    KEY_Pagedown = chr(78) # Page down
    KEY_Right = chr(79) # Right arrow
    KEY_Left = chr(80) # Left arrow
    KEY_Down = chr(81) # Down arrow
    KEY_Up = chr(82) # Up arrow

    KEY_Numlock = chr(83) # Keyboard Num Lock and Clear
    KEY_KPslash = chr(84) # Keypad /
    KEY_KPasterisk = chr(85) # Keypad *
    KEY_KPminus = chr(86) # Keypad -
    KEY_KPplus = chr(87) # Keypad +
    KEY_KPenter = chr(88) # Keypad ENTER
    KEY_KP1 = chr(89) # Keypad 1 and End
    KEY_KP2 = chr(90) # Keypad 2 and Down Arrow
    KEY_KP3 = chr(91) # Keypad 3 and PageDn
    KEY_KP4 = chr(92) # Keypad 4 and Left Arrow
    KEY_KP5 = chr(93) # Keypad 5
    KEY_KP6 = chr(94) # Keypad 6 and Right Arrow
    KEY_KP7 = chr(95) # Keypad 7 and Home
    KEY_KP8 = chr(96) # Keypad 8 and Up Arrow
    KEY_KP9 = chr(97) # Keypad 9 and Page Up
    KEY_KP0 = chr(98) # Keypad 0 and Insert
    KEY_KPdot = chr(99) # Keypad . and Delete

    KEY_102ND = chr(100) # Keyboard Non-US \ and |
    KEY_Compose = chr(101) # Keyboard Application
    KEY_Power = chr(102) # Keyboard Power
    KEY_KPequal = chr(103) # Keypad =

    KEY_F13 = chr(104) # Keyboard F13
    KEY_F14 = chr(105) # Keyboard F14
    KEY_F15 = chr(106) # Keyboard F15
    KEY_F16 = chr(107) # Keyboard F16
    KEY_F17 = chr(108) # Keyboard F17
    KEY_F18 = chr(109) # Keyboard F18
    KEY_F19 = chr(110) # Keyboard F19
    KEY_F20 = chr(111) # Keyboard F20
    KEY_F21 = chr(112) # Keyboard F21
    KEY_F22 = chr(113) # Keyboard F22
    KEY_F23 = chr(114) # Keyboard F23
    KEY_F24 = chr(115) # Keyboard F24

    KEY_Open = chr(116) # Keyboard Execute
    KEY_Help = chr(117) # Keyboard Help
    KEY_Props = chr(118) # Keyboard Menu
    KEY_Front = chr(119) # Keyboard Select
    KEY_Stop = chr(120) # Keyboard Stop
    KEY_Again = chr(121) # Keyboard Again
    KEY_Undo = chr(122) # Keyboard Undo
    KEY_Cut = chr(123) # Keyboard Cut
    KEY_Copy = chr(124) # Keyboard Copy
    KEY_Paste = chr(125) # Keyboard Paste
    KEY_Find = chr(126) # Keyboard Find
    KEY_Mute = chr(127) # Keyboard Mute
    KEY_Volumeup = chr(128) # Keyboard Volume Up
    KEY_Volumedown = chr(129) # Keyboard Volume Down
    KEY_Capslock = chr(130) # Keyboard Locking Caps Lock
    KEY_Numlock = chr(131) # Keyboard Locking Num Lock
    KEY_Scrolllock = chr(132) # Keyboard Locking Scroll Lock
    KEY_KPCOMMA = chr(133) # Keypad Comma
    KEY_KPequal = chr(134) # Keypad Equal Sign
    KEY_RO = chr(135) # Keyboard International1
    KEY_KATAKANAHIRAGANA = chr(136) # Keyboard International2
    KEY_YEN = chr(127) # Keyboard International3
    KEY_HENKAN = chr(138) # Keyboard International4
    KEY_MUHENKAN = chr(139) # Keyboard International5
    KEY_KPJPCOMMA = chr(140) # Keyboard International6
    KEY_International17 = chr(141) # Keyboard International7
    KEY_International18 = chr(142) # Keyboard International8
    KEY_International19 = chr(143) # Keyboard International9
    KEY_HANGEUL = chr(144) # Keyboard LANG1
    KEY_HANJA = chr(145) # Keyboard LANG2
    KEY_KATAKANA = chr(146) # Keyboard LANG3
    KEY_HIRAGANA = chr(147) # Keyboard LANG4
    KEY_ZENKAKUHANKAKU = chr(148) # Keyboard LANG5
    KEY_Lang6 = chr(149) # Keyboard LANG6
    KEY_Lang7 = chr(150) # Keyboard LANG7
    KEY_Lang8 = chr(151) # Keyboard LANG8
    KEY_Lang9 = chr(152) # Keyboard LANG9
    KEY_AlternateErase = chr(153) # Keyboard Alternate Erase
    KEY_Attention = chr(154) # Keyboard SysReq/Attention
    KEY_Cancel = chr(155) # Keyboard Cancel
    KEY_Clear = chr(156) # Keyboard Clear
    KEY_Prior = chr(157) # Keyboard Prior
    KEY_Return = chr(158) # Keyboard Return
    KEY_Separator = chr(159) # Keyboard Separator
    KEY_Out = chr(160) # Keyboard Out
    KEY_Oper = chr(161) # Keyboard Oper
    KEY_Again = chr(162) # Keyboard Clear/Again
    KEY_CrSel = chr(163) # Keyboard CrSel/Props
    KEY_ExSel = chr(164) # Keyboard ExSel
    
    # 165-175 reserved
    '''// = chr(176) # Keypad 00
    // = chr(177) # Keypad 000
    // = chr(178) # Thousands Separator
    // = chr(179) # Decimal Separator
    // = chr(180) # Currency Unit
    // = chr(181) # Currency Sub-unit
    '''
    KEY_KPleftparen = chr(182) # Keypad (
    KEY_KPrightparen = chr(183) # Keypad )
    '''
    // = chr(184) # Keypad {
    // = chr(185) # Keypad }
    // = chr(186) # Keypad Tab
    // = chr(187) # Keypad Backspace
    // = chr(188) # Keypad A
    // = chr(189) # Keypad B
    // = chr(190) # Keypad C
    // = chr(191) # Keypad D
    // = chr(192) # Keypad E
    // = chr(193) # Keypad F
    // = chr(194) # Keypad XOR
    // = chr(195) # Keypad ^
    // = chr(196) # Keypad %
    // = chr(197) # Keypad <
    // = chr(198) # Keypad >
    // = chr(199) # Keypad &
    // = chr(200) # Keypad &&
    // = chr(201) # Keypad |
    // = chr(202) # Keypad ||
    // = chr(203) # Keypad :
    // = chr(204) # Keypad #
    // = chr(205) # Keypad Space
    // = chr(206) # Keypad @
    // = chr(207) # Keypad !
    // = chr(208) # Keypad Memory Store
    // = chr(209) # Keypad Memory Recall
    // = chr(210) # Keypad Memory Clear
    // = chr(211) # Keypad Memory Add
    // = chr(212) # Keypad Memory Subtract
    // = chr(213) # Keypad Memory Multiply
    // = chr(214) # Keypad Memory Divide
    // = chr(215) # Keypad +/-
    // = chr(216) # Keypad Clear
    // = chr(217) # Keypad Clear Entry
    // = chr(218) # Keypad Binary
    // = chr(219) # Keypad Octal
    // = chr(220) # Keypad Decimal
    // = chr(221) # Keypad Hexadecimal
    '''
    # 222-223 reserved
    KEY_LeftCTRL = chr(224) # Keyboard Left Control
    KEY_LeftSHIFT = chr(225) # Keyboard Left Shift
    KEY_LeftALT = chr(226) # Keyboard Left Alt
    KEY_LeftMETA = chr(227) # Keyboard Left GUI
    KEY_RightCTRL = chr(228) # Keyboard Right Control
    KEY_RightSHIFT = chr(229) # Keyboard Right Shift
    KEY_RightALT = chr(230) # Keyboard Right Alt
    KEY_RightMETA = chr(231) # Keyboard Right GUI


    # A multifunctional method that takes an infinite amount of arguments.
    # Depending on how many keypresses are sent to the method, it will determine
    # how many arguments are used.
    def KeyCombine(*args):
        if len(args) == 1: # one keypress
            return "\0\0{}\0\0\0\0\0".format(args[0])
        elif len(args) == 2: # two keypresses
            if (args[0] == Keycode.KEY_MOD_LSHIFT) or \
            (args[0] == Keycode.KEY_MOD_LCTRL) or \
            (args[0] == Keycode.KEY_MOD_LALT or \
            (args[0] == Keycode.KEY_MOD_RSHIFT) or \
            (args[0] == Keycode.KEY_MOD_RCTRL) or \
            (args[0] == Keycode.KEY_MOD_RALT)):
                return "{0}\0{1}\0\0\0\0\0".format(args[0], args[1])
            else:
                return "\0\0{0}{1}\0\0\0\0".format(args[0], args[1])
        elif len(args) == 3: # three keypresses
            if (args[0] == Keycode.KEY_MOD_LSHIFT) or \
            (args[0] == Keycode.KEY_MOD_LCTRL) or \
            (args[0] == Keycode.KEY_MOD_LALT or \
            (args[0] == Keycode.KEY_MOD_RSHIFT) or \
            (args[0] == Keycode.KEY_MOD_RCTRL) or \
            (args[0] == Keycode.KEY_MOD_RALT)):
                return "{0}\0{1}{2}\0\0\0\0".format(args[0], args[1], args[2])
            else:
                return "\0\0{0}{1}{2}\0\0\0".format(args[0], args[1], args[2])
        elif len(args) == 4: # four keypresses
            if (args[0] == Keycode.KEY_MOD_LSHIFT) or \
            (args[0] == Keycode.KEY_MOD_LCTRL) or \
            (args[0] == Keycode.KEY_MOD_LALT or \
            (args[0] == Keycode.KEY_MOD_RSHIFT) or \
            (args[0] == Keycode.KEY_MOD_RCTRL) or \
            (args[0] == Keycode.KEY_MOD_RALT)):
                return "{0}\0{1}{2}{3}\0\0\0".format(args[0], args[1], args[2], args[3])
            else:
                return "\0\0{0}{1}{2}{3}\0\0".format(args[0], args[1], args[2], args[3])
        elif len(args) == 5: # five keypresses
            if (args[0] == Keycode.KEY_MOD_LSHIFT) or \
            (args[0] == Keycode.KEY_MOD_LCTRL) or \
            (args[0] == Keycode.KEY_MOD_LALT or \
            (args[0] == Keycode.KEY_MOD_RSHIFT) or \
            (args[0] == Keycode.KEY_MOD_RCTRL) or \
            (args[0] == Keycode.KEY_MOD_RALT)):
                return "{0}\0{1}{2}{3}{4}\0\0".format(args[0], args[1], args[2], args[3], args[4])
            else:
                return "\0\0{0}{1}{2}{3}{4}\0".format(args[0], args[1], args[2], args[3], args[4])
        elif len(args) == 6: # six keypresses
            if (args[0] == Keycode.KEY_MOD_LSHIFT) or \
            (args[0] == Keycode.KEY_MOD_LCTRL) or \
            (args[0] == Keycode.KEY_MOD_LALT or \
            (args[0] == Keycode.KEY_MOD_RSHIFT) or \
            (args[0] == Keycode.KEY_MOD_RCTRL) or \
            (args[0] == Keycode.KEY_MOD_RALT)):
                return "{0}\0{1}{2}{3}{4}{5}\0".format(args[0], args[1], args[2], args[3], args[4], args[5])
            else:
                return "\0\0{0}{1}{2}{3}{4}{5}".format(args[0], args[1], args[2], args[3], args[4], args[5])
        elif len(args) == 7: # seven keypresses
            if (args[0] == Keycode.KEY_MOD_LSHIFT) or \
            (args[0] == Keycode.KEY_MOD_LCTRL) or \
            (args[0] == Keycode.KEY_MOD_LALT or \
            (args[0] == Keycode.KEY_MOD_RSHIFT) or \
            (args[0] == Keycode.KEY_MOD_RCTRL) or \
            (args[0] == Keycode.KEY_MOD_RALT)):
                return "{0}\0{1}{2}{3}{4}{5}{6}".format(args[0], args[1], args[2], args[3], args[4], args[5], args[6])
            else:
                print("Error: Only 6 non-modifier keypresses are possible simultaneously.")
                pass
