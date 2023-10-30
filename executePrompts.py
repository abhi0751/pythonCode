import json
from dotenv import load_dotenv
import os

load_dotenv()

Prompts_input_file = 'Prompts.json'
# Read the JSON data from the file
with open(Prompts_input_file, 'r') as file:
    input_Json_data = json.load(file)

# Read the configuration from environment file
api_key= os.getenv('23API_KEY')
print(api_key)
def validate_json(data):
    try:
        # Parse the JSON data
        json_data = data
        
        # Check if "Prompts" key exists and is a list of dictionaries
        if "Prompts" in json_data and isinstance(json_data["Prompts"], list):
            for item in json_data["Prompts"]:
                if not isinstance(item, dict):
                    return False
        else:
            return False

        return True  # JSON is valid

    except json.JSONDecodeError:
        return False
    
# Validate the JSON data
is_valid = validate_json(input_Json_data)

if is_valid:
    print("JSON is valid.")
else:
    print("JSON is not valid.")

# import generate prompt function from PromptJsonParser.py
from PromptJsonParser import Generate_Prompts_For_Json

# Access the elements
prompts = input_Json_data['Prompts']

for prompt in prompts:
    
   # print("------now printing  dictoray from functio ---------")
    input_prompt = Generate_Prompts_For_Json(prompt,separator='.\n ')
    print(input_prompt)

  
    

   
    
   

