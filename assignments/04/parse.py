import re 
import collections

def main():
    
    # Read the CSV file with the product orders
    with open('./csv/orders.csv') as f_in:
        text = f_in.read()

    # Tasks / Match the regex with the text
    orders = re.findall(r'(#\d+)',text)                 #1

    product_names = re.findall(r'Product: (\w+)',text)  #2

    prices = re.findall(r'Price: (\$\d+\.\d{2})',text)  #3

    order_dates = re.findall(r'Date: (.{10})',re.sub(r'Date: (\d{4})-(\d{2})-(\d{2})',r'Date: \3-\2-\1',text))     #4 & #6
    
    pricey = []                                         #5
    for i in re.findall(r'(.*)\n',text):
        if float(re.search(r'\$\d+\.\d{2}',i).group()[1:]) > 500:
            pricey.append(re.search(r'(#\d+)',i).group())

    product_names_over6 = re.findall(r'Product: (\w{7,})',text)     #7

    products_unique = collections.Counter()             #8
    for i in product_names:
        products_unique[i] += 1

    orders_99 = re.findall(r'(Order #\d{5}).*Price:.*\.99',text)    #9

    min_price = min([float(i[1:]) for i in prices])     #10

    # Print the results
    print(orders,
          product_names,
          prices,
          order_dates,
          pricey,
          product_names_over6,
          dict(products_unique),
          orders_99,
          min_price,
          sep='\n')
    

if __name__ == '__main__':
    main()
