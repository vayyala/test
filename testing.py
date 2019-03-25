# Written for UCSB INT 5

import os
import sys
# install by 'pip install codePost'. Documentation can be found at https://github.com/codepost-io/codePost-python
import codePost

api_key = "<API - KEY>" # set API key via %env cp_api_key = <API KEY>
course_name = 'New course'
course_period = '2019'

def get_grade_snippet(student_email, assignment_name):
  return '''"import os\\n",
    "test_output = [ok.grade(q[:-3]) for q in os.listdir('tests') if q.startswith('q')]\\n",
    "%run upload_tests.py {student_email} {assignment_name} test_output\\n"'''.format(student_email=student_email, assignment_name=assignment_name)

from shutil import copyfile

def flatten(input_dir, output_dir, assignment):
    ## if output directory doesnt exist then create it
    if(not os.path.exists(output_dir)):
        os.mkdir(output_dir)
    if(not os.path.exists(output_dir+"_temp")):
        os.mkdir(output_dir+"_temp")
    temp_dir = output_dir + "_temp"
    for file in os.listdir(input_dir):
        ## Check for only ipynb
        print(file)
        if(file.endswith(".ipynb")):
            copyfile(input_dir+'/'+file, temp_dir+'/'+file)
            oldF = open(temp_dir+'/'+file, 'r')
            newF = open(output_dir+'/'+file, 'w')
            student_email=file.split('_')[0]
            for line in oldF:
                #newF.write(line.replace('_ = ok.auth(inline=True)', '#_ = ok.auth(inline=True)').replace("_ = ok.submit()", "#_ = ok.submit()").replace("4 = 2 + 2", "# 4 = 2 + 2").replace("six = two plus two", "# six = two plus two" ))
                newF.write(line.replace("#_ = ok.submit()", get_grade_snippet(student_email, assignment["name"])).replace("\"\"", "\""))
            oldF.close()
            newF.close()

            # upload to codePost
            upload_notebook(file, open(temp_dir+'/'+file, 'r').read(), student_email, assignment)

            os.remove(temp_dir+'/'+file)
            # print(student_dir+'_'+file)
    os.rmdir(output_dir + "_temp")
    # pass

def upload_notebook(file_name, file_code, student_email, assignment):
    print(student_email)
    file_to_upload = {"name": file_name, "code": file_code, "extension": "ipynb"}
    # syntax: upload_submission(api_key, assignment, students, files, mode=DEFAULT_UPLOAD_MODE)
    result = codePost.upload_submission(api_key, assignment, [student_email], [file_to_upload], codePost.UploadModes.OVERWRITE)
    if (result):
        print("Successfully uploaded notebook for %s" % student_email)

if __name__ == "__main__":
    assignment = codePost.get_assignment_info_by_name(api_key, course_name, course_period, sys.argv[3])
    if(not assignment):
        print(assignment)
        raise Exception("No Assignment found with the given name and course info. Please check to make sure the name is correct.")

    # flatten('./ucsb-int5-fa18-hw01','./ucsb-int5-fa18-hw01_flatten')
    flatten(sys.argv[1],sys.argv[2], assignment)
