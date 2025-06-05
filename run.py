from agents import researcher, writer, editor
from tasks import task1, task2, task3
from crewai import Crew

crew = Crew(
    agents=[researcher, writer, editor],
    tasks=[task1, task2, task3],
    verbose=True
)

result = crew.kickoff(inputs={
    "topic": "AI in Healthcare"
})
