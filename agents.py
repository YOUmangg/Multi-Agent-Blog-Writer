import os
from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, Task, Crew, LLM

llm = LLM(
    model="gemini/gemini-2.0-flash",
    temperature=0.7,
)

llm2 = LLM(
    model="gemini/gemini-1.5-flash",
    temperature=0.5,
)

# Research Agent
researcher = Agent(
    role='Researcher',
    goal='Find key topics to cover when writing on {topic} and relevant SEO keywords.',
    backstory='''A savvy content strategist with a nose for trends. You can also delegate tasks to the Assistant Researcher 
    agent if needed.''',
    verbose=True,
    allow_delegation=True,
    llm=llm2
)

assistant_researcher = Agent(
    role='Assistant Researcher',
    goal='Assist the Researcher in gathering information and data on {topic}',
    backstory='A diligent assistant with a knack for finding relevant information quickly, helping the Researcher to compile comprehensive research findings',
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Writer Agent
writer = Agent(
    role='Writer',
    goal='Write a compelling, SEO-optimized blog post on the {topic} based on the research findings from the Researcher agent.' \
    ,
    backstory='A creative AI writer skilled at blog writing. ' \
    'After writing the blog, you hand over the blog post to the Editor agent for review and editing.',
    verbose=True,
    allow_delegation=False,
    llm=llm
)

#Editor Agent
editor = Agent(
    role = 'Editor for BlogWorld',
    goal = 'Review and edit the blog post on {topic} for clarity, grammar, and SEO optimization',
    backstory = 'An experienced editor with a keen eye for detail and SEO best practices. ' \
    'You ensure the blog post is polished and ready for publication, aligning with the brand voice and style.',
    verbose = True,
    allow_delegation = False,
    llm = llm
)

#Add image generation agent in the future