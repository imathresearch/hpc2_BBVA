# (C) 2013 iMath Research S.L. - All rights reserved.

""" Implements the class JobPython, a sub class of the class Job

Authors:

@author iMath
"""
from pprint import pprint

import imp
import os
import shutil

import subprocess

from job import Job
from HPC2.exception.exceptions import HPC2Exception

from urlparse import urlparse # ammartinez to parse the name of the python file
from HPC2.common.util.jobUtils import JobUtils
from HPC2.common.util.parseProperties import ParseProperties


from HPC2.common.constants import CONS 

CONS=CONS()
prop = ParseProperties()


class JobPython(Job):
    '''
    Extends:
        Class Job from Colossus.core.job
    Creation:
        JobPython(jobInfo) 
            jobInfo: Class JobInfo from Colossus.core.job
    '''
    
    
    def __init__(self, jobInfo):
        super(JobPython,self).__init__(jobInfo)

    def execute(self):
        
        self.secureThread();
        old_path = os.getcwd();
        
        #1. First the job execution dir is obtained
        ju = JobUtils()
        user_root_dir = ju.getUserRootDir(self.getUserName())             
        job_execution_dir = ju.getJobLocalExecutionDir(self.getIdJob(), self.getUserName())
       
        #2. The complete user file system is copied to the job execution dir
        ju.copyUserDirToJobDir(user_root_dir, job_execution_dir)
        snp = ju.snapshotDir(user_root_dir)
        
        #3. The complete path of job to execute is obtained
        original_code_to_execute = self.getPathNameSourceFile()       
        local_code_to_execute = original_code_to_execute.replace(user_root_dir, job_execution_dir)
        
        #4. The name of the std file is stablished
        file_name,file_ext = self.getNameExtSourceFile() #os.path.splitext(os.path.split(self.getSourceFile())[-1])
        dir_code_execution = os.path.dirname(local_code_to_execute)
        file_out = str(self.getIdJob()) + "_" + file_name + ".out";
        file_err = str(self.getIdJob()) + "_" + file_name + ".err";
        path_file_out = os.path.join(dir_code_execution + '/' + file_out)
        path_file_err = os.path.join(dir_code_execution + '/' + file_err)
        try:
            outfd = open( path_file_out, 'w+');
            errfd = open( path_file_err, 'w+');
        except:
            raise
        
        try:                     
            #5. The job is executed
            if file_ext.lower() == '.py':
              
                #EXECUTE PROCESS
                os.chdir(dir_code_execution);
                os.environ["USER_ROOT"] = user_root_dir;
                os.environ["COLLECTION_NAME"] = str(self.getIdJob()) + "_" + self.getUserName();
                print "-----"
                print ParseProperties.PYTHON_VIRTUALENV
                print "---- " + prop.getProperty(ParseProperties.PYTHON_VIRTUALENV)
                subprocess.call([prop.getProperty(ParseProperties.PYTHON_VIRTUALENV), local_code_to_execute], stdout=outfd, stderr=errfd, env=os.environ, shell=False);
               
                
                if os.path.getsize(path_file_out) == 0:
                    os.remove(path_file_out)
                
                if os.path.getsize(path_file_err) == 0:
                    os.remove(path_file_err)
         

            elif file_ext.lower() == '.pyc':
                
                os.chdir(dir_code_execution);
                subprocess.call(["python", local_code_to_execute], stdout=outfd, stderr=errfd, shell=False);
                
                if os.path.getsize(path_file_out) == 0:
                    os.remove(path_file_out)
                
                if os.path.getsize(path_file_err) == 0:
                    os.remove(path_file_err)
                
            else:
                msg = "Unexpected error: ", "Trying to execute a Non-Python file"
                raise HPC2Exception(msg)
            
            #6. Compare the state of the execution dir with the previous state before the execution
            [tocopy_files, tocopy_dirs, toDB_files, toDB_dirs] = ju.compareSnapshotDir(snp, job_execution_dir)
            
            #7. Copy files and directories
            for f in tocopy_files:
                shutil.copy2(os.path.join(job_execution_dir, f), os.path.join(user_root_dir, f))
                
            for d in tocopy_dirs:
                shutil.copytree(os.path.join(job_execution_dir, d),os.path.join(user_root_dir, d))
                
            #8. Add as job output
            for f in toDB_files:
                self.addOutputFile(os.path.join("/", f));
            
            for d in toDB_dirs:
                self.addOutputDir(os.path.join("/", d))
                     
            shutil.rmtree(job_execution_dir)
            os.chdir(old_path);
        except:
            raise
        finally:
            outfd.close()
            errfd.close()
            #os.seteuid(currentUID)
            #os.setegid(currentGID)  
        return 1