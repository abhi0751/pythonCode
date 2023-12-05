import streamlit as st
import pandas as pd
import json
import os


with open("promptstore.json", 'r') as file:
 # Read the entire content of the file
 mapping_file_content = file.read()

Promptstoredf = pd.read_json(mapping_file_content)

selected_option = st.selectbox("Choose an option:", Promptstoredf["PromptHeading"])
result_row = Promptstoredf[Promptstoredf['PromptHeading'] == selected_option].iloc[0]
#st.write(result_row)

name_of_the_PromptFile = result_row['PromptFileName']
st.write(result_row['PromptShortDescription'])

#st.write(Promptstoredf)
    # Display the selected option
#st.write("You selected:", selected_option)



#st.write(name_of_the_PromptFile)

with open(name_of_the_PromptFile, 'r') as file:
 # Read the entire content of the file
 file_content = file.read()

#st.write(file_content)

user_input = st.text_area("Enter text:", value=file_content,height=200)


st.title("Select Box with Help Example")

    # Define options and corresponding help text
options = ["Option 1", "Option 2", "Option 3"]
help_text = {
        "Option 1": "This is help text for Option 1.",
        "Option 2": "This is help text for Option 2.",
        "Option 3": "This is help text for Option 3."
    }

    # Create a select box
selected_option = st.selectbox("Choose an option:", options)

with st.expander("Help"):
        # Display help text for the selected option
        st.write(help_text.get(selected_option, "No help text available."))

    # Display the selected option
st.write("You selected:", selected_option)


     # Button example
if st.button("Submit"):
        # Execute the processing function
       # template_text=process_comma_separated_string(final_Prompts_parameters,template_text)
        st.write(user_input)
        #process_submission("name, age, gender, subscribe, uploaded_file")


st.title("Streamlit Pop-up Box Example")

    # Button to trigger the "pop-up"


current_directory = os.getcwd()

st.write("Current Working Directory:", current_directory)

script_directory = os.path.dirname(os.path.abspath(__file__))

st.write("Script Directory:", script_directory)


 
fname=st.text_input("Enter file name to save your chat:")
 
filename = current_directory+"\\" + fname
st.write(filename)
st.write(file_content)



if st.button("save"):
    
   st.write(file_content)
   with open(filename, "w") as file:
        file.write(mapping_file_content)


 # Create an empty container

 