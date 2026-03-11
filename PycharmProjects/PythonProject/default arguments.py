
def net_price(list_price, discount=0, tax=0.05):
    net = list_price * (1 - discount) * (1 + tax)
    return net

print(net_price(10))