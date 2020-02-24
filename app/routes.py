from app import app, db


@app.route('/')
@app.route('/index')
def index():
  print("HERE")
  print(request.headers)
  return 'app is here'


@app.route('/test')
def post_test_message():
  # print(type(slackbot.slack))
  # slackbot.slack.chat.post_message('#publications', 'testing from flask app')
  return None
