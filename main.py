
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
bot = ChatBot("My Bot")

convo = [
    'hello',
    'hi there!',
    'what is your name ?',
    'My name is Bot,  i am created by Pooja',
    'How are you?',
    'I am doing great these days',
    'thank you',
    'In Which city you live',
    'I live in Lucknow',
    'In which language you talk',
    'I mostly talk in English'
]

trainer = ListTrainer(bot)

trainer.train(convo)
# answer = bot.get_response("what is your name?")
# print(answer)
print("Talk to bot")
while True:
    query = input()
    if query == 'exit':
        break
    answer = bot.get_response(query)
    print("bot :", answer)
