import os
from IPython.display import HTML


VIDEO_TAG_PARAM = """<video controls>
 <source src="data:video/x-m4v;base64,{0}" type="video/mp4">
 Your browser does not support the video tag.
</video>"""

class iMath():
    
    def __init__(self):
        pass
    
    @staticmethod
    def imath_file(file_path):
        user_root = os.environ.get("USER_ROOT");
        parts_file_path = file_path.split("/");
        #We avoid the lash
        no_absolute_file_path = "/".join(parts_file_path[1:])
        return os.path.join(user_root, no_absolute_file_path);
   
    @staticmethod
    def display_video(videoPath):
	video = open(videoPath, "rb").read()
	VIDEO_TAG = VIDEO_TAG_PARAM.format(video.encode("base64"));	
        return HTML(VIDEO_TAG)

        
