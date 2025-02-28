
import streamlit as st

st.title("Cooper Hogue")

if st.button('Cooper has a good kick'):
    st.video("./media/cooperH_goodkick.mp4") 
if st.button('Soccer'):
    st.toast(":soccer:")
if st.button('Cooper Gets an EZ steal'):
    st.video("./media/easy_steal.mp4")
if st.button('Perfect Assist'):
    st.video("./media/perfect_assist.mp4")


with st.expander("Show Cooper Hogue's code"):
    st.code(
        body='''
# write code below!
import streamlit as st

st.title("Cooper Hogue")

if st.button('Cooper has a good kick'):
    st.video("./media/cooperH_goodkick.mp4") 
if st.button('Soccer'):
    st.toast(":soccer:")
if st.button('Cooper Gets an EZ steal'):
    st.video("./media/easy_steal.mp4")
if st.button('Perfect Assist'):
    st.video("./media/perfect_assist.mp4")

        ''',
        language="python",
        line_numbers=True
    )