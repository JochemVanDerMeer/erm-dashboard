import pandas as pd
 
df = pd.read_excel('opstelling.xlsx')
 
df = df.astype(str)
res = []

for i in range(21):
    temp = "https://erm-dashboard.onrender.com/add/"
    
    if i == 20:
        temp += df['#'][i] + "/" + df["Van"][i] + "/" + df["Naar"][i] + "/" + str(round(float(df["Afstand"][i]))) + "/" + df["Stuur"][i] + "/" + df["Slag"][i] + "/" + df["Boeg"][i] + "/" + "-" + "/" + "-" + "/" + "-"
    elif i == 0:
        temp += df['#'][i] + "/" + df["Van"][i] + "/" + df["Naar"][i] + "/" + str(4000) + "/" + df["Stuur"][i] + "/" + df["Slag"][i] + "/" + df["Boeg"][i] + "/" + df["Stuur"][i+1] + "/" + df["Slag"][i+1] + "/" + df["Boeg"][i+1]
    else:
        temp += df['#'][i] + "/" + df["Van"][i] + "/" + df["Naar"][i] + "/" + str(round(float(df["Afstand"][i]))) + "/" + df["Stuur"][i] + "/" + df["Slag"][i] + "/" + df["Boeg"][i] + "/" + df["Stuur"][i+1] + "/" + df["Slag"][i+1] + "/" + df["Boeg"][i+1]
    res.append(temp)

res_df = pd.DataFrame(res)

res_df.to_excel("urls.xlsx", index=False)