import video
import button
import light
import time
import twitter

INPUT_PINS = (17, 69, 69)

OUTPUT_PINS = (23, 27, 22)


def main():
    vid = video.Video()
    start_button = button.InputButton(pin_number=INPUT_PINS[0])

    # all of the lights
    light_manager = light.LightManager(pins=OUTPUT_PINS)

    twit = twitter.Twitter()

    # map the creating a gif
    def light_show(channel):
        light_manager.final_countdown()
        gif_path = vid.make_gif()
        light_manager.flash()
        twit.post_image(gif_path)
        print('cycle complete')

    start_button.add_onclick_callback(light_show)
    print('waiting forever...')
    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()
