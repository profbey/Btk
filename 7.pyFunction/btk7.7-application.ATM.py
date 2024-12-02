# ATM Application

hesapA = {
        'name'          : 'mark',
        'account.numb'  : 375486535187,
        'balance'       : 1702,
        'extBalance'    : 500
}

hesapB = {
        'name'          : 'orhan keten',
        'account.numb'  : 456465321435,
        'balance'       : 2900,
        'extBalance'    : 3000
}


def paracek(account, amount):
        print(f"welcome {account['name']} ")

        if (account['balance'] >= amount):
                print(f"You can take ${amount} ")
                account['balance'] -= amount

        else:
                total = account['balance'] + account['extBalance']
                remaining = total - amount
                
                if total >= amount:
                        
                        wantingExtBalance = input('Do you want to use additional balance(y/n): ')
                        

                        if wantingExtBalance == 'y':
                                print(f"You can take {amount} $.\nRemaining total balance {remaining}$.")
                               
                        elif wantingExtBalance == 'n':
                                print(f"There is {account['balance']} in your account number :{account['account.numb']}.\nThe request is denied.")

                        else: 
                                print('pls just enter "y" or "n" ')
                
                else:
                        print(f'You do not have ${amount} in your total account.')





paracek(hesapA, 20000)





















