# write code below!
import streamlit as st

st.title("vols win.JPN")
if st.button('vols win buttonnnnnn'):
    st.video("./media/vols_win.jpg")    
with st.expander("Show Jack's code"):
    st.code(
        body='''
# write code below!
import streamlit as st

st.title("vols win.JPN")
if st.button('vols win buttonnnnnn'):
    st.video("./media/vols_win.jpg")    
        ''',
        language="python",
        line_numbers=True
    )