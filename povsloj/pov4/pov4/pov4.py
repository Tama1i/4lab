k = int(input('enter meaning of k(1 - 180): '))
#pair = 1
int i=1
row = 10
rowpl = 10
while rowpl not=100:
    if k == rowpl//10 or k == rowpl%10:
        print('nomer pari: ', i)
        print('chislo obraz paroi s (k): ', rowpl)
        if k == rowpl%10: 
            print('k aya cifra: ', rowpl % 10) 
            break
        else: 
            print('k aya cifra: ', rowpl // 10) 
            break
    
    rowpl += 1
    row = row * 100 + rowpl
    #pair += 1
    
print('\n rad: ', row)