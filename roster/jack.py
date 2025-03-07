# write code below!
import streamlit as st

st.title("Max")
if st.button('Max'):
    st.image("./media/vols_win.jpg")
if st.button ('BALLOONS'):
        st.toast (':balloons:')
st.balloons ()


with st.expander("Show Jack's code"):
    st.code(
        body='''
# write code below!
import streamlit as st

st.title("Max")
if st.button('Max'):
    st.image("./media/vols_win.jpg")
if st.button ('BALLOONS'):
        st.toast (':balloons:')
st.balloons ()   
        ''',
        language="python",
        line_numbers=True
    )