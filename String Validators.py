def word (x):
    Bool_1 = []
    Bool_2 = []
    Bool_3 = []
    Bool_4 = []
    Bool_5 = []
    l_word = list(x)
    for i in l_word:
        if i.isalnum() == True:
            Bool_1.append(1)
        else:
            Bool_1.append(0)
        
        if i.isalpha() == True:
            Bool_2.append(1)
        else:
            Bool_2.append(0)

        if i.isdigit() == True:
            Bool_3.append(1)
        else:
            Bool_3.append(0)

        if i.islower() == True:
            Bool_4.append(1)
        else:
            Bool_4.append(0)

        if i.isupper() == True:
            Bool_5.append(1)
        else:
            Bool_5.append(0)
    
    if sum(Bool_1) >= 1:
        print("True")
    else:
        print("False")
    if sum(Bool_2) >= 1:
        print("True")
    else:
        print("False")
    if sum(Bool_3) >= 1:
        print("True")
    else:
        print("False")
    if sum(Bool_4) >= 1:
        print("True")
    else:
        print("False")
    if sum(Bool_5) >= 1:
        print("True")
    else:
        print("False")

word(input())