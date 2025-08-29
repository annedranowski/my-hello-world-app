import streamlit as st

st.title('🎈 App Name')

st.write('Hello world!')

with st.sidebar:
    st.header("About app")
    st.write("This is my first app!")

st.header("Welcome to My Streamlit App", divider="rainbow")

# Add text
st.markdown("This is a simple app to demonstrate Streamlit features.")

st.subheader("st.columns")
col1, col2 = st.columns(2)

with col1:
    # Add a slider
    x = st.slider("Choose a value", 0, 100, 50)

with col2:
    # Display the selected value: descriptive text is optional
    st.write("The value of :blue[***x***] is:", x)

# Data viz

st.subheader("Random Data Visualization")

df = pd.DataFrame(rng(0).standard_normal((20, 3)), columns=["a", "b", "c"])

st.area_chart(df)
