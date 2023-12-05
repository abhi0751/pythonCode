import streamlit as st
import pandas as pd
import json
import os


# Generate FileName With current directory
def filenameForSavingContent(filename):
    current_directory = os.getcwd()
    return current_directory+"\\" + filename

def savePromptToFile(contentToSave,filename):
    filenameTosave=filenameForSavingContent ("savedPrompt"+"\\"+filename)
    with open(filenameTosave, "w") as file:
        file.write(contentToSave)

def saveChatHistoryToFileAsJson(contentToSave,filename):
    filenameTosave=filenameForSavingContent ("savedSessionHistory"+"\\"+filename)

    json_str = json.dumps(contentToSave, indent=4)
    with open(filenameTosave, "w") as json_file:
       json.dump(json_str, json_file)

def readFileContent(filename):
    with open(filename, 'r') as file:
    # Read the entire content of the file
     return file.read()

def GetTheNameOfPromptFileFromStore(promptStoreJsonFile,prompt_Heading):
    pandas_prompt_df=pd.read_json(promptStoreJsonFile)
    result_row = pandas_prompt_df[pandas_prompt_df['PromptHeading'] == prompt_Heading].iloc[0]
    #st.write(result_row)
    name_of_the_PromptFile = result_row['PromptFileName']
    return name_of_the_PromptFile

def GetTheNameOfPromptFileFromStore(PandasDataFrame,coloumnHeaderName,prompt_Heading):
    result_row = PandasDataFrame[PandasDataFrame[coloumnHeaderName] == prompt_Heading].iloc[0]
    #st.write(result_row['PromptShortDescription'])
    name_of_the_PromptFile = result_row['PromptFileName']
    return name_of_the_PromptFile

def ConvertPromptStoreToPandadDF(prompt_store_Json_content):
    return pd.read_json(prompt_store_Json_content)

def readPromptFrpmPromptFile(name_of_the_PromptFile):
    name_of_the_PromptFile="promptStore"+"\\"+ name_of_the_PromptFile
    return readFileContent(name_of_the_PromptFile)


# Read the entire content of the file
mapping_file_content = readFileContent("promptstore.json")

Promptstoredf =  ConvertPromptStoreToPandadDF(mapping_file_content) # pd.read_json(mapping_file_content)
 
selected_option = st.selectbox("Choose an option:", Promptstoredf["PromptHeading"])


name_of_the_PromptFile = GetTheNameOfPromptFileFromStore(Promptstoredf,"PromptHeading",selected_option)    #result_row['PromptFileName']

#st.write(result_row['PromptShortDescription'])
st.write(name_of_the_PromptFile)

#st.write(Promptstoredf)
#  Display the selected option
#st.write("You selected:", selected_option)



#st.write(name_of_the_PromptFile)



 # Read the entire content of the file
stored_Prompt = readPromptFrpmPromptFile(name_of_the_PromptFile)

#st.write(file_content)

user_input = st.text_area("Enter text:", value=stored_Prompt,height=200)



     # Button example
if st.button("Submit"):
        # Execute the processing function
       # template_text=process_comma_separated_string(final_Prompts_parameters,template_text)
        st.write(user_input)
        #process_submission("name, age, gender, subscribe, uploaded_file")


st.title("Streamlit Pop-up Box Example")



script_directory = os.path.dirname(os.path.abspath(__file__))

st.write("Script Directory:", script_directory)


 
fname=st.text_input("Enter file name to save your chat:")
 

st.write(mapping_file_content)



if st.button("save"):
    
   st.write(user_input)
  
   savePromptToFile(mapping_file_content,fname)
   saveChatHistoryToFileAsJson(mapping_file_content,fname)


 # Create an empty container

 