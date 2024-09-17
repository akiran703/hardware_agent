This is a simplified version of an internal tool that I created for Hyve Solutions to help spread debugging knowledge among various teams.

This is an SQL query agent that is built using langchain. It uses an LLM that processes natural language that then queries a database I created, and returns relevant information on debugging.

Langchain is an open-source framework that serves as an interface to interact with LLMs by creating an environment to build LLM applications and integrate them with external data sources.

The database is a mocked version of readily available hardware issues and solutions on forums. The columns in the database: Server Model, Test Case, Error Message, Root Cause, Action to Take

example 

Q: What is the fix to this error message,[ 3376.798352] pcieport 0000:02:00.0: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=0200(Receiver ID)

*/Thought: Now we need to find the Action to Take column value for the given Error Message.
Action: sql_db_query
Action Input: SELECT "Action to Take" FROM hardware_issues WHERE "Error Message" LIKE '%[ 3376.798352] pcieport 0000:02:00.0: PCIe Bus Error: severity=Corrected, type=Physical Layer, id=0200(Receiver ID)%';[('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',), ('reseat the card',)] I now know the final answer
Final Answer: reseat the card

> Finished chain.
reseat the card

Q: What is the root cause to this error message, Mar 27 19:11:11 archdesktop kernel: pcieport 0000:00:1c.2: AER: Correctable error message received from 0000:04:00.0

> Entering new SQL Agent Executor chain...
I need to query the hardware_issues table to find the Root Cause for the given Error Message.
Action: sql_db_query
Action Input: SELECT Root Cause FROM hardware_issues WHERE Error Message LIKE '%Mar 27 19:11:11 archdesktop kernel: pcieport 0000:00:1c.2: AER: Correctable error message received from 0000:04:00.0%';Error: (sqlite3.OperationalError) near "Message": syntax error
[SQL: SELECT Root Cause FROM hardware_issues WHERE Error Message LIKE '%Mar 27 19:11:11 archdesktop kernel: pcieport 0000:00:1c.2: AER: Correctable error message received from 0000:04:00.0%';]
(Background on this error at: https://sqlalche.me/e/20/e3q8)The error is due to the space in the Error Message column name. I need to enclose the column name in backticks.
Action: sql_db_query
Action Input: SELECT Root Cause FROM hardware_issues WHERE `"Error Message"` LIKE '%Mar 27 19:11:11 archdesktop kernel: pcieport 0000:00:1c.2: AER: Correctable error message received from 0000:04:00.0%';Error: (sqlite3.OperationalError) no such column: Root
[SQL: SELECT Root Cause FROM hardware_issues WHERE `"Error Message"` LIKE '%Mar 27 19:11:11 archdesktop kernel: pcieport 0000:00:1c.2: AER: Correctable error message received from 0000:04:00.0%';]
(Background on this error at: https://sqlalche.me/e/20/e3q8)I need to enclose the Root Cause column name in backticks as well.
Action: sql_db_query
Action Input: SELECT `"Root Cause"` FROM hardware_issues WHERE `"Error Message"` LIKE '%Mar 27 19:11:11 archdesktop kernel: pcieport 0000:00:1c.2: AER: Correctable error message received from 0000:04:00.0%';Error: (sqlite3.OperationalError) no such column: "Root Cause"
[SQL: SELECT `"Root Cause"` FROM hardware_issues WHERE `"Error Message"` LIKE '%Mar 27 19:11:11 archdesktop kernel: pcieport 0000:00:1c.2: AER: Correctable error message received from 0000:04:00.0%';]
(Background on this error at: https://sqlalche.me/e/20/e3q8)Question: What is the root cause to this error message, Mar 27 19:11:11 archdesktop kernel: pcieport 0000:00:1c.2: AER: Correctable error message received from 0000:04:00.0
Thought: I need to query the hardware_issues table to find the Root Cause for the given Error Message.
Action: sql_db_query
Action Input: SELECT "Root Cause" FROM hardware_issues WHERE "Error Message" LIKE '%Mar 27 19:11:11 archdesktop kernel: pcieport 0000:00:1c.2: AER: Correctable error message received from 0000:04:00.0%';[('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',), ('bios issue',)]The root cause of the error message "Mar 27 19:11:11 archdesktop kernel: pcieport 0000:00:1c.2: AER: Correctable error message received from 0000:04:00.0" is "bios issue".
Final Answer: bios issue

> Finished chain.
bios issue
(hardware_langchain) kirakumar@Kirthikas-MacBook-Pro hardware_debug %



Q: What test case does this error message belong to, Mar 27 19:11:11 archdesktop kernel: pcieport 0000:00:1c.2: AER: Correctable error message received from 0000:04:00.0

> Entering new SQL Agent Executor chain...
I need to find the Test Case from the hardware_issues table where the Error Message column contains the given error message.
Action: sql_db_query
Action Input: SELECT `Test Case` FROM `hardware_issues` WHERE `Error Message` LIKE '%Mar 27 19:11:11 archdesktop kernel: pcieport 0000:00:1c.2: AER: Correctable error message received from 0000:04:00.0%';[('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',), ('PCIE_CHECK',)]The Test Case for the given error message is PCIE_CHECK.
Final Answer: PCIE_CHECK

> Finished chain.
PCIE_CHECK
(hardware_langchain) kirakumar@Kirthikas-MacBook-Pro hardware_debug % 
