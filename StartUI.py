import streamlit as st
import pandas as pd

# declare some demo data
dataSet1 = {
    'applicationid': 'App1',
    'technical-stack': 'Don NetFramework1.1, SQL Server 2008, MSMQ',
    'scalabilityneed': 'Highly Scalable',
    'compliances': 'HIPAA , GDPR',
    'targetplateform': 'Azure'
}

dataSet2 = {
    'applicationid': 'App2',
    'technical-stack': 'Python, Flask, PostgreSQL',
    'scalabilityneed': 'Low',
    'compliances': 'HIPAA',
    'targetplateform': 'AWS'
}

dataSet3 = {
    'applicationid': 'App3',
    'technical-stack': 'Java, Oracle, Rabitt MQ',
    'scalabilityneed': 'High',
    'compliances': 'PCI DSS, GDPR , HIPPA',
    'targetplateform': 'Azure'
}

def process_submission(name, age, gender, subscribe, uploaded_file):
    # Add your processing logic here
    st.success(f"Processing Submission...\nName: {name}\nAge: {age}\nGender: {gender}\nSubscribe: {subscribe}")

    # If a file is uploaded, read its contents and pass to another function
    if uploaded_file is not None:
        file_contents = uploaded_file.read()
        # Pass the file contents to another function
        process_file_contents(file_contents)

def process_file_contents(contents):
    # Add your logic for processing the file contents
    st.write("File Contents:")
    st.code(contents)



def switch_demoset(case):
    if case == 'dataSet1':
        return  pd.DataFrame([dataSet1])
    elif case == 'dataSet2':
       return  pd.DataFrame([dataSet2])
    elif case == 'dataSet3':
        return  pd.DataFrame([dataSet3])
    else:
        return 'This is the default case'




# Define your Python function
def loadDemoData(selected_value):
    # Replace this with your actual function logic


    df = switch_demoset(selected_value)
   # st.write(df)
    result = f"You selected: {selected_value}"
    return df

def process_comma_separated_string(input_string,original_text):
    """
    Process a comma-separated string and print each element.

    Parameters:
    - input_string (str): The comma-separated string.
    """
    st.write(input_string)
    elements = input_string.split(',')
    
    for element in elements:
        # Process each element as needed
       st.write(element)
       final_string=  replace_string(original_text, "[{element}]", element)  # .strip() removes leading and trailing whitespaces
       return final_string


def replace_string(original_text, old_substring, new_substring):
    """
    Replace occurrences of old_substring with new_substring in the original_text.

    Parameters:
    - original_text (str): The original text.
    - old_substring (str): The substring to be replaced.
    - new_substring (str): The replacement substring.

    Returns:
    - str: The modified text.
    """
    modified_text = original_text.replace(old_substring, new_substring)
    return modified_text

def create_comma_separated_string(*dynamic_values):
    """
    Create a comma-separated string from dynamic values.

    Parameters:
    - *dynamic_values: Variable number of dynamic values.

    Returns:
    - str: Comma-separated string.
    """
    comma_separated_string = ', '.join(map(str, dynamic_values))
    return comma_separated_string

def add_item_to_dictinary(dictionary, key, value):
    """
    Add a new key-value pair to the dictionary.

    Parameters:
    - dictionary (dict): The original dictionary.
    - key: The key to be added.
    - value: The value associated with the key.

    Returns:
    - dict: The updated dictionary.
    """
    dictionary[key] = value
    return dictionary

def main():

    st.header("Load Demo Input Data")

    # Create a dropdown menu with some options
    selected_value = st.selectbox("Select a demo dataset", ["dataSet1", "dataSet2", "dataSet3"])

      

    st.title("Sample Input from CAT ")




    # Example text with placeholders
    template_text = "i have Application ID: [applicationid], which has Technical Stack: [technical_stack], and wants  Scalability Need: [scalabilityneed], Compliances: [compliances], Target Platform: [targetplateform]"

    df=loadDemoData(selected_value)

# Replace placeholders with values from the DataFrame
   # for column in df.columns:
       # placeholder = f"[{column}]"
       # template_text = template_text.replace(placeholder, str(df[column].values[0]))
   
    applicationid=st.text_input("Application ID:", df.iloc[0, 0])
    technical_stack=st.text_input("Existing Technology stack:", df.iloc[0, 1])
    scalabilityneed=st.text_input("Scalability and Avalibility Need:", df.iloc[0, 2])
    compliances=st.text_input("Compliance Required:", df.iloc[0, 3])
    targetplateform=st.text_input("Target platform to deploy:", df.iloc[0, 4])


    #st.write(applicationid)
    #st.write(technical_stack)
    #st.write(scalabilityneed)
   # st.write(compliances)
    #st.write(targetplateform)

    st.write("-------------------------------------")

    prompt_value_dict = {}

    prompt_value_dict= add_item_to_dictinary(prompt_value_dict, "applicationid", applicationid)
    prompt_value_dict= add_item_to_dictinary(prompt_value_dict, "technical_stack", technical_stack)
    prompt_value_dict= add_item_to_dictinary(prompt_value_dict, "scalabilityneed", scalabilityneed)
    prompt_value_dict= add_item_to_dictinary(prompt_value_dict, "compliances", compliances)
    prompt_value_dict= add_item_to_dictinary(prompt_value_dict, "targetplateform", targetplateform)

    st.write(prompt_value_dict)
    

    dynamic_values = [applicationid, technical_stack, scalabilityneed, compliances,targetplateform]

    final_Prompts_parameters = create_comma_separated_string(*dynamic_values)

    st.write(final_Prompts_parameters)

    df = pd.DataFrame([prompt_value_dict])
    st.write(df)

    for column in df.columns:
      placeholder = f"[{column}]"
      template_text = template_text.replace(placeholder, str(df[column].values[0]))

   # template_text=process_comma_separated_string(applicationid,template_text)


    st.write( template_text)

     # Button example
    if st.button("Submit"):
        # Execute the processing function
       # template_text=process_comma_separated_string(final_Prompts_parameters,template_text)
        st.write( template_text)
        #process_submission("name, age, gender, subscribe, uploaded_file")
if __name__ == "__main__":
    main()
