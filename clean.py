import pandas as pd
# import plotly.express as px

def modified(country):
    res = ""
    for i in country:
        if (i!="," and i!=" "):
            res+=i
    return res

pop = pd.read_csv("./pop.csv")
le = pd.read_csv("./lf.csv")
cm = pd.read_csv("./cm.csv")

n1 = len(pop)
n2 = len(le)
n3 = len(cm)

# pd.read_csv("./finaldata.csv")

fp = open("./finaldata.csv","w")

for i in range(n1):
    country1 = pop.loc[i,"country"]
    for j in range(n2):
        country2 = le.loc[j,"country"]
        if (country1==country2):
            for k in range(n3):
                country3 = cm.loc[k,"country"]
                if (country2 == country3):
                    for years in range(1990,2021):
                        years_ = str(years)
                        country = modified(country1)
                        x = str(pop.loc[i,years_])
                        y = str(le.loc[j,years_])
                        z = str(cm.loc[k,years_])
                        fp.write(x+","+y+","+z+","+years_+","+country+"\n")
fp.close()
