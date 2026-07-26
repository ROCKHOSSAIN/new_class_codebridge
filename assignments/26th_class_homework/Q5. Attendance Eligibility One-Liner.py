def attendance_status(attended,total):
    attend=(attended/total)*100;
    return "eligible" if attend>=75 else "not eligible"

print(attendance_status(20, 26))
print(attendance_status(15, 26))
