A python class that uses pyserial to control an LG tv (**LH30 or better).

It's fairly straight forward to use. 

```python
#the following will use ttyUSB0 and turn the tv off.
#you need pySerial installed for this to work.
import LGtv

tv = LGtv.LGtv('/dev/ttyUSB0')
tv.powerOff()
```