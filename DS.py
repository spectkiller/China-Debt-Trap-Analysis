print("Importing Modules")

import numpy as np
import pandas as pd



print("Save both CSV in different variables")

df = pd.read_csv('https://github.com/spectkiller/PythonChinaDebtTrap.github.io/releases/download/1.0/chinese.debt.trap.all.over.the.world.-.projects.csv')
df2 = pd.read_csv('https://github.com/spectkiller/PythonChinaDebtTrap.github.io/releases/download/1.0/chinese.debt.trap.in.Africa.sector.wise.csv')



print("Analysé the data")

print(df.head())
print("\n")

print(df2.head())
print("\n")


print ("column info")

print(df.info())
print ("\n")

print(df2.info())
print ("\n")



print ("Total Money spent in other countries by China")

perYear = df[["YEAR" ,"AMOUNT"]]
perYear2 = df2[["Year", "$ Allocation"]]

print(perYear.head())
print("\n")

print(perYear2.head())
print("\n")


#I decided to convert the columns to Numpy arrays to better treat the data
npAmount = np.array(perYear['AMOUNT'])
npAllocation = np.array(perYear2['$ Allocation'])


#To convert 'Amount' to INT we need to clean the data
#I made a for loop to iterate over the list created previously and replace the letters and symbols with 0's if needed (Everything is converted to Millions)

lista = []

for i in npAmount:
    if i[-1] == 'B':
        i = i[:-1]
        i = i.replace('.','')
        i = i + '000'
        i = i[1:]
        lista.append(i)
    else:
        i = i[:-1]
        i = i[1:]
        lista.append(i)
intAmount = [int(x) for x in lista]

#Here are the first 5 examples of the result

print(npAmount[:5])
print(intAmount[:5])


#Also need to convert YEAR from object to INT

npYear = np.array(df['YEAR'])
list = []
for i in npYear:
    list.append(i)

intYear = [int(x) for x in npYear]


#Create a new dataframe containing the list created before
data = {'YEAR': intYear,
        'AMOUNT': intAmount}

perYearClean = pd.DataFrame(data)
perYearClean


#Combine the repeated Year values and sum them to calculate the total spent every year

perYearGrouped = perYearClean.groupby("YEAR").agg(sum)
perYearGrouped


#We repeat the procedure with the other CSV file

perYear2.head()


npYear2 = np.array(df2['Year'])
intYear2 = [int(x) for x in npYear2]


lista2 = []

for i in npAllocation:
    if i[-1] == 'B':
        i = i[:-1]
        i = i.replace('.','')
        i = i + '000'
        i = i[1:]
        lista2.append(i)
    else:
        i = i[:-1]
        i = i[1:]
        i = i.replace(',','')
        lista2.append(i)

for i in range(len(lista2)):
    intAllocation = [int(x) for x in lista2]
    

data2 = {'YEAR': intYear2,
        'AMOUNT': intAllocation}

perYearClean2 = pd.DataFrame(data2)
print(perYearClean2.head())


perYearGrouped2 = perYearClean2.groupby("YEAR").agg(sum)
print(perYearGrouped2)



print("Append Dataframe")


#Combine both cleaned dataframes to get the total money spent each year

perYearCombined = pd.concat([perYearGrouped, perYearGrouped2])

perYearCombined["AMOUNT"] = perYearCombined["AMOUNT"].astype(int)
perYearCombinedFinal = perYearCombined.groupby(["YEAR"]).sum()

print(perYearCombinedFinal)

#Simple Panda plot

print(perYearCombinedFinal.plot(kind = 'bar'))



print("Money Invested by Other Countries")


#Select the columns to use in the new dataframe

datos = [df['Country'], perYearClean['AMOUNT']]
headers = ["COUNTRY", "AMOUNT"]
perCountry = pd.concat(datos, axis=1, keys=headers)


#Add repeated values to calculate the total for each country

perCountryGrouped = perCountry.groupby("COUNTRY").agg(sum)
print(perCountryGrouped.head())


#Do the same with the other CSV file

datos2 = [df2['Country'], perYearClean2['AMOUNT']]
headers2 = ["COUNTRY", "AMOUNT"]
perCountry2 = pd.concat(datos2, axis=1, keys=headers)



perCountryGrouped2 = perCountry2.groupby("COUNTRY").agg(sum)
print(perCountryGrouped2.head())



print("Append DataFrames")

perCountryCombined = pd.concat([perCountryGrouped, perCountryGrouped2])
perCountryCombined["AMOUNT"] = perCountryCombined["AMOUNT"].astype(int)
perCountryCombinedFinal = perCountryCombined.groupby(["COUNTRY"]).sum()


print(perCountryCombinedFinal)
print("\n")


print("Plot the result")

print(perCountryCombinedFinal.plot(kind = 'bar', width=0.8, figsize=(94,8)))




