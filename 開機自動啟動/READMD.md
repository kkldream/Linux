# 開機自動啟動 sh 檔
    touch ~/autostart.sh
    sudo chmod u+x ~/autostart.sh
    sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
    @lxterminal -e ~/autostart.sh