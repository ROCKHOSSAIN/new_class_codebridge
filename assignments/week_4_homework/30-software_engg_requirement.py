python_score = int(input("Enter Python skill score: "))
problem_solving_score = int(input("Enter problem solving score: "))
communication = input("Enter communication skill (good/bad): ").lower()
experience = int(input("Enter years of experience: "))

if (python_score >= 80 and 
    problem_solving_score >= 75 and 
    communication == "good" and 
    experience >= 2):
    print("Selected for Final HR Round")
else:
    print("Not Selected")