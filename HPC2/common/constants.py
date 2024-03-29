'''
Created on 12/12/2013

@author: iMath
'''

import os

def constant(f):
    '''
    Decorator to indicate that a property of a class is a constant, so, cannot be set, only get
    '''
    def fset(self, value):
        raise SyntaxError
    def fget(self):
        return f()
    return property(fget, fset)


def deprecated(package="", instead=""):
    '''
    A decorator to indicate that the function or method called is deprecated. It calls anyway the function, but displays a message 
    in the console indicating it
    
    'package' is the optional package or class name where the deprecated function is called
    'instead' is the optional parameter containing the new function that should be called instead of the deprecated one 
    '''
    
    def wrap(f):
        def newF(*args, **kwargs):
            nameFunc = f.__name__
            part1=""
            part2=""
            if package!="":
                part1 = package + "."
            if instead!="":
                part2 = "Use " + package + "." + instead + " instead."
        
                print "Function " + part1 + nameFunc + " is deprecated. " + part2
            return f(*args, **kwargs)
        
        return newF
    return wrap

class CONS(object):
    '''
    It define the global constants for the Colossus core
    
    '''
    '''
    @constant
    def ROOT_FILE_SYSTEM():
        return "/iMathCloud"
    '''
    
    @constant
    def LOCALHOST():
        return "127.0.0.1"
    
    @constant
    def CONFIGFILE():
        return "/etc/hpc2/hpc2.config/config.properties"

    @constant
    def HOSTFILE():
        return "/etc/hpc2/hpc2.config/host_file.txt"
        
    
    @constant
    def PLUGINNAME():
        return "HPC2.plugin"
    
    @constant
    def MAINPLUGIN():
        return "main"
    
    @constant
    def HTTP():
        return "http://"
    
    @constant
    def RESULTRESP():
        return "/iMathCloud/rest/plugin_service/output"
        #return "/com.iMathCloud/rest/plugin_service/output"
        
    @constant #ammartinez
    def RESULTRESPJOBPYTHON():
        return "/iMathCloud/rest/joblang_service/resultJob/exec"
    
    @constant
    def SEPARATOR():
        return "|#|"
    
    ''' 
    @constant
    def EXECUTION_DIR():
        C = CONS()
        return os.path.join(C.ROOT_FILE_SYSTEM, "exec_dir");
    
    
    @constant
    def FILECLIENTDATA():
        C = CONS()
        path_to_fileclientdata = "data/data.txt"
        return os.path.join(C.SHAREIMATHCLOUD,path_to_fileclientdata)
    
    @constant
    #ELIMINAR
    def SHAREIMATHCLOUD():
        return "/mount_iMathCloud"
    '''
    @constant
    def RSCRIPT():
        return "Rscript"
    
    @constant
    def OCTAVESCRIPT():
        return "octave"
    
    '''
    @constant
    def VIRTUALENV_ABS():
        C = CONS();
        return os.path.join(C.SHAREIMATHCLOUD, C.VIRTUALENV)
    
    @constant
    def PYTHONVIRTENV():
        C = CONS()
        #path_to_pythonenv = "colossus/virt_env/virt1/bin/python"
        #return os.path.join(C.SHAREIMATHCLOUD, path_to_pythonenv);
        
        path_to_pythonenv = "bin/python"
        return os.path.join(C.VIRTUALENV_ABS, path_to_pythonenv);
        #return "/iMathCloud/colossus/virt_env/virt1/bin/python"
        
    @constant
    def VIRTUALENV():
        return "environments/virt2"
        
    
    @constant
    def SSHCONFIG():
        return "/home/andrea/.ssh/config"
        
    @constant
    def PATH_TEMP_FILES():
        C = CONS();
        return os.path.join(C.SHAREIMATHCLOUD, "temp");
    '''
    