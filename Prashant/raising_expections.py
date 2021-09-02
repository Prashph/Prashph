def increment(num):
    try:
        return int(num) + 1 
    except:
        raise ValueError("Please enter a valid value")

a = increment('df543')
print(a)
