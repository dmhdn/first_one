from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update
import re
import pandas as pd
from openpyxl import load_workbook
import os

global df
Path_to_load_file = r'E:\WORKING\file_list.xlsx'
try:
    df = pd.read_excel(Path_to_load_file, engine='openpyxl')
except Exception as e:
    print("Error loading the file:", e)
    df = pd.DataFrame()

# Read token from the config.txt file
def read_token_from_config(file_path):
    try:
        with open(file_path, "r") as file:
            token = file.read().strip()
        return token
    except Exception as e:
        print("Error reading token from config file:", e)
        return None

# Create a global variable to store user input
user_input = ""

async def timca(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global user_input
    # Get the user input
    user_input = update.message.text
    san_pham = user_input[7:-6]
    so_lo = user_input[-6:]
    
    # Get the name of the user who sent the request
    user_name = update.message.from_user.first_name
    
    result = df[df['Full Path'].str.lower().str.contains(f'{san_pham}.*{so_lo}')]
    if result.empty:
        await update.message.reply_text("Ket qua khong tim thay")
    else:
        if len(result) <= 20:  # Limiting to 20 results
            await update.message.reply_text(f"Da tim thay {len(result)} ket qua. Day la danh sach file tuong ung:")
            for index, row in result.iterrows():
                file_path = row['Full Path']
                if os.path.isfile(file_path) and os.path.getsize(file_path) > 0:
                    await update.message.reply_text(f"File {index + 1}:")
                    await update.message.reply_document(document=open(file_path, 'rb'))
                else:
                    await update.message.reply_text(f"File {index + 1} khong ton tai.")
        else:
            await update.message.reply_text("Qua nhieu ket qua duoc tim thay. Hay cu the hon.")
    
    # If no results found, still send the response_text message
    await update.message.reply_text("hoan thanh xong yeu cau")
    print(f"Da thuc hien yeu cau cua {user_name}")

if __name__ == "__main__":
    # Specify the path to the config.txt file
    config_file_path = "config_tele.txt"

    # Read the bot token from the config file
    bot_token = read_token_from_config(config_file_path)

    if bot_token is None:
        print("Bot token not found. Please check your config.txt file.")
    else:
        try:
            # Create the ApplicationBuilder with the bot token
            app = ApplicationBuilder().token(bot_token).build()

            # Add the timca command handler
            app.add_handler(CommandHandler("timca", timca))

            # Start the bot
            app.run_polling()
        except Exception as e:
            print("An error occurred while running the bot:")
            print(e)
            import traceback
            traceback.print_exc()

