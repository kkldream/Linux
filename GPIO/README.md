## Raspberry Pi
### Raspberry Pi 2 & 3 GPIO：
![Raspberry Pi 3 GPIO](https://github.com/kkldream/Markdown/blob/main/image/Raspberry%20Pi%203%20GPIO.png)

### Python：
```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup([腳位], GPIO.OUT)
GPIO.output([腳位],[1/0])
```
