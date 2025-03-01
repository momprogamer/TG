import os
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Configura el logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Comando de inicio
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('¡Hola! Soy tu bot. Usa /info para obtener tu información.')

# Comando de ayuda
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Comandos disponibles:\n/info - Muestra tu información de usuario.\n/system - Muestra el sistema en el que estoy desplegado.')

# Comando de info
def info(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    update.message.reply_text(f'Tu ID es: {user.id}\nTu nombre es: {user.first_name} {user.last_name}\nTu nombre de usuario es: {user.username}')

# Comando de sistema
def system(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Estoy desplegado en: {os.uname().sysname} {os.uname().release}')

def main() -> None:
    # Obtén el token de Telegram desde las variables de entorno
    token = os.getenv('TELEGRAM_BOT_TOKEN')
    if not token:
        logger.error("No se encontró el token de Telegram.")
        return

    # Crea el Updater y pasa el token de tu bot
    updater = Updater(token)

    # Obtén el dispatcher para registrar los handlers
    dispatcher = updater.dispatcher

    # Registra los comandos
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("info", info))
    dispatcher.add_handler(CommandHandler("system", system))

    # Inicia el bot
    updater.start_polling()

    # Ejecuta el bot hasta que se presione Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
