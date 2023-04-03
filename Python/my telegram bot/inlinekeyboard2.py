import logging
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
ONE, MOD, FM, THREE, SAM, FIVE, MM = range(7)


def start(update: Update, context: CallbackContext) -> int:
    """Send message on `/start`."""
    # Get user that sent /start and log his name
    user = update.message.from_user
    logger.info("User %s started the conversation.", user.first_name)
    # Build InlineKeyboard where each button has a displayed text
    # and a string as callback_data
    # The keyboard is a list of button rows, where each row is in turn
    # a list (hence `[[...]]`).
    keyboard = [
        [
            InlineKeyboardButton("Get Start", callback_data=str(MOD)),
            ],
          
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Send message with text and appended InlineKeyboard
    update.message.reply_text("Hey Welcome to Whatsapp X⚡️ Bot", reply_markup=reply_markup)
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
            InlineKeyboardButton("Start", callback_data=str(MOD)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    # Instead of sending a new message, edit the message that
    # originated the CallbackQuery. This gives the feeling of an
    # interactive menu.
    query.edit_message_text(text="Welcome to Whatsapp X⚡️ Bot", reply_markup=reply_markup)
    return FIRST

def MOD(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Get Whatsapp", callback_data=str(MM)),
        ],
        [  
            InlineKeyboardButton("Feedback", callback_data=str(FM)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Select what do you want mod", reply_markup=reply_markup
    )
    return FIRST



def MM(update: Update, context: CallbackContext) -> int:
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
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Select what do you want mod", reply_markup=reply_markup
    )
    return FIRST


def three(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("1", callback_data=str(ONE)),
            InlineKeyboardButton("3", callback_data=str(THREE)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Second CallbackQueryHandler, Choose a route", reply_markup=reply_markup
    )
    return FIRST


def FM(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Fouad Whatsapp", callback_data=str(MOD)),
            InlineKeyboardButton("FM Whatsapp", callback_data=str(MOD)),
        ],
        [
            InlineKeyboardButton("GB Whatsapp", callback_data=str(MOD)),
            InlineKeyboardButton("YO Whatsapp", callback_data=str(MOD)),
        ], 
        [        
            InlineKeyboardButton("🔙Back" , callback_data=str(MOD)),
            
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="FM MODS | Select your whatsapp", reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return SECOND



def SAM(update: Update, context: CallbackContext) -> int:
    """Show new choice of buttons"""
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Fouad Whatsapp", callback_data=str(MOD)),
            InlineKeyboardButton("FM Whatsapp", callback_data=str(MOD)),
        ],
        [
            InlineKeyboardButton("GB Whatsapp", callback_data=str(MOD)),
            ],
            [
            InlineKeyboardButton("🔙Back" , callback_data=str(MOD)),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="SAM MODS | Select your whatsapp", reply_markup=reply_markup
    )
    # Transfer to conversation state `SECOND`
    return SECOND


def end(update: Update, context: CallbackContext) -> int:
    """Returns `ConversationHandler.END`, which tells the
    ConversationHandler that the conversation is over.
    """
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="See you next time!")
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
        entry_points=[CommandHandler('start', start)],
        states={
            FIRST: [
                CallbackQueryHandler(MOD, pattern='^' + str(MOD) + '$'),
                CallbackQueryHandler(FM, pattern='^' + str(FM) + '$'),
                CallbackQueryHandler(MM, pattern='^' + str(MM) + '$'),
                CallbackQueryHandler(MM, pattern='^' + str(MM) + '$'),
                CallbackQueryHandler(SAM, pattern='^' + str(SAM) + '$'),
            ],
            SECOND: [
                CallbackQueryHandler(start_over, pattern='^' + str(MOD) + '$'),
                CallbackQueryHandler(end, pattern='^' + str(FM) + '$'),
            ],
        },
        fallbacks=[CommandHandler('start', start)],
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
