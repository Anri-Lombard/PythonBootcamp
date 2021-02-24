import pandas
import random
random_number = random.randint(1, 100)
# iterating through dataframes.
student_dict = {
    "students": ["Angela", "Anri", "Jeff", "Tim"],
    "scores": [random_number, random_number, random_number, random_number]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    print(row.students)
