# write code below!
import streamlit as st

st.title("What do you want to build today?")

st.title("LALALA")
if st.button('YES'):
    st.video('./media/emily_dribble.mp4')
if st.button('SOCCER'):
    st.toast(":soccer:")
if st.button("jeufyfjdjhud"):
    st.balloons()

with st.expander("Show Emily's code"):
    st.code(
        body='''
# write code below!
import streamlit as st

st.title("What do you want to build today?")

st.title("LALALA")
if st.button('YES'):
    st.video('./media/emily_dribble.mp4')
if st.button('SOCCER'):
    st.toast(":soccer:")
if st.button("jeufyfjdjhud"):
    st.balloons()
        ''',
        language="python",
        line_numbers=True
    )