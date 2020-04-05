# from random import random
# from random import choice

def rules(p1, p2):
	sum1=0
	sum2=0
	dict={'Rock':'Scissor', 
		  'Paper':'Rock', 
		  'Scissor':'Paper'}

	for i in range(len(p1)):
		if p1[i]==p2[i]:
			continue
		if dict[p1[i]]==p2[i]:
			sum1+=1
		else:
			sum2+=1
	if sum1>sum2:
		return "Player1"
	elif sum1<sum2:
		return "Player2"
	else:
		return "None. It's a Draw."



def compare(player1, palyer2):
	result= rules(player1,  player2)
	return result


# list= ['Rock', 'Paper', 'Scissor']
# player1= choice(list)
# print("Player1", player1)
# player2= choice(list)
player1= ['Rock', 'Paper', 'Scissor']
player2= ['Scissor', 'Paper', 'Paper']

# print("Player2 ",player2)
win=compare(player1, player2)
print '\nWinning player is ' + win
