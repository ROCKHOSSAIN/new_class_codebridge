tasks = ['Buy groceries', 'Call doctor', 'Pay bills'];
tasks.insert(0, 'Submit report');
tasks.remove('Call doctor');

print(tasks[0].upper())
print(tasks[1].upper())
print(tasks[2].upper())
if(len(tasks)>2):
     print("Busy day ahead!")
else:
    print("Light day")

