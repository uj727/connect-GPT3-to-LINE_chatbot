
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def ask():
    # import openai
    # openai.api_key = "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"
    # response = openai.Completion.create(
    # model="text-curie-001",
    # prompt=q,
    # temperature=0.7,
    # max_tokens=256,
    # top_p=1,
    # frequency_penalty=0,
    # presence_penalty=0
    #                                     )
    # story = response['choices'][0]['text'] 
    message = TextSendMessage(text="555")
    return message
    #return story
    #print( str(story) )
#ask("what are the symptom of heartdisease") 