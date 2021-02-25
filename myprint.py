SCREEN_WIDTH = 100


def print_center(s):
    x_pos = SCREEN_WIDTH // 2
    print((" " * x_pos), s)


def print_bar():
    print("=" * 100)


def print_bar_ln():
    print_bar()
    print()


def input_center(s):
    x_pos = SCREEN_WIDTH // 2
    print((" " * x_pos),s,end='')
    return input()

def print_header():
    print("="*100)
    print("id".ljust(15),
          "room no".ljust(15),
          "beds".ljust(15),
          "available".ljust(15),
          "floor".ljust(15)
          )
    print("="*100)
def print_cust_head():
    print("=" * 130)
    print("name".ljust(15),
          "id".ljust(15),
          "address".ljust(15),
          "phoneno".ljust(15),
          "roomno".ljust(15),
          "checkin".ljust(15),
          "checkout".ljust(15)
          )
    print("=" * 130)