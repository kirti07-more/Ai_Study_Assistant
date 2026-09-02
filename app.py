import streamlit as st


st.set_page_config(
    page_title="AI Study Assistant",
    page_icon="📚",
    layout="centered"
)


st.title("AI Study Assistant")
st.write("A simple study assistant for learning and practice.")


explanations = {
    "Python": """
Python is a high-level programming language that is easy to learn
and widely used in software development, data science, artificial
intelligence, machine learning and automation.

Python has a simple and readable syntax, which makes it suitable
for beginners as well as experienced developers.
""",

    "Artificial Intelligence": """
Artificial Intelligence (AI) is a field of computer science that
focuses on creating systems that can perform tasks that normally
require human intelligence.

Examples include understanding language, recognizing images,
making predictions and solving problems.
""",

    "Machine Learning": """
Machine Learning (ML) is a branch of Artificial Intelligence.

It allows computers to learn patterns from data and use those
patterns to make predictions or decisions without being explicitly
programmed for every possible situation.
""",

    "Data Science": """
Data Science is the process of collecting, analyzing and
interpreting data to find useful information and support
decision-making.

It uses programming, statistics, data analysis, visualization
and machine learning.
"""
}


summaries = {
    "Python": "Python is a readable programming language commonly used in Data Science, AI, ML, automation and software development.",

    "Artificial Intelligence": "AI is a field of computer science that enables machines to perform tasks that normally require human intelligence.",

    "Machine Learning": "Machine Learning is a branch of AI that allows computers to learn patterns from data and make predictions or decisions.",

    "Data Science": "Data Science combines programming, statistics and data analysis to extract useful information from data."
}


quiz_data = {
    "Python": [
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["func", "def", "function", "define"],
            "answer": "def"
        },
        {
            "question": "Which symbol is used to write a comment in Python?",
            "options": ["//", "#", "/*", "--"],
            "answer": "#"
        },
        {
            "question": "Which data type represents True or False?",
            "options": ["String", "Integer", "Boolean", "Float"],
            "answer": "Boolean"
        }
    ],

    "Artificial Intelligence": [
        {
            "question": "What does AI stand for?",
            "options": [
                "Artificial Intelligence",
                "Automated Information",
                "Advanced Internet",
                "Artificial Integration"
            ],
            "answer": "Artificial Intelligence"
        },
        {
            "question": "Which is an example of an AI application?",
            "options": [
                "Recommendation system",
                "Notebook",
                "Chair",
                "Pencil"
            ],
            "answer": "Recommendation system"
        },
        {
            "question": "Which field is closely related to AI?",
            "options": [
                "Machine Learning",
                "Painting",
                "Cooking",
                "Geography"
            ],
            "answer": "Machine Learning"
        }
    ],

    "Machine Learning": [
        {
            "question": "What does Machine Learning learn patterns from?",
            "options": [
                "Data",
                "Keyboard",
                "Monitor",
                "Printer"
            ],
            "answer": "Data"
        },
        {
            "question": "Which is a type of Machine Learning?",
            "options": [
                "Supervised Learning",
                "Manual Learning",
                "Keyboard Learning",
                "Screen Learning"
            ],
            "answer": "Supervised Learning"
        },
        {
            "question": "Which is an application of Machine Learning?",
            "options": [
                "Spam detection",
                "Writing on paper",
                "Opening a book",
                "Turning a page"
            ],
            "answer": "Spam detection"
        }
    ],

    "Data Science": [
        {
            "question": "Which programming language is commonly used in Data Science?",
            "options": [
                "Python",
                "HTML",
                "CSS",
                "XML"
            ],
            "answer": "Python"
        },
        {
            "question": "What does Data Science mainly work with?",
            "options": [
                "Data",
                "Furniture",
                "Paint",
                "Music"
            ],
            "answer": "Data"
        },
        {
            "question": "Which Python library is commonly used for data analysis?",
            "options": [
                "Pandas",
                "Photoshop",
                "PowerPoint",
                "Paint"
            ],
            "answer": "Pandas"
        }
    ]
}


name = st.text_input("Enter your name")

topic = st.selectbox(
    "Select a topic",
    list(explanations.keys())
)

action = st.radio(
    "Select an option",
    [
        "Explain a topic",
        "Make a summary",
        "Take a quiz"
    ]
)


if action == "Explain a topic":

    if name:
        st.write(f"Hello, {name}.")

    st.subheader(topic)
    st.write(explanations[topic])


elif action == "Make a summary":

    if name:
        st.write(f"Hello, {name}.")

    st.subheader(f"Summary: {topic}")
    st.write(summaries[topic])


else:

    if name:
        st.write(f"Hello, {name}.")

    st.subheader(f"{topic} Quiz")

    questions = quiz_data[topic]
    user_answers = []

    for index, question in enumerate(questions):

        answer = st.radio(
            question["question"],
            question["options"],
            key=f"{topic}_{index}"
        )

        user_answers.append(answer)

    if st.button("Submit Quiz"):

        score = 0

        for index, question in enumerate(questions):

            if user_answers[index] == question["answer"]:
                score += 1

        st.success(
            f"Your score is {score}/{len(questions)}."
)
