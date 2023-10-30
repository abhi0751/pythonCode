def Generate_Prompts_For_Json(input_dict, separator=' '):
    concatenated_values = ""
    for value in input_dict.values():
        if concatenated_values:
            concatenated_values += separator
        concatenated_values += str(value)
    return concatenated_values