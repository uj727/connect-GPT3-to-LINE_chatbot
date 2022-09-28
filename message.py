#這些是LINE官方開放的套件組合透過import來套用這個檔案上
from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *


def image_carousel_message1():
    message = TemplateSendMessage(
        alt_text='圖片',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url="https://pic.pimg.tw/anrine910070/1652187202-2764170010-g.jpg",
                    action=URITemplateAction(
                        label="山水沙灘",
                        uri="https://www.penghu-nsa.gov.tw/TravelInformationSceneryDetailC001200.aspx?Cond=eb226be1-d129-473b-bf39-d9b2e6ccf0e2&SortType=1&SearchAdvanced=False&Language=1028"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://pic.easytravel.com.tw/Attachments/m/A78360.jpg",
                    action=URITemplateAction(
                        label="大菓葉柱狀玄武岩",
                        uri="https://rainieis.tw/daguoye-columnar-basalt/"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://www.94i-penghu.com/play-detail/upload/catalog_play_m/tw_catalog_play_list_18j12_8db466e9mc.jpg",
                    action=URITemplateAction(
                        label="奎壁山地質公園",
                        uri="https://www.travelking.com.tw/tourguide/scenery105377.html"
                    )
                ),
                ImageCarouselColumn(
                    image_url="https://image.lanlan.tw/flickr/14383824929_cb1850bb16_o.jpg",
                    action=URITemplateAction(
                        label="仙人掌冰",
                        uri="https://penghuzine.com/eatinpenghu/d090/"
                    )
                )
            ]
        )
    )
    return message
#關於LINEBOT聊天內容範例