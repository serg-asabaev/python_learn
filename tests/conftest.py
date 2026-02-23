import pytest


@pytest.fixture
def dict_list_exec():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

@pytest.fixture
def dict_list_canceled():
    return [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

@pytest.fixture
def transactions():
    return (
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {
                    "amount": "79114.93",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188"
            },
            {
                "id": 873106923,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {
                    "amount": "43318.34",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "to": "Счет 74489636417521191160"
            },
            {
                "id": 895315941,
                "state": "EXECUTED",
                "date": "2018-08-19T04:27:37.904916",
                "operationAmount": {
                    "amount": "56883.54",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод с карты на карту",
                "from": "Visa Classic 6831982476737658",
                "to": "Visa Platinum 8990922113665229"
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
                "operationAmount": {
                    "amount": "67314.70",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "Visa Platinum 1246377376343588",
                "to": "Счет 14211924144426031657"
            }
        ]
    )

@pytest.fixture
def operation():
    return {
    "id": 490100847,
    "state": "EXECUTED",
    "date": "2018-12-22T02:02:49.564873",
    "operationAmount": {
      "amount": "56516.63",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "Visa Gold 8326537236216459",
    "to": "MasterCard 6783917276771847"
  }

@pytest.fixture
def wrong_operation():
  return {
    "id": 490100847,
    "state": "EXECUTED",
    "date": "2018-12-22T02:02:49.564873",
    "operationAmount": {
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "Visa Gold 8326537236216459",
    "to": "MasterCard 6783917276771847"
  }

@pytest.fixture
def currencies():
  return {'Date': '2026-02-21T11:30:00+03:00', 'PreviousDate': '2026-02-20T11:30:00+03:00', 'PreviousURL': '//www.cbr-xml-daily.ru/archive/2026/02/20/daily_json.js', 'Timestamp': '2026-02-23T13:00:00+03:00', 'Valute': {'AUD': {'ID': 'R01010', 'NumCode': '036', 'CharCode': 'AUD', 'Nominal': 1, 'Name': 'Австралийский доллар', 'Value': 53.9796, 'Previous': 54.0392}, 'AZN': {'ID': 'R01020A', 'NumCode': '944', 'CharCode': 'AZN', 'Nominal': 1, 'Name': 'Азербайджанский манат', 'Value': 45.1482, 'Previous': 45.0826}, 'DZD': {'ID': 'R01030', 'NumCode': '012', 'CharCode': 'DZD', 'Nominal': 100, 'Name': 'Алжирских динаров', 'Value': 59.017, 'Previous': 59.0265}, 'GBP': {'ID': 'R01035', 'NumCode': '826', 'CharCode': 'GBP', 'Nominal': 1, 'Name': 'Фунт стерлингов', 'Value': 103.262, 'Previous': 103.8096}, 'AMD': {'ID': 'R01060', 'NumCode': '051', 'CharCode': 'AMD', 'Nominal': 100, 'Name': 'Армянских драмов', 'Value': 20.3683, 'Previous': 20.3323}, 'BHD': {'ID': 'R01080', 'NumCode': '048', 'CharCode': 'BHD', 'Nominal': 1, 'Name': 'Бахрейнский динар', 'Value': 204.0833, 'Previous': 203.7871}, 'BYN': {'ID': 'R01090B', 'NumCode': '933', 'CharCode': 'BYN', 'Nominal': 1, 'Name': 'Белорусский рубль', 'Value': 26.9135, 'Previous': 26.8754}, 'BOB': {'ID': 'R01105', 'NumCode': '068', 'CharCode': 'BOB', 'Nominal': 1, 'Name': 'Боливиано', 'Value': 11.1074, 'Previous': 11.0912}, 'BRL': {'ID': 'R01115', 'NumCode': '986', 'CharCode': 'BRL', 'Nominal': 1, 'Name': 'Бразильский реал', 'Value': 14.6884, 'Previous': 14.6411}, 'HUF': {'ID': 'R01135', 'NumCode': '348', 'CharCode': 'HUF', 'Nominal': 100, 'Name': 'Форинтов', 'Value': 23.8264, 'Previous': 23.8503}, 'VND': {'ID': 'R01150', 'NumCode': '704', 'CharCode': 'VND', 'Nominal': 10000, 'Name': 'Донгов', 'Value': 30.6407, 'Previous': 30.5962}, 'HKD': {'ID': 'R01200', 'NumCode': '344', 'CharCode': 'HKD', 'Nominal': 10, 'Name': 'Гонконгских долларов', 'Value': 98.3746, 'Previous': 98.2445}, 'GEL': {'ID': 'R01210', 'NumCode': '981', 'CharCode': 'GEL', 'Nominal': 1, 'Name': 'Лари', 'Value': 28.6719, 'Previous': 28.6207}, 'DKK': {'ID': 'R01215', 'NumCode': '208', 'CharCode': 'DKK', 'Nominal': 1, 'Name': 'Датская крона', 'Value': 12.073, 'Previous': 12.1505}, 'AED': {'ID': 'R01230', 'NumCode': '784', 'CharCode': 'AED', 'Nominal': 1, 'Name': 'Дирхам ОАЭ', 'Value': 20.8991, 'Previous': 20.8688}, 'USD': {'ID': 'R01235', 'NumCode': '840', 'CharCode': 'USD', 'Nominal': 1, 'Name': 'Доллар США', 'Value': 76.7519, 'Previous': 76.6405}, 'EUR': {'ID': 'R01239', 'NumCode': '978', 'CharCode': 'EUR', 'Nominal': 1, 'Name': 'Евро', 'Value': 90.2833, 'Previous': 90.1669}, 'EGP': {'ID': 'R01240', 'NumCode': '818', 'CharCode': 'EGP', 'Nominal': 10, 'Name': 'Египетских фунтов', 'Value': 16.1287, 'Previous': 16.1053}, 'INR': {'ID': 'R01270', 'NumCode': '356', 'CharCode': 'INR', 'Nominal': 100, 'Name': 'Индийских рупий', 'Value': 84.3874, 'Previous': 84.5297}, 'IDR': {'ID': 'R01280', 'NumCode': '360', 'CharCode': 'IDR', 'Nominal': 10000, 'Name': 'Рупий', 'Value': 45.3482, 'Previous': 45.3924}, 'IRR': {'ID': 'R01300', 'NumCode': '364', 'CharCode': 'IRR', 'Nominal': 1000000, 'Name': 'Иранских риалов', 'Value': 59.7958, 'Previous': 59.709}, 'KZT': {'ID': 'R01335', 'NumCode': '398', 'CharCode': 'KZT', 'Nominal': 100, 'Name': 'Тенге', 'Value': 15.6902, 'Previous': 15.6633}, 'CAD': {'ID': 'R01350', 'NumCode': '124', 'CharCode': 'CAD', 'Nominal': 1, 'Name': 'Канадский доллар', 'Value': 56.0396, 'Previous': 56.0319}, 'QAR': {'ID': 'R01355', 'NumCode': '634', 'CharCode': 'QAR', 'Nominal': 1, 'Name': 'Катарский риал', 'Value': 21.0857, 'Previous': 21.0551}, 'KGS': {'ID': 'R01370', 'NumCode': '417', 'CharCode': 'KGS', 'Nominal': 100, 'Name': 'Сомов', 'Value': 87.7666, 'Previous': 87.6392}, 'CNY': {'ID': 'R01375', 'NumCode': '156', 'CharCode': 'CNY', 'Nominal': 1, 'Name': 'Юань', 'Value': 11.0929, 'Previous': 11.0747}, 'CUP': {'ID': 'R01395', 'NumCode': '192', 'CharCode': 'CUP', 'Nominal': 10, 'Name': 'Кубинских песо', 'Value': 31.98, 'Previous': 31.9335}, 'MDL': {'ID': 'R01500', 'NumCode': '498', 'CharCode': 'MDL', 'Nominal': 10, 'Name': 'Молдавских леев', 'Value': 44.816, 'Previous': 44.9689}, 'MNT': {'ID': 'R01503', 'NumCode': '496', 'CharCode': 'MNT', 'Nominal': 1000, 'Name': 'Тугриков', 'Value': 21.5247, 'Previous': 21.4935}, 'NGN': {'ID': 'R01520', 'NumCode': '566', 'CharCode': 'NGN', 'Nominal': 1000, 'Name': 'Найр', 'Value': 57.2199, 'Previous': 57.2753}, 'NZD': {'ID': 'R01530', 'NumCode': '554', 'CharCode': 'NZD', 'Nominal': 1, 'Name': 'Новозеландский доллар', 'Value': 45.7863, 'Previous': 45.7276}, 'NOK': {'ID': 'R01535', 'NumCode': '578', 'CharCode': 'NOK', 'Nominal': 10, 'Name': 'Норвежских крон', 'Value': 80.162, 'Previous': 80.8487}, 'OMR': {'ID': 'R01540', 'NumCode': '512', 'CharCode': 'OMR', 'Nominal': 1, 'Name': 'Оманский риал', 'Value': 199.6148, 'Previous': 199.3251}, 'PLN': {'ID': 'R01565', 'NumCode': '985', 'CharCode': 'PLN', 'Nominal': 1, 'Name': 'Злотый', 'Value': 21.3806, 'Previous': 21.4199}, 'SAR': {'ID': 'R01580', 'NumCode': '682', 'CharCode': 'SAR', 'Nominal': 1, 'Name': 'Саудовский риял', 'Value': 20.4672, 'Previous': 20.4375}, 'RON': {'ID': 'R01585F', 'NumCode': '946', 'CharCode': 'RON', 'Nominal': 1, 'Name': 'Румынский лей', 'Value': 17.7146, 'Previous': 17.7343}, 'XDR': {'ID': 'R01589', 'NumCode': '960', 'CharCode': 'XDR', 'Nominal': 1, 'Name': 'СДР (специальные права заимствования)', 'Value': 105.4364, 'Previous': 105.57}, 'SGD': {'ID': 'R01625', 'NumCode': '702', 'CharCode': 'SGD', 'Nominal': 1, 'Name': 'Сингапурский доллар', 'Value': 60.4679, 'Previous': 60.4611}, 'TJS': {'ID': 'R01670', 'NumCode': '972', 'CharCode': 'TJS', 'Nominal': 10, 'Name': 'Сомони', 'Value': 81.1537, 'Previous': 81.0316}, 'THB': {'ID': 'R01675', 'NumCode': '764', 'CharCode': 'THB', 'Nominal': 10, 'Name': 'Батов', 'Value': 24.6023, 'Previous': 24.543}, 'BDT': {'ID': 'R01685', 'NumCode': '050', 'CharCode': 'BDT', 'Nominal': 100, 'Name': 'Так', 'Value': 62.7498, 'Previous': 62.6588}, 'TRY': {'ID': 'R01700J', 'NumCode': '949', 'CharCode': 'TRY', 'Nominal': 10, 'Name': 'Турецких лир', 'Value': 17.5511, 'Previous': 17.5322}, 'TMT': {'ID': 'R01710A', 'NumCode': '934', 'CharCode': 'TMT', 'Nominal': 1, 'Name': 'Новый туркменский манат', 'Value': 21.9291, 'Previous': 21.8973}, 'UZS': {'ID': 'R01717', 'NumCode': '860', 'CharCode': 'UZS', 'Nominal': 10000, 'Name': 'Узбекских сумов', 'Value': 62.8455, 'Previous': 62.978}, 'UAH': {'ID': 'R01720', 'NumCode': '980', 'CharCode': 'UAH', 'Nominal': 10, 'Name': 'Гривен', 'Value': 17.7393, 'Previous': 17.7032}, 'CZK': {'ID': 'R01760', 'NumCode': '203', 'CharCode': 'CZK', 'Nominal': 10, 'Name': 'Чешских крон', 'Value': 37.2167, 'Previous': 37.4331}, 'SEK': {'ID': 'R01770', 'NumCode': '752', 'CharCode': 'SEK', 'Nominal': 10, 'Name': 'Шведских крон', 'Value': 84.3721, 'Previous': 85.5131}, 'CHF': {'ID': 'R01775', 'NumCode': '756', 'CharCode': 'CHF', 'Nominal': 1, 'Name': 'Швейцарский франк', 'Value': 98.9836, 'Previous': 99.3525}, 'ETB': {'ID': 'R01800', 'NumCode': '230', 'CharCode': 'ETB', 'Nominal': 100, 'Name': 'Эфиопских быров', 'Value': 49.2504, 'Previous': 49.2504}, 'RSD': {'ID': 'R01805F', 'NumCode': '941', 'CharCode': 'RSD', 'Nominal': 100, 'Name': 'Сербских динаров', 'Value': 76.8592, 'Previous': 76.9685}, 'ZAR': {'ID': 'R01810', 'NumCode': '710', 'CharCode': 'ZAR', 'Nominal': 10, 'Name': 'Рэндов', 'Value': 47.5141, 'Previous': 47.7332}, 'KRW': {'ID': 'R01815', 'NumCode': '410', 'CharCode': 'KRW', 'Nominal': 1000, 'Name': 'Вон', 'Value': 52.9068, 'Previous': 53.1082}, 'JPY': {'ID': 'R01820', 'NumCode': '392', 'CharCode': 'JPY', 'Nominal': 100, 'Name': 'Иен', 'Value': 49.4695, 'Previous': 49.5414}, 'MMK': {'ID': 'R02005', 'NumCode': '104', 'CharCode': 'MMK', 'Nominal': 1000, 'Name': 'Кьятов', 'Value': 36.5485, 'Previous': 36.4955}}}