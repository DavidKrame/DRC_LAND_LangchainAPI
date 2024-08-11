from langchain_community.utilities import SQLDatabase
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from config import OPENAI_API_KEY, SUPABASE_URI
from schemas import get_schema

# Initialize the SQLDatabase instance
db = SQLDatabase.from_uri(SUPABASE_URI)

# Define the template for generating SQL queries
template = """Based on the table schema below, write a SQL query that would answer the user's question:
{schema}

Question: {question}
SQL Query:"""
prompt = ChatPromptTemplate.from_template(template)

# Initialize the language model with the OpenAI API key
llm = ChatOpenAI(api_key=OPENAI_API_KEY)

# Create the SQL chain for processing user questions
sql_chain = (
    RunnablePassthrough.assign(schema=lambda _: get_schema(db))
    | prompt
    | llm.bind(stop=["\nSQLResult:"])
    | StrOutputParser()
)

# Define the template for generating natural language responses
template_response = """Based on the table schema below, question, sql query, and sql response, write a natural language response:
{schema}

Question: {question}
SQL Query: {query}
SQL Response: {response}"""
prompt_response = ChatPromptTemplate.from_template(template_response)

# Create the full chain for processing user questions and generating responses
full_chain = (
    RunnablePassthrough.assign(query=sql_chain).assign(
        schema=lambda _: get_schema(db), response=lambda vars: db.run(vars["query"])
    )
    | prompt_response
    | llm
)


def process_user_query(user_question):
    return full_chain.invoke({"question": user_question})
