#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def Carousel_Template():
    message = TemplateSendMessage(
        alt_text='一則旋轉木馬按鈕訊息6666SS',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png',
                    title='這是第一塊模板',
                    text='一個模板可以有三個按鈕',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='將這個訊息偷偷回傳給機器人'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是1'
                        ),
                        URITemplateAction(
                            label='進入1的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/8/88/Number_1_in_green_rounded_square.svg/200px-Number_1_in_green_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuo7n2_HNSFuT3T7Z9PUZmn1SDM6G6-iXfRC3FxdGTj7X1Wr0RzA',
                    title='這是第二塊模板',
                    text='副標題可以自己改',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=2'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是2'
                        ),
                        URITemplateAction(
                            label='進入2的網頁',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Number_2_in_light_blue_rounded_square.svg/200px-Number_2_in_light_blue_rounded_square.svg.png'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png',
                    title='這是第三11個模塊',
                    text='最多可以放十個',
                    actions=[
                        PostbackTemplateAction(
                            label='回傳一個訊息',
                            data='這是ID=3'
                        ),
                        MessageTemplateAction(
                            label='用戶發送訊息',
                            text='我知道這是3'
                        ),
                        URITemplateAction(
                            label='uri2',
                            uri='https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Number_3_in_yellow_rounded_square.svg/200px-Number_3_in_yellow_rounded_square.svg.png'
                        )
                    ]
                )
            ]
        )
    )
    return message

def image_carousel_message1():
    message = TemplateSendMessage(
        alt_text='圖片畫廊',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="data:image/jpeg;base64,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",
                    action=URITemplateAction(
                        label="新鮮水果",
                        uri="https://www.facebook.com/zhuyu.ceramics.studio/"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QOcAvjt.jpg",
                    action=URITemplateAction(
                        label="新鮮蔬菜",
                        uri="https://cdn.101mediaimage.com/img/file/1410464751urhp5.jpg"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/Np7eFyj.jpg",
                    action=URITemplateAction(
                        label="可愛狗狗",
                        uri="http://imgm.cnmo-img.com.cn/appimg/screenpic/big/674/673928.JPG"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://i.imgur.com/QRIa5Dz.jpg",
                    action=URITemplateAction(
                        label="可愛貓咪",
                        uri="https://m-miya.net/wp-content/uploads/2014/07/0-065-1.min_.jpg"
                    )
                )
            ]
        )
    )
    return message

#關於LINEBOT聊天內容範例