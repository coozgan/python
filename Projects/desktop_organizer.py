import os
import time
import platform
import argparse
import logging


def main():
    # Determines the Desktop Directory on Unix Base System and Windows
    if is_windows():
        path_to_watch = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    else:
        path_to_watch = os.path.join(
            os.path.join(os.path.expanduser('~')), 'Desktop')
    before = dict([(f, None) for f in os.listdir(path_to_watch)])
    args = parse_args()
    video_path = os.path.join(path_to_watch, 'Videos')
    picture_path = os.path.join(path_to_watch, 'Pictures')
    misc_path = os.path.join(path_to_watch, 'Misc')

    # Assign my Parse Arguments
    if args.path:
        path_to_watch = args.path
    if args.pic:
        picture_path = args.pic
    if args.video:
        video_path = args.video
    if args.misc:
        misc_path = args.misc

    # The loop for event notification
    while 1:
        time.sleep(1)
        after = dict([(f, None) for f in os.listdir(path_to_watch)])
        added = [f for f in after if not f in before]
        if added:
            for files in added:
                src_path = os.path.join(path_to_watch, files)
                if not os.path.isdir(src_path):
                    if file_type(files) == 'VIDEO':
                        moved_to_path(src_path, os.path.join(video_path, files))
                    elif file_type(files) == 'PICTURE':
                        moved_to_path(src_path, os.path.join(picture_path, files))
                    elif file_type(files) == 'MISC':
                        moved_to_path(src_path, os.path.join(misc_path, files))

# Function for moving the file to desired path
def moved_to_path(source_file, destination_file):
    logging.basicConfig(filename='file_organizer.log', level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    dest_path = '/'.join(destination_file.split('/')[:-1]) + '/'
    if not os.path.exists(dest_path):
        os.mkdir(dest_path)
        print(f"the Path {dest_path} CREATED")
        logging.info(f'{dest_path} folder has been CREATED!!!')
    os.rename(source_file, destination_file)
    logging.info('The directory {} is moved to {}'.format(source_file, destination_file))


# Function that will identify what is the file type
def file_type(filename):
    video_type = ['mp4', 'avi', 'mkv', 'flv', 'webm', 'mov', 'swf', 'ogg', 'm4p', 'm4v']
    picture_type = ['jpg', 'jpeg', 'gif', 'png', 'heic']
    type_of_file = filename.split('.').pop().lower()
    if type_of_file in video_type:
        return 'VIDEO'
    elif type_of_file in picture_type:
        return 'PICTURE'
    else:
        return 'MISC'


# Arguments
def parse_args():
    parser = argparse.ArgumentParser(
        description='This is an Automated Script for Moving Files to Specific Folder. NOTE that the directory must be created when you run the script')
    parser.add_argument('-p', '--path', help='The Folder to Track')
    parser.add_argument('-v', '--video', metavar='Path/to/Video/Directory', help='Video Files Directory')
    parser.add_argument('-P', '--pic', metavar='Path/to/Picture/Directory', help='Picture files Directory')
    parser.add_argument('-m', '--misc', help='Other Files', metavar='Path/to/Misc/Directory')
    args = parser.parse_args()
    return args


# Identify if the platform is on windows
def is_windows():
    return platform.system() == 'Windows'


if __name__ == '__main__':
    main()
