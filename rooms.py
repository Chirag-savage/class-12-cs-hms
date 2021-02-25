from myprint import *
import csv


def add_room():
    with open('data.csv', 'a', newline='') as f:
        csv_writer = csv.writer(f)
        room_id = input('Enter the room id:')
        room_no = input('Enter the room no:')
        room_bed = input('Enter the no of beds:')
        room_ava = input('Enter the room avialable(true/false) :')
        room_floor = input('Enter the room floor:')
        li = [room_id, room_no, room_bed, room_ava, room_floor]
        csv_writer.writerow(li)
        input_center('===========RECORD ADDED=========')


def show_rooms():
    with open('data.csv', 'r', newline='') as f:
        csv_reader = csv.reader(f)
        print_header()
        for rec in csv_reader:
            print(str(rec[0]).ljust(15), str(rec[1]).ljust(15), str(rec[2]).ljust(15), str(rec[3]).ljust(15),
                  str(rec[4]).ljust(15))
            print_bar()

        print('===========END OF RECORD=========')


def av_room(n):
    with open('data.csv', 'r', newline='') as f:
        csv_reader = csv.reader(f)
        print_header()
        for rec in csv_reader:
            if rec[2] == n and rec[3] == 'true':
                print(str(rec[0]).ljust(15), str(rec[1]).ljust(15), str(rec[2]).ljust(15), str(rec[3]).ljust(15),
                      str(rec[4]).ljust(15))
                print_bar()

        print('===========END OF RECORD=========')


def room_detail(rno):
    with open('data.csv', 'r', newline='') as f:
        csv_reader = csv.reader(f)
        print_header()
        for rec in csv_reader:
            if rec[1] == rno:
                print(str(rec[0]).ljust(15), str(rec[1]).ljust(15), str(rec[2]).ljust(15), str(rec[3]).ljust(15),
                      str(rec[4]).ljust(15))
                print_bar()

        print('===========END OF RECORD=========')


def upd_room(hoi, choi, index):
    f = open('data.csv', 'r', newline='')
    r = csv.reader(f)
    rec = []
    for i in r:
        rec.append(i)
    f.close()
    for col in rec:
        if col[0] == hoi:
            col[index] = choi
    f = open('data.csv', 'w', newline='')
    w = csv.writer(f)
    for fg in rec:
        w.writerow(fg)
    f.close()
    print_bar()
    input_center('RECORD UPDATED')


def del_room(rng):
    f = open('data.csv', 'r', newline='')
    r = csv.reader(f)
    rec = []
    for i in r:
        rec.append(i)
    f.close()

    f = open('data.csv', 'w', newline='')
    w = csv.writer(f)
    for fg in rec:
        if fg[0] == rng:
            continue
        else:
            w.writerow(fg)
    f.close()
    input_center('RECORD DELETED')


def room_menu():
    while True:
        print()
        print("============================")
        print("==========Room Menu=========")
        print("============================")
        print()

        print("1. Add new room")
        print("2. View all rooms")
        print("3. Find available rooms by number of beds")
        print("4. Edit Room details")
        print("5. Delete room")
        print("6. Get room detail by room no")
        print("0. Go Back")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_room()
        elif choice == 2:
            show_rooms()
        elif choice == 3:
            n = input('Enter the no of beds you want:')
            av_room(n)
        elif choice == 4:
            print('1.Edit room id')
            print('2.Edit room no')
            print('3.Edit no beds')
            print('4.Edit availabilty')
            print('5.Edit floor')
            df = int(input('Enter your choice'))
            if df == 1:
                index = 0
                hoi = input('Enter the room id to update the record:')
                choi = input('Enter the new room id:')
                upd_room(hoi, choi, index)

            elif df == 2:
                index = 1
                hoi = input('Enter the  room id to update the record:')
                choi = input('Enter the new room no:')
                upd_room(hoi, choi, index)
            elif df == 3:
                index = 2
                hoi = input('Enter the  room id to update the record:')
                choi = input('Enter the new  no of bed:')
            elif df == 4:
                index = 3
                hoi = input('Enter the  room id to update the record:')
                choi = input('Enter the new room availability:')
                upd_room(hoi, choi, index)
            elif df == 5:
                index = 4
                hoi = input('Enter the  room id to update the record:')
                choi = input('Enter the new room floor:')
                upd_room(hoi, choi, index)
        elif choice == 5:
            rng = input('Enter the room id to delete it:')
            del_room(rng)
        elif choice == 6:
            rno = input('Enter the room no:')
            room_detail(rno)

        elif choice == 0:
            break
        else:
            print("Invalid choice (Press 0 to go back)")
