
	
	
	
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os


application = Flask(__name__)
app=application

bot = ChatBot("Chatterbot",storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.5,
            'default_response': 'I am sorry, Can you kindly reach the Production Support team member'
        }
    ])

bot.set_trainer(ListTrainer)

bot.train(['Hi','Hello','I have a doubt','Go ahead','What is your name','I am a bot you can call me anything','Who is the biggest car maker in the world.','Toyota','Bye','Bye'])


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))


if __name__ == "__main__":
    app.run()