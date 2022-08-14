#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *


def image_carousel_message1():
    message = TemplateSendMessage(
        alt_text='圖片畫廊',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://ireneslife.com/wp-content/uploads/2019/12/1575194969-1e860b27963d9e9d48e73585da40d20f.jpg",
                    action=URITemplateAction(
                        label="球場",
                        uri="http://twbsball.dils.tku.edu.tw/wiki/index.php/%E5%85%84%E5%BC%9F%E9%BE%8D%E6%BD%AD%E6%A3%92%E7%90%83%E5%A0%B4"
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