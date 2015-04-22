import subprocess
import os
import twitter


def main():
    # record the video
    try:
        subprocess.check_output(["ffmpeg", "-f", "video4linux2", "-r", "24", "-s", "640x480", "-i",
                                 "/dev/video0", "raw.avi"], timeout=5)
    except subprocess.TimeoutExpired:
        pass
    # trim the bs lighting part
    subprocess.check_output(["ffmpeg", "-i", "raw.avi", "-ss", "00:00:01", "-async", "1", "cut.avi"])
    # create the gif
    subprocess.check_output(["ffmpeg", "-i", "cut.avi", "-vf", "scale=320:-1", "-t", "10", "-r", "10", "output.gif"])

    # clean up
    os.system("rm ~/raw.avi")
    os.system("rm ~/cut.avi")

    # UPLOAD to twitter
    t = twitter.Twitter()
    t.post_image("output.gif")
    os.system("rm ~/output.gif")

if __name__ == '__main__':
    main()
