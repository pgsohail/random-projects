product1_name, product1_price = 'jumping castle', 2000


# create a company name and information
company_name = 'jane doe, inc.'
company_address = '14 main road.'



# create a top border
print('*' * 50)

# print company information first using format
print('\t\t{}'.format(company_name.title()))
print('\t\t{}'.format(company_address.title()))


# print a line between sections
print('=' * 50)

# print out header for section of items
print('\tProduct Name\tProduct Price')

# create a print statement for each item
print('\t{}\t\t${}'.format(product1_name.title(), product1_price))

# print a line between sections
print('=' * 50)

# print out header for section of total
print('\t\t\tTotal')

# calculate total price and print out
total = product1_price *2
print('\t\t\t${}'.format(total))

# print a line between sections
print('=' * 50)



# create a bottom border
print('*' * 50)
