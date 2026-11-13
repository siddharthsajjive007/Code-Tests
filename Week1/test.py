var = "[1,2,3,4,5],{23:'hello',24:'bye'},25"
a=var.strip().split("],")
print(eval(a[0]+"]"))
print(type(eval(a[0]+"]")))

b= (a[1].split('},'))
print(eval(b[0]+'}'))

print(type(eval(b[0]+'}')))

print(eval(b[1]))
print(type(eval(b[1])))

with open("benchmark_summary_targeted.csv" , 'r') as f:
    data = f.readlines()
    print((data[0].strip().split(',')))
    with open("gg.csv", "w") as new:
        new.write(data[0])