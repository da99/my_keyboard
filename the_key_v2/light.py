import sys
import hid
import struct

# constants
VIALRGB_SET_MODE = 0x41
QMK_RGBLIGHT_COLOR = 0x83
QMK_RGBLIGHT_BRIGHTNESS = 0x80
QMK_RGBLIGHT_EFFECT = 0x81
CMD_VIA_LIGHTING_SET_VALUE = 0x07
MSG_LEN = 32
ALL_OFF = 0
SOLID_COLOR = 1
BREATHING_1 = 2
BREATHING_2 = 3
BREATHING_3 = 4
BREATHING_4 = 5
RAINBOW_SWIRL_1 = 9
RAINBOW_SWIRL_2 = 10
RAINBOW_SWIRL_3 = 11
RAINBOW_SWIRL_4 = 12
RAINBOW_SWIRL_5 = 13
RAINBOW_SWIRL_6 = 14
# hid device path
# use hid.enumerate() to figure out
list = hid.enumerate()
for i in list:
  if i['product_string'] == 'The Key v2' and i['usage'] == 97:
    PATH = i['path']
    break
print(PATH)

# helper functions
def change_rgb_mode(mode):
  msg = struct.pack(">BBB", CMD_VIA_LIGHTING_SET_VALUE, QMK_RGBLIGHT_EFFECT, mode)
  return(msg)

def change_rgb_brightness(v):
  msg = struct.pack(">BBB", CMD_VIA_LIGHTING_SET_VALUE, QMK_RGBLIGHT_BRIGHTNESS, v)
  return(msg)

def change_rgb_color(h, s):
  msg = struct.pack(">BBBB", CMD_VIA_LIGHTING_SET_VALUE, QMK_RGBLIGHT_COLOR, h, s)
  return(msg)

def format_msg(msg):
  msg += b"\x00" * (MSG_LEN - len(msg))
  return(msg)

# example: change RGB mode to 14 (Rainbow Swirl)
# msg = struct.pack(">BBB", CMD_VIA_LIGHTING_SET_VALUE, QMK_RGBLIGHT_EFFECT, SOLID_COLOR)
# msg += b"\x00" * (MSG_LEN - len(msg))
dev = hid.Device(path=PATH)
match sys.argv[1]:
  case "warn":
    dev.write(b"\x00" + format_msg(change_rgb_mode(SOLID_COLOR)))
  case "off":
    dev.write(b"\x00" + format_msg(change_rgb_mode(ALL_OFF)))
  case "playing":
    dev.write(b"\x00" + format_msg(change_rgb_mode(SOLID_COLOR)))
    dev.write(b"\x00" + format_msg(change_rgb_mode(RAINBOW_SWIRL_3)))
  case _:
    print("Unknown command: " + sys.argv[1])
    dev.close()
    sys.exit(1)


# dev.write(b"\x00" + format_msg(change_rgb_color(25,255)))
# dev.write(b"\x00" + format_msg(change_rgb_brightness(40)))
# dev.write(b"\x00" + format_msg(change_rgb_mode(SOLID_COLOR)))
# dev.write(b"\x00" + format_msg(change_rgb_brightness(125)))
dev.close()
