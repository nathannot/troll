import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,11)
y = 2**x
fig, ax = plt.subplots()
ax.plot(x,y)
ax.set_title('Correlation between Android Users and Runners')
ax.set_xlabel('How much you like running on scale 1-10')
ax.set_ylabel('Likelihood of being Android User (%)')
ax.grid()

ans = st.selectbox('Select make of your phone',('Android','Iphone'),
                   placeholder = 'Select an option',
                   index = None
                   )

if ans == 'Android':
    st.write('Eww! You probably like running dont you')
    st.pyplot(fig)
    st.write('Graph shows the more you like running there is a 1000% chance you own an Android')
    st.write('This is mathematically impossible, conveying runners are not human')
elif ans == 'Iphone':
    st.write('You are a legend!')
