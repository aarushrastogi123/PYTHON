'''#Grading Program

student_scores={"Harry":81,"Ron":78,"Hermoine":99,"Draco":76,"Neville":66}
student_grades={}
print("\n",student_scores)
for key in student_scores:
    scores=student_scores[key]
    if scores>90:
        student_grades[key]="Outstanding"
    elif scores>80:
        student_grades[key]="Exceeds Expectations"
    elif scores>70:
        student_grades[key]="Acceptable"
    else:
        student_grades[key]="Fail"           

print("\n",student_grades)'''

#Travel log- nesting list in dictionary

capital={
    "India":"Delhi",
    "Japan":"Tokyo",
}

travel_log=[
    {
        "country":"India",
        "Places visited":["Delhi","Haryana"],
        "Times visited":12,
    }
]

print(travel_log)

