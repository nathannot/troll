import streamlit as st

ans = st.selectbox('Select make of your phone',('Android','Iphone'),
                   placeholder = 'Select an option',
                   index = None
                   )

if ans == 'Android':
    st.write('Eww! You probably like running dont you')
elif ans == 'Iphone':
    st.write('You are a legend!')