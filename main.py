import video
import button
import light
import time

INPUT_PINS = (17, 69, 69)

OUTPUT_PINS = (23, 27, 22)


def main():
    vid = video.Video()
    start_button = button.InputButton(pin_number=INPUT_PINS[0])

    # all of the lights
    light_manager = light.LightManager(pins=OUTPUT_PINS)

    # map the creating a gif
    def light_show(channel):
        light_manager.final_countdown()
        vid.make_gif()
        light_manager.flash()

    start_button.add_onclick_callback(light_show)
    print('waiting forever...')
    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()
