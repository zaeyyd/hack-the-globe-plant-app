import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
color = sns.color_palette()

import plotly.offline as py

import plotly.graph_objs as go
import plotly.express as px
import plotly.tools as tls

df = pd.read_csv("data.csv")

df_info= pd.DataFrame({"Dtype": df.dtypes, "Unique": df.nunique(), "Missing%": (df.isnull().sum()/df.shape[0])*100})

# total emissions size based scatterplot
food_df= df.groupby("Food product")['Total_emissions'].sum().reset_index()
t = go.Scatter(
    y = food_df.Total_emissions,
    x = food_df["Food product"],
    mode='markers',
    marker=dict(
        sizemode = 'diameter',
        sizeref = 1,
        size = food_df.Total_emissions*2,
        color = food_df.Total_emissions,
        colorscale='Portland',
        showscale=True
    )
)
data = [t]

layout= go.Layout(
    autosize= True,
    title= 'Total Emissions by Foods',
    hovermode= 'closest',
     xaxis= dict(
         ticklen= 5,
         showgrid=False,
        zeroline=False,
        showline=False
     ),
    yaxis=dict(
        title= 'Total Emissions',
        showgrid=False,
        zeroline=False,
        ticklen= 5,
        gridwidth= 2
    ),
    showlegend= False
)
figure = go.Figure(data=data, layout=layout)
figure.show()

# total emissions subplots 
temp_df= df.sort_values(by= "Total_emissions", ascending= True).iloc[:,:8]
figure, axis = plt.subplots(figsize=(15,20))
sns.set()
temp_df.set_index('Food product').plot(kind='barh', stacked=True, ax= axis)
plt.xlabel("Greenhouse gas Emissions")
plt.show()

# land use horizontal bar graph
land_df= df.dropna().sort_values(by= 'Land use per 1000kcal (m² per 1000kcal)', ascending= True)[['Food product','Land use per 1000kcal (m² per 1000kcal)']]

figure, axis = plt.subplots(figsize=(15,10))
sns.set()
land_df.set_index('Food product').plot(kind='barh', stacked=True, ax= axis, color= "sienna")
plt.xlabel("Land Use per 100 Kcal")
plt.title("Land Use by Foods per 1000 Kcal\n", size= 20)
plt.show()

#water usage horizontal bar graph
water_df= df.dropna().sort_values(by= 'Freshwater withdrawals per 1000kcal (liters per 1000kcal)', ascending= True)[['Food product',
       'Freshwater withdrawals per 1000kcal (liters per 1000kcal)']]

figure, axis = plt.subplots(figsize=(15,10))
sns.set()
water_df.set_index('Food product').plot(kind='barh', stacked=True, ax= axis, color= "lightblue")
plt.xlabel("Fresh Water Use litres per 1000kcal")
plt.title("Fresh Water Use by Foods per 1000Kcal \n", size= 20)
plt.show()

#eutrophication horizontal bar graph
eutrophication_df= df.dropna().sort_values(by= 'Eutrophying emissions per kilogram (gPO₄eq per kilogram)', ascending= True)[['Food product',
       'Eutrophying emissions per kilogram (gPO₄eq per kilogram)']]

figure, axis = plt.subplots(figsize=(15,10))
sns.set()
eutrophication_df.set_index('Food product').plot(kind='barh', stacked=True, ax= axis, color= "black")
plt.xlabel('Eutrophication emissions Per Kg')
plt.title('Food distribution by Eutrophication Emissions Per Kg \n', size= 20)
plt.show()

#emissions via transportation
plt.figure(figsize=(10,10))
temp = df.groupby('Food product')['Transport'].sum()
labels = (np.array(temp.index))
sizes = (np.array((temp / temp.sum())*100))
plt.pie(sizes, labels=labels, 
        autopct='%1.1f%%', startangle=200)
plt.title("Food distribution by transport emissions", fontsize=20)
plt.show()

#packaging required
plt.figure(figsize=(10,10))
temp = df.groupby('Food product')['Packging'].sum()
labels = (np.array(temp.index))
sizes = (np.array((temp / temp.sum())*100))
plt.pie(sizes, labels=labels, 
        autopct='%1.1f%%', startangle=200)
plt.title("Food distribution by relative packaging volume", fontsize=20)
plt.show()