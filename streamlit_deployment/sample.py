from PIL import Image

import streamlit as st

st.success("Success")
st.info("Information")
st.warning("Warning")
st.error("Error")

exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)


st.write("Text with write")
# Writing python inbuilt function range()
st.write(range(10))


img = Image.open("./streamlit.png")
st.image(img, width=200)


if st.checkbox("Show"):
    st.text(">>   Showing Text after Checkbox tick !!")


status = st.radio("Select Gender:", ["Male", "Female"])
if status == "Male":
    st.success("Male")
else:
    st.error("Female")


hobby = st.selectbox("Select a Hobby:", ["Dancing", "Reading", "Sports"])
st.write("Your Hobby is: ", hobby)

hobbies = st.multiselect("Select Hobbies:", ["Dancing", "Reading", "Sports"])
st.write("You Selected", len(hobbies), "hobbies")


# A simple button that does nothing
st.button("Click Me")

# A button that displays text when clicked
if st.button("About"):
    st.text("Welcome to GeeksForGeeks!")


# Create a text input box with a default placeholder
name = st.text_input("Enter your name", "Write Anything...")

# Display the name after clicking the Submit button
if st.button("Submit"):
    result = name.title()  # Capitalize the first letter of each word
    st.success(result)


# Create a slider to select a level between 1 and 5
level = st.slider("Choose a level", min_value=1, max_value=100)

# Display the selected level
st.write(f"Selected level: {level}")
