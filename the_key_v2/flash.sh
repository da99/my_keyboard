
set -e -u -x
the_file="/apps/my_keyboard/the_key_v2/massdrop_thekey_vial.hex"
test -f "$the_file"
stat --format "%s" "$the_file"
sleep 1; echo -n ".";
sleep 1; echo -n ".";
sleep 1; echo -n ".";
lsusb | grep "DFU bootloader"
set -x
sudo dfu-programmer atmega32u4 get | grep Bootloader
sudo dfu-programmer atmega32u4 erase --force
sleep 2
sudo dfu-programmer atmega32u4 flash "$the_file"
sleep 2
sudo dfu-programmer atmega32u4 reset
