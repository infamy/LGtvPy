import serial

class LGtv():
    
    INPUT_DTV_ANT = 0x00
    INPUT_DTV_CBL = 0x01
    INPUT_AN_ANT = 0x10
    INPUT_AN_CBL = 0x11
    INPUT_AV = 0x20
    INPUT_AV1 = 0x20
    INPUT_AV2 = 0x21
    INPUT_COMP = 0x40
    INPUT_COMP1 = 0x41
    INPUT_COMP2 = 0x42
    INPUT_PC = 0x60
    INPUT_HDMI = 0x90
    INPUT_HDMI1 = 0x90
    INPUT_HDMI2 = 0x91
    INPUT_HMDI3 = 0x92

    RATIO_43 = 0x01
    RATIO_169 = 0x02
    RATIO_ZOOM = 0x04
    RATIO_PROGRAM = 0x06
    RATIO_JUST_SCAN = 0x09
    RATIO_CINEMA_ZOOM_1 = 0x10
    RATIO_CINEMA_ZOOM_2 = 0x11
    RATIO_CINEMA_ZOOM_3 = 0x12
    RATIO_CINEMA_ZOOM_4 = 0x13
    RATIO_CINEMA_ZOOM_5 = 0x14
    RATIO_CINEMA_ZOOM_6 = 0x15
    RATIO_CINEMA_ZOOM_7 = 0x16
    RATIO_CINEMA_ZOOM_8 = 0x17
    RATIO_CINEMA_ZOOM_9 = 0x18
    RATIO_CINEMA_ZOOM_10 = 0x10
    RATIO_CINEMA_ZOOM_11 = 0x1A
    RATIO_CINEMA_ZOOM_12 = 0x1B
    RATIO_CINEMA_ZOOM_13 = 0x1C
    RATIO_CINEMA_ZOOM_14 = 0x1D
    RATIO_CINEMA_ZOOM_15 = 0x1E
    RATIO_CINEMA_ZOOM_16 = 0x1F
    
    COLOR_MEDIUM = 0x0
    COLOR_COOL = 0x1
    COLOR_WARM = 0x2
    
    ENERGY_SAVING_OFF = 0x0
    ENERGY_SAVING_MINIMUM = 0x1
    ENERGY_SAVING_MEDIUM = 0x2
    ENERGY_SAVING_MAXIMUM = 0x3
    ENERGY_SAVING_SCREEN_OFF = 0x5

    def __init__(self, serialport, id=1):
        self.id = "%02X" % id
        self.ser = serial.Serial(serialport, 9600, timeout=1)

    def __sendCmd(self, cmd):
        self.ser.write(cmd)
        read = self.ser.readline()
        if read.find("OK") > 0:
            return True
        else:
            return False

    def powerOff(self):
        """Turn the TV off"""
        return self.__sendCmd('ka %s %02X\r' % (self.id, 0x0))
    
    def powerOn(self):
        """Turn the TV on"""
        return self.__sendCmd('ka %s %02X\r' % (self.id, 0x1))
    
    def inputSelect(self, input):
        """Select the TV's input"""
        return self.__sendCmd('xb %s %02X\r' % (self.id, input))
    
    def ratio(self, ratio):
        """Select the TV's ratio"""
        return self.__sendCmd('xc %s %02X\r' % (self.id, ratio))
    
    def screenMuteOff(self):
        """Screen mute off (video on)"""
        return self.__sendCmd('kd %s %02X\r' % (self.id, 0x0))
    
    def screenMuteOn(self):
        """Screen mute on (video off)"""
        return self.__sendCmd('kd %s %02X\r' % (self.id, 0x1))
    
    def screenMuteVideoOut(self):
        """Screen mute video out, but video is on"""
        return self.__sendCmd('kd %s %02X\r' % (self.id, 0x10))
    
    def volumeMuteOn(self):
        """Mute TV volume"""
        return self.__sendCmd('ke %s %02X\r' % (self.id, 0x0))
    
    def volumeMuteOff(self):
        """Unmute TV volume"""
        return self.__sendCmd('ke %s %02X\r' % (self.id, 0x1))
    
    def setVolume(self, level):
        """Set the volume, must be a level between 0 and 64"""
        if level > 64 or level < 0:
            raise ValueError
        return self.__sendCmd('kf %s %02X\r' % (self.id, level))
    
    def setContrast(self, level):
        """Set the contrast, must be a level between 0 and 64"""
        if level > 64 or level < 0:
            raise ValueError
        return self.__sendCmd('kg %s %02X\r' % (self.id, level))

    def setBrightness(self, level):
        """Set the brightness, must be a level between 0 and 64"""
        if level > 64 or level < 0:
            raise ValueError
        return self.__sendCmd('kh %s %02X\r' % (self.id, level))
    
    def setColor(self, level):
        """Set the color, must be a level between 0 and 64"""
        if level > 64 or level < 0:
            raise ValueError
        return self.__sendCmd('ki %s %02X\r' % (self.id, level))

    def setTint(self, level):
        """Set the tint, must be a level between 0 and 64"""
        if level > 64 or level < 0:
            raise ValueError
        return self.__sendCmd('kj %s %02X\r' % (self.id, level))

    def setSharpness(self, level):
        """Set the sharpness, must be a level between 0 and 64"""
        if level > 64 or level < 0:
            raise ValueError
        return self.__sendCmd('kk %s %02X\r' % (self.id, level))
    
    def OSDoff(self):
        """Turn off OSD"""
        return self.__sendCmd('kl %s %02X\r' % (self.id, 0x0))
    
    def OSDon(self):
        """Turn on OSD"""
        return self.__sendCmd('kl %s %02X\r' % (self.id, 0x1))

    def remoteControlLockModeOff(self):
        """Turn remote control lock off"""
        return self.__sendCmd('km %s %02X\r' % (self.id, 0x0))
    
    def remoteControlLockModeOn(self):
        """Turn remote control lock on"""
        return self.__sendCmd('km %s %02X\r' % (self.id, 0x1))
    
    def setTreble(self, level):
        """Set the treble, must be a level between 0 and 64"""
        if level > 64 or level < 0:
            raise ValueError
        return self.__sendCmd('kr %s %02X\r' % (self.id, level))

    def setBass(self, level):
        """Set the bass, must be a level between 0 and 64"""
        if level > 64 or level < 0:
            raise ValueError
        return self.__sendCmd('ks %s %02X\r' % (self.id, level))
    
    def setBalance(self, level):
        """Set the balance, must be a level between 0 and 64"""
        if level > 64 or level < 0:
            raise ValueError
        return self.__sendCmd('kt %s %02X\r' % (self.id, level))
    
    def setColorTemperature(self, color):
        """Set the color temperature"""
        return self.__sendCmd('ku %s %02X\r' % (self.id, color))
    
    def setEnergySaving(self, energy):
        """Set the energy saving"""
        return self.__sendCmd('jq %s %02X\r' % (self.id, energy))
    
    def autoConfig(self):
        """Trigger auto configuration"""
        return self.__sendCmd('ju %s %02X\r' % (self.id, 0x1))

    def setBacklight(self, level):
        """Set the backlight, must be a level between 0 and 64"""
        if level > 64 or level < 0:
            raise ValueError
        return self.__sendCmd('mg %s %02X\r' % (self.id, level))