from  pynput.mouse import Button, Controller
import time 

mouse = Controller()
print(mouse.position)
time.sleep(3)
print('The current pointer position is {0}'.format(mouse.position))


#set pointer positon
mouse.position = (277, 645)
print('now we have moved it to {0}'.format(mouse.position))

#鼠标移动（x,y）个距离
mouse.move(5, -5)
print(mouse.position)

mouse.press(Button.left)
mouse.release(Button.left)

#Double click
mouse.click(Button.left, 1)

#scroll two  steps down
mouse.scroll(0, 500)

from pynput import mouse

def on_move(x, y ):
    print('Pointer moved to {o}'.format(
        (x,y)))

def on_click(x, y , button, pressed):
    print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    if not pressed:
        return False

def on_scroll(x, y ,dx, dy):
    print('scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

while True:
    with mouse.Listener( no_move = on_move,on_click = on_click,on_scroll = on_scroll) as listener:
        listener.join()