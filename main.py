from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.schema import HumanMessage, SystemMessage
from read_data import DATA
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.agent_toolkits import create_sql_agent



if __name__ == '__main__':
    table = DATA.create_sql_table()

    print(table)

    sqllite_url = "sqlite:///database.sqlite"
    db = SQLDatabase.from_uri(sqllite_url, include_tables=['{}'.format(table)])
    
    llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key='enter API ')
    
    chain = SQLDatabaseChain.from_llm(llm, db, verbose = True)
    
    
    
    final_prompt = ChatPromptTemplate.from_messages(
        [
            ("system",
            """
            You are a helpful AI assistant expert in querying SQL Database to find answers to user's question about the table hardware_issues.
            The hardware_issues table contains information of known hardware issues and debug actions to resolve these issues.
            The below information is about the table, understand this and then answer the questions asked by the user:
            The hardware_issues table has columns?: Server Model, Test Case,Error Message,Root Cause,Action to Take.
            The hardware_issues table contains columns like Error Message which indicate what kind of issue the system is having.
            The user could give some part of the error message, and this part could be found in the Error Message Column.
            The hardware_issues table contains column like Root Cause that explain why this issue is happening. 
            Action to Take is a column that tells what the fix is to the associated error message.
            """
            ),
            ("user", "{question}\n ai: "),
        ]   
    )
    
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)

    agent_executor = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True,
        handle_parsing_errors=True
    )
    print(agent_executor.run(final_prompt.format(
            question="What is the fix to this error message,[ 3376.798352] pcieport 0000:02:00.0: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=0200(Receiver ID)")))
    
    
    