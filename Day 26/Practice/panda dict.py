import pandas as pd
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}


df = pd.DataFrame(student_dict)
# print(df)
for index, rows in df.iterrows():
    print(rows)
