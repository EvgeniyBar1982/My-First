import requests
import json
from Config import exchanges

class APIException(Exception):
    pass

class Convertor:
    @staticmethod
    def get_price(base, sym, amount):
        try:
            base_key = exchanges[base.lower()]
        except KeyError:
            raise APIException(f'Валюта {base} не найдена!')

        try:
            sym_key = exchanges[sym.lower()]
        except KeyError:
            raise APIException(f'Валюта {base} не найдена!')

        if base_key == sym_key:
            raise APIException(f'Невозможно конвертировать одинаковую валюту {base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать колличество {amount}!')



        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_key}&tsyms={sym_key}')
        resp = json.loads(r.content)
        new_price = resp[sym_key] * amount
        message = f'Цена{amount}{base} в {sym} : {new_price}'
        return message


