import streamlit as st
st.title('LALALA')
if st.button('YES!'):
    st.video('./media/emily_dribble.mp4')
if st.button('SOCCER'):
    st.toast(":soccer:")
if st.button("jeufyfud"):
    st.ballons()
with st.expander("Show Emily's code"):
    st.code(
        body='''
st.title('LALALA')
if st.button('YES!'):
    st.video('./media/emily_dribble.mp4')
if st.button('SOCCER'):
    st.toast(":soccer:")
if st.button("jeufyfud"):
    st.ballons()
        ''',
        language="python",
        line_numbers=True
    )