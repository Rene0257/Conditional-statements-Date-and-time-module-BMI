work = int(input("Total number of working days: "))
absent = int(input("Number of days absent: "))

present = work-absent
percent = round((present*100)/work,2)

if percent<75:
    print("Attendance: ", percent, " .You are not eligible to give the exam")
else:
    print("Attendance: ", percent, " .You are eligible to give the exam")
