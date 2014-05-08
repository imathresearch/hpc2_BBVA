import os

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
        