# 텔레그램 봇 (Telegram Bot)

- 챗봇 시작하기

  ![1571877409982](https://user-images.githubusercontent.com/39547788/67467938-9a847a00-f684-11e9-99ca-781720c5e77c.png)

- 새로운 봇 만들기

  ![1571877555299](https://user-images.githubusercontent.com/39547788/67467872-92c4d580-f684-11e9-920e-34b3b8bac037.png)

- 봇 이름 설정 & 인증키

  ![1571877577486](https://user-images.githubusercontent.com/39547788/67467875-92c4d580-f684-11e9-9ded-9ad5d0dd3899.png)

- 요청 URL

  ```
  https://api.telegram.org/bot<token>/METHOD_NAME
  ```

- 나의 봇 시작

  ![1571877988105](https://user-images.githubusercontent.com/39547788/67467877-92c4d580-f684-11e9-9b4a-05eefd7dd0c8.png)



### getMe

- 나의 챗봇에 대한 정보

  ```
  https://api.telegram.org/bot<token>/getMe
  ```

  - 결과화면

    ![1571878285426](https://user-images.githubusercontent.com/39547788/67467879-935d6c00-f684-11e9-9ea5-f398ce085834.png)



### getUpdates

- 나의 챗봇에게 들어온 메시지 내역 확인

  ```
  https://api.telegram.org/bot<token>/getUpdates
  ```

  - 챗봇에게 보낸 메시지 

    ![1571878391657](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1571878391657.png)

  - 결과화면

    ![1571878370343](https://user-images.githubusercontent.com/39547788/67467880-935d6c00-f684-11e9-8ac6-258d2f9b725d.png)



<br>

### sendMessage

#### URL로 메시지 보내기

- chat_id (필수)

- text (필수)

  ```
  https://api.telegram.org/bot<token>/sendMessage?chat_id=[chat_id]&text=메시지 보냈다
  ```

  

  - 실행화면

    ![1571879347388](https://user-images.githubusercontent.com/39547788/67467882-935d6c00-f684-11e9-85e9-e676fdc9c333.png)

  - 챗봇이 보낸 메시지 받기

    ![1571879373154](https://user-images.githubusercontent.com/39547788/67467883-93f60280-f684-11e9-9e22-74ee674c7e08.png)

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

  ![1571879872234](https://user-images.githubusercontent.com/39547788/67467886-93f60280-f684-11e9-8231-3c3c1be15ed7.png)





##### Token과 Chat_id 숨기기

- decouple 모듈 설치하기

  - 프로젝트에서 사용할 환경변수에서 설정한다.

    ```bash
    $pip install python-decouple
    ```

    ![1571880283888](https://user-images.githubusercontent.com/39547788/67467887-93f60280-f684-11e9-9fa4-e31713e19d4c.png)

    - 설치 확인

      ![1571880311320](https://user-images.githubusercontent.com/39547788/67467889-93f60280-f684-11e9-9937-9b3883095a43.png)

  

  - vi .env

    - 

      ```bash
      $vi .env
      ```

      

      - 여기에 쓰기 ( `i` )

        ![1571880507028](https://user-images.githubusercontent.com/39547788/67467890-948e9900-f684-11e9-84c7-108de7ce59f1.png)

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

        ![1571881815513](https://user-images.githubusercontent.com/39547788/67467894-95272f80-f684-11e9-8292-ec45e331f658.png)

    - 실행화면

      ![1571881963203](https://user-images.githubusercontent.com/39547788/67467895-95272f80-f684-11e9-9935-58fec4544a1e.png)

- vi .gitignore

  - env 파일은 무시한다.

    ![1571880769920](https://user-images.githubusercontent.com/39547788/67467891-948e9900-f684-11e9-82cf-16ef882450a5.png)











------

- app.py에 send_message.py를 합치기

  - 실행화면

    ![1571883927281](https://user-images.githubusercontent.com/39547788/67467898-95bfc600-f684-11e9-8da5-9c5043c040fd.png)

- 실행화면

  ![1571883907259](https://user-images.githubusercontent.com/39547788/67467897-95272f80-f684-11e9-9752-d27fb1ab56f2.png)

- 실행화면

  ![1571883943034](https://user-images.githubusercontent.com/39547788/67467899-95bfc600-f684-11e9-993c-ad88f6089d0c.png)





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

  ![1571884917082](https://user-images.githubusercontent.com/39547788/67467900-95bfc600-f684-11e9-92dc-5f4e81a13eeb.png)

- 결과화면

  ![1571884894630](https://user-images.githubusercontent.com/39547788/67467901-95bfc600-f684-11e9-9af7-8792fc0efe46.png)





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

    ![1571890236378](https://user-images.githubusercontent.com/39547788/67467903-96585c80-f684-11e9-8517-1ec659ef9678.png)



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

      ![1571891281581](https://user-images.githubusercontent.com/39547788/67467904-96585c80-f684-11e9-92cf-f58e1cf06a16.png)

    - 실행화면

      ![1571891444610](https://user-images.githubusercontent.com/39547788/67467905-96585c80-f684-11e9-970c-ef21945b8d53.png)



#### Echo + lotto + vonvon 

- 실행화면

  ![1571895096732](https://user-images.githubusercontent.com/39547788/67467907-96f0f300-f684-11e9-8c3e-f06577c4d511.png)



PythonAnyWhere

> https://www.pythonanywhere.com/

- 무료로 빠르게 할 수 있다. 

![1571897247462](https://user-images.githubusercontent.com/39547788/67467908-96f0f300-f684-11e9-8a99-0d4c12d643bb.png)



- ```
  https://sunah.pythonanywhere.com/
  ```

  

![1571897347563](https://user-images.githubusercontent.com/39547788/67467911-96f0f300-f684-11e9-856e-18d761333dd2.png)





- ssss

  ![1571897386269](https://user-images.githubusercontent.com/39547788/67467912-97898980-f684-11e9-831a-675359a2bf71.png)



- ksjd

  ![1571897458757](https://user-images.githubusercontent.com/39547788/67467913-97898980-f684-11e9-8f1f-81e92581a337.png)



- skjds

  ![1571897479786](https://user-images.githubusercontent.com/39547788/67467918-98222000-f684-11e9-9db0-1b8b90169987.png)



- request 등의 라이브러리는 이미 설치 됨

  - decouple 설치하자

    ![1571897525207](https://user-images.githubusercontent.com/39547788/67467919-98222000-f684-11e9-8787-df659d6213ee.png)

  - Bash를 열어 설치

    ![1571897597101](https://user-images.githubusercontent.com/39547788/67467920-98bab680-f684-11e9-94cc-4f1d50ad7a87.png)

    - 설치 완료

      ![1571897630166](https://user-images.githubusercontent.com/39547788/67467922-98bab680-f684-11e9-9275-5560c408d682.png)

- 환경 설정하기

  - .env 파일 생성하기

    ![1571897875686](https://user-images.githubusercontent.com/39547788/67467924-98bab680-f684-11e9-9879-7fd840f567e1.png)

  - .env 파일 작성하기

    ```
    TELEGRAM_BOT_TOKEN='1056054121:AAH1U9wfbuqp-fJ6JGfEBr1vgX1qYFfpIVY'
    CHAT_ID='968602197'
    ```

    ![1571897825967](https://user-images.githubusercontent.com/39547788/67467923-98bab680-f684-11e9-8a60-72e3d1b708b7.png)

- webhook을 변경한다. 

  - 기존의 ngrok webhook을 없앤다.

    ```
    https://api.telegram.org/bot1056054121:AAH1U9wfbuqp-fJ6JGfEBr1vgX1qYFfpIVY/deleteWebhook
    ```

    ![1571898353388](https://user-images.githubusercontent.com/39547788/67467930-99ebe380-f684-11e9-94bc-86c9ec8ee10e.png)

    ![1571898327031](https://user-images.githubusercontent.com/39547788/67467926-99534d00-f684-11e9-914c-1700d2a21b32.png)

  - 새로운 webhook을 설정한다.

    ```
    https://api.telegram.org/bot1056054121:AAH1U9wfbuqp-fJ6JGfEBr1vgX1qYFfpIVY/setWebhook?url=https://sunah.pythonanywhere.com/1056054121:AAH1U9wfbuqp-fJ6JGfEBr1vgX1qYFfpIVY
    ```

    ![1571898607195](https://user-images.githubusercontent.com/39547788/67467933-99ebe380-f684-11e9-8796-5efe39e377b5.png)



- 실행화면

  - 로또

    ![1571898981555](https://user-images.githubusercontent.com/39547788/67467935-99ebe380-f684-11e9-87a9-5f6edf819936.png)

  - 신이 나를 만들 때

    ![1571900747156](https://user-images.githubusercontent.com/39547788/67467937-9a847a00-f684-11e9-8d71-330e586de8a0.png)





#### 구글 클라우드 API

> [google cloud api](https://cloud.google.com/apis/docs/overview?hl=ko)

