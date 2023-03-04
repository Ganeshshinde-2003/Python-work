# Write a Pandas program to import excel data into a Pandas DataFrame and find a list of employees
# where hire_date is between two specific months and year.
import numpy as np
import pandas as pd

# data = pd.read_csv("hire_date.csv")

# hire = (data["hire_date"]>"10-11-2003") & (data["hire_date"]<"31-12-2004")
# print(hire)
# data2 = data[hire]
# print(data2[['emp_id',"first_name","last_name"]])
# arr = np.array([[1,2,3,4],[5,6,7,8]])
# data = pd.DataFrame(arr)
# print(data)
# # newdata = data.loc[[1]]-data.loc[[0]]
# # print(newdata)
# arr2 = np.array(data.iloc[[1]])
# print(arr2)
# arr3 = np.array(data.iloc[[0]])
# print(arr3)
# print(arr2-arr3)

arr = np.array([["gani","appu","manju"],[19,23,16],["24-04-2003","03-11-2000","25-10-2005"],["M","M","M"]])
# col = ["12","112","12"]
# row = ["X","Y","Z","w"]
# dataaa = pd.DataFrame(arr,row,col)
# print(dataaa)
arr2 = pd.DataFrame(arr,["name","age","dob","gender"],["first","sec","third"])
arr2.to_csv("data.csv")
csvfile = pd.read_csv("data.csv")
print(csvfile)
print(csvfile.loc["1","first"])
# data = pd.read_csv("hire_date.csv")
# print(data)
# hire_date = [(data["hire_date"]>"01-01-2000")&(data["hire_date"]<"30-11-2003")]
# print(hire_date)
# data["hire_date"] = pd.to_datetime(data["hire_date"])
# elig = data["hire_date"]>"01-01-2000"
# print(elig)