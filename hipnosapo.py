# -*- coding UTF-8 -*-

import random

IMAGES = ['''
         
              
              
             
               /                 :
              /                   \
           
           
           
             
               :               `.//  )      )     , ;
          
          
             
          
         
             
               
                   ''','''
         
              
              
             
               /                 :
              /                   \
           
           
           
             
               :               `.//  )      )     , ;
          
          
             
          
         
             
               
                   ''','''
         
              
              
               `,'       `---'  `.
               /                 :
              /                   \
           
           
           
              `.              (   //          `'    \
               :               `.//  )      )     , ;
          
          
             `,'\ ``--....-)='    `._,  \  ,') _ '``._
          
         
             
               
                   ''','''
         
              
              
               `,'       `---'  `.
               /                 :
              /                   \
           
           
           
              `.              (   //          `'    \
               :               `.//  )      )     , ;
             ,-|`.            _,'/       )    ) ,' ,'
            (  :`.`-..____..=:.-':     .     _,' ,'
             `,'\ ``--....-)='    `._,  \  ,') _ '``._
          _.-/ _ `.       (_)      /     )' ; / \ \`-.'
         
             
               
                   ''','''
               ,'``.._   ,'``.
              
              
               `,'       `---'  `.
               /                 :
              /                   \
           
           
           
              `.              (   //          `'    \
               :               `.//  )      )     , ;
             ,-|`.            _,'/       )    ) ,' ,'
            (  :`.`-..____..=:.-':     .     _,' ,'
             `,'\ ``--....-)='    `._,  \  ,') _ '``._
          _.-/ _ `.       (_)      /     )' ; / \ \`-.'
         `--(   `-:`.     `' ___..'  _,-'   |/   `.)
             `-. `.`.``-----``--,  .'
               |/`.\`'        ,','); 
                   `         (/  (/''','''
               ,'``.._   ,'``.
              
              
               `,'       `---'  `.
               /                 :
              /                   \
            ,'                     :\.___,-.
           `...,---'``````-..._    |:       \
             (                 )   ;:    )   \  _,-.
              `.              (   //          `'    \
               :               `.//  )      )     , ;
             ,-|`.            _,'/       )    ) ,' ,'
            (  :`.`-..____..=:.-':     .     _,' ,'
             `,'\ ``--....-)='    `._,  \  ,') _ '``._
          _.-/ _ `.       (_)      /     )' ; / \ \`-.'
         `--(   `-:`.     `' ___..'  _,-'   |/   `.)
             `-. `.`.``-----``--,  .'
               |/`.\`'        ,','); 
                   `         (/  (/''','''
               ,'``.._   ,'``.
              :,--._:)\,:,._,.:
              :`--,''   :`...';\      ¡Hipnosapo te ha atrapado!
               `,'       `---'  `.
               /                 :
              /                   \
            ,'                     :\.___,-.
           `...,---'``````-..._    |:       \
             (                 )   ;:    )   \  _,-.
              `.              (   //          `'    \
               :               `.//  )      )     , ;
             ,-|`.            _,'/       )    ) ,' ,'
            (  :`.`-..____..=:.-':     .     _,' ,'
             `,'\ ``--....-)='    `._,  \  ,') _ '``._
          _.-/ _ `.       (_)      /     )' ; / \ \`-.'
         `--(   `-:`.     `' ___..'  _,-'   |/   `.)
             `-. `.`.``-----``--,  .'
               |/`.\`'        ,','); 
                   `         (/  (/''']

WORDS = [
		'Leela',
		'Bender',
		'Fry',
		'Hermes',
		'Zoidberg',
		'Farnsworth',
		'Zapp',
		'Kif',
		'Amy',
		'Scruffy',
		]

def random_word():
	idx = random.randint(0, len(WORDS) - 1)
	return WORDS[idx]

def display_board(hidden_word, tries):
	print(IMAGES[tries])
	print('')
	print(hidden_word)
	print('########## ########## ########## ########## ########## ')

def run():
	word = random_word()
	hidden_word = ['-'] * len(word)
	tries = 0

	while True:
		display_board(hidden_word, tries)
		current_letter = str(input('Selecciona una letra: '))

		letter_indexes = []

		for i in range(len(word)):
			if word[i] == current_letter:
				letter_indexes.append(i)

		if len(letter_indexes) == 0:
			tries += 1

			if tries == 6:
				display_board(hidden_word, tries)
				print('')
				print('¡Perdiste! La palabra correcta es: {}'.format(word))
				break
		else:
			for i in letter_indexes:
				hidden_word[i] = current_letter

			letter_indexes = []

		try:
			hidden_word.index('-')
		except ValueError:
			display_board(hidden_word, tries)
			print('¡Ganaste! :D')
			break

if __name__ == '__main__':
	print('----------- B I E N V E N I D O S  A  F U T U R A M A  G A M E ----------- \n')
	print('¡Adivina el personaje de Futurama antes de que aparezca el Hipnosapo!')
	run()