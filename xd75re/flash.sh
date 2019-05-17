
set -x
set -e
lsusb | grep "DFU bootloader"
sudo dfu-programmer atmega32u4 erase --force
sleep 2
sudo dfu-programmer atmega32u4 flash xd75_da99.hex
sleep 2
sudo dfu-programmer atmega32u4 reset
