# write code below!
import streamlit as st

st.title("Chace is cooking")

if st.button("I AM HIM"):
    st.video("./media/imHIM.mp4")

with st.expander("Show Chace's code"):
    st.code(
        body='''
# write code below!
import streamlit as st

st.title("Chace is cooking")

if st.button("I AM HIM"):
    st.video("./media/imHIM.mp4")

        ''',
        language="python",
        line_numbers=True
    )
