# set API key via %env cp_api_key = <API KEY>
import os

api_key = os.environ["cp_api_key"]
course_name = 'New course'
course_period = '2019'
student_name = sys.argv[1]
assn_name = sys.argv[2]
test_output = sys.arg[3]

import requests
import codePost
assn = codePost.get_assignment_info_by_name(api_key, course_name, course_period, assn_name)
sub = codePost.get_assignment_submissions(api_key, assn.id, student=student_name)
f = codePost.post_file(api_key, sub.id, "test_output", String(test_output), "txt")
print(f.id)
codePost.post_comment(api_key, f, "Final grade", 10, 0, 1, 1, 1)