# 目錄
* [根目錄](https://github.com/kkldream/Linux-Note)
    * [GPIO](GPIO)
    * [OpenCV](OpenCV)
    * [Uart-Serial](Uart-Serial)
* [常用](#常用)
    * [壓縮與解壓縮](#壓縮與解壓縮)
    * [使用者/群組](#使用者/群組)
* [環境](#環境)
    * [SSH](#SSH)
    * [VNC](#VNC)
* [其他](#其他)
    * [開機自動啟動](#開機自動啟動)
    * [改變 Swap (交換空間)](#改變-Swap-(交換空間))
    * [將 Ubuntu 家目錄資料夾的語言改為英文](#將-Ubuntu-家目錄資料夾的語言改為英文)

# 常用
## 壓縮與解壓縮
|格式(套件名)|壓縮|解壓縮|
|:---:|---|---|
|.zip (zip)|zip -r FileName.zip DirName|unzip FileName.zip|
|.rar (rar)|rar a FileName.rar DirName|rar e FileName.rar|
|"||unrar e FileName.rar|
|"||rar x FileName.rar DirName|
|.tar (tar)|tar cvf FileName.tar DirName|tar xvf FileName.tar|
|.gz (gzip)|gzip FileName|gunzip FileName.gz|
|"||gzip -d FileName.gz|
|.tar.gz (gzip)|tar zcvf FileName.tar.gz DirName|tar zxvf FileName.tar.gz|

原文網址：http://note.drx.tw/2008/04/command.html#zip

## 使用者/群組
### 新增使用者：
```sh
adduser username
```
### 刪除使用者：
```sh
userdel username
```
### 既有使用者加入群組：
```sh
usermod --gid YOUR_GROUP YOUR_ACCOUNT                           # 設定既有帳號的主要群組
usermod --append --groups YOUR_GROUP1,YOUR_GROUP2 YOUR_ACCOUNT  # 將既有帳號加入指定群組
```
### 其他指令：
```sh
id                  # 查詢自己所隸屬的所有群組與 ID
id YOUR_ACCOUNT     # 查詢指定帳號所隸屬的所有群組與 ID
groups              # 查詢自己所隸屬的所有群組
groups YOUR_ACCOUNT # 查詢指定帳號所隸屬的所有群組
```
使用者檔案存放在`/etc/passwd`

原文連結：https://officeguide.cc/linux-add-user-to-group-tutorial/

# 環境
## SSH
Install SSH：
```sh
sudo apt install ssh
```
### 修復 "sshd error: could not load host key"：
```sh
service ssh status                      # 查看 SSH 狀態
ls -al /etc/ssh/ssh*key                 # 查看密鑰
sudo rm -r /etc/ssh/ssh*key             # 移除舊密鑰
sudo dpkg-reconfigure openssh-server    # 生成新密鑰
```
原文網址：https://kknews.cc/code/lpy6jp9.html

## VNC
### Install VNC Server (遠端桌面環境將採用xfce)：
```sh
sudo apt install vnc4server xfce4 xfce4-goodies
```
in `~/.vnc/xstartup`：
```sh
#!/bin/sh
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
exec startxfce4 
```
```sh
chmod 755 ~/.vnc/xstartup   # 修改權限
vncpasswd                   # 修改密碼
```
原文網址：https://go-linux.blogspot.com/2019/01/ubuntu-1804-vnc-server.html
### Ubuntu 配置自带桌面共享：
1. 安装dconf-editor

    sudo apt install dconf-editor
2. 打开dconf-editor，依次展开org->gnome->desktop->remote-access

3. 将 requre-encryption 设为 False
4. 使用vnc远程连接

原文網址：https://blog.csdn.net/jiaqi0109/article/details/78594568

# 其他
## 將 Ubuntu 家目錄資料夾的語言改為英文
```sh
export LANG=en_US
xdg-user-dirs-gtk-update
```
原文網址：https://blog.jaycetyle.com/2018/06/ubuntu-home-folder-lang/

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
原文連結：https://blog.csdn.net/AlexWang30/article/details/90341172
