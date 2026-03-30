"""Video Editor Module"""

class VideoEditor:
    def __init__(self, video_path):
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)

    def resize(self, width, height):
        # Resize the video to the specified width and height
        pass

    def change_fps(self, fps):
        # Change the frames per second of the video
        pass

    def extract_frames(self):
        # Extract frames from the video
        pass

    def get_info(self):
        # Get information about the video
        pass
