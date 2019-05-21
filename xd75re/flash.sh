
set -x
set -e
the_file="/apps/my_keyboard/xd75re/xd75_da99.hex"
stat --format "%s" "$the_file"
sleep 1; echo -n ".";
sleep 1; echo -n ".";
sleep 1; echo -n ".";
lsusb | grep "DFU bootloader"
sudo dfu-programmer atmega32u4 erase --force
sleep 2
sudo dfu-programmer atmega32u4 flash "$the_file"
sleep 2
sudo dfu-programmer atmega32u4 reset
