# main.py
import pricing


net_price = pricing.get_net_price(
    price=100,
    tax_rate=0.01
)

print(net_price)