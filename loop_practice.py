study_minutes = [25, 40, 60, 35, 90, 50]
total = 0
for minutes in study_minutes:
    total+=minutes;

print(f"Total study time: {total} minutes")
average = total/len(study_minutes)
print(f"Average study duration: {average} minutes")