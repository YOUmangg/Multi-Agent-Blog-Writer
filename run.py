from agents import researcher, assistant_researcher, writer, editor
from tasks import research_task, writing_task, editing_task
from crewai import Crew, Process
from dotenv import load_dotenv
import os

# from  import GEMINI_API_KEY  # Ensure you have your API key in a config file
# from Ipython.display import Markdown

load_dotenv()  # Load environment variables from .env file
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

crew = Crew(
    agents=[researcher, assistant_researcher , writer, editor],
    tasks=[research_task, writing_task, editing_task],
    process = Process.sequential,  # Sequential process to ensure tasks are completed in order
    max_rpm = 10,  # Maximum requests per minute
    # memory = True,  # Enable memory to retain information across tasks
    memory = False,
    embedder={
        "provider": "google",
        "config": {
            "api_key": GEMINI_API_KEY,  # Replace with your actual API key
            "model": "gemini-embedding-exp-03-07"
        }
    }, #use when memory is enabled. By default, the embedder used is OpenAI's text-embedding
    verbose=1
)

#create user input to give topic for a blog post
topic = input("Enter the topic for the blog post: ")
result = crew.kickoff(inputs={"topic": topic})

#checking the token usage
print('result_max_tokens:', result.token_usage)

with open('result.txt', 'w') as f:
    f.write(result.raw)

#Saving the result to a text file
print('Blog post saved to result.txt')

#Aesthetically print the result with markdown formatting
# print(Markdown(result))

