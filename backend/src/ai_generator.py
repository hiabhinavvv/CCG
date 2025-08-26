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

def generate_challenge_with_ai(difficulty: str) -> Dict[str, Any]:
    system_prompt = """You are an expert AI/ML educator and question author.

Your task is to generate a unique multiple-choice question about Artificial Intelligence (AI), Machine Learning (ML), or Deep Learning (DL), tailored to a specified difficulty level.

The question's difficulty should be determined as follows:

For easy questions: Focus on fundamental definitions, core concepts, and identifying common models or tasks (e.g., supervised vs. unsupervised, the purpose of a training set, what a neuron is).

For medium questions: Cover the mechanics of specific algorithms, evaluation metrics, and intermediate concepts (e.g., the role of an activation function, precision/recall trade-offs, gradient descent).

For hard questions: Dive into advanced architectures, mathematical foundations, optimization techniques, and cutting-edge topics (e.g., attention mechanisms in Transformers, loss functions for GANs, reinforcement learning policies).

Constraint: Each question you generate must be novel. Avoid overly common or trivial questions that appear in basic tutorials. Strive for variety in the topics covered.

Return the challenge in the following JSON structure:

{
    "title": "The question title",
    "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
    "correct_answer_id": 0,
    "explanation": "A detailed explanation of the concept and why the correct answer is right, including why the other options are incorrect."
}
Ensure the options are plausible and contextually relevant, but with only one clearly correct answer."""
    try:
        response = client.chat.completions.create(
            model='llama3-70b-8192',
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Generate a {difficulty} difficulty coding challenge."}
            ],
            response_format={"type": "json_object"},
            temperature=0.6
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