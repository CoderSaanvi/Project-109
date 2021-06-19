import random
import plotly.figure_factory as ff
import statistics as ss
import plotly.graph_objects as go
import csv
import pandas as pd
df=pd.read_csv("StudentsPerformance.csv")
diceResult=df["reading score"].tolist()
mean=ss.mean(diceResult)
sd=ss.stdev(diceResult)
median=ss.median(diceResult)
mode=ss.mode(diceResult)
#fig.show()
print("Mean: ",mean)
print("Standard Deviation: ",sd)
print("Median: ",median)
print("Mode: ",mode)
firstsdStart,firstsdEnd=mean-sd,mean+sd
secondsdStart,secondsdEnd=mean-(2*sd),mean+(2*sd)
thirdsdStart,thirdsdEnd=mean-(3*sd),mean+(3*sd)
listofdatainfirstsd=[result for result in diceResult if result>firstsdStart and result<firstsdEnd]
listofdatainsecondsd=[result for result in diceResult if result>secondsdStart and result<secondsdEnd]
listofdatainthirdsd=[result for result in diceResult if result>thirdsdStart and result<thirdsdEnd]
print("List First: ",len(listofdatainfirstsd)*100.0/len(diceResult))
print("List Second: ",len(listofdatainsecondsd)*100.0/len(diceResult))
print("List Third: ",len(listofdatainthirdsd)*100.0/len(diceResult))
fig=ff.create_distplot([diceResult],["Result"])
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.05],mode="lines",name="Mean"))
fig.add_trace(go.Scatter(x=[firstsdStart,firstsdStart],y=[0,0.05],mode="lines",name="First sd"))
fig.add_trace(go.Scatter(x=[firstsdEnd,firstsdEnd],y=[0,0.05],mode="lines",name="First sd"))
fig.add_trace(go.Scatter(x=[secondsdStart,secondsdStart],y=[0,0.05],mode="lines",name="Second sd"))
fig.add_trace(go.Scatter(x=[secondsdEnd,secondsdEnd],y=[0,0.05],mode="lines",name="Second sd"))
fig.add_trace(go.Scatter(x=[thirdsdStart,thirdsdStart],y=[0,0.05],mode="lines",name="Third sd"))
fig.add_trace(go.Scatter(x=[thirdsdEnd,thirdsdEnd],y=[0,0.05],mode="lines",name="Third sd"))
fig.show()