# write code below!
import streamlit as st

st.title('Me Win')
if st.button('EMILY DE GREAT turns on the JETS'):
    st.video('./media/emily_goal.mp4')
if st.button('SOCCER'):
    st.toast(":soccer:")

with st.expander("Show Emily's code"):
    st.code(
        body='''
# write code below!
import streamlit as st

st.title('Me Win')
if st.button('EMILY DE GREAT turns on the JETS'):
    st.video('./media/emily_goal.mp4')
if st.button('SOCCER'):
    st.toast(":soccer:")
        ''',
        language="python",
        line_numbers=True
    )