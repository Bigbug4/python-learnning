from pynput.mouse import Controller, Button
from pynput import keyboard
import time

def on_press(key):
    try:
        print('alphanumeric key  {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        return False

m = Controller()

# mouse left click

def left_trick(click=2,interval=1):

     with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
       # listener. join()

        #for i in range(times):
        while True:
            #Double click
            m.click(Button.left, click)
            print('The current pointer position is {0}'.format(m.position))
            time.sleep(interval)

            if not listener.is_alive():
                break
            
        print('Exited!')

if __name__ == '__main__':

#    path=r'D:\PyCharm Community Edition 2017.2.1\python-learnning\pynput'
#    import os
#    os.chdir(path)
    
    left_trick()
