

# Importing all necessary libraries
import cv2
import os
import argparse


def save_images(cam, dir, prefix):
    currentFrame = 0
    while(True):

        # reading from frame
        ret, frame = cam.read()

        if ret:
            # if video is still left continue creating images
            name = str(prefix) + str(currentFrame) + '.jpg'
            name = os.path.join(dir, name)
            print('Creating...' + name)

            # writing the extracted images
            cv2.imwrite(name, frame)

            # increasing counter so that it will
            # show how many frames are created
            currentFrame += 1
        else:
            break

    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows()


def main(args):
    cam = cv2.VideoCapture(args.video)
    try:

        # creating a folder named data
        if not os.path.exists(args.dataset_dir):
            os.makedirs(args.dataset_dir)

    # if not created then raise error
    except OSError:
        print('Error: Creating directory of data')

    # frame
    currentframe = 0
    save_images(cam, args.dataset_dir, args.prefix)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Script to sample a video into frames')
    parser.add_argument('--video', metavar='path', required=True,
                        help='the path to input video')
    parser.add_argument('--dataset_dir', default="datasets", metavar='path', required=False,
                        help='path to dataset')
    parser.add_argument('--prefix', default='frame', metavar='str', required=False,
                        help='prefix for name while saving the frames')
    args = parser.parse_args()
    main(args=args)
