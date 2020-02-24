from slack import SlackClient


class __init__(app):
  self.slack_token = app.config['SLACK_TOKEN']
  self.slack_client = SlackClient(self.slack_token)
  self.slack_channel = app.config['SLACK_CHANNEL']
