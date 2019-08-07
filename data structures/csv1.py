import csv
class Stock:
    def __init__(self,name,symbol,exchange,price):
        self.name = name
        self.symbol = symbol
        self.exchange = exchange
        self.price = price

    def __str__(self):
        return f"{self.name},{self.name},{self.exchange},{self.price}"


def clean_init_get_stocks():
    stock_lst = []
    try:
        with open("c.csv") as f:
            data = csv.reader(f,delimiter=",")
            line = 0
            for d in data:
                if line == 0:
                    line+=1
                    continue
                stock_lst.append(Stock(*d))
        for s in stock_lst:
            if "k" in s.price:
                s.price = float(s.price.strip().replace("k",""))*1000
            else:
                s.price = float(s.price)
            print(s)
    except Exception as e:
        print(e)
    return stock_lst

def stock_by_price(price):
    st_lst = clean_init_get_stocks()
    f =filter(lambda x:x.price <= price,st_lst)
    if f:
        show_stock_