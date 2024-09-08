from google.generativeai import palm
from langchain import PromptTemplate, LLMChain
from langfuse import Langfuse

# Initialize Langfuse client
lf = Langfuse(api_key="YOUR_LANGFUSE_API_KEY")

# Set the Google PaLM API key
palm.configure(api_key="YOUR_GOOGLE_API_KEY")

# Step 1: Create the Langchain 'Hello World' prompt
template = "What is a good response to: {question}?"
prompt = PromptTemplate(template=template, input_variables=["question"])

# Step 2: Define a custom function to use Google Gemini (PaLM)
def call_google_gemini(question):
    # Make a request to Google PaLM (Gemini) API
    response = palm.generate_text(prompt=question)
    return response.result

# Step 3: Create a chain with the custom function (using Langchain for orchestration)
def chain_run(question):
    return call_google_gemini(question)

# Step 4: Run the pipeline
question = "Hello World"
response = chain_run(question)

# Step 5: Log the input and output to Langfuse
lf.log(
    inputs={"question": question},
    outputs={"response": response},
    metadata={"example": "Langchain Hello World with Google Gemini"}
)

# Print the result
print("LLM Response:", response)
