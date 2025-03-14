# write code below!
import streamlit as st

st.title("What do you want to build today?")

if st.button('Arjun Slays'):
    st.video("./media/arjun_slays.mp4")

with st.expander("Show Arjun's code"):
    st.code(
        body='''
# write code below!
import streamlit as st

st.title("What do you want to build today?")

if st.button('Arjun Slays'):
    st.video("./media/arjun_slays.mp4")

        ''',
        language="python",
        line_numbers=True
    )