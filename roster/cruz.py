# write code below!
import streamlit as st

# write code below!
import streamlit as st

st.title("broke bones")

if st.button('broken bones'):
    st.video("./media/broken_bones.mp4")
    
st.image("./media/peashooter.gif")
   
with st.expander("Show Cruz's code"):
    st.code(
        body='''
# write code below!
import streamlit as st

st.title("broke bones")

if st.button('broken bones'):
    st.video("./media/broken_bones.mp4")
    
st.image("./media/peashooter.gif")
   
        ''',
        language="python",
        line_numbers=True
    )