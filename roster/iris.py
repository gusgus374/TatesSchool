# write code below!
import streamlit as st

st.title("My dog is da best")
if st.button ('SOCCER'):
        st.toast (':soccer:')
if st.button ('BALLOONS'):
        st.toast (':balloons:')
st.balloons ()

with st.expander("Show Iris's code"):
    st.code(
        body='''
import streamlit as st

st.title("My dog is da best")
if st.button ('SOCCER'):
        st.toast (':soccer:')
if st.button ('BALLOONS'):
        st.toast (':balloons:')
st.balloons ()
        ''',
        language="python",
        line_numbers=True
    )