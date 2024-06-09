import csv

# Read the input CSV file
input_file = 'students_marks.csv'
output_file = 'processed_marks.csv'

students = []
subjects = []

with open(input_file, mode='r') as file:
    csv_reader = csv.DictReader(file)
    subjects = csv_reader.fieldnames[1:]
    for row in csv_reader:
        students.append(row)

# Calculate average marks for each student
for student in students:
    marks = [int(student[subject]) for subject in subjects]
    average_mark = sum(marks) / len(marks)
    student['Average Mark'] = round(average_mark, 2)

# Calculate average marks for each subject
subject_averages = {}
for subject in subjects:
    total_marks = sum(int(student[subject]) for student in students)
    subject_averages[subject] = round(total_marks / len(students), 2)

# Identify the student with the highest average mark
highest_avg_student = max(students, key=lambda x: x['Average Mark'])['Student Name']

# Identify the subject with the highest average mark
highest_avg_subject = max(subject_averages, key=subject_averages.get)

# Write the results to the output CSV file
with open(output_file, mode='w', newline='') as file:
    fieldnames = ['Student Name', 'Average Mark', 'Highest Mark Student', 'Subject Name', 'Subject Average Mark', 'Highest Mark Subject']
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    csv_writer.writeheader()
    
    for i, student in enumerate(students):
        row = {
            'Student Name': student['Student Name'],
            'Average Mark': student['Average Mark'],
            'Highest Mark Student': highest_avg_student if i == 0 else '',
            'Subject Name': highest_avg_subject if i == 0 else '',
            'Subject Average Mark': subject_averages[highest_avg_subject] if i == 0 else '',
            'Highest Mark Subject': highest_avg_subject if i == 0 else ''
        }
        csv_writer.writerow(row)
