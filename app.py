import pandas as pd
import streamlit as st
import pickle
import statsmodels.api as sm 
import datetime
import plotly.express as px

model = pickle.load(open('model.pkl','rb'))


def main():
    st.title("Forecasting the Particulate Matter (PM)")
    
    st.sidebar.header('Importing the CSV file')
    uploaded_file = st.sidebar.file_uploader("Choose a file")
    if uploaded_file is not None:
        df = pd.read_excel(uploaded_file,index_col=0,parse_dates=True)
        model1 = sm.tsa.statespace.SARIMAX(df,order=(1,0,1),seasonal_order=(1,0,1,24)).fit()
        
        #b1, b2, b3 = st.beta_columns(3)
        if st.sidebar.button('Dataset Detils'): 
            
            st.write('Start date : ',df.index[0])
            st.write('End date : ',df.index[-1])
            st.write('Number of records = ',len(df))
            
            
            st.write('Sample data')
            st.write(df.head(5))
        
        if st.sidebar.button('Forecast for 24hours'):
            m = []
            #start = datetime.datetime.strptime("20-04-2018", "%d-%m-%Y")
            
            start = df.index[-1]
            for j in range(0,24):
                date_generated = start + datetime.timedelta(hours=j+1)
                m.append(date_generated)
            new = pd.DataFrame(m,columns=['Date'])
            new.set_index("Date", inplace = True)
            df_new = pd.concat([df,new],axis=0)
            df_new['forecast'] = model1.predict(start=len(df),end=len(df)+24)
            
            fig = px.line(df_new, x=df_new.index, y = df_new.columns,width =1000, title='Forecasting For next 24 Hours')
            st.plotly_chart(fig)

            st.write(df_new)
        
        
        if st.sidebar.button('AQI Standards'):
            from PIL import Image
            image = Image.open('AQI.jpg')
            st.header('AQI Standards')
            st.image(image)

if __name__=='__main__':
    main()