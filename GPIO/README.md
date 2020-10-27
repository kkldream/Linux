
### Raspberry Pi 3 GPIO：
![Raspberry Pi 3 GPIO](https://github.com/kkldream/kk-repository/blob/master/Markdown_images/Raspberry%20Pi%203%20GPIO.png?raw=true)

GPIO：

```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup([腳位], GPIO.OUT)
GPIO.output([腳位],[1/0])
```