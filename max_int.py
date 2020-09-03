#leyfa notenda að slá inn jákvæðar tölur og sýna þegar notandinn slær inn neikvæða tölu hvaða tala var stærst og loka keyrslu.

#bera saman tölu sem sláð var inn við fyrrverandi tölu og sjá hvor þeirra er stærri
#ef talan er stærri en fyrrverandi tala þá skal tölunni út fyrir nýju tölunni
#annars biðja notenda um aðra tölu og ferlið heldur áfram.

num_int = int(input("Input a number: "))  # Do not change this line
#fill in the missing code
max_int = 0
while num_int >= 0:
    if(num_int > max_int):
        max_int = num_int
    num_int = int(input("Input a number: "))
print("The maximum is", max_int)


