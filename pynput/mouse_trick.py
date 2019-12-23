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

def left_trick(click=2,interval=1,times=1000,loop=0):

     with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:

        if loop:
            while True:
                m.click(Button.left, click)
                print('The current pointer position is {0}'.format(m.position))
                time.sleep(interval)

                if not listener.is_alive():
                    break
        else:
            for i in range(times):
                m.click(Button.left, click)
                print('The current pointer position is {0}'.format(m.position))
                time.sleep(interval)

                if not listener.is_alive():
                    break

        print('Exited!')

def is_null(arg1, arg2):

    arg1 = int(arg1) if(arg1.strip() != '') else arg2

    return arg1

if __name__ == '__main__':

#    path=r'D:\PyCharm Community Edition 2017.2.1\python-learnning\pynput'
#    import os
#    os.chdir(path)

    click = input('Please input click type(options:2(default)| 1):')
    click = is_null(click,2)
    interval = input('Please input interval time(default:1):')
    interval = is_null(interval,1)
    times = input('Please input click times(default:1000):')
    times = is_null(times,1000)
    loop = input('Choose an endless loop or not(options:0(default)| 1):')
    loop = is_null(loop,0)

    left_trick(click=click,interval=interval,times=times,loop=loop)

