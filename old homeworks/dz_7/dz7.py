def read_last(lines: int, file: str):
    if lines > 0:
        with open(file, 'r') as f:
            return f.readlines()[-lines:]                     
    

def longest_words(file: str):
    res = [''] #костыль
    with open(file, encoding='utf-8') as f:
        for line in f:
            for word in line.split():
                if len(res[0]) < len(word):
                    res = [word]
                elif len(res[0]) == len(word):
                    res.append(word)
        return res

def get_basket_amount(file: str) -> int:
    with open(file, 'r') as f:
        total = 0
        for line in f:
            line = line.split()
            line[1] = int(line[1])
            line[2] = int(line[2])
            cost = line[1] * line[2]
            total += cost
        return(total)






      


        





