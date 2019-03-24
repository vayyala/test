# One time -- done for all students
1) set env variable of cp_api_key="API_KEY"
2) run testing.py as the pre-processing script
  - Check to make sure that the student_email and assignment_name are being processed appropriately. Current implementation is that file must be named <student_email>_<assignment_name>.<ext>
3) Put the upload_tests.py file in the jupyerhub grader repository
  - Make sure that the course and course_period variables are appropriately set

#During Grading
1) When each student's file have run, run the final cell, which will run the upload_tests.py script, pushing the test outputs to codePost
