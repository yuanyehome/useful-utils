import openai
import json
import keys

openai.api_key = keys.openai_key
print(openai.Model.list())

system_prompt = (
    "You are a helpful assistant that be good at answer multiple-choice questions about "
    "language arts and social studies. "
    "You are good at answering questions step-by-step with intermediate reasoning paths. "
    "I need you to answer my questions not only with the answer but also with the intermediate steps about how you get the answers. "
)
user_prompt = (
    "Here is my question and choices:\n\nWhat month comes right before March?\n(a) February (b) January \n\n"
    "Now give me the answer step-by-step. You **MUST** give me your answer and explain step-by-step how you get it. "
)

res = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": user_prompt
        }
    ],
    temperature=0.0,
    top_p=0.9,
)
print(res)
print("\033[36mAssistant\033[0m: ", res["choices"][0]["message"]["content"])
