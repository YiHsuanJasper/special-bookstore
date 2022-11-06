import streamlit as st
import requests



def getAllBookstore():
    url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M' 
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    res = response.json()
    return res



def getCountyOption(items):
    optionList = []# 創建一個空的 List 並命名為 optionList
    for item in items:
        name = item['cityName'][0:3]
        if name not in optionList:
            optionList.append(name)

    
		#name = # 把 cityname 欄位中的縣市名稱擷取出來 並指定給變數 name
		# hint: 想辦法處理 item['cityName'] 的內容

		# 如果 name 不在 optionList 之中，便把它放入 optionList
		# hint: 使用 if-else 來進行判斷 / 用 append 把東西放入 optionList
    return optionList




def app():
  bookstorelist = getAllBookstore()# 呼叫 getAllBookstore 函式並將其賦值給變數 bookstoreList
  countyOption = getCountyOption(bookstorelist)
  st.header('特色書店地圖')
  st.metric('Total bookstore', len(bookstorelist)) # 將 118 替換成書店的數量
  county = st.selectbox('請選擇縣市', countyOption)
  district = st.multiselect('請選擇區域', ['a', 'b', 'c', 'd'])

if __name__ == '__main__':
    app()

