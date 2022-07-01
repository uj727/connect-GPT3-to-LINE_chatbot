# import os

# from linebot import (LineBotApi, WebhookHandler)
# from linebot.exceptions import (InvalidSignatureError)
# from linebot.models import *



def ask(): 
    message = TextSendMessage(text="工三小")
    #import openai
    #openai.api_key = "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"
    # response = openai.Completion.create(
    # model="text-curie-001",
    # prompt="how old are you",
    # temperature=0.7,
    # max_tokens=256,
    # top_p=1,
    # frequency_penalty=0,
    # presence_penalty=0
    #                                     )
    #story = response['choices'][0]['text'] 
    
    return message
    #print( str(story) )
#ask("what are the symptom of heartdisease") 