#Algrími sem tekur input frá notenda sem segir til um lengd runu

#runan tekur seinustu 3 stök og leggur þau saman.

#Þarf fjórar breytur
#fyrsta stak fyrir fyrstu tölu 
#annað stak fyrir aðra töluna
#þriðja stak fyrir þriðju töluna
#fjórða stak fyrir summu allra talnanna

#Runan keyrir þangað til að input notendans er náð

n = int(input("Enter the length of the sequence: ")) # Do not change this line
num_one = 0
num_two = 0
num_three = 1
sum_num = 0

for i in range(0, n):
    num_one = num_two
    num_two = num_three
    num_three = sum_num
    sum_num = num_one + num_two + num_three
    print(sum_num)
