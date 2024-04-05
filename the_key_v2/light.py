import hid
import struct

# constants
CMD_VIA_LIGHTING_SET_VALUE = 0x07
QMK_RGBLIGHT_EFFECT = 0x81
MSG_LEN = 32

# hid device path
# use hid.enumerate() to figure out
list = hid.enumerate()
for i in list:
  if i['product_string'] == 'The Key v2' and i['usage'] == 97:
      print(i)
      PATH = i['path']
print(PATH)

# example: change RGB mode to 14 (Rainbow Swirl)
mode = 14
msg = struct.pack(">BBB", CMD_VIA_LIGHTING_SET_VALUE, QMK_RGBLIGHT_EFFECT, mode)
msg += b"\x00" * (MSG_LEN - len(msg))
dev = hid.Device(path=PATH)
dev.write(b"\x00" + msg)
dev.close()
