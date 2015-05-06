import subprocess
import os
import picamera


camera = None


def setup():
    # setup the camera and start the preview
    camera = picamera.PiCamera(resolution=(1280, 720))
    camera.start_preview()


def make_gif():
    camera.start_preview()
    camera.start_recording('video.h264')
    camera.wait_recording(3)
    # create the gif
    subprocess.check_output(["ffmpeg", "-i", "video.h264", "-vf", "scale=720:-1", "-t", "10", "-r", "10", "output.gif"])
    # clean up
    os.system("rm ~/video.h264")
