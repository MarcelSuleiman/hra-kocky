#!/usr/bin/env python3

# hra kocky

import random

class Player:
	def __init__(self, name: str):
		self.name = name
		self.money = 100
		self.rank = 0
		self.status = 0

	def __str__(self):
		return self.name

class Game:
	def __init__(self, players:list = None):
		self.players = players or []
		#self.playable_players = None

	def create_players(self):
		name = input('Zadaj meno hráča: ')
		player = Player(name)
		self.players.append(player)

	def replace_dice_in_dices(self, number:int):
		self.roll[self.royal_dice] = number

	def evaluate(self, number:int) -> str:
		if self.royal_dice == 0:
			if number > self.roll[1] and number < self.roll[2]:
				return 'win'
			else:
				return 'loose'
		if self.royal_dice == 1:
			if number > self.roll[0] and number < self.roll[2]:
				return 'win'
			else:
				return 'loose'
		if self.royal_dice == 2:
			if number > self.roll[0] and number < self.roll[1]:
				return 'win'
			else:
				return 'loose'

	def select_a_dice(self):
		while True:
			try:
				choice = int(input('Vyber kocku s ktorou skúsiš štastie. (1/2/3): '))
				break
			except Exception as e:
				print('Chyba. kocka musí byť vyjadrená číslom (napr.: 2) ')

		self.royal_dice = choice-1

	def redemption(self):
		while True:
			choice = input('Nakoľko si prehral/a, máš záujem sa vykúpiť? (y/n): ')

			if choice == 'y':
				self.redemption_choice = 1
				break

			elif choice == 'n':
				self.redemption_choice = 0
				break

			else:
				print('zadaj korektnú odpoveď... "y" alebo "n"')

	def risk_or_skip(self) -> str:
		while True:
			choice = input('Chceš hrať ďalej alebo posúvaš kolo? (y/n)')
			if choice == 'y':
				return 'yes'

			elif choice == 'n':
				return 'no'

			else:
				print('Nepoznám tvoju voľbu. Zadaj správny príkaz.')

	def roll_the_dices(self):
		input(f'Hráč {player.name} hoď kockami: (enter)')
		self.roll = []
		for i in range(3):
			number = random.randint(1, 6)
			self.roll.append(number)

		self.roll.sort()
		print(self.roll)

	def roll_the_dice(self, flag=None) -> int or None:
		'''
		owerloaded method
		'''
		if flag == 'rank':
			input(f'Hráč {player.name} hoď kockou: (enter)')
		
		number = random.randint(1, 6)
		
		if flag == 'rank':
			player.rank = number

		print(f'Hodil si cislo: {number}')

		if flag == 'select':
			return number

	def chech_playable_players(self):
		self.count_playable_players = 0
		for player in self.players:
			if player.money > 0:
				self.count_playable_players += 1

	def check_player_money(self):

		self.playable_players = []

		for player in self.players:
			if player.money >= self.bet:
				print(f'{player.name}: {player.money}')
				player.status = 1
				self.playable_players.append(player)
			else:
				print(f'Hráč s menom: {player.name} sa tohto kola nezúčastní nakoľko nemá dosť financných prostriedkov pre zahájenie hry.')
				
				pass

		self.bank = self.bet * len(self.playable_players)

		for player in self.playable_players:
			player.money -= self.bet

	def set_bet(self):

		while True:
			try:
				self.bet = int(input('Zadaj sumu, o koľko sa ide hrať: '))
				break
			except Exception as e:
				print('Chyba. Suma "o koľko sa ide hrať" musí byť vyjadrená číslom, napr.: 35 alebo 25.50')


if __name__ == '__main__':

	msg = 'voľba "1" Hraj hru\nVoľba "2" pravidlá'
	print(msg)
	choice = input('Napíš svoju voľbu: ')

	if choice == '1':
		while True:
			try:
				count_of_players = int(input('Zadaj počet hráčov: '))
				break
			except Exception as e:
				print('Chyba. Počet hráčov musí byť celočíselný a vyjadrený číslom (napr.: 3) ')

		
		# Toto zakomentovat vo finalnej verzii kde si uzivatel zada pocet a mena hracov
		players = [Player('Marcel'), Player('Tomáš'), Player('Ivan')]

		game = Game(players)

		'''
		# toto odkomentovat vo finalnej verzii kde si uzivatel zada pocet a mena hracov

		for player in range(count_of_players):
			game.create_players()
		'''

		while True:
			game.chech_playable_players()
			if game.count_playable_players > 1:
				game.set_bet()
				game.check_player_money()

				for player in game.playable_players:
					game.roll_the_dice(flag='rank')

				game.playable_players.sort(key=operator.attrgetter('rank'), reverse=True)


				print('\n\nHra sa hrá v tomto poradí: ', end=' ')

				for player in game.playable_players:
					print(player, end=' ')
				print('')

				fin = 'no'
				while True:
					if fin == 'yes':
						for player in game.players:
							print(f'{player.name}: {player.money}')
						break

					for player in game.playable_players:

						if player.status != 1:
							continue

						#loose_players = []
						game.roll_the_dices()
						choice = game.risk_or_skip()
						if choice == 'yes':
							game.select_a_dice()
							
							number = game.roll_the_dice(flag='select')

							result = game.evaluate(number)

							game.replace_dice_in_dices(number)

							print(result)
							
							if result == 'win':
								
								#game.count_playable_players = 0
								
								player.money += game.bank
								fin = 'yes'
								break

							if result == 'loose':
								'''
								Vyradenemu hracovi nastavime status z defaultneho 1 (pridelene v metode check_player_money) na 0
								a preratame zoznam hracov ktori maju status 1 (stale aktivny)
								ak je zoznam aktivnych hracov rovny 1 - teda hrac uz nema proti komu hrat, stava sa vitazom.
								Aj keby sa nedostal ani raz na tah
								Peniaze z banku pripocitame poslednemu hracovi

								'''
								game.redemption()
								if game.redemption_choice == 1:
									player.status = 1
									player.money -= game.bank
									game.bank += game.bank
								elif game.redemption_choice == 0:
									player.status = 0

								online_players = 0

								for i, player in enumerate(game.playable_players):
									if player.status == 1:
										online_players += 1

								if online_players == 1:
									for i, player in enumerate(game.playable_players):
										if player.status == 1:
											player.money += game.bank
									fin = 'yes'
									break

						else:
							# move to another player
							continue

					if fin == 'yes':
						for player in game.players:
							print(f'{player.name}: {player.money}')
						
						break


					for player in game.playable_players:
						print(player.name, end=' ')

					print('')
			else:
				break

		print('Koniec hry.')


	elif choice == '2':
		msg = '''\n\n\n
			Hra 3 kocky.
			Hra pre 2 - oo hráčov.
			Ako prvé sa hráči dohodnú, o akú sumu budú hrať.
			V prvom "nultom" kole každý hráč hodí jednou kockou a podľa výsledku sa určí, v akom poradí hráči hrajú. Najvyššie číslo začína.
			Následne v poradí hádžu troma kockami naraz. Po každom hode 3 kockami sa hráč rozhodne, či chce pokračovať alebo prenechá kolo ďalšiemu hráčovi.
			Ak sa rozhodne hrať, z hodených kociek si vyberie tú, pri ktorej má najvyššiu šancu druhým hodom sa trafiť medzi rozpätie zvyšných dvoch hodených kociek.
			
			Príklad, hod troma kockami 2, 4, 6 -> hráč si vyberie kocku č.: 2 (s hodnotou 4) a ak sa mu ňou podarí hodiť číslo 3, 4 alebo 5, vyhráva. Ak by hodil 1, 2 alebo 6 - prehráva.
			
			V prípade že sa mu to podarí, vyhráva obsah banku a hra začína odznova.
			V prípade neúspechu vypadáva z hry a na rade je ďalší hráč.

			V prípade prehry sa hráč môže vykúpiť a to tým, že doloží výšku celého vkladu a tým pádom ostáva v hre.
			príklad: 3 hráči, každý vložil po 10 tj. bank = 30.
			Hráč 1 prehral ale ak má záujem, doložením 30 sa vykúpi a môže pokračovať v hre.
			'''
		print(msg.replace('			', ''))

	else:
		print('Tuto voľbu nepoznám')
