
CihatAcount = {
        "name": "Cihat Aksakal",
        "AcountNum" : "12345",
        "balance": 3000,
        "add_balance": 2000,
}
JacopAcount = {
        "name": "Jacop Mod",
        "AcountNum" : "12346",
        "balance": 5000,
        "add_balance": 3000
}
def MoneyWihdraw(acount, wantmoney ):
    print(f"welcome {acount['name']} ")
    if acount['balance'] >= wantmoney :
        acount['balance'] -= wantmoney
        print("you can get your money")
    else: 
        totalbalance = acount['balance']+  acount['add_balance']
        if totalbalance >= wantmoney: 
            add_balance_use =input("Use additional account? (y=yes) (n=no) ")
            if add_balance_use== 'y': 
                    add_balance_used = wantmoney - acount['balance']
                    acount['balance'] = 0
                    acount['add_balance'] -= add_balance_used
                    print("you can get your money")
            else: 
                 print(f"{acount['AcountNum']} your balance  {totalbalance} ")
        else: 
            print("you have insufficient balance")

MoneyWihdraw(CihatAcount, 3000)
MoneyWihdraw(CihatAcount, 2000)