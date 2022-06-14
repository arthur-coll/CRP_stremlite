import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
from datetime import datetime

st.markdown("<h1 style='text-align: center; color: red;'>French Political Stability Index</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: white;'>Corporate Research Project</h2>", unsafe_allow_html=True)


#Image Creation
img1 = Image.open("data/ESSEClogo.jpg")
img2 = Image.open("data/Quantcubelogo.png")
img3 = Image.open("data/Centrale_logo.jpg")

col1, col2, col3 = st.columns([1.5,1.5,1.5])

with col1:
    st.image(img1,width=140)

with col2:
    st.image(img2,width=140)

with col3:
    st.image(img3,width=140)

st.markdown("<h3 style='text-align: center; color: white;'>Quantcube - ESSEC/CentraleSupelec</h3>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: white;'>Arthur COLL - Xinyu HU - Patrick LEYENDECKER - Saurajey VERMA - Ranqi ZHONG</h4>", unsafe_allow_html=True)

st.write("The scope of our research project follows the interdisciplinary concept of Geoeconomics, consisting of Geological and Economics and the impacts of politics on the stability of a region. Following the sometimes rather unpredictable developments of political decisions, such as Brexit or the election of Donald Trump as president of the United States, these events can have immediate or delayed effects on financial markets. As QuantCube offers a platform consisting in part of macro-economic and non-financial indicators to provide investors the option to gather a macroscopic view of various parameters in order to help make informed investment decisions.")
st.write("A numeric metric to measure and display the political development within a country could be of great value. These metric could entail the popularity of a government,the stability of a region and/or country or the rise of extremist parties. Our focus during our research was thus to develop an accurate and robust index that integrates well in the existing platform of QuantCube. ")
st.write("In the following plots we detail our result of developping an  index that measures the impact of the stability of politics within France, gathered from the analysis of social media data using Natural Language Processing Techniques and specifically focused on the 2017 presidential elections.")

#SideBar Creation
st.sidebar.title("Selection")
aggregation = st.sidebar.radio("Aggregation level", ["Monthly","Weekly","Daily"])


min_date = datetime(2016,12,10)
max_date = datetime(2017,4,30)
a_date = st.sidebar.date_input("Time Frame", (min_date, max_date))

scale = st.sidebar.checkbox("Fixed Scale", value=False)

#Data Loading
if aggregation == "Monthly":
    df=pd.read_csv("data/monthly.csv")
    var="month"
    
elif aggregation == "Weekly":
    df=pd.read_csv("data/weekly.csv")
    var="week"

else:
    df=pd.read_csv("data/daily.csv")
    var="day"
#Filter by date
df[var] = pd.to_datetime(df[var])
df = df.loc[(df[var].dt.date > a_date[0]) & (df[var].dt.date < a_date[1])]

st.title("Our Indicator")

#First Plot
f = plt.figure(1)
plt.plot(df[var],df["indicator"],"r")
plt.title('French Political Stability')
plt.xlabel(var)
plt.ylabel('Stability')
plt.xticks(rotation ='vertical',fontsize=8)
plt.grid(True)
if scale:
    plt.ylim(ymax = 1, ymin = 0)
st.pyplot(f)

st.title("Impact of politicians support on Social Media")

#Second Plot

#Filtering by candidates

col1,col2,col3,col4 = st.columns([2,2,2,2])
with col1:   
    macron = st.checkbox("Macron", value=True)
with col2:
    hamon = st.checkbox("Hamon", value=True)
with col3:
    lepen = st.checkbox("Le Pen", value=True)
with col4:
    fillion = st.checkbox("Fillion", value=True)

g = plt.figure(2)

plt.plot(df[var],df["indicator"], "r--_", label=" Our indicator")

if macron:
    plt.plot(df[var],df["macron"],color="orange", label="Center - Macron")
if hamon:
    plt.plot(df[var],df["hamon"], color="pink", label="Left - Hamon")
if lepen:
    plt.plot(df[var],df["lePen"], color="darkblue", label="Far Right - Le Pen")
if fillion:
    plt.plot(df[var],df["fillion"], color="skyblue", label="Left - Fillion")
    

#Plot creation
plt.title('Support of candidates on Social Media')
plt.xlabel(var)
plt.ylabel('Stability')
plt.xticks(rotation ='vertical',fontsize=8)
plt.grid(True)
plt.legend(loc='best', bbox_to_anchor=(0.9, 0.6, 0.5, 0.5))
if scale:
    plt.ylim(ymax = 1, ymin = 0)
st.pyplot(g)
