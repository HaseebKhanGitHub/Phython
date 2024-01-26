# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 08:33:23 2024

@author: khanb
"""

# Sample data (replace this with your actual data)
students_data = [
    (1, 2.86),(2, 2.7),(3, 3.17),(4,3.4 ),(6,2.66 ),(7,3.44 ),(8,2.5 ),(9, 3.59),(11, 3.27),(14, 2.3),(15, 2.67),
    (16, 2.44),(18, 3.42),(20, 3.42),(21, 2.47),(22, 2.26),(23, 1.88),(25, 1.91),(28, 3.73),(29, 2.87),(30, 2.62),(31, 3.53),
    (32, 2.89),(33,3.68),(36, 3.17),(39, 2.36),(40, 3.36),(41, 2.94),(43, 3.23),(44, 3.63),(45, 2.58),(46, 3.02)
    
]

# Sort students based on CGPA in descending order
sorted_students = sorted(students_data, key=lambda x: x[1], reverse=True)

# Calculate rank based on CGPA
for i, (student_id, cgpa) in enumerate(sorted_students, start=1):
    print(f"Student_ID: {student_id}, CGPA: {cgpa}, Rank: {i}")
