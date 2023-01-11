#Specifying the base image
FROM python:3.9

ADD example-telegram-bot.py .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir pyTelegramBotAPI

#The installed the dependencies
CMD [ "python", "./example-telegram-bot.py" ]

#lastly we specified the entry command this line is simply running python 
# ./example-telegram-bot.py in our container terminal