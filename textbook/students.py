def search_student(num):
  stu_no = [39, 14, 67, 105]
  stu_name = [ "justin", "john", "mike", "summer" ]
  for i in range(0, len(stu_no)):
    if(num == stu_no[i]):
      return stu_name[i]

print(search_student(14))
print(search_student(39))
print(search_student(67))
  