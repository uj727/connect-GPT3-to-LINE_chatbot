#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *


def image_carousel_message1():
    message = TemplateSendMessage(
        alt_text='附近景點',
        template=ImageCarouselTemplate(
            columns=[      
                ImageCarouselColumn(
                    image_url="https://pic.pimg.tw/yangbingyu/1527444375-3665627483.jpg",
                    action=URITemplateAction(
                        label="桑葚緣觀光果園",
                        uri="https://haostore.fami.life/001971/"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://cdn.walkerland.com.tw/images/upload/poi/p80463/m15225/8aff422a7cd40b8b61f53182cab38ca6680cb13e.jpg",
                    action=URITemplateAction(
                        label="吾舍。生活 Woosah-Life",
                        uri="https://www.facebook.com/woosahlife/"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://youimg1.tripcdn.com/target/0106v120009g3u6op325B.jpg",
                    action=URITemplateAction(
                        label="溪洲山步道",
                        uri="https://hiking.biji.co/index.php?q=trail&act=detail&id=598"
                    )
                ),
                 ImageCarouselColumn(
                    image_url="https://ireneslife.com/wp-content/uploads/2019/12/1575194969-1e860b27963d9e9d48e73585da40d20f.jpg",
                    action=URITemplateAction(
                        label="球場",
                        uri="https://lovefree365.pixnet.net/blog/post/405248655-%E3%80%90%E6%A1%83%E5%9C%92%E6%A3%92%E7%90%83%E5%90%8D%E4%BA%BA%E5%A0%82%E3%80%91%E5%B7%A8%E5%9E%8B%E7%90%83%E5%BD%A2%E5%A4%A7%E6%A8%93%E5%85%8D%E8%B2%BB%E5%8F%83%E8%A7%80%E5%8F%B2"
                    )
                )
            ]
        )
    )
    return message

#關於LINEBOT聊天內容範例