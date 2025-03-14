# write code below!
import streamlit as st

st.title("my dog Nash Hot-Chiken Hicks is just a chill guy!!!!!!!")
if st.button ('goach gus does a flop'):
    st.video("./media/coach_gus_goes_flop.mp4")


with st.expander("Show Iris's code"):
    st.code(
        body='''
# write code below!
import streamlit as st

st.title("my dog Nash Hot-Chiken Hicks is just a chill guy!!!!!!!")
if st.button ('goach gus does a flop'):
    st.video("./media/coach_gus_goes_flop.mp4")
        ''',
        language="python",
        line_numbers=True
    )