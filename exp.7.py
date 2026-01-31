#Tahseen
#251P116
print("Tahseen")
print("251P116")
students = {
101:{"name": "john","grade":"A","attendence":90},102:{"name":"Alice","grade":"B","attendence":85},103:{"name":"Bob","grade":"A","attendence":95}}
students[104]={"name":"Charlie","grade":"B","attendence":80}
    
print(students)
students[101]["grade"]="A+"
print(students)
for student_id,details in students.items():
  print(f"ID:{student_id},Name:{details['name']},Grade:{details['grade']},Attendence:{details['attendence']}%")
  print(students.keys())
  print(students.values())
  print(students.items())
