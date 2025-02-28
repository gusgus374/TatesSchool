# write code below!
import streamlit as st

st.title("broke bones")

if st.button('broken bones'):
    st.video("./media/broken_bones.mp4")
   
with st.expander("Show Cruz's code"):
    st.code(
        body='''
# write code below!
import streamlit as st

st.title("broke bones")

if st.button('broken bones'):
    st.video("./media/broken_bones.mp4")
   
        ''',
        language="python",
        line_numbers=True
    )