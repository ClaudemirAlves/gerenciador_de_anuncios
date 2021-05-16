from datetime import datetime
from time import sleep

ads = [[]]
ad_name = ""
client = ""
investment = 0
total_views = 0
total_clicks = 0 
total_shares = 0

def ad_registration(ads):
    new_ad = []
    print('''
___________________________________________________________________________________________________
    ''')
    ad_name = input('''
    Por favor, digite aqui o nome do anúncio: ''')
    while ad_name == "":
        print('''
    O nome do anúncio não pode ficar vazio. Por favor, insira algo.''')
        sleep(3)
        ad_name = input('''
    Por favor, digite aqui o nome do anúncio: ''')
    ad_name_low = ad_name.lower()
    client = input('''
    Agora digite aqui o nome do cliente, por favor: ''')
    while client == "":
        print('''
    O nome do cliente não pode ficar vazio. Por favor, insira algo.''')
        sleep(3)
        client = input('''
    Digite aqui o nome do cliente, por favor: ''')
    client_low = client.lower()
    day1 = int(input('''
    Digite aqui o dia do início do anúncio, no formato DD: '''))
    if day1 < 1 or day1 > 31:
        while day1 < 1 or day1 > 31:
            print('''
    São permitidos apenas números de 1 a 31.''')
            sleep(3)
            day1 = int(input('''
    Digite aqui o dia do início do anúncio, no formato DD: '''))
    month1 = int(input('''
    Digite também o mês do início do anúncio no formato MM, por favor: '''))
    if month1 < 1 or month1 > 12:
        while month1 < 1 or month1 > 12:
            print('''
    São permitidos apenas números de 1 a 12.''')
            sleep(3)
            month1 = int(input('''
    Digite o mês do início do anúncio no formato MM, por favor: '''))
    year1 = int(input('''
    E também o ano de início do anúncio, no formato AAAA: '''))
    if year1 < 1:
        while year1 < 1:
            print('''
    Não são permitidos zero ou valores negativos para este campo.''')
            sleep(3)
            year1 = int(input('''
    Digite o ano de início do anúncio, no formato AAAA: '''))
    start_date = datetime(year1, month1, day1)
    day2 = int(input('''
    Digite aqui o dia do término do anúncio, no formato DD: '''))
    if day2 < 1 or day2 > 31:
        while day2 < 1 or day2 > 31:
            print('''
    São permitidos apenas números de 1 a 31.''')
            sleep(3)
            day2 = int(input('''
    Digite aqui o dia do término do anúncio, no formato DD: '''))        
    month2 = int(input('''
    Digite também o mês do término do anúncio no formato MM, por favor: '''))
    if month2 < 1 or month2 > 12:
        while month2 < 1 or month2 > 12:
            print('''
    São permitidos apenas números de 1 a 12.''')
            sleep(3)
            month2 = int(input('''
    Digite o mês do término do anúncio no formato MM, por favor: '''))
    year2 = int(input('''
    E também o ano de término do anúncio, no formato AAAA: '''))
    if year2 < 1:
        while year2 < 1:
            print('''
    Não são permitidos zero ou valores negativos para este campo.''')
            sleep(3)
            year2 = int(input('''
    Digite o ano de término do anúncio, no formato AAAA: '''))
    end_date = datetime(year2, month2, day2)
    check_date = total_days(start_date, end_date)
    if check_date < 1:
        while check_date < 1:
            print('''
    A data final não pode ser a mesma ou anterior a data inicial. Por favor, verifique as datas inseridas e as corrija.
    ''')
            sleep(7)
            day1 = int(input('''
    Digite aqui o dia do início do anúncio, no formato DD: '''))
            if day1 < 1 or day1 > 31:
                while day1 < 1 or day1 > 31:
                    print('''
    São permitidos apenas números de 1 a 31.''')
                    sleep(3)
                    day1 = int(input('''
    Digite aqui o dia do início do anúncio, no formato DD: '''))        
            month1 = int(input('''
    Digite também o mês do início do anúncio no formato MM, por favor: '''))
            if month1 < 1 or month1 > 12:
                while month1 < 1 or month1 > 12:
                    print('''
    São permitidos apenas números de 1 a 12.''')
                    sleep(3)
                    month1 = int(input('''
    Digite o mês do início do anúncio no formato MM, por favor: '''))
            year1 = int(input('''
    E também o ano de início do anúncio, no formato AAAA: '''))
            if year1 < 1:
                while year1 < 1:
                    print('''
    Não são permitidos zero ou valores negativos para este campo.''')
                    sleep(3)
                    year1 = int(input('''
    Digite o ano de início do anúncio, no formato AAAA: '''))
            start_date = datetime(year1, month1, day1)
            day2 = int(input('''
    Digite aqui o dia do término do anúncio, no formato DD: '''))
            if day2 < 1 or day2 > 31:
                while day2 < 1 or day2 > 31:
                    print('''
    São permitidos apenas números de 1 a 31.''')
                    sleep(3)
                    day2 = int(input('''
    Digite aqui o dia do término do anúncio, no formato DD: '''))
            month2 = int(input('''
    Digite também o mês do término do anúncio no formato MM, por favor: '''))
            if month2 < 1 or month2 > 12:
                while month2 < 1 or month2 > 12:
                    print('''
    São permitidos apenas números de 1 a 12.''')
                    sleep(3)
                    month2 = int(input('''
    Digite o mês do término do anúncio no formato MM, por favor: '''))
            year2 = int(input('''
    E também o ano de término do anúncio, no formato AAAA: '''))
            if year2 < 1:
                while year2 < 1:
                    print('''
    Não são permitidos zero ou valores negativos para este campo.''')
                    sleep(3)
                    year2 = int(input('''
    Digite o ano de término do anúncio, no formato AAAA: '''))
            end_date = datetime(year2, month2, day2)
            check_date = total_days(start_date, end_date)
    investment_per_day = float(input('''
    Digite aqui o valor do investimento por dia do anúncio, em R$: '''))
    date_range = total_days(start_date, end_date)
    investment = total_investment(start_date, end_date, investment_per_day)
    total_views = calculator_views(investment)
    total_clicks = calculator_clicks(total_views)
    total_shares = calculator_shares(total_clicks)
    print('''
___________________________________________________________________________________________________
___________________________________________________________________________________________________
                              Novo anúncio cadastrado com sucesso!
                           O novo anúncio cadastrado ficará ativo por
                                          %d dias.
___________________________________________________________________________________________________
___________________________________________________________________________________________________
    '''%(date_range))
    sleep(5)
    new_ad.append(ad_name)
    new_ad.append(ad_name_low)
    new_ad.append(client)
    new_ad.append(client_low)
    new_ad.append(investment_per_day)
    new_ad.append(date_range)
    new_ad.append(investment)
    new_ad.append(total_views)
    new_ad.append(total_clicks)
    new_ad.append(total_shares)
    ads.append(new_ad)
    return ads

def total_days(start_date, end_date):
    date_range = int((end_date - start_date).days)
    return date_range

def total_investment(start_date, end_date, investment_per_day):
    date_range = int((end_date - start_date).days)
    investment = date_range * investment_per_day
    return investment

def calculator_views(investment):
    original_views = int(30 * investment)
    clicks = (original_views * 12) / 100
    shares = (clicks * 3) / 20
    new_views = int(shares) * 40
    total_views = int(new_views + original_views)
    return total_views

def calculator_clicks(total_views):
    clicks = (total_views * 12) / 100
    total_clicks = int(clicks)
    return total_clicks

def calculator_shares(total_clicks):
    shares = (total_clicks * 3) / 20
    total_shares = int(shares)
    return total_shares

def consult_ad(ads):
    consult_option = int(input('''
___________________________________________________________________________________________________
    
    Se você quer consultar anúncios pelo cliente, digite 1.
    
    Se quer consultar por intervalo de tempo, em dias, digite 2.
    
    Qual sua opção? 1 ou 2?
    '''))
    if consult_option == 1:
        client_name = input('''
___________________________________________________________________________________________________

    Digite aqui o nome do cliente para consulta: ''').lower()
        control = 0
        if control == 0:
            for mostrar in ads:
                if client_name in mostrar:
                    if client_name == mostrar[3]:
                        print('''
___________________________________________________________________________________________________
___________________________________________________________________________________________________
                                       Cliente encontrado!
                
                                   O nome de seu anúncio é %s.
    '''%(mostrar[0]))
                        print('''
                    - O valor total investido no anúncio foi de R$ %.2f;
                    - a quantidade máxima de visualizações foi/será de %d;
                    - a quantidade máxima de cliques foi/será de %d;
                    - e a quantidade máxima de compartilhamentos foi/será de %d.
___________________________________________________________________________________________________
___________________________________________________________________________________________________
    '''%(mostrar[6], mostrar[7], mostrar[8], mostrar[9]))
                        control += 1
        sleep(15)
        if control == 0:
            print('''
    Nenhum anúncio encontrado para este cliente.''')
        sleep(3)
        new_consult = input('''
___________________________________________________________________________________________________

    Você gostaria de fazer outra consulta? Digite "s" para sim ou "n" para não.
    ''').lower()
        if new_consult == "s":
            consult_ad(ads)
        elif new_consult == "n":
            main()
        else:
            while new_consult != "s" and new_consult != "n":
                print('''
    Opção inválida. 
    Você será redirecionado(a) para as opções novamente.''')
                sleep(5)
                new_consult = input('''
___________________________________________________________________________________________________

    Você gostaria de fazer outra consulta? Digite "s" para sim ou "n" para não.
    ''').lower()
            if new_consult == "s":
                consult_ad(ads)
            elif new_consult == "n":
                main()
        main()
    elif consult_option == 2:
        time_interval = int(input('''
___________________________________________________________________________________________________

    Digite aqui o intervalo de tempo, em dias, para consultar: '''))
        control = 0
        if control == 0:
            for mostrar in ads:
                if time_interval in mostrar:
                    if time_interval == mostrar[5]:
                        print('''
___________________________________________________________________________________________________
___________________________________________________________________________________________________
                    O seguinte anúncio apresenta o intervalo de tempo solicitado:

                                        Nome do anúncio: %s
                                        Nome do cliente: %s
    '''%(mostrar[0], mostrar[2]))
                        print('''
                    - O valor total investido no anúncio foi/será de R$ %.2f;
                    - a quantidade máxima de visualizações foi/será de %d;
                    - a quantidade máxima de cliques foi/será de %d;
                    - e a quantidade máxima de compartilhamentos foi/será de %d.
___________________________________________________________________________________________________
___________________________________________________________________________________________________
    '''%(mostrar[6], mostrar[7], mostrar[8], mostrar[9]))
                        control += 1
        sleep(15)
        if control == 0:
            print('''
    Nenhum anúncio encontrado para este intervalo de tempo.''')
        sleep(3)
        new_consult = input('''
___________________________________________________________________________________________________

    Você gostaria de fazer outra consulta? Digite "s" para sim ou "n" para não.
    ''').lower()
        if new_consult == "s":
            consult_ad(ads)
        elif new_consult == "n":
            main()
        else:
            while new_consult != "s" and new_consult != "n":
                print('''
    Opção inválida. 
    Você será redirecionado(a) para as opções novamente.''')
                sleep(5)
                new_consult = input('''
___________________________________________________________________________________________________

    Você gostaria de fazer outra consulta? Digite "s" para sim ou "n" para não.
    ''').lower()
            if new_consult == "s":
                consult_ad(ads)
            elif new_consult == "n":
                main()
        main()   
    else:
        print('''
    Opção inválida
    Você será redirecionado(a) para as opções novamente.''')
    sleep(5)
    consult_ad(ads)

def main():
    option = int(input('''
___________________________________________________________________________________________________
    
    Bem vindo ao Sistema de Cadastro de Anúncios da Divulga Tudo!!!
    
    Se você quer cadastrar um novo anúncio, digite 1.
    
    Se quer consultar um anúncio já existente, digite 2.

    E se quiser sair do programa, digite 3
    
    Qual sua opção? 1, 2 ou 3?
    '''))
    if option == 1:
        ad_registration(ads)
        register_option = input('''
___________________________________________________________________________________________________
    
    Você gostaria de fazer outro registro? Digite "s" para sim e "n" para não.
    ''').lower()
        if register_option == "s":
            ad_registration(ads)
        elif register_option == "n":
            main()
        else:
            while register_option != "s" and register_option != "n":
                print('''
    Opção inválida. 
    Você será redirecionado(a) para as opções novamente.''')
                sleep(5)
                register_option = input('''
___________________________________________________________________________________________________

    Você gostaria de fazer outro registro? Digite "s" para sim ou "n" para não.
    ''').lower()
            if register_option == "s":
                ad_registration(ads)
            elif register_option == "n":
                main()
        main()
    elif option == 2:
        consult_ad(ads)
        main()
    elif option == 3:
        print('''
___________________________________________________________________________________________________
___________________________________________________________________________________________________
___________________________________________________________________________________________________
    
                                O programa será encerrado.
___________________________________________________________________________________________________
___________________________________________________________________________________________________
___________________________________________________________________________________________________

    ''')
        sleep(3)
        quit()
    else:
        print('''
    Opção inválida. 
    Você será redirecionado(a) para as opções novamente.''')
        sleep(5)
        main()

def test_investment_0():
    assert calculator_views(0.00) == 0

def test_investment_1_05():
    assert calculator_views(1.05) == 31

def test_investment_2():
    assert calculator_views(2.00) == 100

def test_investment_100():
    assert calculator_views(100.00) == 5160

def test_investment_500():
    assert calculator_views(500.00) == 25800

def test_investment_1500():
    assert calculator_views(1500.00) == 77400

def test_investment_159753_02():
    assert calculator_views(159753.02) == 8243230

def test_investment_2000000():
    assert calculator_views(2000000.00) == 103200000

def test_views_0():
    assert calculator_clicks(0) == 0

def test_views_1():
    assert calculator_clicks(1) == 0

def test_views_100():
    assert calculator_clicks(100) == 12

def test_views_200():
    assert calculator_clicks(200) == 24

def test_views_1000():
    assert calculator_clicks(1000) == 120

def test_views_77400():
    assert calculator_clicks(77400) == 9288

def test_views_1000000():
    assert calculator_clicks(1000000) == 120000

def test_views_258000000000():
    assert calculator_clicks(258000000000) == 30960000000

def test_clicks_0():
    assert calculator_shares(0) == 0

def test_clicks_12():
    assert calculator_shares(12) == 1

def test_clicks_18():
    assert calculator_shares(18) == 2

def test_clicks_24():
    assert calculator_shares(24) == 3

def test_clicks_27():
    assert calculator_shares(27) == 4

def test_clicks_3096():
    assert calculator_shares(3096) == 464

def test_clicks_9288():
    assert calculator_shares(9288) == 1393

def test_clicks_30960000000():
    assert calculator_shares(30960000000) == 4644000000

def test_dates_1():
    assert total_days(datetime(2021,12,15,0,0), datetime(2021,12,16,0,0)) == 1

def test_dates_2():
    assert total_days(datetime(2020,10,10,0,0), datetime(2020,11,10,0,0)) == 31

def test_dates_3():
    assert total_days(datetime(2022,1,1,0,0), datetime(2022,3,30,0,0)) == 88

def test_dates_4():
    assert total_days(datetime(2021,12,15,0,0), datetime(2022,12,15,0,0)) == 365

def test_dates_5():
    assert total_days(datetime(2021,12,15,0,0), datetime(2023,10,25,0,0)) == 679

def test_dates_6():
    assert total_days(datetime(2012,11,10,0,0), datetime(2032,11,10,0,0)) == 7305

def test_dates_7():
    assert total_days(datetime(2000,6,5,0,0), datetime(2050,8,7,0,0)) == 18325

def test_dates_8():
    assert total_days(datetime(1989,2,9,0,0), datetime(2089,9,2,0,0)) == 36730

def test_investment_per_day_1():
    assert total_investment(datetime(2021,12,15,0,0), datetime(2021,12,16,0,0), 1.00) == 1.0

def test_investment_per_day_2():
    assert total_investment(datetime(2020,10,10,0,0), datetime(2020,11,10,0,0), 2.00) == 62.0

def test_investment_per_day_3():
    assert total_investment(datetime(2022,1,1,0,0), datetime(2022,3,30,0,0), 10.00) == 880.0

def test_investment_per_day_4():
    assert total_investment(datetime(2021,12,15,0,0), datetime(2022,12,15,0,0), 150.40) == 54896

def test_investment_per_day_5():
    assert total_investment(datetime(2021,12,15,0,0), datetime(2023,10,25,0,0), 1000.00) == 679000.0

def test_investment_per_day_6():
    assert total_investment(datetime(2012,11,10,0,0), datetime(2032,11,10,0,0), 500.50) == 3656152.5

def test_investment_per_day_7():
    assert total_investment(datetime(1989,2,9,0,0), datetime(2089,9,2,0,0), 100.00) == 3673000.0

def test_investment_per_day_8():
    assert total_investment(datetime(2000,6,5,0,0), datetime(2050,8,7,0,0), 2533.77) == 46431335.25