import os
import sys
import requests
# install by 'pip install codePost'. Documentation can be found at https://github.com/codepost-io/codePost-python
import codePost

api_key = os.environ["cp_api_key"] # set API key via %env cp_api_key = <API KEY>
course_name = 'New course'
course_period = '2019'
student_email = sys.argv[1]
assn_name = sys.argv[2]
test_output = sys.argv[3]

upload_test_output(api_key, course_name, course_period, student_name, assn_name, test_output)

def upload_test_output(api_key, course_name, course_period, student_name, assn_name, test_output):
    # Find Assignment
    assn = codePost.get_assignment_info_by_name(api_key, course_name, course_period, assn_name)
    if(not assn):
        raise Exception("No Assignment found with the given name and course info. Please check to make sure the names are correct.")

    # Find Submission for student
    sub = codePost.get_assignment_submissions(api_key, assn['id'], student=student_email)
    if(len(sub) != 1):
        raise Exception("No submission found for this student and assignment.")

    # Parse the test output to the format desired to upload to codePost
    test_output_to_be_uploaded = parse_test_output(test_output)

    # Upload test output to codePost
    new_file = codePost.post_file(api_key, sub[0]['id'], "test_output", str(test_output_to_be_uploaded), "txt")

    # Add comments to file
    add_comments(api_key, test_output, new_file)

def parse_test_output(test_output):
    """
    Given a test output file and returns the file to be uploaded to codePost
    NOTE: THIS FUNCTION SHOULD BE EDITED BASED ON DESIRED USER BEHAVIOR
    """
    # example: returns full test output
    return test_output

def add_comments(api_key, test_output, file):
    """
    Adds comments to a codePost file, given an API Key, output to parse for comments, and a file object
    NOTE: THIS FUNCTION SHOULD BE EDITED BASED ON DESIRED USER BEHAVIOR
    """
    # example: posts a single comment
    # syntax: post_comment(api_key, file, text, pointDelta, startChar, endChar, startLine, endLine, rubricComment=None)
    # pointDelta is parsed as a negative. e.g., a pointDelta of 1 is -1 on codePost
    codePost.post_comment(api_key, f, "Final grade", 10, 1, 2, 1, 1)
