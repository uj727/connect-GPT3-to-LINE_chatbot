import os
import openai
# from linebot import (LineBotApi, WebhookHandler)
# from linebot.exceptions import (InvalidSignatureError)
# from linebot.models import *
openai.api_key = "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"


def ask(question): 
    print(question)
    response = openai.Completion.create(
    model="text-curie-001",
    prompt=question,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)
    story = response['choices'][0]['text'] 
    a='51515'
    #return a
    #return str(story) 
    print( str(story) )
#ask("what are the symptom of heartdisease") 