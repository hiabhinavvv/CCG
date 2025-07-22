# 🚀 Coding Challenge Generator

A full-stack application that generates programming challenges at different difficulty levels (Easy, Medium, Hard) in MCQ format. Built with React, FastAPI, and powered by Groq's LLM.

## 🔧 Tech Stack

### Frontend
- React
- Clerk (Authentication)

### Backend
- FastAPI
- SQLAlchemy (ORM)
- Uvicorn (ASGI server)

### AI Integration
- Groq (LLM for challenge generation)

### Authentication
- Clerk (User management)

## 🛠️ Setup & Installation

### Backend Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\Activate    # Windows
   ```

2. Install backend dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the backend directory with:
   ```
   DATABASE_URL=your_database_url
   CLERK_SECRET_KEY=your_clerk_secret
   GROQ_API_KEY=your_groq_api_key
   ```

4. Run the backend server:
   ```
   python server.py
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install frontend dependencies:
   ```
   npm install
   ```

3. Create a `.env` file with:
   ```
   REACT_APP_CLERK_PUBLISHABLE_KEY=your_clerk_pub_key
   REACT_APP_API_URL=http://localhost:8000
   ```

4. Start the frontend:
   ```
   npm start
   ```

## 🌟 Features

- 🔐 Clerk authentication (Sign up/Login)
- 🎚️ Three difficulty levels (Easy/Medium/Hard)
- ❓ MCQ format challenges
- 🧠 AI-powered challenge generation via Groq
- 📊 User progress tracking (via SQL database)


## 🚦 API Endpoints

- `POST /generate-challenge`: Generate a new coding challenge
  - Parameters: `difficulty` (easy/medium/hard)
- `GET /challenges`: Get user's challenge history
- `POST /submit-answer`: Submit answer for a challenge

## 🤖 AI Prompt Structure

The system uses carefully crafted prompts to generate challenges:

```
You are an expert coding challenge creator. 
    Your task is to generate a coding question with multiple choice answers.
    The question should be appropriate for the specified difficulty level.

    For easy questions: Focus on basic syntax, simple operations, or common programming concepts.
    For medium questions: Cover intermediate concepts like data structures, algorithms, or language features.
    For hard questions: Include advanced topics, design patterns, optimization techniques, or complex algorithms.

    Return the challenge in the following JSON structure:
    {
        "title": "The question title",
        "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
        "correct_answer_id": 0, // Index of the correct answer (0-3)
        "explanation": "Detailed explanation of why the correct answer is right"
    }

    Make sure the options are plausible but with only one clearly correct answer.
```

## 📜 License

MIT License - do whatever the fuck you want with this code. Just don't blame me if it breaks.