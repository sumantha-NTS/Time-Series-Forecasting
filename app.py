import pandas as pd
import streamlit as st
import statsmodels.api as sm 
import datetime
import plotly.express as px

def main():
    st.title("Forecasting the Particulate Matter (PM)")

    st.sidebar.header('Upload CSV file')
    uploaded_file = st.sidebar.file_uploader("Choose a file")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file,index_col=0,parse_dates=True)
        model = sm.tsa.statespace.SARIMAX(df,order=(1,0,1),seasonal_order=(1,0,1,24)).fit()

        if st.sidebar.button('Dataset Details'):
            
            st.write('Start date : ',df.index[0])
            st.write('End date : ',df.index[-1])
            st.write('Number of records = ',len(df))
            st.write('Sample data')
            st.write(df.head(5))
        
        if st.sidebar.button('Forecast for 24hours'):
            m = []
            start = df.index[-1]
            for j in range(0,24):
                date_generated = start + datetime.timedelta(hours=j+1)
                m.append(date_generated)
            new = pd.DataFrame(m,columns=['Date'])
            new.set_index("Date", inplace = True)
            df_new = pd.concat([df,new],axis=0)
            df_new['forecast'] = model.predict(start=len(df),end=len(df)+24)
            
            fig = px.line(df_new, x=df_new.index, y = df_new.columns,width =1000, title='Forecasting For next 24 Hours')
            st.plotly_chart(fig)

        if st.sidebar.button('Model Used'):
            st.subheader('SARIMA(1,0,1,24) model is used for Forecasting')

if __name__=='__main__':
    main()