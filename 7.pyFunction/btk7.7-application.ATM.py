# ATM Application

account_A = {
        'name'          : 'mark spencer',
        'accountNo'     : 375486535187,
        'balance'       : 1702,
        'extBalance'    : 500
}

account_B = {
        'name'          : 'calvin klein',
        'accountNo'     : 456465321435,
        'balance'       : 2000,
        'extBalance'    : 3000
}


def withdraw(account, amount):
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
                                # Assuming 'c' represents the amount to be withdrawn from extBalance,
                                # you need to assign it a value before using it.
                                # For example, if 'c' should be the difference between the requested amount and the main balance:
                                c = amount - account['balance']  
                                if amount == account['balance'] + c :
                                        account['extBalance'] = account['extBalance'] - c
                                        account['balance'] = 0       
                                print(f"You can take {amount} $")
                                print(f"Remaining normal account balance: {account['balance']}.\nAdditional account balance: {account['extBalance']}$.")
                                

                               
                        elif wantingExtBalance == 'n':
                                print(f"There is {account['balance']} in your account number({account['accountNo']}).\nThe request is denied.")

                        else: 
                                print('pls just enter "y" or "n" ')
                
                else:
                        print(f'You do not have ${amount} in your total account.')
        print('*** '* 10 + '\n')


def balanceInquiry(account):
        print(f"Account number: {account['accountNo']} have ${account['balance']} and additional account have: ${account['extBalance']}")
        print('** '* 10 + '\n')



balanceInquiry(account_A)
withdraw(account_A, 2000)
withdraw(account_A, 200)