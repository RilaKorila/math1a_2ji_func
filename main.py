import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


# sidebarについて
st.sidebar.latex(r'''y = a(x-p)^2 + q''')

# Forms can be declared using the 'with' syntax
with st.form(key='my_form'):
    a_input = st.sidebar.slider(
        'a = ',
        -3.0, 3.0, 0.1
    )
    p_input = st.sidebar.slider(
        'p = ',
        -30.0, 30.0, 0.0
    )
    q_input = st.sidebar.slider(
        'q = ',
        -30.0, 30.0, 0.0
    )
    # inputを数字に限定するエラー処理

    # Every form must have a submit button.
    submit_button = st.form_submit_button(label='Check')
    if submit_button:
        x = np.linspace(-100.0,100.0,1000)
        fig = plt.figure()
        ax = fig.add_subplot(111)

        ax.set_xlim([-30.0, 30.0])
        ax.set_ylim([-50.0, 50.0])
        
        ax.plot(x, a_input*(x - p_input)**2.0 + q_input)
        ax.axhline(linewidth=1, color='black')
        ax.axvline(linewidth=1, color='black')
        st.pyplot(fig)


