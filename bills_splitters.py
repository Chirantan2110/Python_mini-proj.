#customer names with their paid bills

names=["Madhu","Krish","Gopu","Shyam"]
bills=[50,250,60,100]

for name,amount in zip(names,bills):
    print(f"{name} paid {amount} rupess")