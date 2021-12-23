import os 

def beep(frequency, amplitude, duration):
    sample = 8000
    half_period = int(sample/frequency/2)
    beep = chr(amplitude)*half_period+chr(0)*half_period
    beep *= int(duration*frequency)
    audio =os.open('/dev/audio', 'wb')
    audio.write(beep)
    audio.close()


print(beep(500,20,200))
