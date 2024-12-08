card_num, target = map(int,input().split())
card_list = list(map(int,input().split()))
result = 0

for i in range(card_num):
    for j in range(i+1,card_num):
        for k in range(j+1,card_num):
            sum_of_card = card_list[i] + card_list[j] + card_list[k]
            if sum_of_card <= target and sum_of_card > result:
                result = sum_of_card
        
print(result)