def rem_left_recursion(gram):
    found = False
    found_at=[]
    for i in range(lines):
        c=gram[i][0]
        if gram[i][3]==c:
            found = True
            found_at.append(i)
        elif '|' in gram[i]:
            j=0
            while j < len(gram[i]):
                if '|' == gram[i][j]:
                    if gram[i][j+1]==c:         #Look at the terminal after |
                        found = True
                        found_at.append(i)
                j+=1
        else:
            pass

    if found:
        recursion_at = [x+1 for x in found_at]
        print(f"\nLeft Recursion found at rule {recursion_at}.\n")
        check=False             #To continue looking for terminal before the next |
        cont = False            #check for rule with recursion and cont for rule without recursion
        for i in found_at:
            original = []
            new = []
            c=gram[i][0]
            index=3
            while index < len(gram[i]):
                if (gram[i][index] == c or check) and gram[i][index+1]!='|' and gram[i][index+1] != '$':    #for rules A->Aα
                    check=True
                    new.append(gram[i][index+1])
                elif gram[i][index]!= '|' and (gram[i][index-1] == '|' or gram[i][index-1] == '>' or cont) and gram[i][index] != '$':  #for rules A->ß 
                    cont = True
                    original.append(gram[i][index])
                else:
                    check = False
                    cont = False
                    if len(new)>0 and new[-1]!= '|':
                        new.append('|')
                    if len(original)>0 and original[-1]!= '|':
                        original.append(c)
                        original.append('*')
                        original.append('|')
                index+=1
            
            if len(original)>0:
                original.pop()
            else:
                original.append(c)
                original.append('*')

            new.append('ε')
            original = ''.join(original)
            new = ''.join(new)

            rule = gram[i][:-1]
            print(f"The production rule {rule} will be decomposed as {c}->{original} and {c}*->{new}")
    else:
        print("Left recursion not found.")


if __name__=="__main__":
    grammar=[]
    lines = int(input("Enter the number of rules in production: "))
    print("Enter the production:")
    for i in range(lines):
        try:
            line = input()
        except EOFError:
            break
        line = line + '$'
        grammar.append(line)
    
    rem_left_recursion(grammar)

    