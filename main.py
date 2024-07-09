from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.schema import HumanMessage, SystemMessage
from read_data import DATA




if __name__ == '__main__':
    table = DATA.create_sql_table()

    print(table)

    sqllite_url = "sqlite:///database.sqlite"
    db = SQLDatabase.from_uri(sqllite_url, include_tables=['{}'.format(table)])