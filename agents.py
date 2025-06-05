import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, Task, Crew, LLM

llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.7,
)

# Research Agent
researcher = Agent(
    role='Researcher',
    goal='Find key topics to cover when writing on {topic} and relevant SEO keywords',
    backstory='A savvy content strategist with a nose for trends',
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Writer Agent
writer = Agent(
    role='Writer',
    goal='Write a compelling, SEO-optimized blog post on the {topic} based on the research findings from the Researcher agent',
    backstory='A creative AI writer skilled at blog writing',
    verbose=True,
    allow_delegation=False,
    llm=llm
)

#Editor Agent
editor = Agent(
    role = 'Editor',
    goal = 'Review and edit the blog post for clarity, grammar, and SEO optimization',
    backstory = 'An experienced editor with a keen eye for detail and SEO best practices',
    verbose = True,
    allow_delegation = False,
    llm = llm
)