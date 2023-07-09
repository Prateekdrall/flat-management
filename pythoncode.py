import mysql.connector
from datetime import date

water_electric_expenses = 1000
maintenance = 1000


def clear():
    for _ in range(65):
        print()


def flat_exist(flat_no):
    conn = mysql.connector.connect(
        host='localhost', database='flat', user='root', password='raghav123@')
    cursor = conn.cursor()
    sql = "select * from flat where flat_no =" + flat_no + ";"
    cursor.execute(sql)
    record = cursor.fetchone()
    return record

def cust_exist(cust_no):
    conn = mysql.connector.connect(
        host='localhost', database='flat', user='root', password='raghav123@')
    cursor = conn.cursor()
    sql = "select * from customer_details where id =" + cust_no + ";"
    cursor.execute(sql)
    record = cursor.fetchone()
    return record

def add_flat():
    conn = mysql.connector.connect( host='localhost', database='flat', user='root', password='raghav123@')
    cursor = conn.cursor()
    clear()
    print('Add New FLAT - Screen')
    print('-' * 120)
    flat_no = input('\n Enter FLAT No :')
    flat_type = input('\n Enter FLAT Type( AC/DELUX) :')
    flat_rent = input('\n Enter FLAT Rent (INR) :')
    flat_bed = input('\n Enter BHK Type(Single/Double/Triple) :')
    sql = 'insert into flat(flat_no,flat_type,flat_rent,flat_bed,status) values \
        (' + flat_no + ',"' + flat_type.upper() + '",' + flat_rent + ',"' + flat_bed.upper() + '","free");'

    result = flat_exist(flat_no)
    if result is None:
        cursor.execute(sql)
    else:
        print('\n\n\FLAT No ', flat_no, ' already exists in our database')
    conn.close()
    wait = input('\n\n\n Press any key to continue....')

def add_customer_details():
    conn = mysql.connector.connect(
        host='localhost', database='flat', user='root', password='raghav123@')
    cursor = conn.cursor()
    clear()
    print('Add New customer - Screen')
    print('-' * 120)
    name = input('\n Enter customer Name :')
    address = input('\n Enter customer Address:')
    phone = input('\n Enter customer Phone NO :')
    email = input('\n Enter customer Email ID :')
    males = input('\n Enter Total Males :')
    females = input('\n Enter Total Females :')
    children = input('\n Enter Total Childeren :')

    sql = 'insert into customer_details(name,address,phone,email,males,females,children) values \
        ("' + name + '","' + address.upper() + '","' + phone + '","' + email + '","' + males + '","' + females + '","' + children + '");'

    cursor.execute(sql)
    print('\n\n\nCustomer Added success fully ...............')
    conn.close()
    wait = input('\n\n\n Press any key to continue....')


def modify_customer_info():
    conn = mysql.connector.connect(
        host='localhost', database='flat', user='root', password='raghav123@')
    cursor = conn.cursor()
    clear()
    print(' Change customer Information ')
    print('*' * 120)
    print('1.   Name')
    print('2.   Address')
    print('3.   Phone No')
    print('4.   Email ID')
    print('5.   Males')
    print('6.   Females')
    print('7.   Children')
    choice = int(input('Enter your choice :'))
    field_name = ''
    if choice == 1:
        field_name = 'name'
    if choice == 2:
        field_name = 'address'
    if choice == 3:
        field_name = 'phone'
    if choice == 4:
        field_name = 'email'
    if choice == 5:
        field_name = 'males'
    if choice == 6:
        field_name = 'females'
    if choice == 7:
        field_name = 'children'
    cust_no = input('Enter customer No :')
    value = input('Enter new value :')
    sql = 'update customer_details set ' + field_name + ' = ' +  value + ' where  id =' + cust_no + ';'
        #   value + ' where  id =' + cust_no + ';'
    cursor.execute(sql)
    wait = input(
        '\n\n\n Record Updated .............Press any key to continue......')





def flat_booking():
    conn = mysql.connector.connect(
        host='localhost', database='flat', user='root', password='raghav123@')
    cursor = conn.cursor()
    flat_no = input('Enter Flat No to book :')
    cust_id = input('Enter Customer ID :')
    date_of_occ = input('Enter date of occupancy (yyyy-mm-dd) :')
    advance = input('Enter advance amount :')
    sql1 = 'update flat set status = "occupied" where flat_no =' + flat_no + ';'
    sql2 = 'insert into booking_details(flat_id,cust_id,doo,advance) values (' + flat_no + ',' + cust_id + ',"' + date_of_occ + '",' + advance + ');'
    result = flat_exist(flat_no)
    result1 = cust_exist(cust_id)

    if result[4] == 'free' and result1 is not None:
        cursor.execute(sql1)
        cursor.execute(sql2)
        print('\n\n\FLAT no ', flat_no, 'booked for customer having id ', cust_id)

    if result[4] != 'free':
        print('\n Flat is already booked for ')
    if result1 is None:
        print('Customer does not exist....Please add customer first in our database')
    conn.close()
    wait = input('\n\n\n Press any key to continue....')


def bill_generation():
    global water_electric_expenses
    global maintenance
    conn = mysql.connector.connect(host='localhost', database='flat', user='root', password='raghav123@')
    cursor = conn.cursor()
    flat_no = input('Enter flat no whose bill is to be generated :')
    sql = 'select * from booking_details where flat_id = ' + flat_no + ' and dol is NULL;'
    cursor.execute(sql)
    record = cursor.fetchone()
    clear()
    print('Bill Generation ')
    print('-' * 100)
    print('Flat occupied  :', flat_no)
    dol = date.today()
    book_id = record[0]  # book_id
    doo = record[3]
    advance = record[5]
    total_months = int(((dol - doo).days)/30)
    result = flat_exist(flat_no)
    rent =int(result[2]) 
    amount = int(total_months*rent)
    payable_amount = int(amount  + water_electric_expenses + maintenance - advance)

    print('Date of Occupancy :', doo, '\nDate of bill generation :', dol)
    print('Total Payable Months : ', total_months)
    print('Flat Rent Per Month : ', rent)
    print('Total Amount  :', amount)
    print('Advance :', advance, '\nwater_electric_expenses: {}'.format( water_electric_expenses),
          '\nmaintenance : {}'.format(maintenance))
    print('Amount Payable :', payable_amount)
    sql1 = 'update flat set status ="free" where flat_no =' + flat_no + ';'
    sql2 = 'update booking_details set dol ="' + str(dol) + '" where flat_id="' + flat_no + '" '
    sql3 = 'insert into bill(book_id,amount,bill_date,water_electric_expens,maintenance) values(' + str(book_id) + ',' + str( payable_amount) + ',"' + str(dol) + '",' + str(water_electric_expenses) + ',' + str(maintenance) + ');'
    cursor.execute(sql1)
    cursor.execute(sql2)
    cursor.execute(sql3)
    conn.close()
    wait = input('\n\n\n Press any key to continue....')


def search_flat():
    conn = mysql.connector.connect(
        host='localhost', database='flat', user='root', password='raghav123@')
    cursor = conn.cursor()
    flat_no = input('Enter Flat No :')
    sql = 'select * from flat where flat_no =' + flat_no + ';'
    cursor.execute(sql)
    record = cursor.fetchone()
    clear()
    print('FLAT Status')
    print('*' * 120)
    print('FLAT NO :', record[0])
    print('FLAT Type :', record[1])
    print('FLAT rent :', record[2])
    print('FLAT bed :', record[3])
    print('FLAT status :', record[4])
    conn.close()
    wait = input('\n\n\nPress any key to continue......')


def search_customer():
    conn = mysql.connector.connect(
        host='localhost', database='flat', user='root', password='raghav123@')
    cursor = conn.cursor()

    clear()
    print('Search CUSTOMER DataBase')
    print('*' * 120)
    print('1.   Customer Name')
    print('2.   Customer Address')
    print('3.   Customer Phone')
    print('4.   Customer Email')

    choice = int(input('Enter your choice : '))
    field_name = ''
    if choice == 1:
        field_name = 'name'
    if choice == 2:
        field_name = 'address'
    if choice == 3:
        field_name = 'phone'
    if choice == 4:
        field_name = 'email'


    value = input('Enter value that you want to search :')
    if field_name == 'id':
        sql = 'select * from customer_details where ' + field_name + ' = ' + value + ';'
    else:
        sql = 'select * from customer_details where ' + field_name + ' like "%' + value + '%";'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Search Result for {} = {}'.format(field_name, value))
    print('*' * 140)
    print('{} {:20s} {:30s} {:15s} {:30s} '.format('ID', 'Name', 'Address', 'Phone', 'Email'))
    for record in records:
        print('{} {:20s} {:30s} {:15s} {:30s} '.format(
            record[0], record[1], record[2], record[3], record[4]))

    conn.close()
    wait = input('\n\n\nPress any key to continue......')


def search_booking():
    conn = mysql.connector.connect(
        host='localhost', database='flat', user='root', password='raghav123@')
    cursor = conn.cursor()
    flat_no = input('Enter flat No :')
    sql = 'select book_id,cust_id,doo,advance from booking_details where flat_id ='+flat_no
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print('Booking information for flat Number :{}'.format(flat_no))
    print('{}      {}      {}             {} '.format('BOOKING ID', 'CUSTOMER ID', 'Date of Occupancy', 'Advance'))
    print('*' * 140)
    for record in records:
        print('{}      {}      {}             {} '.format(
            record[0], record[1], record[2], record[3]))
    conn.close()
    wait = input('\n\n\nPress any key to continue......')




def search_bills():
    conn = mysql.connector.connect(
        host='localhost', database='flat', user='root', password='raghav123@')
    cursor = conn.cursor()
    bill_no = input('Enter Bill No :')
    sql = ' select bill.bill_id,bill.amount,bill_date,water_electric_expens,maintenance,b.book_id,doo,dol,advance, name,address,phone,email,flat_no \
            from bill, booking_details b, customer_details c , flat r \
            where bill.book_id = b.book_id \
            and b.flat_id = r.flat_no and b.cust_id = c.id AND NOT dol is NULL AND \
            bill_id = ' + bill_no + ';'
    cursor.execute(sql)
    record = cursor.fetchone()
    clear()
    print('Bill information for Bill No :{}'.format(bill_no))
    print('*' * 140)
    print('Bill NO ', record[0])
    print('Amount ', record[1])
    print('Bill Date ', record[2])
    print('water_electric_charges Charges ', record[3])
    print('Maintenance Charges', record[4])
    print('Booking ID ', record[5])
    print('Customer Used ID ', record[13])
    print('Date of Occupancy ', record[6])
    print('Date of Bill generation ', record[7])
    print('Advance Paid ', record[8])
    print('Customer Name ', record[9])
    print('Customer Address ', record[10])
    print('Customer Phone ', record[11])
    print('Customer Email ID ', record[12])

    conn.close()
    wait = input('\n\n\nPress any key to continue......')


def search_menu():
    while True:
        clear()
        print(' Search Menu')
        print('*' * 120)
        print("\n1.  SEARCH FLAT")
        print('\n2.  Customer Details')
        print('\n3.  Booking Details')
        print('\n4.  Search Bills')
        print('\n5.  Back to Main Menu')
        print('\n\n')
        choice = int(input('Enter your choice ...: '))
        if choice == 1:
            search_flat()
        if choice == 2:
            search_customer()
        if choice == 3:
            search_booking()
        if choice == 4:
            search_bills()
        if choice == 5:
            break


def main_menu():
    while True:
        clear()
        print("")
        print('***********************************************WELCOME TO FLAT MANAGEMENT SYSTEM*******************************')
        print("")
        print("\n1.   ADD NEW FLAT INFORMATION ")
        print('\n2.   ADD A NEW CUSTOMER ')
        print('\n3.   BOOK A FLAT')
        print('\n4.   MODIFY DETAILS OF CUSTOMER')
        print('\n5.   GENERATE EXPENSES UP TO THE CURRENT DATE')
        print('\n6.   FIND INFOO ')
        print('\n7.   EXIT PROGRAM')
        print('\n\n')
        choice = int(input('Enter your choice ...: '))
        if choice == 1:
            add_flat()
        if choice == 2:
            add_customer_details()
        if choice == 3:
            flat_booking()
        if choice == 4:
            modify_customer_info()
        if choice == 5:
            bill_generation()
        if choice == 6:
            search_menu()
        if choice == 7:
            break


# if __name__ == "_main_":
main_menu()
print("hello world")