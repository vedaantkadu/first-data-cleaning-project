import pandas as pd

pf = pd.read_excel(r"C:\Users\Vedant Kadu\OneDrive\Desktop\Data Cleaning\Customer Call List.xlsx")
print(pf)

#checking the head
print(pf.head())

#getting the info of the dataset
print(pf.info())

#dropping the duplicate values
df = pf.drop_duplicates()
print(df)

#dropping un necessary coloums
df.drop(columns=["Not_Useful_Column"], inplace=True)
print(df)

#modifying the last_name
df["Last_Name"] = df["Last_Name"].str.strip("123._/")
print(df)

#modifying on the phone number
df["Phone_Number"] = df["Phone_Number"].str.replace(r"[^0-9]","",regex=True)
print(df)

#doing operation on the Phone_Number
df["Phone_Number"] = df["Phone_Number"].apply(lambda x :str(x)) #this line convert the phone number coloum to the str
df["Phone_Number"] = df["Phone_Number"].apply(lambda x : x[0:3] + "-" + x[3:6] + "-" + x[6:10]) 
df["Phone_Number"]=df["Phone_Number"].str.replace("nan--","")
df["Phone_Number"]=df["Phone_Number"].str.replace("--","")
print(df)

#working on the adress
df[["Street_Address","State","Zip_Code"]] = df["Address"].str.split(',',n=2,expand=True)
print(df)

#deleting the address coloum
df.drop(columns=["Address"],inplace=True)
print(df)

#replacing the y and n in the paying cusstomer
df["Paying Customer"] = df["Paying Customer"].str.replace("No","N", regex=True)
df["Paying Customer"] = df["Paying Customer"].str.replace("Yes","Y",regex=True)
df["Paying Customer"] = df["Paying Customer"].str.replace("N/a","",regex=True)
print(df)

#for Do_Not_Contact
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("Yes","Y",regex=True)
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("No","N",regex=True)
print(df)

#filling the null value
df.fillna("",axis=0, inplace=True)
print(df)

#now performing the operation on the do not contact
for x in df.index:
    if df.loc[x,"Do_Not_Contact"] == 'Y':
        df.drop(x, inplace=True)
print(df)

#phone number

for i in df.index:
    if str(df.loc[i, "Phone_Number"]).strip() == "":
        df.drop(i, inplace=True)
print(df)

df.reset_index(drop=True, inplace=True)
print(df.head())

df.drop(columns=["Zip_Code"],inplace=True)
print(df)
df.to_excel("Result_First_DataCleaning_edit.xlsx")
