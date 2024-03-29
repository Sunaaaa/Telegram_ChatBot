# 텔레그램 봇 (Telegram Bot)

<br>

## 텔레그램 챗봇 (SunAh)

- 챗봇 시작하기

  ![1571877409982](https://user-images.githubusercontent.com/39547788/67467938-9a847a00-f684-11e9-99ca-781720c5e77c.png)

  <br>

- 새로운 봇 만들기

  ![1571877555299](https://user-images.githubusercontent.com/39547788/67467872-92c4d580-f684-11e9-920e-34b3b8bac037.png)

  <br>

- 봇 이름 설정 & 인증키

  ![1571985217198](https://user-images.githubusercontent.com/39547788/67549654-ba2ca880-f73f-11e9-9662-c2781fae4255.png)

  <br>

- 요청 URL

  ```
  https://api.telegram.org/bot<token>/METHOD_NAME
  ```

  <br>

- 나의 봇 시작

  ![1571877988105](https://user-images.githubusercontent.com/39547788/67467877-92c4d580-f684-11e9-9b4a-05eefd7dd0c8.png)

<br><br>

### getMe

- 나의 챗봇에 대한 정보

  ```
  https://api.telegram.org/bot<token>/getMe
  ```

  - 결과화면

    ![1571985133537](https://user-images.githubusercontent.com/39547788/67549653-b9941200-f73f-11e9-9f17-d7ea6dab7d47.png)

<br><br>

### getUpdates

- 나의 챗봇에게 들어온 메시지 내역 확인

  ```
  https://api.telegram.org/bot<token>/getUpdates
  ```

  - 챗봇에게 보낸 메시지 

    ![1571878391657](https://user-images.githubusercontent.com/39547788/67467881-935d6c00-f684-11e9-80f1-2932ae2c1c39.png)

    <br>

  - 결과화면

    ![1571985092748](https://user-images.githubusercontent.com/39547788/67549651-b9941200-f73f-11e9-8973-bd1987b9835d.png)



<br><br>

### sendMessage

#### URL로 메시지 보내기

- chat_id (필수)

- text (필수)

  ```
  https://api.telegram.org/bot<token>/sendMessage?chat_id=[chat_id]&text=메시지 보냈다
  ```

  <br>

  - 실행화면

    ![1571984978875](https://user-images.githubusercontent.com/39547788/67549650-b9941200-f73f-11e9-89b6-6a38fcde7caa.png)

    <br>

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

  - (venv) 가상환경 실행화면

    ![1571880906881](https://user-images.githubusercontent.com/39547788/67467892-948e9900-f684-11e9-8f84-9321458b13fc.png)

    <br>

- 가상환경 터미널에서 보낸 메시지를 텔레그램에서 받기

  ![1571879872234](https://user-images.githubusercontent.com/39547788/67467886-93f60280-f684-11e9-8231-3c3c1be15ed7.png)

  <br>





##### Token과 Chat_id 숨기기

- decouple 모듈 설치하기

  - 프로젝트에서 사용할 환경변수에서 설정한다.

    ```bash
    $pip install python-decouple
    ```

    ![1571880283888](https://user-images.githubusercontent.com/39547788/67467887-93f60280-f684-11e9-9fa4-e31713e19d4c.png)

    <br>

    - 설치 확인 `pip list`

      ![1571880311320](https://user-images.githubusercontent.com/39547788/67467889-93f60280-f684-11e9-9937-9b3883095a43.png)

      <br>

- .env 환경 설정 파일 생성

  - .env 파일을 만들어 Token과 Chat_id 값을 저장한다.

    - .env 파일 생성 (`vi .env`)

      ```bash
      $vi .env
      ```

      <br>

    - 여기에 쓰기 ( `i` )

      ![1571984904819](https://user-images.githubusercontent.com/39547788/67549649-b9941200-f73f-11e9-9267-6640cf5fc862.png)

      <br>

    - ESC 키를 눌러 수정모드 종료

    - `:wq`를 눌러 저장하고 나가기

    - vi .env 로 확인한 뒤, :q로 나가기

  <br>

- 환경변수로 저장한 데이터를 가져와서 사용한다.

  - Token과 Chat_id를 Python 코드에서 숨긴다.

    - decouple 모듈의 config를 import한다.

      ```python 
      from decouple import config
      ```

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

        - (venv) 가상환경 실행화면

          ![1571881815513](https://user-images.githubusercontent.com/39547788/67467894-95272f80-f684-11e9-8292-ec45e331f658.png)

          <br>

      - 가상환경 터미널에서 보낸 메시지를 텔레그램에서 받기

        ![1571881963203](https://user-images.githubusercontent.com/39547788/67467895-95272f80-f684-11e9-9935-58fec4544a1e.png)

        <br>

- vi .gitignore

  - env 파일은 무시하는 gitignore 파일 생성

    - [gitignore](https://github.com/github/gitignore/blob/master/Python.gitignore)의 내용을 복사 붙여넣기 한다.

    ![1571880769920](https://user-images.githubusercontent.com/39547788/67467891-948e9900-f684-11e9-82cf-16ef882450a5.png)





#### app.py 완성

##### app.py에 send_message.py를 추가하기

- Form에 메시지를 입력한다.

  ![1571883927281](https://user-images.githubusercontent.com/39547788/67467898-95bfc600-f684-11e9-8da5-9c5043c040fd.png)

- 메시지 보내기 버튼을 누르면 아래의  전송 완료 화면이 보인다.

  ![1571883907259](https://user-images.githubusercontent.com/39547788/67467897-95272f80-f684-11e9-9752-d27fb1ab56f2.png)

- Form을 통해 보낸 메시지를 텔레그램에서 받는다. 

  ![1571883943034](https://user-images.githubusercontent.com/39547788/67467899-95bfc600-f684-11e9-993c-ad88f6089d0c.png)



#### Message 수신 알림

> Telegram 서버가 사용자로부터 Message를 받으면 나의 Flask 서버로 알린다. 

<br>

- 텔레그램 서버가 우리 서버에게 HTTP POST 요청을 통해, 사용자 메시지 정보를 받아! 라고 전달해 주는 것

  - 우리가 local에서만 알수 있도록 Token정보를 준다.
  - 특정 서버에게 보낼 때는 GET이 아닌 POST로 정해져 있기 때문에 무조건 POST 방식

  <br>

  - 우리가 status 200을 리턴해줘야 텔레그램 측이 더 이상의 전송을 중단한다.

    - 200을 안돌려주면 계~~~속 POST 요청을 여러번 보낸다.

    - 상태 코드 (200) 를 돌려주면 그만 보낸다.

      ```python 
      @app.route('/{token}', methods=['POST'])
      def telegram():
          return '', 200
      ```

      <br><br>

### ngrok

- ngrok을 통해 로컬에 켜져있는 서버를 다른 사람들이 접근할 수 있도록 한다.

- cmd 창에서 `ngrok http 5000`명령어로 서버를 열어준다.

  ![1571884917082](https://user-images.githubusercontent.com/39547788/67467900-95bfc600-f684-11e9-92dc-5f4e81a13eeb.png)

  <br>

- 결과화면

  ![1571884894630](https://user-images.githubusercontent.com/39547788/67467901-95bfc600-f684-11e9-9af7-8792fc0efe46.png)



<br>

- 텔레그램아, 너네가 메시지를 받으면 https://e824e940.ngrok.io  여기로 보내줘로 설정

  ```
  [ngrok주소]/<token>
  ```

<br>



#### setWebhook()

- 웹훅 설정 

  ```
  https://api.telegram.org/bot<token>/setWebhook?url=https://e824e940.ngrok.io/<token>
  ```

  - 실행화면

    ![1571890236378](https://user-images.githubusercontent.com/39547788/67467903-96585c80-f684-11e9-8517-1ec659ef9678.png)

<br>

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

      <br>

    - 실행화면

      ![1571891444610](https://user-images.githubusercontent.com/39547788/67467905-96585c80-f684-11e9-970c-ef21945b8d53.png)

      <br>



#### Echo + lotto + vonvon 

- 실행화면

  ![1571895096732](https://user-images.githubusercontent.com/39547788/67467907-96f0f300-f684-11e9-8c3e-f06577c4d511.png)

  <br>

<br>



### PythonAnyWhere

> https://www.pythonanywhere.com/

- 무료로 빠르게 할 수 있다. 

- **Python을 기반으로 한 온라인 IDE 및 웹 호스팅을 통합한 서비**스이다.

  ![1571897247462](https://user-images.githubusercontent.com/39547788/67467908-96f0f300-f684-11e9-8a99-0d4c12d643bb.png)

<br>



1. 나의 PythonAnyWhere 서버 주소

   ```
   https://sunah.pythonanywhere.com/
   ```

   <br>

   - PythonAnyWhere 서버 주소로 실행한 화면

     ![1571897347563](https://user-images.githubusercontent.com/39547788/67467911-96f0f300-f684-11e9-856e-18d761333dd2.png)

<br>

2. 나의 python 코드 (app.py) 저장하기 

   ![1571897386269](https://user-images.githubusercontent.com/39547788/67467912-97898980-f684-11e9-831a-675359a2bf71.png)

<br>



3. 기존에 작성한 app.py의 코드를 flask_app.py 파일에 옮겨 적는다.

   ![1571897458757](https://user-images.githubusercontent.com/39547788/67467913-97898980-f684-11e9-8f1f-81e92581a337.png)

<br>



4. Reload 버튼을 눌러 새로고침을 수행

   ![1571897479786](https://user-images.githubusercontent.com/39547788/67467918-98222000-f684-11e9-9db0-1b8b90169987.png)

<br>



5. 필요한 라이브러리 설치하기

   - request 등의 라이브러리는 이미 설치 되어있다.

     - decouple 설치하자

     ![1571897525207](https://user-images.githubusercontent.com/39547788/67467919-98222000-f684-11e9-8787-df659d6213ee.png)

     <br>

   - Bash를 열어 설치

     ![1571897597101](https://user-images.githubusercontent.com/39547788/67467920-98bab680-f684-11e9-94cc-4f1d50ad7a87.png)

   - decouple  설치 완료

     ![1571897630166](https://user-images.githubusercontent.com/39547788/67467922-98bab680-f684-11e9-9275-5560c408d682.png)

<br>



6. .env 파일 생성

   - .env 파일 생성하기

     ![1571897875686](https://user-images.githubusercontent.com/39547788/67467924-98bab680-f684-11e9-9879-7fd840f567e1.png)

     <br>

   - .env 파일 작성하기

     - token과 chat_id 값을 저장한다.

       ```bash
       TELEGRAM_BOT_TOKEN='<token>'
       CHAT_ID='<chat_id>'
       ```

       - .env 파일

         ![1571984764666](https://user-images.githubusercontent.com/39547788/67549655-ba2ca880-f73f-11e9-8221-33076e90c85c.png)

<br>



7. webhook 변경

   - 기존의 ngrok webhook을 제거한다.

     ```
     https://api.telegram.org/bot<token>/deleteWebhook
     ```

     ![1571898353388](https://user-images.githubusercontent.com/39547788/67467930-99ebe380-f684-11e9-94bc-86c9ec8ee10e.png)

     <br>

     ![1571898327031](https://user-images.githubusercontent.com/39547788/67467926-99534d00-f684-11e9-914c-1700d2a21b32.png)

   - 새로운 webhook 설정

     ```
     https://api.telegram.org/<token>/setWebhook?url=https://sunah.pythonanywhere.com/<token>
     ```

     ![1571898607195](https://user-images.githubusercontent.com/39547788/67467933-99ebe380-f684-11e9-8796-5efe39e377b5.png)

<br>

8. pythonanywhere 서버를 이용해 텔레그램 챗봇 실행 화면

   - 로또

     ![1571898981555](https://user-images.githubusercontent.com/39547788/67467935-99ebe380-f684-11e9-87a9-5f6edf819936.png)

     <br>

   - 신이 나를 만들 때

     ![1571900747156](https://user-images.githubusercontent.com/39547788/67467937-9a847a00-f684-11e9-8d71-330e586de8a0.png)

<br>





### 구글 클라우드 API

> [google cloud api](https://cloud.google.com/apis/docs/overview?hl=ko)

