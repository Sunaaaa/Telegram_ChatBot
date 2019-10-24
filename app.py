from flask import Flask, render_template, request
from decouple import config
import requests, random

app=Flask(__name__)

api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')

@app.route('/')
def hello():
    return "Hello World!"
    # return render_template('index.html')

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    text = request.args.get('message')
    requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    return '<h1>메시지 전송 완료!!</h1>'

# 텔레그램 서버가 우리 서버에게 HTTP POST 요청을 통해,
# 사용자 메시지 정보를 받아! 라고 전달해 주는 것
# 우리가 status 200을 리턴해줘야 텔레그램 측이 더 이상의 전송을 중단한다.
# 200을 안돌려주면 계~~~속 POST 요청을 여러번 보낸다.

'''
@app.route('/{token}', methods=['POST'])
def telegram():
    return '', 200
'''
 
@app.route(f'/{token}', methods=['POST'])
def telegram():
    # 1. 메아리 (Echo) : 사용자가 메시지를 보내면 그대로 다시 보내준다.
    # 1.1 request.get_json() 구조 확인하기
    print(request.get_json())

    # 1.2 [실습] 사용자 아이디, 텍스트 가져오기
    echo_chat_id = request.get_json().get('message').get('from').get('id')
    echo_text = request.get_json().get('message').get('text')

    # 1.3 [실습] 텔레그램 API에게 요청을 보내서 답변해주기
    # requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={echo_chat_id}&text={echo_text}')
    
    # 1. [기본]  로또 기능 (random ... ?)
    #           사용자가 '/로또'라고 말하면 랜덤으로 번호 6개 뽑아서 돌려주기!
    #           나머지 경우엔 전부 메아리 칩니다.


    # 2. [심화] vonvon 기능
    #           사용자가 '/vonvon 이름'이라고 말하면 신이 나를 만들었을 때 요소 돌려주기!

    # switch echo_text:
    #     case '/로또':
    if echo_text == '/로또':
        lotto_num = lotto()
        requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={echo_chat_id}&text={lotto_num}')

    elif echo_text[0:8] == '/vonvon ' and len(echo_text) > 7:
        user_name = echo_text[8:]

        # 2. 사용자에게 보여줄 여러가지 재밌는 특성 리스트를 만든다.
        first_list = ['잘생김', '못생김', '많이 못생김', '많이 잘생김', '앙주']
        second_list = ['자신감', '귀찮음', '쑥쓰러움', '열정적임']
        third_list = ['허세', '물욕', '식욕', '똘기']

        # 3. 특성 리스트에서 랜덤으로 하나씩을 선택한다. 
        first_choice = random.choice(first_list)
        second_choice = random.choice(second_list)
        third_choice = random.choice(third_list)

        vonvon_text = f'{user_name}를 만들 때, {first_choice}, {second_choice}, {third_choice}'
        requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={echo_chat_id}&text={vonvon_text}')


    else :
        requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={echo_chat_id}&text={echo_text}')
        
    return '', 200

def lotto():
    numbers = [str(i) for i in range(1,47)]
    lotto_list = random.sample(numbers, 6)
    result_list = sorted(lotto_list, key=int)
    return ','.join(result_list)

# end of file !!!!!
# debug 모드를 활성화해서 서버 새로고침을 생략한다.
if __name__ == '__main__':
    app.run(debug=True)