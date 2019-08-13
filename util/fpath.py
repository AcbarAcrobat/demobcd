import os,sys

class FPATH:
    def ffpath(self):
        os.path.dirname('file')
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        CONFIG_PATH = os.path.join(ROOT_DIR, 'file/VIDEO_FILE.mp4')