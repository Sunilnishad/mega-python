def clockMirror(hour,minute):
    time = 11/2*hour + 30*minute
    return time
hr = int(input("Enter Hour: "))
m = int(input("Enter Minute: "))
print("Exact time is  :",clockMirror(hr,m))
