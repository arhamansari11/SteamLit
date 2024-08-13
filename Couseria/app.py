
from langchain.llms import GooglePalm
api_key = "AIzaSyDv-r1KMe0rypeM_VhPCxbRx_Wq-1FT2xA"
llm = GooglePalm(google_api_key=api_key, temperature=0.2)
poem = llm("What are popular courses now a day")
print(poem)