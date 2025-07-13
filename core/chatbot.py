import openai
import wolframalpha
from core.calculator import offline_calculator

openai.api_key = ""
wolfram_client = wolframalpha.Client("LX98QQ-ALEGAGKYU4")

def get_openai_answer(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return "OpenAI error: " + str(e)

def get_wolfram_answer(query):
    try:
        res = wolfram_client.query(query)
        return next(res.results).text
    except:
        return "WolframAlpha error"

def get_best_answer(query):
    answer = get_wolfram_answer(query)
    if "WolframAlpha error" in answer:
        answer = offline_calculator(query)
    if "couldn't" in answer:
        answer = get_openai_answer(query)
    return answer
