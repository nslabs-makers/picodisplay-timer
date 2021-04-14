import utime
import picodisplay as display

buf = bytearray(display.get_width() * display.get_height() * 2)
display.init(buf)
display.set_backlight(0.8)

def convert(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    return "%d:%02d:%02d" % (hour, min, sec)

timeCount = 0

while True:
    
    display.set_pen(255, 255, 0) 
    display.clear()
    display.set_pen(0, 0, 0)  # Set pen to black 
    display.text("Timer", 10, 10, 240, 5)  # Add some text
    display.text("Press Y to Start", 10, 60, 240, 4)  # Add some text
    if display.is_pressed(display.BUTTON_A):
        display.set_pen(255, 255, 0)
        display.clear()
        timeCount += 60
        display.set_pen(0, 0, 0)                    # change the pen colour
        display.text(str(timeCount / 60)+" minutes", 10, 10, 240, 4)  # display some text on the screen
        display.update()                                  # update the display
        utime.sleep(0.5)                                    # pause for a sec
    elif display.is_pressed(display.BUTTON_B):
        display.set_pen(255, 255, 0)
        display.clear()
        timeCount -= 60
        display.set_pen(0, 0, 0)                    # change the pen colour
        display.text(str(timeCount / 60)+" minutes", 10, 10, 240, 4)  # display some text on the screen
        display.update()                                  # update the display
        utime.sleep(0.5)
    elif display.is_pressed(display.BUTTON_Y):
        timeFinal = timeCount
        print(timeFinal)
        for i in range(timeFinal):
            display.set_pen(255, 255, 0)
            display.clear()
            utime.sleep(1)
            display.set_pen(0, 0, 0)                    # change the pen colour
            display.text(str(convert(timeCount)), 10, 10, 240, 5)  # display some text on the screen
            display.update()
            timeCount -= 1
        display.set_pen(47, 210, 253)
        display.clear()
        display.set_pen(255, 255, 255) 
        display.text("Your timer is done!", 10, 10, 240, 5)  # display some text on the screen
        display.update()
        utime.sleep(6)
            
    display.update()
