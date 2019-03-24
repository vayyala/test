import os
import sys

def get_grade_script(student_email, assn_name):
  return '''"import os\\n",
    "test_output = [ok.grade(q[:-3]) for q in os.listdir('tests') if q.startswith('q')]\\n",
    "%run upload_tests.py {student_email} {assn_name} test_output\\n"'''.format(student_email=student_email, assn_name=assn_name)

def flatten(input_dir, output_dir):
  oldF = open(input_dir, 'r')
  newF = open(output_dir, 'w')
  student_email=input_dir.split('_')[0]
  assn_name=input_dir.split('_')[1].split('.')[0]
  for line in oldF:
    newF.write(line.replace("#_ = ok.submit()", get_grade_script(student_email, assn_name)).replace("\"\"", "\""))
  oldF.close()
  newF.close()

if __name__ == "__main__":
  flatten(sys.argv[1],sys.argv[2])
