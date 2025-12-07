from langchain_core.messages import HumanMessage
from rag import graph

input_messages = [HumanMessage("What's the world cup?")]
config = {"configurable": {"thread_id": "abc123"}}
response = graph.invoke({"messages": input_messages}, config=config)