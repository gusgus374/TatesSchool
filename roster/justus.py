import streamlit as st

st.title('Justus_skills')
if st.button('Justus goes crazy'):
    st.video("./media/justus_skills.mp4")
if st.button('Soccer'):
    st.toast(":soccer:")
    
    st.balloons()

with st.expander("Show Justus's code"):
    st.code(
        body='''
# write code below!
import streamlit as st

st.title('Justus_skills')
if st.button('Justus goes crazy'):
    st.video("./media/justus_skills.mp4")
if st.button('Soccer'):
    st.toast(":soccer:")
    
    st.balloons()
        ''',
        language="python",
        line_numbers=True
    )