# write code below!
import streamlit as st

st.title("What do you want to build today?")

if st.button('GOAL'):
    st.video("./media/goal_celebration.mp4")
    
with st.expander("Show Charlie's code"):
    st.code(
        body='''
# write code below!
import streamlit as st

st.title("What do you want to build today?")

if st.button('GOAL'):
    st.video("./media/goal_celebration.mp4")
    
        ''',
        language="python",
        line_numbers=True
    )