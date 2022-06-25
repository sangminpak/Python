def show_homepage():
    print("")
    print("          === DonateMe Homepage ===        ")
    print("------------------------------------------")
    print("| 1.    Login        | 2.    Register     |")
    print("------------------------------------------")
    print("| 3.    Donate       | 4.  Show donations |")
    print("------------------------------------------")
    print("|              5. Exit                    |")
    print("------------------------------------------")


donation_amt_list = []


def donate(username):
    donation_amt = float(input("Enter amount to donate: "))
    donation_amt_list.append(donation_amt)
    donation_string = (f"{username} donated $ {str(donation_amt)}.")
    print("")
    print("Thank you for your donation!")
    return donation_string


total = 0


def show_donations(donations):
    global total
    print("\n--- All Donations ---")
    if donations == []:
        print("Currently, there are no donations.")
    else:
        for donated in donations:
            print(donated)

        for donated in donation_amt_list:
            total += donated
        print("Total = $"+str(total))
