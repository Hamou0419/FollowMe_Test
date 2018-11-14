def inter(a,b):
    result=list(set(a).intersection(set(b)))
    return sorted(result)

a = [1, 2, 3, 4, 5, 5, 8]
b = [1, 5, 8, 4]
print (inter(a,b))