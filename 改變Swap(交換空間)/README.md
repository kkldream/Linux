# 改變 Swap (交換空間)
    sudo nano /etc/dphys-swapfile

这里树莓派是默认的100Mb的交换空间，我们把它修改成4096，也就是4Gb。最尾有一个最大限制的参数–CONF_MAXSWAP，把它前面的井号标注去掉，并把这个参数也改成4096。

    sudo service dphys-swapfile restart