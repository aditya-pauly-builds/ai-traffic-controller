import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(
    api_key  = api_key
)

def query_answer(query):
    chat_answer = client.chat.completions.create(
            messages=[{"role": "user", "content": query}],
            model = "openai/gpt-oss-120b",
    
        )
    
    answer = chat_answer.choices[0].message.content
    return answer

def coding_ai(query):
    return query_answer(query)
    

def writing_ai(query):
    return query_answer(query)

def math_ai(query):
    return query_answer(query)

def general_ai(query):
    return query_answer(query)

 
while True:

    query = input("What do u want to know?? :")

    if query.lower() == "exit" or query.lower() == "quit":
            break


    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"""
        Classify the user's input into exactly ONE of these categories:

        coding
        writing
        math
        general

        User request:
        {query}

        Return only the category name.
        """
            }
        ],
        model="openai/gpt-oss-120b",

    )

    category= chat_completion.choices[0].message.content.strip().lower()
    print("Category:",category)

    routes = {
        "coding" : coding_ai,
        "writing" : writing_ai,
        "math" : math_ai,
        "general" : general_ai
    }

    route = routes.get(category)


    if route:
        print("Routing to", route.__name__)
        print(route(query))

        
    else:
        print("Sorry I don't understand the request...")
        print(route(query))



