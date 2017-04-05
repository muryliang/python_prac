width = int(raw_input("width: "))

price_width = 10
item_width = width - 10

header_format = "%-*s%*s"
price_format = "%-*s%*.2f"

print width * '='
print header_format % (item_width, "item", price_width, "price")
print width * '-'
print price_format % (item_width, "apple", price_width, 11.2)
print price_format % (item_width, "pear", price_width, 12.2)
print width * '='
