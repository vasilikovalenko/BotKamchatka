import telebot 
from telebot import types
import  random
import aiogram 
bot = telebot.TeleBot('7191666647:AAEtZq_1EvUzuxdE_hm2rRyadSe0Lbn-00U')
import photo


answers=['(→_→)', '┐(￣ヘ￣;)┌', '(•ิ_•ิ)?', '╮(︶▽︶)╭','ー ー','ヽ(　￣д￣)ノ']
anecdot=['— Твоя бабушка такая веселая!\n Все время только и улыбается!\n— Да это ей протез не того размера вставили!','В стоматологии.c\n— Боишься? \n— Не-а!\n— А че бахилы запотели?','В тюремной камере:\n— Ты из-за чего сюда попал?\n— Из-за простуды.\n— Как это?\n— Очень просто. Я чихнул, а сторож проснулся.,','Встречаются две Акулы:\n–Ну, как дела?\n\n–Голодно, объявили запрет на купание…\n–А, я слышала, у вас дайвингистов развилось видимо-невидимо…\n– Да, они жесткие и резиной отдают…\n– Вот, дура, их же чистить надо!','Итальянский мальчик спрашивает у отца:\n– Можешь сказать мне какие женщины самые верные? Брюнетки, рыжие или блондинки?\n– Седые, сыночек мой! Седые!']
@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('💖 Кардио тренировка❗')
    button2 = types.KeyboardButton('💪 Силовая тренировка❗ ')
    button3 = types.KeyboardButton('📙 Анекдоты')
    markup.row(button1,button2,button3)
    if message.text == '/start':
        bot.send_message(message.chat.id,f' 👋 Привет❗ {message.from_user.first_name}', reply_markup=markup)
    else:
        bot.send_message(message.chat.id,text='🟣Перекинул тебя в главном меню ⤴️❗ Выбирай ❗', reply_markup=markup)
@bot.message_handler()
def info(message):
    if message.text == '💖 Кардио тренировка❗':
        goods01(message)
    elif message.text =='💪 Силовая тренировка❗':
        goods02(message)   
    elif message.text == '📙 Анекдоты':
        bot.send_message(message.chat.id, anecdot[random.randint(0,1)])
    elif message.text == ('❗(ﾒ﹏ﾒ)❗ Назад ❗(ﾒ﹏ﾒ)❗'):
        welcome(message)
    elif message.text == '⚽Пенедельник⚽':
        bot.send_message(message.chat.id,'Бег 2.5км\nСкакалка 50\nприседания 50\nСкакалка 50\nПриседания 50\nСкакалка 50\nПрес на турнике 15\nСкакалка 50\nПрес на турнике 15\nСкакалка 50\nПриседания  50\nСкакалка 50\nПриседания 50')    
    elif message.text == '🥎Среда🥎':
        bot.send_message(message.chat.id,'Бег 2.5 км\nСкакалка 50\nОтжимания 20\nСкакалка 50\nОтжимания 20\nСкакалка 50\nБрусья 15\nСкакалка 50\nБрусья 15\nСкакалка 50\nПодтягивания 10\nСкакалка 50\nПодтягивания 10')
    elif message.text == '⚾Вторник⚾':
        bot.send_message(message.chat.id,'Бег 2.5 км\nСкакалка 50\nОтжимания 20\nСкакалка 50\nОтжимания 20\nСкакалка 50\nБрусья 15\nСкакалка 50\nБрусья 15\nСкакалка 50\nПодтягивания 10\nСкакалка 50\nПодтягивания 10')
    elif message.text == '🏀Четверг🏀':
        bot.send_message(message.chat.id,'Бег 2.5км \nскакалка 50\nПриседания 50\nскакалка 50\nПриседания 50\nскакалка 50\nБрусья 15\nскакалка 50\nБрусья 15\nскакалка 50\nОтжимания 20\nСкакалка 20')
    elif message.text =='🏐Пятница🏐':
        bot.send_message(message.chat.id,'Бег 2.5 км\nСкакалка 50\nПриседания 50\nскакалка 50\nПриседания 50\nскакалка 50\nПодтягивания 10\nскакалка 50\nПодтягивания 10\nскакалка 50\nОтжимания 20\nскакалка 50\nОтжимания 20')
    elif message.text =='🎾Суббота🎾':
        bot.send_message(message.chat.id,'Бег 2.5 км\nскакалка 50\nПриседания 50\nскакалка 50\nПриседания 50\nскакалка 50\nБрусья 15\nскакалка 50\nБрусья 15\nскакалка 50n\Отжимания 20\nскакалка 50\nОтжимания 20')
    elif message.text == '🏈Воскресенье🏈':
        bot.send_message(message.chat.id,'Бег 2.5 км  \nскакалка 50\nПодтягивания 10\nскакалка 50\nПодтягивания 10\nскакалка 50\nОтжимания 20\nскакалка 50\nОтжимания 20\nскакалка 50\nПриседания 50\nскакалка 50\nПриседания 50')
    elif message.text == '💢Пенедельник💢':
        bot.send_message(message.chat.id,'Жим штанги лежа классический 5-5x8-12\nЖим штанги лежа под углом 4-5x8-12\nРазводы с гантелями  лежа 3-4x10-12\nПодтягивание в машине смитта  3-4x10-15\nТяга горизонтального блока 3-4x10-15\nСкручивание на наклонной лавке 3-4x10-15') 
    elif message.text =='🏋️Вторник🏋️':
        bot.send_message(message.chat.id,'Приседание со штангой 4-5x8-12\nЖим ногами в тренажере 3-4x8-12\nВыводы со штангой 3-4x10-15\nСгибание ног в тренажере лежа    \nГиперэкстензия 3-4x10-15\nСтановая тяга со штангой 4-5x8-12') 
    elif message.text == '🏋️‍♂️Среда🏋️‍♂️':
        bot.send_message(message.chat.id,'Жим штанги с груди стоя 4-5x8-12\nЖим штанги  из за головы 3-4x10-12\nПротяжка со штангой 3-4x10-15\nМахи гантелями вперед 3-4x10-15\nПодьем ног в упоре 3-4x10-15\nПодьем ног на наклонной скамье 3-4x10-15 ')
    elif message.text == '🏅Четверг🏅':
        bot.send_message(message.chat.id,'Потягивания  широким хватом 4-5x8-12\nТяга штанги в наклонной 3-4x10-15\nТяга за голову  с верхнего блока 3-4x10=15 \nТяга с груди с верхнего блока широким хватом  3-4x 10-15\nТяга с верхнего блока узким хватом 3-4x10-15\nТяга одной гантелей в наклоне 3-4x10-15')
    elif message.text == '🏆Пятница🏆':
        bot.send_message(message.chat.id,'Отжимания от брусьев в гравитронне 4-5x8-12\nЖим штанги лежа узким хватом  4-5x8-12\nОтжимания от лавки сзади 4-5x8-12\nПодтягивания обратным хватом 4-5x10-15\nСгибание рук со штангой стоя 3-4x10-15 ')
    else:
         bot.send_message(message.chat.id, answers[random.randint(0, 3)])
def goods01(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button05 = types.KeyboardButton('⚽Пенедельник⚽')
    button10 = types.KeyboardButton('⚾Вторник⚾')
    button20 = types.KeyboardButton('🥎Среда🥎')
    button30 = types.KeyboardButton('🏀Четверг🏀')
    button40 = types.KeyboardButton('🏐Пятница🏐')
    button50 = types.KeyboardButton('🎾Суббота🎾')
    button60 = types.KeyboardButton('🏈Воскресенье🏈')
    button70 = types.KeyboardButton('❗(ﾒ﹏ﾒ)❗ Назад ❗(ﾒ﹏ﾒ)❗')
    markup.add(button05)
    markup.add(button10)
    markup.add(button20)
    markup.add(button30)
    markup.add(button40)
    markup.row(button50)
    markup.row(button60)
    markup.row(button70)
    bot.send_message(message.chat.id, '❗Выбирай❗', reply_markup=markup)
    
def goods03(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button051 = types.KeyboardButton('📙 Анекдоты')  
    button708 = types.KeyboardButton('❗(ﾒ﹏ﾒ)❗ Назад ❗(ﾒ﹏ﾒ)❗')
    markup.add(button051)
    markup.row(button708)
   
    bot.send_message(message.chat.id, '❗Выбирай❗', reply_markup=markup)

def goods02(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button057 = types.KeyboardButton('💢Пенедельник💢 ')
    button106 = types.KeyboardButton('🏋️Вторник🏋️')
    button205 = types.KeyboardButton('🏋️‍♂️Среда🏋️‍♂️')
    button304 = types.KeyboardButton('🏅Четверг🏅')
    button403 = types.KeyboardButton('🏆Пятница🏆')
    button700 = types.KeyboardButton('❗(ﾒ﹏ﾒ)❗ Назад ❗(ﾒ﹏ﾒ)❗')
    markup.add(button057)
    markup.add(button106)
    markup.add(button205)
    markup.add(button304)
    markup.add(button403)
    markup.row(button700)
    
    bot.send_message(message.chat.id, '❗Выбирай❗', reply_markup=markup)    
        

bot.polling(none_stop=True)