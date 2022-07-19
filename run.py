import app
import time

if __name__ == '__main__':
    print('Runner started...')
    while True:
        time.sleep(0.2)
        app.outer.apply_async().get()
