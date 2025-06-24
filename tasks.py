from crewai import Task, LLM
# from crewai.tools import DuckDuckGoSearchRun
from tools import DuckDuckGoSearchTool
from agents import researcher, writer, editor
from tools import DuckDuckGoSearchRun

# Initialize the LLM
llm = LLM(
    model="gemini/gemini-2.0-flash",    
    temperature=0.7,
)

research_task = Task(
    description="Find trending tech topics and top SEO keywords for blogging.",
    agent=researcher,
    backstory="You are a content strategist who specializes in identifying trending topics and SEO keywords.",
    expected_output="A list of trending topics and a set of relevant SEO keywords, which are less than 500 words in total.",
    tools=[DuckDuckGoSearchTool()]
)

writing_task = Task(
    description="Write a 1000-word SEO-optimized blog based on the research findings.",
    agent=writer,
    backstory="You are a creative AI writer skilled at crafting engaging blog posts.",
    expected_output="A complete blog post in Markdown format, including title, headings, sub-headings and SEO keywords at the end.",
    context=[research_task]
)

editing_task = Task(
    description="Review and edit the blog post for clarity, grammar, and SEO optimization.",
    agent=editor,
    backstory="You are an experienced editor with a keen eye for detail and SEO best practices.",
    expected_output="A polished blog post ready for publication, with suggestions for improvement if needed.",
    context=[writing_task, research_task]
)
