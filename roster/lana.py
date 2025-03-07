import streamlit as st

if st.button("Hi"):
    st.balloons()

st.title("hehehe")

if st.button("FLOP"):
    st.video("./media/coach_gus_goes_flop.mp4")

with st.expander("Show Lana's code"):
    st.code(
        body='''
import streamlit as st

if st.button("Hi"):
    st.balloons()

st.title("hehehe")

if st.button("FLOP"):
    st.video("./media/coach_gus_goes_flop.mp4")

        ''',
        language="python",
        line_numbers=True
    )