GPIO：

```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup([腳位], GPIO.OUT)
GPIO.output([腳位],[1/0])
```