def luckBalance(k, contests):
    n = len(contests)
    not_imp_sum = 0
    imp_luck = []
    for contest in contests:
        if contest[1]==0:
            not_imp_sum+=contest[0]
        else:
            imp_luck.append(contest[0])
    imp_luck.sort(reverse=True)
   
    imp_sum = sum(imp_luck[:min(k, len(imp_luck))])
    win_sum = sum(imp_luck[k:])
    print("win sum:",win_sum)
    return not_imp_sum+imp_sum-win_sum
