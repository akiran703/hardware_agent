This a simplified version of a internal tool that I created for Hyve Solutions to help spread debugging knowledge through various team. 

This a SQL query agent that is built using langchain. It uses a LLM that proccesses natural language that then queries a database I created, and returns relevant information 
on debugging. 

Langchain is a open source framework that serves as a interface to interact with LLMs by creating a environment to build LLM applications 
and integrate them with external data sources.


The database is a mocked version of readily avaliable hardware issues and solutions found on forums. The columns in the database: Server Model, Test Case,Error Message,Root Cause,Action to Take

example 

Q: What is the fix to this error message,[ 3376.798352] pcieport 0000:02:00.0: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=0200(Receiver ID)

*/Thought: Now we need to find the Action to Take column value for the given Error Message.
Action: sql_db_query
Action Input: SELECT "Action to Take" FROM hardware_issues WHERE "Error Message" LIKE '%[ 3376.798352] pcieport 0000:02:00.0: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=0200(Receiver ID)%';[('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',)] I now know the final answer
Final Answer: reseat the card

> Finished chain.
reseat the card
