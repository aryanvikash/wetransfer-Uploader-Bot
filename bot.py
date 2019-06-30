
import json
from telegram.ext import CommandHandler,MessageHandler, Filters,Updater
from telegram import ParseMode
from telegram.ext.dispatcher import run_async
import os , sys 
import uploader
from pySmartDL import SmartDL






######################################################################################
bot_token ='804364893:AAH9CzzBh4mEtHGkxQeYzMUlyP5oWlGGJ_8'                           #

updater = Updater(token= bot_token, use_context=True)                                #

dp = updater.dispatcher                                                          #
                                                                                     #

######################################################################################







def help(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="please Use  /id   for Chat ID & Other Info")

@run_async
def start(update,context):
    context.bot.send_message(chat_id =update.message.chat_id,text ="Hey Send me a direct link")

@run_async
def download(update,context):

    url = update.message.text
    url =url.split()
    sent_message =context.bot.send_message(chat_id=update.message.chat_id,text ="Processing Url...")

    # dest = "C:\\Downloads\\" # or '~/Downloads/' on linux
    dest = "Downloads/"
    # dest = "Downloads\\"

    try:
        obj = SmartDL(url, dest)
        sent_message.edit_text(obj.start())   
        
        sent_message.edit_text("Downloading complete")   
        DownloadStatus = True

    except Exception as e :
        print(e)
        sent_message.edit_text("Downloading error :{}".format(e))   
        DownloadStatus = False

    filename = obj.get_dest()
    print(filename)
    # filename = download_file(url)
    try:
        if DownloadStatus:
            sent_message.edit_text("Uploading Your file")   
            wurl = uploader.upload([filename]) 
            sent_message.edit_text(wurl)
    except Exception as e :
        print(e)
        if DownloadStatus:
            sent_message.edit_text("Uploading fail :".format(e))
# @run_async
# def downloadhand(update, context):
#     print(update.message.chat_id)
#     print(update.message.text)
#         # To Get Google Drive Direct Link

#     if "youtube"  or "youtu" in update.message.text:

#         context.bot.send.message(chat_id =update.message.chat_id, text ="Wait Processing Your Url....")
#         oldfile = ytaudio.download(update.message.text)

#         filename = oldfile.split(".")
#         extn = filename[1].replace("mp4",".mp3")
#         filename = filename[0]+extn
#         os.rename(oldfile,filename)
#         context.bot.send_document(chat_id =update.message.chat_id,
#                     document=open(filename, 'rb'),
#                     caption ="here is your file")

#     if "drive.google.com"  in update.message.text:
        
#         direct_url = direct_link.gdrive_gen(update.message.text)
#         context.bot.send_message(chat_id = update.message.chat_id, text=direct_url)
        
#          # Here is Dropbox part 

#     elif "dropbox.com" in update.message.text:
#         direct_url = direct_link.db_gen(update.message.text)
#         context.bot.send_message(chat_id=update.message.chat_id,text = direct_url)
        
        
#     else:
#         # Here is Download from url and upload as a document
#         context.bot.send_document(chat_id =update.message.chat_id,
#             document=open(DLFILE, 'rb'),
#             caption ="here is your file")
#         print("send successfully")
#         # print("we entered else")
#         # context.bot.send_message(chat_id=update.message.chat_id,text="Sorry Not A valid Url",reply_to_message_id=update.reply_to_message.message_id)


start_handler = CommandHandler('start', start)
dp.add_handler(start_handler)

downloader_handler = MessageHandler(Filters.regex(r'http' ), download)
dp.add_handler(downloader_handler)

# help_handler = CommandHandler('help',help)
# dp.add_handler(help_handler)



updater.start_polling()
updater.idle()
