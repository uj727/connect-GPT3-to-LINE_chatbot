在LINE導入預訓練語言模型
#python #flask #chatbot #heroku 
功能 LINE模擬真人，客智化自動回覆(非罐頭回覆)

使用方法
1.下載git & heroku crl
2.註冊帳戶 -LINE DEVELOPER(要新增LINE機器人帳號) -openai -heroku(要新增專案)
3.將帳戶的access token(LINE) & secret(LINE) & openai_apikey寫入程式
4.程式中模型為範例模型，可自行更動
5.將專案推上heroku & 把heroku專案的URL + '/callback'放到LINE Developer建立連線
6.關閉LINE自動回覆功能

目前實驗室有 -客服回答模型 -醫療問答模型 -ESG報告生成模型
