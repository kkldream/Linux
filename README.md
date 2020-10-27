# 目錄
* [根目錄](https://github.com/kkldream/Linux-Note)
    * [GPIO](GPIO)
    * [OpenCV](OpenCV)
    * [UART (Serial)](UART-(Serial))
* [其他](#其他)
    * [開機自動啟動](#開機自動啟動)
    * [改變 Swap (交換空間)](#改變-Swap-(交換空間))
    * [將 Ubuntu 家目錄資料夾的語言改為英文](#將-Ubuntu-家目錄資料夾的語言改為英文)

# 其他
## 將 Ubuntu 家目錄資料夾的語言改為英文
```sh
export LANG=en_US
xdg-user-dirs-gtk-update
```
參考網址：https://blog.jaycetyle.com/2018/06/ubuntu-home-folder-lang/

## 開機自動啟動
### Raspberry Pi OS：
自動啟動 sh 檔
```sh
touch ~/autostart.sh
sudo chmod u+x ~/autostart.sh
sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
```
/etc/xdg/lxsession/LXDE-pi/autostart：
```sh
@lxterminal -e ~/autostart.sh
```

## 改變 Swap (交換空間)
```sh
free -h # 先查看目前剩餘的記憶體用量
df -h   # 確認你的硬碟空間確實足夠
```
### Raspberry Pi OS：
    sudo nano /etc/dphys-swapfile

这里树莓派是默认的100Mb的交换空间，我们把它修改成4096，也就是4Gb。最尾有一个最大限制的参数–CONF_MAXSWAP，把它前面的井号标注去掉，并把这个参数也改成4096。

    sudo service dphys-swapfile restart

### Ubuntu-Mate：
在开始之前，请先使用命令检查您的 Ubuntu 系统的SWAP 分区
```sh
sudo swapon --show
```
创建 swap 的文件
```sh
swapoff -a
sudo fallocate -l 1G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
```
要让创建好的 swap 分区永久生效，可以将 swapfile 路径内容写入到 /etc/fstab 文件当中 ：
```sh
sudo cp /etc/fstab /etc/fstab.bak
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```
參考連結：https://blog.csdn.net/AlexWang30/article/details/90341172
