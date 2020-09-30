# 開機自動啟動 sh 檔
```sh
touch ~/autostart.sh
sudo chmod u+x ~/autostart.sh
sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
```
/etc/xdg/lxsession/LXDE-pi/autostart：
```sh
@lxterminal -e ~/autostart.sh
```