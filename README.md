# Multi-Agent-Blog-Writer
A multi-agentic-AI system for writing blogs.

Problem Statement : 
🚨 Manual Blog Creation is Time-Consuming, Inconsistent, and Inefficient. With the growing demand of content creation I have observed on sites such as LinkedIn and other similar ones, with the low availability of writers we need to make the most out of the available ones; while ensuring quick, correct and efficient writing. In competitive domains, we need to deep research to identify trending & relevant topics, tuning it for better search engine optimization and careful editing for grammar and structure. Traditionally, this would require a team of human specialists, and the process is time-consuming and prone to burnout; along with being costly when outsourced. It can also have inconsistency in tone, quality and SEO.

## 🧠 Agent Architecture

### Core Agents
1. **Planner Agent**  
   - Analyzes user input and research data
   - Creates content outline/structure
   - Defines tone and target audience

2. **Writer Agent**  
   - Generates blog content using Gemini 2.0-Flash-EXP LLM
   - Incorporates real-time data from Serper API
   - Implements SEO best practices

3. **Editor Agent**  
   - Refines content for clarity and engagement
   - Ensures factual accuracy
   - Maintains consistent tone

### Interaction Workflow
A[User Input] --> B(Planner)
B --> C{Research Phase}
C --> D[Writer]
D --> E{Editing Phase}
E --> F[Editor]
F --> G[Final Output]

### Backend
- **Framework**: Crew AI v1.2+
- **LLM**: Gemini 2.0-Flash-EXP

Steps to run: 

Clone repository
git clone https://github.com/YOUmangg/Multi-Agent-Blog-Writer.git
cd Multi-Agent-Blog-Writer

Install Python dependencies
pip install -r requirements.txt

Set up a .env file containing GEMINI_API_KEY = <your_key_here>

Run command on terminal python run.py
