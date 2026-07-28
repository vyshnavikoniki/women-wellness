import pandas as pd
import numpy as np

student_data = {
    'Name': ['John', 'Emma', 'Liam', 'Olivia', 'Noah'],
    'Roll Number': [1, 2, 3, 4, 5],
    'Age': [20, 19, 21, 20, 19],
    'Marks': [85, 95, 76, 92, 88],
    'Grade': ['B', 'A', 'C', 'A', 'B']
}
df = pd.DataFrame(student_data)
df.to_excel('student_records.xlsx', index=False)
print("Success: 'student_records.xlsx' created!\n")


loaded_df = pd.read_excel('student_records.xlsx')

marks_array = np.array(loaded_df['Marks'])
class_average = np.mean(marks_array)

print(f"--- Class Average: {class_average} ---\n")

top_students = loaded_df[loaded_df['Marks'] > 90]

print("Top Performing Students:")
print(top_students)