import pandas as pd
data = {
    "names" : ["remo","sai","kiran","priya"],
    "marks" : [80,79,92,85],
    "age" : [20,19,21,19],
    "city" : ["hyd","chennai","mumbai","goa"]
}

df = pd.DataFrame(data)
print(df)