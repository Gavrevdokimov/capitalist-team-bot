# -*- coding: utf8 -*-

import telebot
from telebot import types
import copy
import math
import json
from threading import Timer
import os

token = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(token)

companies = {1: {'Standard Oil': 0, 'White Star Line': 0, 'Charron': 0, 'Путиловские заводы': 0, 'Grönvik glasbruk': 0},
             2: {'Тульский оружейный завод': 0, 'US steel': 0, 'Victor Talking Machine Company': 0, 'Darmstädter-National bank': 0, 'Benz and Cie': 0, 'Пивоваренная компания Alexander Keith’s': 0},
             3: {'RKO pictures': 0, 'Procter and Gamble': 0, 'Parker Brothers': 0, 'Waggonfabriek L. Steinfurt': 0, 'Bally Пинбольные столы': 0},
             4: {'BMW': 0, 'Sumitomo': 0, 'IBM': 0, 'Cuban Telephone Company': 0, 'Grundig': 0},
             5: {'Panther': 0, 'Chrysler': 0, 'Consett Iron Company': 0, 'Peabody Energy': 0, 'Esso': 0},
             6: {'Federal Express': 0, 'Singer': 0, 'Ultimate': 0, 'Starbucks': 0, 'Firma Gebrüder Grill': 0},
             7: {'Lego': 0, 'Kodak': 0, 'Apple': 0, 'Polaroid': 0, 'Global Crossing': 0, 'Nintendo': 0}}

multipliers = {1: {'Standard Oil': 4, 'White Star Line': 0, 'Charron': 5, 'Путиловские заводы': 2, 'Grönvik glasbruk': 0},
             2: {'Тульский оружейный завод': 0, 'US steel': 1/3, 'Victor Talking Machine Company': 5, 'Darmstädter-National bank': 0, 'Benz and Cie': 1, 'Пивоваренная компания Alexander Keith’s': 4},
             3: {'RKO pictures': 5, 'Procter and Gamble': 8, 'Parker Brothers': 3, 'Waggonfabriek L. Steinfurt': 0, 'Bally Пинбольные столы': 0},
             4: {'BMW': 4, 'Sumitomo': 10, 'IBM': 8, 'Cuban Telephone Company': 0, 'Grundig': 5},
             5: {'Panther': 3, 'Chrysler': 0.1, 'Consett Iron Company': 0.1, 'Peabody Energy': 2, 'Esso': 3},
             6: {'Federal Express': 15, 'Singer': 0.2, 'Ultimate': 10, 'Starbucks': 2, 'Firma Gebrüder Grill': 0},
             7: {'Lego': 0.1, 'Kodak': 0, 'Apple': 2, 'Polaroid': 0, 'Global Crossing': 0, 'Nintendo': 1}}

finish = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}

years = {1: "1900 — 1915", 2: "1915 — 1932", 3: "1932 — 1945", 4: "1945 — 1960", 5: "1960 — 1975", 6: "1975 — 1990", 7: "1990 — 2005"}

debt = {1: 6, 2: 11, 3: 36, 4: 195, 5: 321, 6: 1746, 7: 0}

# открываем сохраненную игру
with open('save_players.json') as f:
    try:
        players = json.load(f)
        players_2 = copy.deepcopy(players)
        players = {}
        for player in players_2:
            player_2 = int(player)
            players[player_2] = copy.deepcopy(players_2[player])
            companies_2 = copy.deepcopy(players[player_2]["companies"])
            players[player_2]["companies"] = {}
            for round_n in companies_2:
                round_2 = int(round_n)
                players[player_2]["companies"][round_2] = copy.deepcopy(companies_2[round_n])
            finish_2 = copy.deepcopy(players[player_2]["finish"])
            players[player_2]["finish"] = {}
            for round_num in finish_2:
                round_3 = int(round_num)
                players[player_2]["finish"][round_3] = copy.deepcopy(finish_2[round_num])
    except:
        players = {}

print(players)


sticker = 'CAACAgIAAxkBAAIPnV67u5l7uBx-N1IYtu70VgclQuO4AAIVAwACnNbnCgbnCWarj1O-GQQ'
sticker_2 = 'CAACAgIAAxkBAAIP3167xcJI92k-JiH6O1tBSEvKzSUEAAISAwACnNbnChxSQ7QkdV0oGQQ'
sticker_3 = 'CAACAgIAAxkBAAIiGV6_wT-LBUzOSIcwmBNHdCFuUNp2AAIXAwACnNbnCtb0SKu1OIHZGQQ'

putin = 'https://i.ytimg.com/vi/hhuusyppgx4/hqdefault.jpg'

yesfraselist = [
    "Это были непростые годы. Давно скопились обиды государств друг на друга, и к ним постоянно прибавлялись новые. Назревавший конфликт обернулся кровопролитной войной, которая прямо сейчас в самом разгаре. Но деньги и эмоции — несовместимые вещи, мы надеемся, что даже из этого периода, вы смогли извлечь выгоду.",
    "Это были непростые годы. Только закончилась крупнейшая в истории человечества война, и по миру прокатилась волна революций, как разгорелся экономический кризис. Но настоящая акула фондового рынка только рада потрясениям, потому что на них можно заработать. ",
    "Это были непростые годы. Вы думали, что хуже Первой Мировой некуда? Оказалось, что есть. Война - это ад... если ты не догадался не ввязываться в нее. Гораздо приятнее смотреть на драку со стороны, а еще приятнее продавать драчунам бейсбольные биты.",
    "Это были непростые годы. Только-только закончилась война. Целый материк оказался в руинах. Но жизнь продолжается. Наконец агрессивный трейдинг может уступить место вдумчивому долгосрочному инвестированию.",
    "Это были непростые годы. Казалось бы, живите себе спокойно, все же поняли, каким ужасом может обернуться война. Но битвы бывают не только на полях сражений с автоматами в руках, но и экономические, за богатство этого мира. И если ты скопил богатства и получил власть, готовься их защищать.",
    "Это были непростые годы. Но человечество держалось молодцом. Конфликты носили больше локальный характер. Мир стал чуть более предсказуемым, а это лучшее состояние для бизнеса и инвесторов, когда вы уверены в завтрашнем дне и можете спокойно вкладывать деньги.",
    "Это были непростые годы. Скорость жизни постоянно увеличивается, за какие-то 15 лет мир изменился до неузнаваемости. Целые состояния появляются из ниоткуда за считанные годы и также быстро растворяются. Да что там состояния, если теперь можно утром проснуться в другой стране. Но мастер фондового рынка только рад такой волатильности."]


stop_game_flag = 0

#пишем правильную форму слова "доллар"
def dollar_word(dollar_sum):
    if isinstance(dollar_sum, float):
        return "доллара"
    elif 11 <= int(str(dollar_sum).split()[0][-2:]) <= 14:
        return "долларов"
    elif 1 < int(str(dollar_sum).split()[0][-1]) <= 4:
        return "доллара"
    elif int(str(dollar_sum).split()[0][-1]) == 1:
        return "доллар"
    else:
        return "долларов"

#ответ на простые сообщения
def small_talk(message):
    if ("привет" in message.text.lower()) or ("hi" in message.text.lower()) or ("hello" in message.text.lower()) or ("здравствуй" in message.text.lower()) or ("хай" in message.text.lower()):
        bot.send_message(message.from_user.id, "Здравствуйте! Как поживаете?")
    elif ("хорошо" in message.text.lower()) or ("отлично" in message.text.lower()) or ("лучше всех" in message.text.lower()) or ("прекрасно" in message.text.lower()):
        if ("ты" in message.text.lower() and "милый" not in message.text.lower()) or ("тебя" in message.text.lower()) or ("твои" in message.text.lower()) or ("ваши" in message.text.lower()) or ("вас" in message.text.lower()) or ("вы" in message.text.lower()):
            bot.send_message(message.from_user.id, "И у меня все хорошо) Желаю удачи в игре!\nP.S. Я болею именно за вас 😉, только никому не говорите)")
        else:
            bot.send_message(message.from_user.id, "Я очень рад за вас! Желаю удачи в игре!\nP.S. Я болею именно за вас 😉, только никому не говорите)")
    elif ("не очень" in message.text.lower()) or ("плохо" in message.text.lower()) or ("так себе" in message.text.lower()) or ("грустно" in message.text.lower()) or ("скучно" in message.text.lower()) or ("сойдет" in message.text.lower()) or ("бомж" in message.text.lower()) or ("проиграл" in message.text.lower()) or ("проебал" in message.text.lower()) or ("просрал" in message.text.lower()):
        if ("ты" in message.text.lower()) or ("тебя" in message.text.lower()) or ("твои" in message.text.lower()) or ("ваши" in message.text.lower()) or ("вас" in message.text.lower()) or ("вы" in message.text.lower()):
            bot.send_message(message.from_user.id, "У меня хорошо, и у вас все обязательно наладится! Желаю удачи в игре!\nP.S. Я болею именно за вас 😉, только никому не говорите)")
        else:
            bot.send_message(message.from_user.id, "Я уверен, все обязательно наладится, когда вы победите в этой игре) Желаю удачи!\nP.S. Я болею именно за вас 😉, только никому не говорите)")
    elif ("спасибо" in message.text.lower()) or ("приятно" in message.text.lower()) or ("мило" in message.text.lower()) or ("милый" in message.text.lower()) or ("классный" in message.text.lower()):
        bot.send_sticker(chat_id=message.from_user.id, data=sticker_2)
    elif ("тебя" in message.text.lower()) or ("твои" in message.text.lower()) or ("ваши" in message.text.lower()) or ("вас" in message.text.lower()) or ("вы" in message.text.lower()) or ("как сам" in message.text.lower()) or ("че как" in message.text.lower()) or ("как поживае" in message.text.lower()) or ("дела" in message.text.lower()):
        bot.send_message(message.from_user.id, "У меня все хорошо, только Роспотребнадзор постоянно блокирует 😔")
    else:
        bot.send_message(message.from_user.id, "Извините, я не понимаю такие сообщения")
        bot.send_message(325051402, f"**{message.text}**")


#красивая выдача описания раунда в начале
def beautiful(id):
    return f"Раунд {players[id]['round_number']}/7: {years[players[id]['round_number']]} годы."


#составляем список компаний на раунд по номеру раунда
def round_list(id):
    roundlist = []
    for company in players[id]["companies"][players[id]["round_number"]]:
        roundlist.append(company)
    return roundlist


#считаем деньги на конец раунда
def money_result(id):
    investment_list = []
    for i in players[id]["companies"][players[id]["round_number"]].values():
        investment_list.append(i)
    multipliers_list = []
    for i in multipliers[players[id]["round_number"]].values():
        multipliers_list.append(i)
    almost_result = [x * y for x, y in zip(investment_list, multipliers_list)]
    round_result = sum([int(x) for x in almost_result])
    return round_result


#компания с максимальной доходностью
def max_profitable_company(id):
    investment_list = []
    result_list = []
    max_profit_companies = []
    for round in players[id]["companies"]:
        for company in players[id]["companies"][round]:
            if players[id]["companies"][round][company] > 0:
                investment_list.append(company)
    for round in multipliers:
        for company in multipliers[round]:
            if (company in investment_list):
                result_list.append(multipliers[round][company])
    max_result = max(result_list)
    for round in multipliers:
        for company in multipliers[round]:
            if multipliers[round][company] == max_result:
                max_profit_companies.append(company)
    if len(max_profit_companies) == 1:
        return f"Ваше самое успешное вложение - {max_profit_companies[0]}, доходность составила {(max_result - 1) * 100}%"
    elif len(max_profit_companies) > 1:
        return f"Ваши самые успешные вложения - {', '.join(max_profit_companies)}, доходность составила {(max_result - 1) * 100}%"


#компания с наибольшим выигрышем в деньгах
def max_profit_from_company(id):
    players[id]["companies_result"] = copy.deepcopy(multipliers)
    all_results_list = []
    max_profit_companies = []
    max_lose_companies = []
    for round in multipliers:
        for company in multipliers[round]:
            players[id]["companies_result"][round][company] = players[id]["companies"][round][company] * (multipliers[round][company] -1)
    for round in players[id]["companies_result"]:
        for company in players[id]["companies_result"][round]:
            all_results_list.append(players[id]["companies_result"][round][company])
    max_result = max(all_results_list)
    for round in players[id]["companies_result"]:
        for company in players[id]["companies_result"][round]:
            if players[id]["companies_result"][round][company] == max_result:
                max_profit_companies.append(company)
    if len(max_profit_companies) == 1:
        max_profit =  f"Больше всего вы заработали на компании {max_profit_companies[0]}, прибыль от инвестиции составила {max_result} {dollar_word(max_result)}"
    else:  #len(max_profit_companies) > 1
        max_profit = f"Больше всего вы заработали на компаниях - {', '.join(max_profit_companies)}, прибыль от каждой инвестиции равнялась {max_result} {dollar_word(max_result)}"
    min_result = min(all_results_list)
    for round in players[id]["companies_result"]:
        for company in players[id]["companies_result"][round]:
            if players[id]["companies_result"][round][company] == min_result:
                max_lose_companies.append(company)
    if len(max_lose_companies) == 1:
        max_lose = f"Больше всего вы потеряли на компании {max_lose_companies[0]}, убыток от инвестиции составил {math.ceil(-min_result)} {dollar_word(math.ceil(-min_result))}"
    else: #len(max_lose_companies) > 1
        max_lose = f"Больше всего вы потеряли на компаниях - {', '.join(max_lose_companies)}, убыток от каждой инвестиции равнялся {math.ceil(-min_result)} {dollar_word(math.ceil(-min_result))}"
    if min_result >= 0:
        return max_profit
    else:
        a = '\n'.join([max_profit, max_lose])
        return a


#клава со списком компаний
def keyboard(x, id):
    keyboard = types.InlineKeyboardMarkup()
    for company in x(id):   #x = round_list
        keyboard.add(types.InlineKeyboardButton(text=company,callback_data=company))
    return keyboard


#клава готовы начать раунд?
def keyboard_begin_round():
    keyboard = types.InlineKeyboardMarkup()
    yes = types.InlineKeyboardButton(text="Начнем", callback_data='begin')
    keyboard.add(yes)
    return keyboard


#клава уверены, что хотите выйти?
def keyboard_leave():
    keyboard = types.InlineKeyboardMarkup()
    yes = types.InlineKeyboardButton(text="Да", callback_data='sure')
    no = types.InlineKeyboardButton(text="Нет", callback_data="notsure")
    keyboard.add(yes, no)
    return keyboard


#клава Гавр, покажи результат
def keyboard_result():
    keyboard = types.InlineKeyboardMarkup()
    yes = types.InlineKeyboardButton(text="Смотрим", callback_data='yes')
    keyboard.add(yes)
    return keyboard


#табличка, кто куда инвестировал
def investment_table():
    invest = {}
    local_round_list = []
    result = []
    for player in players:
        round_number = players[player]["round_number"]
        break
    for company in players[player]["companies"][round_number]:
        invest[company] = []
        local_round_list.append(company)
    for company in local_round_list:
        for player in players:
            if players[player]["companies"][round_number][company] > 0:
               invest[company].append(players[player]["name"])
    for company in invest:
        invest[company] = ", ".join(invest[company])
        result.append(": ".join([company, invest[company]]))
        final = "\n".join(result)
    return final


#табличка с уже сделанными инвестициями для участника
def already_invested(id):
    invest_list = sorted([players[id]["companies"][players[id]["round_number"]][company] for company in players[id]["companies"][players[id]["round_number"]] if players[id]["companies"][players[id]["round_number"]][company] > 0], reverse=True)
    company_list = []
    for result in invest_list:
        for company in players[id]["companies"][players[id]["round_number"]]:
            if players[id]["companies"][players[id]["round_number"]][company] == result:
                company_list.append(company)
    company_list_2 = company_list[::-1]
    for i in range(0, len(company_list_2)):
        if company_list_2[i] in company_list_2[i + 1:]:
            company_list.remove(company_list_2[i])
    table_list = []
    for i in range (0, len(company_list)):
        a = "".join(str(company_list[i]) +" — "+ str(invest_list[i]) + " " + str(dollar_word(invest_list[i])))
        table_list.append(a)
    table_str = "\n".join(table_list)
    return table_str


#табличка с результатами раунда
def round_table():
    for player in players:   #проверяем, всё ли игрок инвестировал, если нет, бабло сгорает
        round_investment = sum([i for i in players[player]["companies"][players[player]["round_number"]].values()])
        if players[player]["money"] != round_investment:
            players[player]["round_result"] = money_result(player)
    result_money_list = sorted(list(set([players[i]["round_result"] - players[i]["debt"] for i in players])), reverse=True)
    names_list = []
    money_list = []
    debt_list = []
    for result in result_money_list:
        for player in players:
            if players[player]["round_result"] - players[player]["debt"] == result:
                names_list.append(str(players[player]["name"]))
                money_list.append(players[player]["round_result"])
                debt_list.append(players[player]["debt"])
    table_list = []
    winners_list = []
    if players[[player for player in players][0]]["round_number"] == 7:
        for i in range(0, len(names_list)):
            row = "".join(str(names_list[i]) + " — " + str(money_list[i]-debt_list[i]) + " " + str(dollar_word(money_list[i]-debt_list[i])))
            table_list.append(row)
            if (money_list[i]-debt_list[i]) == max(result_money_list):
                row = "".join(str(names_list[i]))
                winners_list.append(row)
        if len(winners_list) > 1:
            winners = ", ".join(winners_list)
            congratulation = "".join(["Поздравляем победителей: ", winners, " !"])
        else:
            winner = winners_list[0]
            congratulation = "".join(['Поздравляем победителя - Команду "', winner, '"!'])
        table_str = "\n".join(table_list)
        return table_str, congratulation
    else:
        for i in range (0, len(names_list)):
            if debt_list[i] > 0:
                a = "".join(str(names_list[i]) + " — " + str(money_list[i]) + " " + str(dollar_word(money_list[i])) + ", " + "долг — " + str(debt_list[i]) + " " + str(dollar_word(debt_list[i])))
                table_list.append(a)
            else:
                a = "".join(str(names_list[i]) + " — " + str(money_list[i]) + " " + str(dollar_word(money_list[i])))
                table_list.append(a)
        table_str = "\n".join(table_list)
    return table_str


#итоговый прирост денег
def delta(money):
    delta_abs = round((money - 3) / 105, 2)
    if money >= 0:
        delta_otn = round(((money / 3) ** (1 / 105) - 1) * 100 , 2)
        return f"Каждый год он в среднем рос на {delta_otn}% и прибавлял {delta_abs} {dollar_word(delta_abs)}! Это впечатляющий результат, и вы по праву можете им гордиться!"
    else:
        return f"Каждый год в среднем вы теряли {-delta_abs} {dollar_word(-delta_abs)}! Это полезный опыт, который позволит вам сберечь деньги в реальной жизни!"


#сообщение о появлении долга у игрока
def lose_money(player):
    creditor_list = ['ваш богатый дядюшка одолжил вам', 'ваша любимая бабуленька одолжила вам', 'сын маминой подруги одолжил вам', 'Банк "Деньги под залог почки" дал вам в кредит', 'ваш богатый дядюшка', 'местный бандит одолжил вам']
    return f"К сожалению, в прошлом раунде вы все потеряли. Но {creditor_list[players[player]['round_number']-1]} {debt[players[player]['round_number']]} {dollar_word(debt[players[player]['round_number']])}, " \
    f"чтобы вы могли продолжить попытки разбогатеть. До конца игры долг будет увеличиваться на 100% каждый раунд и будет вычтен из вашего результата в 7 раунде."


#подсчитываем риск профиль участника
def risk_profile(id):
    company_list = []
    for round in players[id]["companies"]:
        for company in players[id]["companies"][round]:
            if players[id]["companies"][round][company] > 0:
                company_list.append(company)
    risk = len(company_list)
    if 29 <= risk <= 35:
        return "Ваш риск-профиль: Неразборчивый перестраховщик, уровень риска 1 из 5. Вы вкладываетесь во все подряд, не вникая в особенности каждой компании. Диверсификация - это, разумеется, очень хорошо, но, даже диверсифицируясь, стоит с умом выбирать компании для инвестиций."
    elif 21 <= risk <= 28:
        return "Ваш риск-профиль: Диверсификатор, уровень риска 2 из 5. Вы молодец, у вас очень грамотный и взвешенный подход. Вы не кидались на все, что вам предлогалось, но и не складывали все яйца в одну корзину. Вас можно обойти по доходности на дистанции нескольких лет, но в долгосрочной перспективе вы кому угодно дадите фору."
    elif 17 <= risk <= 20:
        return "Ваш риск-профиль: Умеренно рискованный, уровень риска 3 из 5. Данный уровень риска подходит людям, которые давно на рынке и уделяют достаточное время анализу компаний. Если вы из таких, то так держать! Если нет, то советуем в реальной жизни составлять чуть более диверсифицированный портфель."
    elif 12 <= risk <= 16:
        return "Ваш риск-профиль: Очень рискованный, уровень риска 4 из 5. Либо вы профессиональный трейдер, которой по 16 часов в день тратит на анализ компаний и оценку ситуации на рынке, либо вы просто слишком самонадеянны и считаете себя умнее других. Если вы из вторых, то скоро рынок преподаст вам урок, но он будет дорогой."
    else:
        return 'Ваш риск-профиль: "Стальные яйца", уровень риска 5 из 5. Вы явно либо Ванга, либо инсайдер. Если я угадал, то давайте дружить) Если ни то, ни другое, то рынок вас очень скоро прожует и выплюнет. Нельзя все яйца класть в одну корзину.'


#сохраняем players в файл
def saving():
    with open("save_players.json", "w") as write_file:
        json.dump(players, write_file)
    return


#клава со списком участников для удаления
def delete_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    for player in players:
        keyboard.add(types.InlineKeyboardButton(text=players[player]["name"],callback_data=player))
    return keyboard


#клава для запрета инвестирования
def keyboard_stop_game():
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Остановить инвестиции",callback_data="stop_game"))
    return keyboard


#составляем список тех, кто еще не закончил вкладывать
def turtle():
    turtle_list = []
    for player in players:
        round_number = players[player]["round_number"]
        break
    for player in players:
        if players[player]["finish"][round_number] == 0:
            turtle_list.append(players[player]["name"])
    return ", ".join(turtle_list)


#клава для начала игры
def keyboard_start_game():
    keyboard = types.InlineKeyboardMarkup()
    go = types.InlineKeyboardButton(text="Начать игру", callback_data='start_game')
    keyboard.add(go)
    return keyboard


#клава запустить таймер?
def keyboard_time_go():
    keyboard = types.InlineKeyboardMarkup()
    go = types.InlineKeyboardButton(text="Запустить обратный отсчет?", callback_data='time_go')
    keyboard.add(go)
    return keyboard


#отправляем сообщение о времени
def time_alert():
    for player in players:
        round_num = players[player]["round_number"]
        break
    for gamer in players:
        if players[gamer]["finish"][round_num] == 0  and stop_game_flag == 0:
            bot.send_message(gamer, "Осталась 1 минута")
    if stop_game_flag == 0:
        bot.send_message(325051402, "Осталась 1 минута")


def time_to_stop():
    if stop_game_flag == 0:
        bot.send_message(325051402, "Гавр, пора закрывать инвестиции", reply_markup= keyboard_stop_game())


@bot.message_handler(commands=["start", "help", "delete", "cleaning", "turtle", "mistake"])  # реакция на команду, которая вводится после /
def command_hadler(message):
    global players
    global stop_game_flag
    if message.text == "/start":
        if message.from_user.id not in players:
            players[message.from_user.id] = {}
            players[message.from_user.id]["money"] = 3
            players[message.from_user.id]["choose"] = 0
            players[message.from_user.id]["debt"] = 0
            players[message.from_user.id]["finish"] = copy.deepcopy(finish)
            players[message.from_user.id]["name"] = 0
            players[message.from_user.id]["companies"] = copy.deepcopy(companies)
            if len(players) == 1:
                players[message.from_user.id]["round_number"] = 1
                bot.send_message(message.from_user.id, 'Добро пожаловать в игру "Капиталист"! Придумайте название вашей команды и напишите его мне.')
                bot.send_message(325051402, "Гавр, начнем игру?", reply_markup=keyboard_start_game())
            else:
                players[message.from_user.id]["round_number"] = [players[player]["round_number"] for player in players if player != message.from_user.id][0]
                if players[message.from_user.id]["round_number"] == 1:
                    bot.send_message(message.from_user.id, 'Добро пожаловать в игру "Капиталист"! Придумайте название вашей команды и напишите его мне.')
                else:
                    bot.send_message(message.from_user.id, "К сожалению, вы пропустили первые раунды, но оставшиеся можете сыграть вместе со всеми. Включайтесь в игру!")
                    try:
                        a = max([int(players[player]["name"][9:]) for player in players if players[player]["name"][:9] == "Опоздyны-"]) + 1
                    except:
                        a = 1
                    players[message.from_user.id]["name"] = ("Опоздуны-" + str(a))
                    bot.send_message(325051402, f'Подключился новый игрок - {players[message.from_user.id]["name"]}')
            saving()
        else:
            bot.send_message(message.from_user.id, "Вы уже в игре")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "/delete - удалить игрока\n\n/cleaning - удалить всех игроков\n\n/turtle - список не закончивших\n\n/mistake - разрешить инвестиции")
    elif message.text == "/delete":
        bot.send_message(message.from_user.id, "Кого удалим?", reply_markup=delete_keyboard())
    elif message.text == "/cleaning":
        players = {}
        bot.send_message(325051402, "Все чисто")
        saving()
    elif message.text == "/turtle":
        bot.send_message(325051402, f"Не закончили раунд: {turtle()}")
    elif message.text == "/mistake":
        stop_game_flag = 0
        bot.send_message(325051402, "Можно инвестировать.")


@bot.callback_query_handler(func=lambda message: True)
def answer(message):
    global players
    global stop_game_flag
    if message.data == 'yes':
        for i in players:
            players[i]["debt"] *= 2
        round_table_str = round_table()
        for player in players:
            if players[player]['round_number'] == 7:
                players[player]["money"] = (money_result(player) - players[player]["debt"])
                money = players[player]["money"]
                bot.send_message(player, f"Незаметно пролетел целый век! Ваш капитал после 105 лет инвестирования составляет {money} {dollar_word(money)}! {delta(money)}\n\n{max_profitable_company(player)}.\n\n{max_profit_from_company(player)}.\n\n{risk_profile(player)}")
                bot.send_message(player, f"{round_table_str[0]}")
                bot.send_message(player, f"{round_table_str[1]}")
            else:
                if money_result(player) == 0:
                    bot.send_message(player, lose_money(player))
                bot.send_message(player, f"Результаты {players[player]['round_number']} раунда:\n{round_table_str}")
        bot.send_message(325051402, f"{round_table_str[0] if players[player]['round_number'] == 7 else round_table_str}")
        if players[player]['round_number'] < 7:
            bot.send_message(325051402, f"Гавр, начнем следующий раунд?", reply_markup=keyboard_begin_round())
        saving()
    elif message.data == 'begin':
        stop_game_flag = 0
        for player in players:
            if money_result(player) == 0:
                players[player]["money"] = debt[players[player]['round_number']]
                players[player]["debt"] += debt[players[player]['round_number']]
            else:
                players[player]["money"] = money_result(player)
            players[player]["round_number"] += 1
            bot.send_message(player, f"{beautiful(player)}\nВ какую компанию вы хотите инвестировать?", reply_markup=keyboard(round_list, player))
        saving()
        bot.send_message(325051402, f"Гавр, запустим таймер?", reply_markup=keyboard_time_go())
        bot.send_message(325051402, f"Гавр, остановим инвестиции?", reply_markup=keyboard_stop_game())
    elif message.data.isdigit() == True:
        if int(message.data) in [player for player in players]:
            leaver = int(message.data)
            bot.send_message(325051402, f"{players[leaver]['name']} удален из игры")
            players.pop(leaver)
            saving()
        else:
            bot.send_message(325051402, "Этот игрок уже был удален ранее")
    elif message.data == "sure":
        if message.from_user.id in [player for player in players]:
            bot.send_message(message.from_user.id,"Жаль, что вы остановились, не дойдя до цели. Так миллиард не заработать.")
            bot.send_message(325051402, f"{players[message.from_user.id]['name']} вышел из игры")
            players.pop(message.from_user.id)
            saving()
        else:
            bot.send_message(message.from_user.id, "Выйти из игры чтобы, надобно войти в нее прежде!")
    elif message.data == "notsure":
        bot.send_message(message.from_user.id, "Чтобы преуспеть на фондовом рынке, нужно быть более решительным")
    elif message.data == "start_game":
        for player in players:
            bot.send_message(player, f"{beautiful(player)}\nВ какую компанию вы хотите инвестировать?", reply_markup=keyboard(round_list, player))
        bot.send_message(325051402, f"Гавр, запустим таймер?", reply_markup=keyboard_time_go())
        bot.send_message(325051402, f"Гавр, остановим инвестиции?", reply_markup=keyboard_stop_game())
    elif message.data == "stop_game":
        stop_game_flag = 1
        bot.send_message(325051402, f"Гавр, разреши посмотреть результаты", reply_markup=keyboard_result())
    elif message.data == "time_go":
        Timer(120, time_alert).start()
        Timer(180, time_to_stop).start()
    else:
        if stop_game_flag == 0:
            if message.data in round_list(message.from_user.id):
                bot.send_message(message.from_user.id, f"Сколько вы хотите инвестировать в {message.data}?\nСвободные средства — {players[message.from_user.id]['money']-sum([i for i in players[message.from_user.id]['companies'][players[message.from_user.id]['round_number']].values()])} {dollar_word(players[message.from_user.id]['money']-sum([i for i in players[message.from_user.id]['companies'][players[message.from_user.id]['round_number']].values()]))}.")
                players[message.from_user.id]["choose"] = message.data
                saving()
            else:
                bot.send_message(message.from_user.id, f'Компания "{message.data}" более не нуждается в инвестициях. Выберите компанию из нынешнего раунда.')
        else:
            bot.send_message(message.from_user.id, "К сожалению, время на инвестирование в этом раунде вышло.")


@bot.message_handler(content_types=["text"])
def sticker_hadler(message):
    global players
    if message.from_user.id in players:
        if message.text.isdigit() == False:
            if players[message.from_user.id]["name"] == 0:
                players[message.from_user.id]["name"] = message.text
                bot.send_message(325051402, f'Подключился новый игрок - {players[message.from_user.id]["name"]}')
                bot.send_message(message.from_user.id, f'Мы дождемся остальные команды и начнем.\nЖелаю удачи, {players[message.from_user.id]["name"]}!')
            else:
                small_talk(message)
        else:
            if stop_game_flag == 0:
                if players[message.from_user.id]['choose'] in round_list(message.from_user.id):
                    investment = int(message.text)
                    money = players[message.from_user.id]["money"]
                    round_investment = sum([i for i in players[message.from_user.id]["companies"][players[message.from_user.id]["round_number"]].values()])
                    if investment > money - round_investment:
                        bot.send_message(message.from_user.id, f"К сожалению, у вас только {money - round_investment} {dollar_word(money - round_investment)}. Сколько вы хотите инвестировать в {players[message.from_user.id]['choose']}?")
                    else:
                        players[message.from_user.id]["companies"][players[message.from_user.id]["round_number"]][players[message.from_user.id]["choose"]] += investment
                        round_investment = sum([i for i in players[message.from_user.id]["companies"][players[message.from_user.id]["round_number"]].values()])
                        if money == round_investment:
                            players[message.from_user.id]["round_result"] = money_result(message.from_user.id)
                            if players[message.from_user.id]['round_number'] == 1:
                                bot.send_photo(message.from_user.id, photo=putin)
                            bot.send_message(message.from_user.id, f"Свободные средства закончились. Ваши инвестиции:\n{already_invested(message.from_user.id)}.\n\nКраткая справка об этом периоде истории.\n\n{yesfraselist[players[message.from_user.id]['round_number'] - 1]}")
                            players[message.from_user.id]["finish"][players[message.from_user.id]["round_number"]] = 1
                            bot.send_message(325051402,f'{players[message.from_user.id]["name"]} закончил {players[message.from_user.id]["round_number"]} раунд c {money_result(message.from_user.id)} $')
                            if sum([players[i]["finish"][players[message.from_user.id]["round_number"]] for i in players]) == len(players):
                                bot.send_message(325051402, 'Гавр, все закончили, разреши посмотреть результаты', reply_markup=keyboard_result())
                                bot.send_message(325051402, investment_table())
                        else:
                            bot.send_message(message.from_user.id, f"Не останавливайтесь, у вас еще {money - round_investment} {dollar_word(money - round_investment)}.\n\nВы уже проинвестировали:\n{already_invested(message.from_user.id)}.\n\nЧьи акции хотите купить?", reply_markup=keyboard(round_list, message.from_user.id))
                    saving()
                else:
                    bot.send_message(message.from_user.id, "Сначала выберите компанию из списка предложенного выше. Иначе мы раздадим ваши деньги стартаперам из Сколково.")
            else:
                bot.send_message(message.from_user.id, "К сожалению, время на инвестирование в этом раунде вышло.")
    else:
        bot.send_message(message.from_user.id, 'Извините, мне разрешают разговаривать только с участниками игры. Чтобы начать игру, нажмите сюда >>> /start')


@bot.message_handler(content_types=["sticker"])     # отправил стикер в ответ на стикер
def sticker_hadler(message):
    bot.send_sticker(chat_id=message.from_user.id, data = sticker)


bot.polling(timeout=60)
