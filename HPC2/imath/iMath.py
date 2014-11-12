import os
from IPython.display import HTML


VIDEO_TAG_PARAM_2 = """<video controls>
 <source src="data:video/mp4;base64,{0}" type="video/mp4">
 Your browser does not support the video tag.
</video>"""


VIDEO_TAG_PARAM = """<video controls>
 <source src="getVideoContent/{username}/{video}" type="video/mp4">
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
	user_root = os.environ.get("USER_ROOT").split("/")[2];
	VIDEO_TAG = VIDEO_TAG_PARAM.format(username=user_root, video=videoPath);	
        return HTML(VIDEO_TAG)

    @staticmethod
    def display_video_2(videoPath):
	video = open(videoPath, "rb").read()
	VIDEO_TAG = VIDEO_TAG_PARAM_2.format(video.encode("base64"));	
        return HTML(VIDEO_TAG)

    

        
