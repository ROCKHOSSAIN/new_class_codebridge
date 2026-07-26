subjects= ['Math', 'Science', 'English']
grades= ['Grade 10', 'Grade 11']
scores = [
    [
    [72, 85, 61, 90],  
    [55, 48, 79, 83],  
    [88, 91, 74, 65],       
    ],
    [
    [95, 88, 77, 69],  
    [60, 72, 85, 91], 
    [45, 78, 83, 90]  
    ]

]
print("========================================")
print("EXAM SCORE REPORT")
print("========================================")
g=0
average=0
highest_score=0
highest_grade=" "
highest_subject=" "
count=0
highest_student = 0
row=" "
while g<len(scores):
    print("\nGrade:",grades[g])

    s=0
    while(s<len(subjects)):
        average=0
        row=subjects[s] + " | "+"scores : "

        st=0
        while(st<len(scores[g][s])):

            row = row + str(scores[g][s][st]) + " "
            average+=scores[g][s][st]

            if(scores[g][s][st]<50):
                count+=1
            if(scores[g][s][st]>highest_score):
                highest_score=scores[g][s][st]
                highest_grade = grades[g]
                highest_subject=subjects[s]
                highest_student=st+1
            

            st+=1

        
        print(row+" | " + "Average: "+str(average/4))
        s+=1
    
    g+=1
print("\n========================================")

print("Highest score:", highest_score)
print("Grade:", highest_grade, "| Subject:", highest_subject, "| Student", highest_student)
print("Failing students (below 50):", count)
