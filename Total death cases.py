import pandas as pd
import os
import openpyxl
import matplotlib.pyplot as plt
import numpy as np
# cases = pd.read_excel("C:\\Users\\Admin\\Documents.xlsx")
os.chdir("C:\\Users\\Admin\\Documents")
open("covidreports.xlsx")
cases = pd.read_excel("covidreports.xlsx")
plt.figure(figsize=(8,5))
plt.title("COVID-19 DEATHS (jan2021-jun2021)", fontdict={"fontweight":"bold"})
plt.plot(cases.month,cases.uk,'r.-',label="UK")
plt.plot(cases.month,cases.usa,'b.-',label="USA")
plt.plot(cases.month,cases.india,'g.-',label="INDIA")
plt.xticks(cases.month)
plt.xlabel("months")
plt.ylabel("number of deaths")
plt.savefig("total_cases.png",dpi=300)
plt.legend()
plt.show()