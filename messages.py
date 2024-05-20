from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from datetime import datetime
from taxi import main
import taxi

#Constants
TOKEN = '7011760420:AAFvkit_3t8XZCispRt3mIkQHwrd2MG92xk'
BOT_USERNAME = '@TaxiNumberBot'
LOG_FILE = 'logs.txt'

#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Welcome, enter your Medallion number to start!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Close your app, and wait for further instructions.')

# Log
def log(event: str):
    currTime = datetime.now()
    with open(LOG_FILE, 'a') as f:
        f.write(f'{currTime} - {event}\n')

# Responses
def is_valid_user(medallion: str) -> str:
    registered_users = ['6d24', '1t65', '7y91', '8f83']
    if medallion.lower() in registered_users:
        log(f'{medallion} logged in')
        return True
    return False

def register(medallion):
    return taxi.main(medallion)

#Handlers
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    log(f'User ({update.message.chat.id}) sent: {text}')

    if message_type == 'group':
        await update.message.reply_text('Please send me a private message.')
        return

    if not is_valid_user(text):
        await update.message.reply_text('Invalid Medallion number, please try again.')
        return
    
    await update.message.reply_text(f'Welcome {text}!')
    await update.message.reply_text('Please wait, your number is being entered...')
    await update.message.reply_text(register(text))
    
        
#Error
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(f'Update {update} caused error {context.error}')
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    log('Starting bot...')
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    #Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print('Polling...')

    app.run_polling(poll_interval=15)