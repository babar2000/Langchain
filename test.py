from langchain import GooglePaLM, PromptTemplate, LLMChain
from langfuse import Langfuse

# Initialize Langfuse client
lf = Langfuse(api_key="sk-lf-fe68ca2f-1298-42b2-8e51-e9aaf1491861")

# Step 1: Create the Langchain 'Hello World' prompt
template = "What is a good response to: {question}?"
prompt = PromptTemplate(template=template, input_variables=["question"])

# Step 2: Define your LLM (using Google PaLM API)
llm = GooglePaLM(google_api_key="YOUR_GOOGLE_API_KEY")

# Step 3: Create the Langchain pipeline (LLMChain)
chain = LLMChain(llm=llm, prompt=prompt)

# Step 4: Run the pipeline
question = "Hello World"
response = chain.run(question)

# Step 5: Log the input and output to Langfuse
lf.log(
    inputs={"question": question},
    outputs={"response": response},
    metadata={"example": "Langchain Hello World with Google PaLM"}
)

# Print the result
print("LLM Response:", response)
