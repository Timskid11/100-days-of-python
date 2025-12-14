def calculate_love_score(name1 ,name2):
    total_name = (name1 + name2).lower()
    print(total_name)
    t = total_name.count("t")
    r = total_name.count("r")
    u = total_name.count("u")
    e = total_name.count("e")
    sum_for_true = t + r + u + e
    
    l = total_name.count("l")
    o = total_name.count("o")
    v = total_name.count("v")
    e = total_name.count("e")
    sum_for_love = l + o + v + e
    
    score = str(sum_for_true)+str(sum_for_love)
    print(score)

calculate_love_score("Angela Yu" , "Jack Bauer")
