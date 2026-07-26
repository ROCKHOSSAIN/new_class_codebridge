headlines = [
    "Sunday News",
    "Monday News",
    "Tuesday News",
    "Wednesday News",
    "Thursday News"
]
recent = headlines[-3:]
if len(headlines) >= 3:
    print(f"Total headlines: {len(headlines)}")
    print(f"Showing: {len(recent)}")
    print(recent)
    print(f"1: {recent[0].title()}")
    print(f"2: {recent[1].title()}")
    print(f"3: {recent[2].title()}")
else:
    print("Not enough news yet")

