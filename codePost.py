api_key = ''
course_name = 'New course'
course_period = '2019'
assn_name = 'NBody'
student_name = 'richard@codepost.io'
import requests
import codePost
try:
  assn = codePost.get_assignment_info_by_name(api_key, course_name, course_period, assn_name)
  sub = codePost.get_assignment_submissions(api_key, assn.id, student=student_name)
  f = codePost.post_file(api_key, sub.id, "test_output", String(grades), "txt")
  print(f)'''