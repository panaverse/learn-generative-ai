# import module
import streamlit as st
 
# Title
st.title("This is a title")

# Header
st.header("This is a header") 
 
# Subheader
st.subheader("This is a subheader")

# Text
st.text("Hello this is text")

# Markdown
st.markdown("### This is a markdown")

# success
st.success("Success")
 
# success
st.info("Information")
 
# success
st.warning("Warning")
 
# success
st.error("Error")
 
# Exception - This has been added later
exp = ZeroDivisionError("Trying to divide by Zero")
st.exception(exp)

# Write text
st.write("Text with write")
 
# Writing python inbuilt function range()
st.write(range(10))

# Display Images
 
# import Image from pillow to open images
from PIL import Image
img = Image.open("streamlit.png")
 
# display image using streamlit
# width is used to set the width of an image
st.image(img, width=200)

# checkbox
# check if the checkbox is checked
# title of the checkbox is 'Show/Hide'
if st.checkbox("Show/Hide"):
    # display the text if the checkbox returns True value
    st.text("Showing the widget")


# radio button
# first argument is the title of the radio button
# second argument is the options for the radio button
status = st.radio("Select Gender: ", ('Male', 'Female'))
 
 
# conditional statement to print 
# Male if male is selected else print female
# show the result using the success function
if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")


