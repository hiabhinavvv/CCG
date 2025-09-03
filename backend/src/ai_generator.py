import os
import json
from openai import OpenAI
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_challenge_with_ai(difficulty: str, topic: str = "topic1") -> Dict[str, Any]:
    print(f"DEBUG: Received difficulty: {difficulty}")
    print(f"DEBUG: Received topic: {topic}")
    topic_mapping = {
        "topic1": "Machine Learning Fundamentals",
        "topic2": "Neural Networks and Deep Learning",
        "topic3": "Computer Vision",
        "topic4": "Natural Language Processing",
        "topic5": "Reinforcement Learning",
        "topic6": "Data Structures and Algorithm",
        "topic7": "AI Ethics and Bias"
    }

    selected_topic = topic_mapping.get(topic, "Computer Vision")
    print(f"DEBUG: Mapped to topic: {selected_topic}")

    system_prompt = f"""You are an expert AI/ML educator and question author.
Your task is to generate a new and completely different multiple-choice question specifically about "{selected_topic}". The question must be tailored to the specified difficulty level and must focus on the selected topic area.

Topic Focus: {selected_topic}
- Ensure the question is directly related to this specific topic area
- Draw from concepts, techniques, algorithms, or applications within this domain
- Make the question contextually relevant to this topic

The question's difficulty should be determined as follows:
For easy questions: Focus on fundamental definitions, core concepts, and basic understanding within {selected_topic} (e.g., basic definitions, simple concepts, introductory knowledge).
For medium questions: Cover intermediate concepts, practical applications, and specific techniques within {selected_topic} (e.g., algorithm mechanics, evaluation methods, implementation details).
For hard questions: Dive into advanced concepts, mathematical foundations, cutting-edge research, and complex applications within {selected_topic} (e.g., state-of-the-art methods, theoretical foundations, advanced optimizations).

Crucial Constraint: Every time you generate a response, you must create a question that is different from any you have generated before within this topic area. Focus on different aspects, sub-concepts, or applications within {selected_topic}.

Return the challenge in the following JSON structure:

{{
    "title": "The question title",
    "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
    "correct_answer_id": 0,
    "explanation": "A detailed explanation of the concept and why the correct answer is right, including why the other options are incorrect."
}}

Ensure the options are plausible and contextually relevant to {selected_topic}, but with only one clearly correct answer."""
    try:
        response = client.chat.completions.create(
            model='openai/gpt-oss-120b',
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Generate a {difficulty} difficulty question about {selected_topic}."}
            ],
            response_format={"type": "json_object"},
            temperature=2.0,
            stream = False
        )

        content=response.choices[0].message.content
        challenge_data = json.loads(content)

        required_fields = ["title", 'options', 'correct_answer_id', 'explanation']
        for field in required_fields:
            if field not in challenge_data:
                raise ValueError(f"missing required field: {field}")
            
        return challenge_data

    except Exception as e:
        print(e)
        return {
            "title": "Basic Python List Operation",
            "options": [
                "my_list.append(5)",
                "my_list.add(5)",
                "my_list.push(5)",
                "my_list.insert(5)",
            ],
            "correct_answer_id": 0,
            "explanation": "In Python, append() is the correct method to add an element to the end of a list."
        
        }