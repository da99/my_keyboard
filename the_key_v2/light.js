
import HID from 'node-hid';
const DPATH= '/dev/hidraw2';

const VIALRGB_SET_MODE = 0x41
const QMK_RGBLIGHT_COLOR = 0x83
const QMK_RGBLIGHT_BRIGHTNESS = 0x80
const QMK_RGBLIGHT_EFFECT = 0x81
const CMD_VIA_LIGHTING_SET_VALUE = 0x07
const MSG_LEN = 32
const ALL_OFF = 0
const SOLID_COLOR = 1
const BREATHING_1 = 2
const BREATHING_2 = 3
const BREATHING_3 = 4
const BREATHING_4 = 5

const device = await HID.HIDAsync.open(DPATH);
device.on("error", function(err) {
  console.warn(`------ ${err.message} ------------`);
  console.warn(err);
  console.warn(`----------------------------------`);
});
