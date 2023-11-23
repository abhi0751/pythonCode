import pandas as pd

# Generate a single-row dataset
data = {
    'applicationid': 'App123',
    'technical-stack': 'Python, Flask, PostgreSQL',
    'scalabilityneed': 'High',
    'compliances': 'HIPAA',
    'targetplateform': 'AWS'
}

# Convert the data to a DataFrame
df = pd.DataFrame([data])

# Save the DataFrame to a CSV file
#df.to_csv('dataset.csv', index=False)

# Read the dataset from the CSV file
#df_read = pd.read_csv('dataset.csv')

# Example text with placeholders
template_text = "i have Application ID: [applicationid], which has Technical Stack: [technical-stack], and wants  Scalability Need: [scalabilityneed], Compliances: [compliances], Target Platform: [targetplateform]"

# Replace placeholders with values from the DataFrame
for column in df.columns:
    placeholder = f"[{column}]"
    template_text = template_text.replace(placeholder, str(df[column].values[0]))

# Display the modified text
print(template_text)
