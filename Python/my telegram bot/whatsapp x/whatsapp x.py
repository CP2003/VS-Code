import logging
from dotenv import load_dotenv 
import requests, json, os, threading, pyttsx3, time
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackQueryHandler,
    ConversationHandler,
    CallbackContext,
)

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Stages
FIRST, SECOND = range(2)
# Callback data
ONE, MOD, FM, THREE, SAM, FIVE, whatsapp = range(7)







def start(update: Update, context: CallbackContext) -> int:
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    
    keyboard = [
        [
            InlineKeyboardButton("Get Start", callback_data=str(MOD)),
            ],
          
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    update.message.reply_text(f"Hello {user.first_name} Welcome to Whatsapp X⚡️.", reply_markup=reply_markup)
    # Tell ConversationHandler that we're in state `FIRST` now
    
    return FIRST
    
def what(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)

    keyboard = [
        [
            InlineKeyboardButton("FM MODS", callback_data=str(FM)),
            InlineKeyboardButton("SAM MODS", callback_data=str(SAM)),
        ],
        [  
            InlineKeyboardButton("🔙Back", callback_data=str(MOD)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    update.message.reply_text(f"{user.first_name} , select your mod here", reply_markup=reply_markup)
    # Tell ConversationHandler that we're in state `FIRST` now
    
    return FIRST


def start_over(update: Update, context: CallbackContext) -> int:
    """Prompt same text & keyboard as `start` does but not as new message"""
    # Get CallbackQuery from Update
    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Get Start", callback_data=str(MOD)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Instead of sending a new message, edit the message that
    # originated the CallbackQuery. This gives the feeling of an
    # interactive menu.
    update.message.reply_text(f"Hello {user.first_name} Welcome to Whatsapp X⚡️.", reply_markup=reply_markup)
    return FIRST

def MOD(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("🛠Get Whatsapp", callback_data=str(whatsapp)),
         
            InlineKeyboardButton("⚠️Feedback", callback_data=str(FM)),
        ],
         [
            InlineKeyboardButton("🚫cancel", callback_data=str(end)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Whatsapp x⚡️", reply_markup=reply_markup
    )
    return FIRST




def whatsapp(update: Update, context: CallbackContext) -> int:

    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("FM MODS", callback_data=str(FM)),
            InlineKeyboardButton("SAM MODS", callback_data=str(SAM)),
        ],
        [  
            InlineKeyboardButton("🔙Back", callback_data=str(MOD)),
        ],
        [
            InlineKeyboardButton("🚫cancel", callback_data=str(end)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Select what do you want mod", reply_markup=reply_markup
        
    )
    return FIRST

def FM(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Fouad Whatsapp", callback_data=str(FMFU)),
            InlineKeyboardButton("FM Whatsapp", callback_data=str(FMFM)),
        ],
        [
            InlineKeyboardButton("GB Whatsapp", callback_data=str(FMGB)),
            InlineKeyboardButton("YO Whatsapp", callback_data=str(FMYO)),
        ], 
        [        
            InlineKeyboardButton("🔙Back" , callback_data=str(whatsapp)),
            
        ],
        [
            InlineKeyboardButton("🚫cancel", callback_data=str(end)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="FM MODS | Select your whatsapp", reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return FIRST



def SAM(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Fouad Whatsapp", callback_data=str(SMFU)),
            InlineKeyboardButton("FM Whatsapp", callback_data=str(SMFM)),
        ],
        [
            InlineKeyboardButton("GB Whatsapp", callback_data=str(SMGB)),
            ],
            [
            InlineKeyboardButton("🔙Back" , callback_data=str(whatsapp)),
        ],
        [
            InlineKeyboardButton("🚫cancel", callback_data=str(end)),
        ],
       
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="SAM MODS | Select your whatsapp", reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return FIRST
    
def SMFU(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Fouad Whatsapp", callback_data=str(MOD)),
        ],
        [
            InlineKeyboardButton("🔙Back" , callback_data=str(SAM)),
        ],
       
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="SAM MODS | Download Fouad whatsapp", reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return FIRST
    
def SMGB(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("GB Whatsapp", callback_data=str(MOD)),
        ],
        [
            InlineKeyboardButton("🔙Back" , callback_data=str(SAM)),
        ],
       
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="SAM MODS | Download GB whatsapp", reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return FIRST

def SMFM(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("FM Whatsapp", callback_data=str(MOD)),
        ],
        [
            InlineKeyboardButton("🔙Back" , callback_data=str(SAM)),
        ],
       
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="SAM MODS | Download FM whatsapp", reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return FIRST










def FMFU(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Fouad Whatsapp", callback_data=str(MOD)),
       
        ],
        [
            InlineKeyboardButton("🔙Back" , callback_data=str(FM)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="FM MODS | Download Fouad whatsapp", reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return FIRST
    
def FMFM(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("FM Whatsapp", callback_data=str(MOD)),
           
        ],
        [
           InlineKeyboardButton("🔙Back" , callback_data=str(FM)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="FM MODS | Download FM whatsapp", reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return FIRST

def FMYO(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("YO Whatsapp", callback_data=str(MOD)),
         ],
       
        [
           InlineKeyboardButton("🔙Back" , callback_data=str(FM)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="FM MODS | Download YO whatsapp", reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return FIRST
    
def FMGB(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("GB Whatsapp", callback_data=str(MOD)),
       
        ],
        [
            InlineKeyboardButton("🔙Back" , callback_data=str(FM)),
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="FM MODS | Download GB whatsapp", reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return FIRST
    
    
    
    
    
    

def end(update: Update, context: CallbackContext) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Thank you for using this bot")
    return ConversationHandler.END


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("2034497572:AAFAkRFxFAqmZh0CWgcW_1FDNnFs82iI7KA")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Setup conversation handler with the states FIRST and SECOND
    # Use the pattern parameter to pass CallbackQueries with specific
    # data pattern to the corresponding handlers.
    # ^ means "start of line/string"
    # $ means "end of line/string"
    # So ^ABC$ will only allow 'ABC'
    conv_handler = ConversationHandler(
        entry_points=[
        CommandHandler('start', start),
        CommandHandler('whatsapp', what),
        ],
        
                      
                    
        states={
            FIRST: [
                CallbackQueryHandler(MOD, pattern='^' + str(MOD) + '$'),
                CallbackQueryHandler(FM, pattern='^' + str(FM) + '$'),
                CallbackQueryHandler(whatsapp, pattern='^' + str(whatsapp) + '$'),
                CallbackQueryHandler(SAM, pattern='^' + str(SAM) + '$'),
                CallbackQueryHandler(end, pattern='^' + str(end) + '$'),
                CallbackQueryHandler(FMFU, pattern='^' + str(FMFU) + '$'),
                CallbackQueryHandler(FMFM, pattern='^' + str(FMFM) + '$'),
                CallbackQueryHandler(FMGB, pattern='^' + str(FMGB) + '$'),
                CallbackQueryHandler(FMYO, pattern='^' + str(FMYO) + '$'),
                CallbackQueryHandler(SMFU, pattern='^' + str(SMFU) + '$'),
                CallbackQueryHandler(SMFM, pattern='^' + str(SMFM) + '$'),
                CallbackQueryHandler(SMGB, pattern='^' + str(SMGB) + '$'),
            ],
        },
        fallbacks=[
        CommandHandler('start', start),
        CommandHandler('whatsapp', what)
        ],

    )

    # Add ConversationHandler to dispatcher that will be used for handling updates
    dispatcher.add_handler(conv_handler)
    

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
