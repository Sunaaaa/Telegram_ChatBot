import requests

api_url = "https://translation.googleapis.com/language/translate/v2"
key = "AIzaSyDj5MSH4w0_PxtZPUxQMryPrzikGRMH2Ag"
data = {
    'q' : '엄마 판다는 새끼가 있네',
    'source' : 'ko',
    'target' : 'en'
}

# POST 방식
# 결과 값은 json으로 받는다.
result = requests.post(f'{api_url}?key={key}', data).json()

print(result)
# -> {'data' : {"translations": [{"translatedText": "Mother Panda has a baby" }]}}
