def rem_left_factoring(gram):
    found = False
    found_at=[]
    factored_keys={}
    for i in range(lines):
        first_production = gram[i].find('>') + 1
        right_side = gram[i][first_production:]
        rules=right_side.split('|')
        sorted_rules = sorted(rules)
        no = len(rules)
        n=1
        while n < no:
            if sorted_rules[n-1][0] == sorted_rules[n][0]:
                found = True
                found_at.append(i)
                index = rules.index(sorted_rules[n-1])
                factored_keys[i] = [index]
                break
            n+=1
        
        if i in found_at:
            for j in range(no):
                if rules[factored_keys[i][0]][0] == rules[j][0]:
                    factored_keys[i].append(j)
            factored_keys[i] = list(set(factored_keys[i]))

    if found:
        print(f"The left factoring occurs at rule {found_at}.")
        for i in found_at:
            first_production = gram[i].find('>') + 1
            right_side = gram[i][first_production:]
            rules=right_side.split('|')
            factors = []
            unique=[]
            different_ends=[]
            no = len(rules)

            factored_rules = [rules[j] for j in factored_keys[i]]
            shortest_rule = min(enumerate(factored_rules), key=lambda x: len(x[1]))[1]

            for j in range(len(shortest_rule),0,-1):
                y = all(x.startswith(shortest_rule[:j]) for x in factored_rules )
                if y:
                    break

                
            repeat = shortest_rule[:j]

            for rule in rules:
                if rule in factored_rules:
                    different_ends.append(rule[j:])
                    different_ends.append('|')
                else:
                    unique.append(rule)
                    unique.append('|')
                    

        
            # n=i
            # # while n<no:
            # m=1
            # while m<no:
            #     if rules[n][0] == rules[m][0]:
            #         if n not in factors:
            #             factors.append(n)
            #         if m not in factors:
            #             factors.append(m)
            #         if rules[n][0] not in repeat:
            #             repeat.append(rules[n][0])
            #     else:
            #         unique.append(rules[m])
            #         unique.append('|')
            #     m+=1
            #     # n+=1
            # handle = rules[factors[0]]
            # j=1
            # while j < no:
            #     count = 0
            #     for i in factors[1:]:
            #         if rules[i][j] == handle[j]:
            #             count +=1                    
            #     if count == len(factors)-1:
            #         repeat.append(rules[i][j])
            #     else:
            #         if j == 1:
            #             different_ends.append(handle[j:])
            #             different_ends.append('|')
            #         different_ends.append(rules[i][j:])
            #         different_ends.append('|')
            #     j+=1

            if len(different_ends)>0:
                different_ends.pop()          
            different_ends=''.join(different_ends)

            if len(unique)>0:
                unique.pop()

            unique=''.join(unique)

            terminal = gram[i].find('-')
            c=gram[i][:terminal]

            
            print(f"The production rule {gram[i]} will be decomposed as {c}->{repeat}{c}*|{unique} and {c}*->{different_ends}")
    else:
        print("No left factoring.")


if __name__=="__main__":
    grammar=[]
    lines = int(input("Enter the number of rules in production: "))
    print("Enter the production:")
    for i in range(lines):
        try:
            line = input()
        except EOFError:
            break
        
        grammar.append(line)
    
    rem_left_factoring(grammar)

    