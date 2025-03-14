# write code below!
import streamlit as st

st.title("What do you want to build today?")

st.title('justus_skills')
if st.button('Justus goes crazy'):
    st.video("./media/justus_skills.mp4")
    
    st.title('too_cool')
#if st.button('crazy'):
 #   st.video("./media/too_cool.mp4")
    

with st.expander("Show Justus's code"):
    st.code(
        body='''
# write code below!
import streamlit as st

st.title("What do you want to build today?")

st.title('justus_skills')
if st.button('Justus goes crazy'):
    st.video("./media/justus_skills.mp4")
    
    st.title('too_cool')
#if st.button('crazy'):
 #   st.video("./media/too_cool.mp4")
    
        ''',
        language="python",
        line_numbers=True
    )