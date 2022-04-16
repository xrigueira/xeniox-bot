
import ssl
import time
import email
import smtplib

from telegram.update import Update
from telegram.ext.updater import Updater
from telegram.ext.filters import Filters
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.callbackcontext import CallbackContext


updater = Updater('API TOKEN', use_context=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello. This is Xenio, a work in progress.\nWrite /help to see the commands available.')

def help(update: Update, context: CallbackContext):
    update.message.reply_text('I cannot do much now. \nAvalable commands: \n/youtube - To get the youtube URL \n/email - To send an email')

def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text('"Youtube Link =>\
    https://www.youtube.com/"')

class Mail():

    def __init__(self):
        self.port = 465
        self.smtp_server_domain_name = "smtp.gmail.com"
        self.sender = "account@gmail.com"
        self.password = "password"
    
    def send(self, emails, subject, content):
        ssl_context = ssl.create_default_context()
        service = smtplib.SMTP_SSL(self.smtp_server_domain_name, self.port, context=ssl_context)
        service.login(self.sender, self.password)

        for email in emails:
            result = service.sendmail(self.sender, email, f"Subject: {subject}\n{content}")

        service.quit()

def sender(update: Update, context: CallbackContext):
    
    update.message.reply_text('Enter the destinary: ')
    time.sleep(10)
    destinatary = update.message.text # add the command to get the text
    update.message.reply_text('Enter the subject: ')
    time.sleep(10)
    subject = update.message.text # add the command to get the text
    print(destinatary, email)
    
    # mail = Mail()
    # mail.send(destinatary, subject, content)
    # print('email sent to %s' % destinatary)
    
def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry I can't recognize you , you said '%s'" % update.message.text)

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('email', sender))

updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    # Filters out unknown commands
    Filters.command, unknown))

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()