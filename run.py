import app
import time

if __name__ == '__main__':
    print('Runner started...')
    while True:
        time.sleep(0.2)

        # Both of these would trigger the bug
        # app.outer.apply_async().get()
        app.outer.apply_async()
