import re

def offline_calculator(query):
    query = query.replace("plus", "+").replace("minus", "-").replace("into", "*") \
                 .replace("multiply", "*").replace("divided by", "/").replace("divide", "/")
    query = re.sub(r'[^\d\+\-\*/\.]', '', query)

    try:
        result = eval(query)
        return f"The answer is {result}"
    except:
        return "Sorry, I couldn't calculate that."
