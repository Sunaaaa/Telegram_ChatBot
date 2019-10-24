# 텔레그램 봇 (Telegram Bot)

- 챗봇 시작하기

  ![1571877409982](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571877409982.png)

- 새로운 봇 만들기

  ![1571877555299](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571877555299.png)

- 봇 이름 설정 & 인증키

  ![1571877577486](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571877577486.png)

- 요청 URL

  ```
  https://api.telegram.org/bot<token>/METHOD_NAME
  ```

- 나의 봇 시작

  ![1571877988105](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571877988105.png)



### getMe

- 나의 챗봇에 대한 정보

  ```
  https://api.telegram.org/bot<token>/getMe
  ```

  - 결과화면

    ![1571878285426](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571878285426.png)



### getUpdates

- 나의 챗봇에게 들어온 메시지 내역 확인

  ```
  https://api.telegram.org/bot<token>/getUpdates
  ```

  - 챗봇에게 보낸 메시지 

    ![1571878391657](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571878391657.png)

  - 결과화면

    ![1571878370343](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571878370343.png)



<br>

### sendMessage

#### URL로 메시지 보내기

- chat_id (필수)

- text (필수)

  ```
  https://api.telegram.org/bot<token>/sendMessage?chat_id=[chat_id]&text=메시지 보냈다
  ```

  

  - 실행화면

    ![1571879347388](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571879347388.png)

  - 챗봇이 보낸 메시지 받기

    ![1571879373154](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571879373154.png)

<br>

#### python 코드로 메시지 보내기

##### Token과 Chat_id 공개

- send_message.py

  ```
  import requests
  
  api_url = 'https://api.telegram.org'
  token = '<token>'
  chat_id = '968602197'
  text = input('메시지를 입력해주세요!')
  
  requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
  ```

  - 실행화면

    ![1571880906881](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571880906881.png)

- 실행화면

  ![1571879872234](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571879872234.png)





##### Token과 Chat_id 숨기기

- decouple 모듈 설치하기

  - 프로젝트에서 사용할 환경변수에서 설정한다.

    ```bash
    $pip install python-decouple
    ```

    ![1571880283888](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571880283888.png)

    - 설치 확인

      ![1571880311320](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571880311320.png)

  

  - vi .env

    - 

      ```bash
      $vi .env
      ```

      

      - 여기에 쓰기 ( `i` )

        ![1571880507028](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571880507028.png)

      - ESC 키를 눌러 수정모드 종료

      - `:wq`를 눌러 저장하고 나가기

      - vi .env 로 확인한 뒤, :q로 나가기

  

- 환경변수로 저장한 데이터를 가져와서 사용한다.

  - Token과 Chat_id를 Python 코드에서 숨긴다.

    - send_message.py

      ```
      from decouple import config
      import requests
      
      api_url = 'https://api.telegram.org'
      token = config('TELEGRAM_BOT_TOKEN')
      chat_id = config('CHAT_ID')
      text = input('메시지를 입력해주세요!')
      
      requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
      ```

      - 실행화면

        ![1571881815513](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571881815513.png)

    - 실행화면

      ![1571881963203](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571881963203.png)

- vi .gitignore

  - env 파일은 무시한다.

    ![1571880769920](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571880769920.png)





- app.py에 send_message.py를 합치기

  - 실행화면

    ![1571883927281](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571883927281.png)

- 실행화면

  ![1571883907259](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571883907259.png)

- 실행화면

  ![1571883943034](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571883943034.png)





Telegram 서버가 사용자로부터 Message를 받으면 나의 Flask 서버로 알린다. 

- 텔레그램 서버가 우리 서버에게 HTTP POST 요청을 통해, 사용자 메시지 정보를 받아! 라고 전달해 주는 것

  - 우리가 local에서만 알수 있도록 Token정보를 준다.
  - 특정 서버에게 보낼 때는 GET이 아닌 POST로 정해져 있기 때문에 무조건 POST 방식

  

  - 우리가 status 200을 리턴해줘야 텔레그램 측이 더 이상의 전송을 중단한다.

    - 200을 안돌려주면 계~~~속 POST 요청을 여러번 보낸다.

    - 상태 코드 (200) 를 돌려주면 그만 보낸다.

      ```
      @app.route('/{token}', methods=['POST'])
      def telegram():
          return '', 200
      
      ```

      

### ngrok

- ngrok을 통해 로컬에 켜져있는 서버를 다른 사람들이 접근할 수 있도록 한다.

- cmd 창에서 `ngrok http 5000`명령어로 서버를 열어준다.

  ![1571884917082](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571884917082.png)

- 결과화면

  ![1571884894630](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571884894630.png)





- 텔레그램아, 너네가 메시지를 받으면 https://e824e940.ngrok.io  여기로 보내줘로 설정

  ```
  [ngrok주소]/<token>
  ```



setWebhook()

- 웹훅 설정 

  ```
  https://api.telegram.org/bot1056054121:AAH1U9wfbuqp-fJ6JGfEBr1vgX1qYFfpIVY/setWebhook?url=https://e824e940.ngrok.io/1056054121:AAH1U9wfbuqp-fJ6JGfEBr1vgX1qYFfpIVY
  ```

  - 실행화면

    ![1571890236378](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571890236378.png)



#### Echo

- 메아리

  - 사용자가 메시지를 보내면 그대로 다시 보내준다.

    - app.py

      ```python 
      @app.route(f'/{token}', methods=['POST'])
      def telegram():
          # 1. 메아리 (Echo) : 사용자가 메시지를 보내면 그대로 다시 보내준다.
          # 1.1 request.get_json() 구조 확인하기
          print(request.get_json())
      
          # 1.2 [실습] 사용자 아이디, 텍스트 가져오기
          echo_chat_id = request.get_json().get('message').get('from').get('id')
          echo_text = request.get_json().get('message').get('text')
      
      
          # 1.3 [실습] 텔레그램 API에게 요청을 보내서 답변해주기
          requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={echo_chat_id}&text={echo_text}')
      
          return '', 200
      ```

      

    - 실행화면

      ![1571891281581](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571891281581.png)

    - 실행화면

      ![1571891444610](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571891444610.png)



#### Echo + lotto + vonvon 

- 실행화면

  ![1571895096732](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571895096732.png)



PythonAnyWhere

> https://www.pythonanywhere.com/

- 무료로 빠르게 할 수 있다. 

![1571897247462](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571897247462.png)



- ```
  https://sunah.pythonanywhere.com/
  ```

  

![1571897347563](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571897347563.png)





- ssss

  ![1571897386269](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571897386269.png)



- ksjd

  ![1571897458757](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571897458757.png)



- skjds

  ![1571897479786](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571897479786.png)



- request 등의 라이브러리는 이미 설치 됨

  - decouple 설치하자

    ![1571897525207](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571897525207.png)

  - Bash를 열어 설치

    ![1571897597101](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571897597101.png)

    - 설치 완료

      ![1571897630166](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571897630166.png)

- 환경 설정하기

  - .env 파일 생성하기

    ![1571897875686](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571897875686.png)

  - .env 파일 작성하기

    ```
    TELEGRAM_BOT_TOKEN='1056054121:AAH1U9wfbuqp-fJ6JGfEBr1vgX1qYFfpIVY'
    CHAT_ID='968602197'
    ```

    ![1571897825967](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571897825967.png)

- webhook을 변경한다. 

  - 기존의 ngrok webhook을 없앤다.

    ```
    https://api.telegram.org/bot1056054121:AAH1U9wfbuqp-fJ6JGfEBr1vgX1qYFfpIVY/deleteWebhook
    ```

    ![1571898353388](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571898353388.png)

    ![1571898327031](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571898327031.png)

  - 새로운 webhook을 설정한다.

    ```
    https://api.telegram.org/bot1056054121:AAH1U9wfbuqp-fJ6JGfEBr1vgX1qYFfpIVY/setWebhook?url=https://sunah.pythonanywhere.com/1056054121:AAH1U9wfbuqp-fJ6JGfEBr1vgX1qYFfpIVY
    ```

    ![1571898607195](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571898607195.png)



- 실행화면

  - 로또

    ![1571898981555](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571898981555.png)

  - 신이 나를 만들 때

    ![1571900747156](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571900747156.png)





#### 구글 클라우드 API

> [google cloud api](https://cloud.google.com/apis/docs/overview?hl=ko)

