# import os
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *
from googletrans import Translator

def ask(q): 
    
    import openai
    translator = Translator()
    openai.api_key = "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"
    response = openai.Completion.create(
    model="text-curie-001",
    prompt=q,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
                                        )
    story = response['choices'][0]['text'] 
    results = (translator.translate(response['choices'][0]['text'],dest='zh-tw').text)
    #message = TextSendMessage(text=results)
    #return message
    return story
    #print( str(story) )
#ask("what are the symptom of heartdisease") 