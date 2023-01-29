kerdes1:str = str(input('Mondj egy számot(1 és 8 között): '))
print({kerdes1})
if kerdes1 not in {1, 4, 5, 8}:
    print('''
    Választható színek:
    -kék
    -zöld
    -rózsasín
    -sárga
    ''')
    kerdes2:str = str(input('Melyik színt választod? '))
    
    
    kek:str = 'Szép vagy'
    if kerdes2 == kek: 
        print(f'Akkor az az üzeneted az hogy: {kek}')

    zold:str = 'Legyen csodaszép napod!'
    if kerdes2 == zold: 
        print(f'Akkor az az üzeneted az hogy: {zold}')

    rozsaszin:str = 'Nincs egy kis csokid? \nÁh mindegy téged látva már nem kell édesség olyan édes vagy ;)'    
    if kerdes2 == rozsaszin: 
        print(f'Akkor az az üzeneted az hogy: {rozsaszin}')

        
    else:
        sarga:str = 'Ne félj mindjárt hétvége ;)'
        print(f'Akkor az az üzeneted az hogy: {sarga}')
        

else:
    print('''
    Választható színek:
    -piros
    -fehér
    -lila
    -narancs
    ''')
    kerdes3:str = str(input('Melyik színt választod? '))
    piros:str = 'A holdig meg vissza ;)'
    feher:str = 'Jó a szetted'
    lila:str = 'Valakinek most is hiányzol. \nIgaz nem nekem de valakinek biztos :))'
    narancs:str = 'A barátaidra mindig számíthatsz! \nHa mégse nem igazi barátok!!'
    if kerdes3 == piros:
        print(f'Akkor az üzeneted: {piros}')
    if kerdes3 == feher:
        print(f'Akkor az üzeneted: {feher}')
    if kerdes3 == lila:
        print(f'Akkor az üzeneted: {lila}')
    else:
        print(f'Akkor az üzeneted: {narancs}')

#kys

