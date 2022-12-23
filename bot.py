import telebot
from docxtpl import DocxTemplate
from docx2pdf import convert

doc = DocxTemplate("INSURANCE ILLINOIS 2.docx")
bot = telebot.TeleBot('5822889761:AAHvm8fI2GNCGCYkflRkvKodKaMNdzGCxFI')


@bot.message_handler(content_types=['text'])
def after_text(message):
    if message.text == 'Сумрак':
        msg = bot.send_message(message.from_user.id, '1) Firstname Middlename Lastname\nнапример: OMAR IBN ALHATTAB')
        bot.register_next_step_handler(msg, after_text_2)

def after_text_2(message):
    name = message.text
    print('name', name)
    msg = bot.send_message(message.from_user.id, '2) Year Make Model \nнапример: 2002 TOYOTA PRIUS')
    bot.register_next_step_handler(msg, after_text_3, name)

def after_text_3(message, name):
    model = message.text
    name = name
    print('model:', message.text)
    msg = bot.send_message(message.from_user.id, ' 3) VIIN NUMBER \nнапример:JT2BK12UX20056855')
    bot.register_next_step_handler(msg, after_text_4, name, model)

def after_text_4(message, name, model):
    viin = message.text
    name = name
    model = model
    context = { 'name' : name, 'car' : model, 'viin': viin}
    doc.render(context)
    doc.save("final.docx")
    print('viin:', message.text)
    bot.send_message(message.from_user.id, 'Ожидайте PDF файл...')

    # docx_file = "final.docx"
    # convert(docx_file)

    uis_pdf = open("final.docx", 'rb')
    bot.send_document(message.chat.id, uis_pdf)
    uis_pdf.close()
    


bot.polling()