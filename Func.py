def most_frequent(string):
    d=dict()
    for key in string:
        if key not in d:
            d[key]=1
        else:
            d[key]+=1
    sorted_orders = sorted(d.items(),key=lambda x:x[1],reverse=True)
    for i in sorted_orders
        print(i[0],i[1]

most_frequent("Mississippi")
