#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

def Carousel_Template():
    message = TemplateSendMessage(
        alt_text='附近',
        template=CarouselTemplate(
            columns=[
                # CarouselColumn(
                #     thumbnail_image_url='data:image/png;base64,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',
                #     title='這是第一塊模板',
                    
                #     actions=[
                        
                #         LocationSendMessage(
                #             title="1",
                #             address ="1",
                #             latitude ="25.0477545",
                #             longitude ="121.5170599"
                #         ),
                #         URITemplateAction(
                #             label='進入1的網頁',
                #             uri='https://www.facebook.com/zhuyu.ceramics.studio/'
                #         )
                #     ]
                # ),
                # CarouselColumn(
                #     thumbnail_image_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuo7n2_HNSFuT3T7Z9PUZmn1SDM6G6-iXfRC3FxdGTj7X1Wr0RzA',
                #     title='這是第二塊模板',
                #     text='副標題可以自己改',
                #     actions=[
                        
                #         MessageTemplateAction(
                #             label='用戶發送訊息',
                #             text='我知道這是2'
                #         ),
                #         URITemplateAction(
                #             label='進入2的網頁',
                #             uri='https://upload.wikimedia.org/wikipedia/commons/thumb/c/cd/Number_2_in_light_blue_rounded_square.svg/200px-Number_2_in_light_blue_rounded_square.svg.png'
                #         )
                #     ]
                # ),
                CarouselColumn(
                    thumbnail_image_url='data:image/png;base64,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',
                    title='這是第三11個模塊',
                    text='最多可以放十個',
                    actions=[
                        
                        MessageTemplateAction(
                            label='用戶發送訊',
                            text='我知道這是3'
                        ),
                        URITemplateAction(
                            label='uri2',
                            uri='https://www.facebook.com/zhuyu.ceramics.studio/'
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
                    image_url="",
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