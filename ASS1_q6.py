#Program to convert seconds into minutes and seconds
time=int(input("Enter time in seconds"))
min=time//60
sec=time%60
print("Minutes are", min)
print("seconds are", sec)