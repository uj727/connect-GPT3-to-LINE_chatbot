from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
from googletrans import Translator 

#======這裡是呼叫的檔案內容=====
from model import *
#======這裡是呼叫的檔案內容=====

#======python的函數庫==========
import tempfile, os
import datetime
import time
import openai 
#======python的函數庫==========

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('QnQ0GccEGvNeJSJKjnHMm5+VcorJPuAxgrCtxqHAhgW+IQKOGJtz8V8p2M2Vql+NvgUQeScpZI3JJBAQ+bct4N86V7OeKMTTmmCYJG8git3YAm50kEYoE3Syi1gdb8ijlVlgfa5sWiceYbjrbFVl/AdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('acfb595de7ce00a944e38464f437c693')


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

def translate_text(text,de):
    translator = Translator()
    result = translator.translate(text, dest=de).text
    return result

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #msg = event.message.text
    msg = translate_text(event.message.text, 'en')#輸入的句子轉英文

    if 'picture' in msg:
        message = TextSendMessage(text="工三小"+msg)
        line_bot_api.reply_message(event.reply_token, message)
    
    elif '111' in msg:
        ans=ask()
        #ans = translate_text(event.message.text, 'zh-tw')#輸出轉成中文
        message = TextSendMessage(text=ans)
        line_bot_api.reply_message(event.reply_token, message)
    else:
        #ans = translate_text(msg, 'zh-tw')
        message = TextSendMessage(text=msg) #回一樣的訊息
        line_bot_api.reply_message(event.reply_token, message)


@handler.add(PostbackEvent)
def handle_message(event):
    print(event.postback.data)

@handler.add(MemberJoinedEvent)
def welcome(event):
    uid = event.joined.members[0].user_id
    gid = event.source.group_id
    profile = line_bot_api.get_group_member_profile(gid, uid)
    name = profile.display_name
    message = TextSendMessage(text=f'{name}歡迎加入')
    line_bot_api.reply_message(event.reply_token, message)
        
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
