departments = ["Engineering", "Business", "Arts"]

courses = [
    [   # Engineering SUBJECT
        ["Algorithms", 3, 30, 28],
        ["Networks", 3, 25, 25],
        ["Databases", 2, 35, 10],
        ["AI Basics", 4, 20, 20]
    ],

    [   # Business SUBJECT
        ["Marketing", 3, 40, 38],
        ["Finance", 3, 30, 30],
        ["Management", 2, 35, 20],
        ["Economics", 4, 25, 25]
    ],

    [   # Arts SUBJECT
        ["History", 3, 30, 15],
        ["Philosophy", 3, 20, 20],
        ["Literature", 2, 25, 10],
        ["Fine Arts", 4, 20, 18]
    ]
]
d=0
count=0
while d<len(courses):
    dept_num=int(input("Enter department number (0-2, or -1 to exit): "))
    if (dept_num == -1):
        break

    if (dept_num==0 or dept_num==1 or dept_num==2):
        course_no=int(input("Enter course number (0-3):"))
        c=0       
        while c<len(courses):
            if(courses[dept_num][course_no][2]>courses[dept_num][course_no][3]):
               courses[dept_num][course_no][3]+=1
            #    courses[dept_num][course_no][2]-=1
               count+=1;
               print(f"Registered successfully for Algorithms! (Enrolled:{courses[dept_num][course_no][2]}/{courses[dept_num][course_no][3]})") 

            elif(courses[dept_num][course_no][2]==courses[dept_num][course_no][3]):
                print("Registration failed: Course is full.")
            c+=1
    d+=1
print(f"Total successful registrations this session: {count}")