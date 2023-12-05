import streamlit as st
from streamlit_chat import message
#from utils import get_initial_message, get_chatgpt_response, update_chat
import os
#from dotenv import load_dotenv
#load_dotenv()
#import openai

import random
import string

def generate_random_text(length):
    # Define the characters you want to include in the random text
    characters = string.ascii_letters + string.digits + string.punctuation + string.whitespace

    # Generate a random string of the specified length
    random_text = ''.join(random.choice(characters) for _ in range(length))

    return random_text

def get_initial_message():
    messages=[
            {"role": "system", "content": "You are a helpful AI Tutor. Who anwers brief questions about AI."},
            {"role": "user", "content": "I want to learn AI"},
            {"role": "assistant", "content": "Thats awesome, what do you want to know aboout AI"}
        ]
    return messages

def get_chatgpt_response(prompt, model="gpt-3.5-turbo"):
        #st.write(query)
        return "my random response : your prompt was "+ prompt +" : "+ generate_random_text(50)

def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages

#openai.api_key = "key here"
st.title("Augmented Architect : Customized")


model = 41 #st.selectbox("Select a model",("gpt-3.5-turbo", "gpt-4"))

if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

prompt = st.text_input("Prompt: ", key="input")


if 'messages' not in st.session_state:
    st.session_state['messages'] = get_initial_message()

if prompt:
    with st.spinner("generating..."):
        
        messages = st.session_state['messages']
        #st.write(query)
        messages = update_chat(messages, "user", prompt)
        response = get_chatgpt_response(prompt, model)
        messages = update_chat(messages, "assistant", response)
        st.session_state.past.append(prompt)
        st.session_state.generated.append(response)
         # Clear the input prompt using JavaScript
        
        
if st.session_state['generated']:
     if len(st.session_state['generated'])>0:
      for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))

     with st.expander("Show Messages"):
        st.write(messages)


    