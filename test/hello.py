#!/usr/bin/env python3
from time import sleep
from ev3dev2.sound import Sound
import os
os.system('setfont Lat15-TerminusBold14')
# os.system('setfont Lat15-TerminusBold32x16')  # try this larger font

sound = Sound()

print('Hello World!')
print() # empty line
print('EV3', 'Python rules!')

#play a standard beep
sound.beep()

sleep(2) # pause for 2 seconds

# Play a SINGLE 2000 Hz tone for 1.5 seconds
sound.play_tone(2000, 1.5)

sleep(2)

# Play a SEQUENCE of tones
sound.tone([(200, 2000, 400),(800, 1800, 2000)])

sleep(2)

# Play a 500 Hz tone for 1 second and then wait 0.4 seconds
# before playing the next tone
# Play the tone three times
sound.tone([(500, 1000, 400)] * 3)

sleep(2)

#text to speech
sound.speak('Hello, my name is Auto Cat, nee ya!')

sleep(10)
