
# Student Attendance Eligibility Checker
# Static Version for Docker

print("=" * 50)
print("       STUDENT ATTENDANCE ELIGIBILITY CHECKER")
print("=" * 50)

# Fixed student details
name = "Samarth K"
usn = "BCA001"
course = "BCA"
semester = 2

# Fixed attendance details
total_classes = 100
attended_classes = 60

# Calculate attendance percentage
attendance_percentage = (attended_classes / total_classes) * 100

# Determine eligibility
if attendance_percentage >= 85:
    category = "Excellent Attendance"
    status = "Eligible"
elif attendance_percentage >= 75:
    category = "Satisfactory Attendance"
    status = "Eligible"
else:
    category = "Attendance Shortage"
    status = "Not Eligible"

# Calculate additional classes required to reach 75%
required_classes = 0

if attendance_percentage < 75:
    while (
        (attended_classes + required_classes)
        / (total_classes + required_classes)
    ) * 100 < 75:
        required_classes += 1

# Display report
print("\nSTUDENT DETAILS")
print("-" * 50)
print("Name       :", name)
print("USN        :", usn)
print("Course     :", course)
print("Semester   :", semester)

print("\nATTENDANCE DETAILS")
print("-" * 50)
print("Total Classes     :", total_classes)
print("Classes Attended  :", attended_classes)
print(f"Attendance        : {attendance_percentage:.2f}%")
print("Category          :", category)
print("Eligibility       :", status)

if required_classes > 0:
    print("Additional classes needed:", required_classes)
else:
    print("Additional classes needed: 0")

print("=" * 50)
print("         REPORT GENERATED SUCCESSFULLY")
print("=" * 50)
