from myprint import *
import csv
from datetime import date



def add_cust():
    name = input('Enter name of customer:')
    id_2 = input('Enter id of customer:')
    address = input('Enter address of customer:')
    phono = input('Enter phone no of customer:')
    roomnoo = input('Enter room no of customer:')
    check_in = input('Enter check in date of customer:')
    check_out = input('Enter check out date of customer:')
    data_1 = [name, id_2, address, phono, roomnoo, check_in, check_out]
    with open('data2.csv', 'a', newline='') as f:
        wr = csv.writer(f)
        wr.writerow(data_1)
        print('========RECORD ADDED=======')


def f_2():
    name_sear = input('Enter the name of customer to search its data:')
    with open('data2.csv', 'r', newline='') as f:
        re = csv.reader(f)
        print_cust_head()
        for i in re:
            if i[0] == name_sear:
                print(str(i[0]).ljust(15), str(i[1]).ljust(15), str(i[2]).ljust(15), str(i[3]).ljust(15),
                      str(i[4]).ljust(15), str(i[5]).ljust(15), str(i[6]).ljust(15))
                print("=" * 130)


def f_3():
    name_sear = input('Enter the id of customer to search its data:')
    with open('data2.csv', 'r', newline='') as f:
        re = csv.reader(f)
        print_cust_head()
        for i in re:
            if i[1] == name_sear:
                print(str(i[0]).ljust(15), str(i[1]).ljust(15), str(i[2]).ljust(15), str(i[3]).ljust(15),
                      str(i[4]).ljust(15), str(i[5]).ljust(15), str(i[6]).ljust(15))
                print("=" * 130)


def f_4():
    name_sear = input('Enter the address of customer to search its data:')
    with open('data2.csv', 'r', newline='') as f:
        re = csv.reader(f)
        print_cust_head()
        for i in re:
            if i[2] == name_sear:
                print(str(i[0]).ljust(15), str(i[1]).ljust(15), str(i[2]).ljust(15), str(i[3]).ljust(15),
                      str(i[4]).ljust(15), str(i[5]).ljust(15), str(i[6]).ljust(15))
                print("=" * 130)


def f_5():
    name_sear = input('Enter the phoneno of customer to search its data:')
    with open('data2.csv', 'r', newline='') as f:
        re = csv.reader(f)
        print_cust_head()
        for i in re:
            if i[3] == name_sear:
                print(str(i[0]).ljust(15), str(i[1]).ljust(15), str(i[2]).ljust(15), str(i[3]).ljust(15),
                      str(i[4]).ljust(15), str(i[5]).ljust(15), str(i[6]).ljust(15))
                print("=" * 130)


def f_6():
    name_sear = input('Enter the roomno of customer to search its data:')
    with open('data2.csv', 'r', newline='') as f:
        re = csv.reader(f)
        print_cust_head()
        for i in re:
            if i[4] == name_sear:
                print(str(i[0]).ljust(15), str(i[1]).ljust(15), str(i[2]).ljust(15), str(i[3]).ljust(15),
                      str(i[4]).ljust(15), str(i[5]).ljust(15), str(i[6]).ljust(15))
                print("=" * 130)


def f_7():
    name_sear = input('Enter the check in date of customer to search its data:')
    with open('data2.csv', 'r', newline='') as f:
        re = csv.reader(f)
        print_cust_head()
        for i in re:
            if i[5] == name_sear:
                print(str(i[0]).ljust(15), str(i[1]).ljust(15), str(i[2]).ljust(15), str(i[3]).ljust(15),
                      str(i[4]).ljust(15), str(i[5]).ljust(15), str(i[6]).ljust(15))
                print("=" * 130)
def f_12():
    with open('data2.csv', 'r', newline='') as f:
        re = csv.reader(f)
        print_cust_head()
        for i in re:
                print(str(i[0]).ljust(15), str(i[1]).ljust(15), str(i[2]).ljust(15), str(i[3]).ljust(15),
                      str(i[4]).ljust(15), str(i[5]).ljust(15), str(i[6]).ljust(15))
                print("=" * 130)
def f_8():
    with open('data2.csv', 'r', newline='') as f:
        re = csv.reader(f)
        print("=" * 30)
        print('NAME OF CUSTOMERS')
        print("=" * 30)
        for i in re:
            print(str(i[0]))
            print("=" * 30)
def f_11():
    rng = input('Enter the name of customer to delete record:')
    f = open('data2.csv', 'r', newline='')
    r = csv.reader(f)
    rec = []
    for i in r:
        rec.append(i)
    f.close()

    f = open('data2.csv', 'w', newline='')
    w = csv.writer(f)
    for fg in rec:
        if fg[0] == rng:
            continue
        else:
            w.writerow(fg)
    f.close()
    input_center('RECORD DELETED')


def f_9():
    rng=input('Enter the customer id to check out:')
    f = open('data2.csv', 'r', newline='')
    r = csv.reader(f)
    rec = []
    for i in r:
        rec.append(i)
    f.close()
    for col in rec:
        if col[1] == rng:
            col[6]=str(date.today())
    f = open('data2.csv', 'w', newline='')
    w = csv.writer(f)
    for fg in rec:
        w.writerow(fg)
    f.close()
    print_bar()
    input_center('CUSTOMER CHECK OUTED')

def f_10(hoi,choi,index):
    f = open('data2.csv', 'r', newline='')
    r = csv.reader(f)
    rec = []
    for i in r:
        rec.append(i)
    f.close()
    for col in rec:
        if col[1] == hoi:
            col[index] = choi
    f = open('data2.csv', 'w', newline='')
    w = csv.writer(f)
    for fg in rec:
        w.writerow(fg)
    f.close()
    print_bar()
    input_center('RECORD UPDATED')
def f_13():
    rng=input('Enter the customer id to check out:')
    f = open('data2.csv', 'r', newline='')
    r = csv.reader(f)
    rec = []
    for i in r:
        rec.append(i)
    f.close()
    for col in rec:
        if col[1] == rng:
            col[5]=str(date.today())
    f = open('data2.csv', 'w', newline='')
    w = csv.writer(f)
    for fg in rec:
        w.writerow(fg)
    f.close()
    print_bar()
    input_center('CUSTOMER CHECK IN')

def customer_menu():
    while True:
        print()
        print("==============================")
        print("==========Customer Menu=========")
        print("==============================")
        print()
        print("1. New Customer")
        print("2. Show Customer Details by name")
        print("3. Show customer details by id")
        print("4. Show customer details by address")
        print("5. Show customer details by phone number")
        print("6. Show customer details by room no")
        print("7. Show customer details by check in date")
        print("8. Show current list of customers")
        print("9. Check out")
        print("10. Edit customer Details")
        print("11. Delete Customer record")
        print("12. View all customers")
        print("13.Check in")
        print("0. Go Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_cust()
        elif choice == 2:
            f_2()
        elif choice == 3:
            f_3()

        elif choice == 4:
            f_4()
        elif choice == 5:
            f_5()
        elif choice == 6:
            f_6()
        elif choice == 7:
            f_7()
        elif choice == 8:
            f_8()
        elif choice == 9:
            f_9()
        elif choice == 10:
            print('1.Edit name')
            print('2.Edit customer id ')
            print('3.Edit address')
            print('4.Edit Phone number')
            print('5.Edit room no')
            print('6.Edit check in date')
            print('7.Edit check out date')
            n=int(input('ENTER YOUR CHOICE:'))
            if n==1:
                hoi=input('Enter the customer id:')
                choi=input("ENTER THE NEW NAME:")
                index=0
                f_10(hoi,choi,index)
            if n==2:
                hoi=input('Enter the customer id:')
                choi=input("ENTER THE NEW CUSTOMER ID:")
                index=1
                f_10(hoi,choi,index)

            if n==3:
                hoi=input('Enter the customer id:')
                choi=input("ENTER THE NEW ADDRESS:")
                index=2
                f_10(hoi,choi,index)
            if n==4:
                hoi=input('Enter the customer id:')
                choi=input("ENTER THE NEW PHONE NO:")
                index=3
                f_10(hoi,choi,index)
            if n==5:
                hoi=input('Enter the customer id:')
                choi=input("ENTER THE NEW ROOM NO:")
                index=4
                f_10(hoi,choi,index)
            if n==6:
                hoi=input('Enter the customer id:')
                choi=input("ENTER THE NEW CHECK IN DATE:")
                index=5
                f_10(hoi,choi,index)
            if n==7:
                hoi=input('Enter the customer id:')
                choi=input("ENTER THE NEW CHECK OUT DATE")
                index=6
                f_10(hoi,choi,index)
        elif choice == 11:
            f_11()
        elif choice == 12:
            f_12()
        elif choice==13:
            f_13()
        elif choice == 0:
            break
        else:
            print("Invalid choice (Press 0 to go back)")
