scores = [('Mike', 10), ('Mike', 8), ('Mike', 6), ('John', 7), ('John', 8), ('John', 5), ('John', 8), ('Tom', 8), ('Tom', 9)]
total_dict_scores = {}

for i in scores:
    
    name,score = i
    
    if(name in total_dict_scores):
        total_dict_scores[name] += score
    else:
        total_dict_scores[name] = score

print(total_dict_scores)