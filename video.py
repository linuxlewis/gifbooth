import subprocess
import os
import picamera


class Video:

    def __init__(self):
        # setup the camera and start the preview
        self.camera = picamera.PiCamera(resolution=(1280, 720))
        self.camera.start_preview()
        self.current_overlay = 0

    def remove_overlay(self):
        """
        removes any overlays from the preview
        """
        self.camera

    def next_overlay(self):
        """
        removes the current overlay and adds the next one
        """
        self.current_overlay += 1

    def prev_overlay(self):
        """
        removes the current overlay and goes back one
        """
        self.current_overlay -= 1

    def make_gif(self):
        self.camera.start_preview()
        self.camera.start_recording('video.h264')
        self.camera.wait_recording(3)
        # create the gif
        subprocess.check_output(["ffmpeg", "-i", "video.h264", "-vf", "scale=720:-1", "-t", "10", "-r", "10",
                                 "output.gif"])
        # clean up
        os.system("rm ~/video.h264")
