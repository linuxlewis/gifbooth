import video
import button
import time


def main():
    video.setup()
    button.setup()
    # map the creating a gif
    button.add_button_handler(video.make_gif)
    print('waiting forever...')
    while True:
        time.sleep(1)


if __name__ == '__main__':
    main()
