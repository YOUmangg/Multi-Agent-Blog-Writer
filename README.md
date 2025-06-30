# Multi-Agent-Blog-Writer
A multi-agentic-AI system for writing blogs.

Problem Statement : 
🚨 Manual Blog Creation is Time-Consuming, Inconsistent, and Inefficient. With the growing demand of content creation I have observed on sites such as LinkedIn and other similar ones, with the low availability of writers we need to make the most out of the available ones; while ensuring quick, correct and efficient writing. In competitive domains, we need to deep research to identify trending & relevant topics, tuning it for better search engine optimization and careful editing for grammar and structure. Traditionally, this would require a team of human specialists, and the process is time-consuming and prone to burnout; along with being costly when outsourced. It can also have inconsistency in tone, quality and SEO. 

The solution to this is building up your own content team to produce complete blogs along with relevant images. This is a solid use-case of Agentic AI in real-world scenario.

## 🧠 Agent Architecture

### Core Agents
1. **Researcher Agent**  
   - Analyzes user input and research data
   - Creates content outline/structure
   - Defines tone and target audience
   - Uses DuckDuckGo search for getting real-time updated information
  
2. **Assistant Researcher Agent**
   - Assists the researcher in their task
   - Works as asked for when deledgated work by the Researcher Agent

3. **Writer Agent**  
   - Generates blog content using Gemini 2.0-Flash-EXP LLM
   - Incorporates real-time data from Researcher Agents
   - Implements SEO best practices

4. **Images Generator Agent**
   - Generates images based on the written article
   - Stores images and metadata in a pydantic format

3. **Editor Agent**  
   - Refines content for clarity and engagement
   - Ensures factual accuracy
   - Maintains consistent tone
   - Adds the images generated to the blog

### Interaction Workflow
A[User Input] --> B(Researcher)
B --> C{Research Phase} <-> Delegation to assistant_researcher can happen
C --> D[Writer]
D --> E[Images Generator]
E --> F[Editor]
F --> G[Final Output]

### Backend
- **Framework**: Crew AI v1.2+
- **LLMS**: Gemini 2.0-Flash-EXP, Gemini 1.0-Flash-EXP, black-forest-labs/FLUX.1-schnell
- **Embeddings**: gemini-embedding-exp-03-07

Steps to run: 

Clone repository
git clone https://github.com/YOUmangg/Multi-Agent-Blog-Writer.git
cd Multi-Agent-Blog-Writer

Install Python dependencies
pip install -r requirements.txt

Set up a .env file containing GEMINI_API_KEY = <your_key_here>
TOGETHER_API_KEY = <your_key_here>

Run command on terminal python run.py
