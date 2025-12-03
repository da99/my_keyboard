
Permissions:
===========
```
sudo nano /etc/udev/rules.d/99-hidraw.rules
SUBSYSTEMS=="hidraw", GROUP="input", MODE="0666"
sudo udevadm control --reload-rules
sudo udevadm trigger
```


Backups:
==========
1. https://chosfox.com/products/fox65-qmk-via-mechanical-keyboard-kit?variant=45341156868290
2. SKYLOONG GK61 QMK/VIA Wired Keyboard RGB https://www.aliexpress.us/item/3256806484161107.html?spm=a2g0o.cart.0.0.33ae38daNE9DS4&mp=1&pdp_npi=5%40dis%21USD%21USD%2055.35%21USD%2050.46%21%21USD%2050.46%21%21%21%402101d97817644273454255851e4200%2112000041701295338%21ct%21US%21720033231%21%211%210&gatewayAdapt=glo2usa
