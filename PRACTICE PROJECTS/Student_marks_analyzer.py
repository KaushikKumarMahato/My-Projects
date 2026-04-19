# STUDENTS MARKS ANALYZER

# Calculate mean, median, max, min
def analyze(records):
    sorted_record = sorted(records , key =lambda x: (x["marks"]["Physics"] + x["marks"]["Chemistry"] + x["marks"]["Maths"]))
    

    marks =[(x["marks"]["Physics"] + x["marks"]["Chemistry"] + x["marks"]["Maths"]) for x in sorted_record ]
    
    mean = sum(marks)/len(marks)

    median = marks[len(marks)//2]

    max_marks = max(marks)

    min_marks = min(marks)

# Find topper & weakest subject
    topper = sorted_record[len(records)-1]
    weakest_subject_marks = min(topper["marks"]["Physics"],topper["marks"]["Chemistry"],topper["marks"]["Maths"])
    weakest_subject = [k for k,v in topper['marks'].items() if v == weakest_subject_marks]

    print(f"mean : {mean}")
    print(f"median : {median}")
    print(f"maximum marks : {max_marks}")
    print(f"minimum marks : {min_marks}")
    print(f"student with highest marks : {topper["name"]} and his/her weakest subject is : {weakest_subject[0]} with marks : {weakest_subject_marks}\n")
    



# Input marks of students in a dicrionary
student_records = [

    {"name": "Will" , "marks": {"Physics": 99  , "Chemistry": 95 ,"Maths": 100 } },

    {"name": "Mike" , "marks":{"Physics": 93 , "Chemistry": 98 , "Maths": 97 } },

    {"name": "Lucas" , "marks": {"Physics":  95, "Chemistry": 96 , "Maths": 97 } },

    {"name": "Dustin" , "marks": {"Physics": 100 , "Chemistry": 95 , "Maths": 100 } },

    {"name": "El" , "marks": {"Physics": 92, "Chemistry": 94 , "Maths": 96 } },

    {"name": "Max ", "marks": {"Physics": 92 , "Chemistry": 93 , "Maths": 97 } }
    ]

analyze(student_records)
