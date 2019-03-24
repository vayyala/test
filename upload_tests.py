# set API key via %env cp_api_key = <API KEY>
import os
import sys
import requests
import codePost

api_key = os.environ["cp_api_key"]
course_name = 'New course'
course_period = '2019'
student_name = sys.argv[1]
assn_name = sys.argv[2]
test_output = sys.argv[3]

assn = codePost.get_assignment_info_by_name(api_key, course_name, course_period, assn_name)
print(assn)
sub = codePost.get_assignment_submissions(api_key, assn['id'], student=student_name)
print(sub)
f = codePost.post_file(api_key, sub[0]['id'], "test_output", str(test_output), "txt")
print(f['id'])
codePost.post_comment(api_key, f, "Final grade", 10, 1, 2, 1, 1)