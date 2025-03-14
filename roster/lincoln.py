# write code below!
import streamlit as st

st.title("What do you want to build today?")
if st.button('Arjun scores'):
    st.video("./media/arjun_scores.mp4")
#if st.button('bread roll'):
#    st.("./downloads/bread.gif")
with st.expander("Show Lincoln's code"):
    st.code(
        body='''
# write code below!
import streamlit as st

st.title("What do you want to build today?")
if st.button('Arjun scores'):
    st.video("./media/arjun_scores.mp4")
#if st.button('bread roll'):
#    st.("./downloads/bread.gif")
        ''',
        language="python",
        line_numbers=True
    )