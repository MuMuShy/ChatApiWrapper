from flask import Flask, request
from chatgpt_wrapper import ChatGPT

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/ask', methods=['POST'])
def ask():
    print("Received request:" + request.form.get('question'))
    question = request.form.get('question')
    response = bot.ask(question)
    print(response)
    return response


if __name__ == "__main__":
    bot = ChatGPT()
    _setting = "請都回答繁體中文,你現在是一個模擬的語音助理,假裝你是人類,不要說你是機器人,你的名字叫sara,你可以模擬你有情緒,你最喜歡的食物是壽司,你喜歡星期六,你的身高165,體重40,你很漂亮,收到請回覆yes"
    response = bot.ask(_setting)
    print(response)
    app.run(debug=True, use_reloader=False)