#!/usr/bin/python3
# -*- coding:utf-8 -*-

#Pour utiliser par défaut le corpus brown
from nltk.corpus import brown

class NltkBigrams :
	'''Classe contenant des attributs et méthodes permettant de combiner les éléments présents dans les phrases du corpus deux à deux
	Attributs :
		| bigrams : liste des bigrammes dans le corpus (par défaut brown des data de NLTK)
		| bigrams_and_tags : liste de pairs bigrammes dans le corpus, concaténation des tags des deux tokens
		| bigrams_sents : liste de phrases du corpus (corpus.sents()) où deux tokens sont concaténés
		| tagged_sents_bigram : bigrams_sents dotés de tag pour chaque token, ou concaténation de tags pour les bigrammes 
	
	'''
	
	def __init__(self, corpus = brown, construct = True) :
		'''Constructeur de la classe
		En entrée:
		| corpus : corpus du même type que les corpus NLTK (brown de nltk.corpus par défaut)
		| construct : construction de tout les attributs de la classe si vrai (Vraie est la valeurs par défaut)
		'''
		
		#Définition des attributs
		self.bigrams = []
		self.bigram_and_tags = []
		self.bigram_sents = []
		self.tagged_sents_bigram = []
		
		if(construct):
			#Construction de la liste bigrams
			self.build_bigrams()
			#Construction de la liste bigram_and_tags
			self.build_bigram_and_tags()
			#Construction de la liste bigram_sents
			self.build_bigram_sents()
			#Construction de la liste tagged_sents_bigram
			self.build_tagged_sents_bigram()
			
	def build_bigrams(self,corpus = brown) :
		'''
		Méthode de construction de l'attribut bigrams qui est une liste des paire de mots du corpus
		En entrée :
		| corpus : objet corpus (possédant une méthode sents() qui renvoie la liste des mots du corpus) utliisé pour la construction (par défaut brown de nltk.corpus)
		'''
		
		print('Construction de bigrams')
		
		#Parcours des phrases (Pour ne pas relier des mots en fin de phrase avec les premiers mots des phrases suivantes)
		for sent in corpus.sents(categories = 'science_fiction'): #Pour test sur machine non puissante categories = 'science_fiction'
			#Liaison des mots deux à deux
			tmp_bigram = [sent[i]+'_'+sent[i+1] for i in range(0,len(sent)-1)]
			#Ajout des nouveaux bigrams dans la liste de tous les bigrams
			[self.bigrams.append(bigram) for bigram in tmp_bigram]
		
		
	def build_bigram_and_tags(self,corpus = brown) :
		'''
		Méthode de construction de l'attribut bigram_and_tags qui est une liste des paire de mots du corpus
		En entrée :
		| corpus : objet corpus (possédant une méthode tagged_sents() renvoyant une liste de paires mots/tag) utliisé pour la construction (par défaut brown de nltk.corpus)
		'''
		
		print('Construction de bigram_and_tags')
		#Parcours des phrases de la même manière que pour les bigrams sans tag
		for tagged_sent in corpus.tagged_sents(categories = 'science_fiction',tagset = 'universal'): #Si corpus de nltk, il vaut mieux stipler le tagset = 'universal'
			tmp_bigram_and_tags = [(tagged_sent[i][0]+'_'+tagged_sent[i+1][0],tagged_sent[i][1]+tagged_sent[i+1][1]) for i in range(0,len(tagged_sent)-1)]
			[self.bigram_and_tags.append(bigramtag) for bigramtag in tmp_bigram_and_tags]
			 
		
	def build_bigram_sents(self,corpus = brown) :
		'''
		Méthode de construction de l'attribut bigram_sents qui est une liste des paire de mots du corpus
		En entrée :
		| corpus : objet corpus (possédant une méthode sents() qui renvoie la liste des phrase du corpus) utliisé pour la construction (par défaut brown de nltk.corpus)
		'''
		
		print('Consturction de bigram_sents')
		#Parcours des phrases du corpus
		for sent in corpus.sents(categories = 'science_fiction'):
			#Pour chacune des phrases n-1 phrases sont générée
			#Chacune des nouvelles phrase contien un bigramme dans les deux éléments sont reliés par un '_' et le reste inchangé du corpus
			for i in range(0, len(sent) -1) :
				new_sent = []
				j = 0
				#Génération de la phrase
				while(j < len(sent)):
					if(j==i):
						new_sent.append(sent[j]+'_'+sent[j+1])
						j = j+2
					else :
						new_sent.append(sent[j])
						j = j+1
				
				#Ajout de la phrase au nouveau corpus		
				self.bigram_sents.append(new_sent)
		
		
	def build_tagged_sents_bigram(self,corpus = brown) :
		'''
		Méthode de construction de l'attribut tagged_sents_bigram qui est une liste des paire de mots du corpus
		En entrée :
		| corpus : objet corpus (possédant une méthode ) utliisé pour la construction (par défaut brown de nltk.corpus)
		'''
		
		print('Construction de tagged_sents_bigram')
		#Parcours des phrases tagguées du corpus
		for tagged_sent in corpus.tagged_sents(categories = 'science_fiction',tagset = 'universal'):
			#Pour chacune des phrases n-1 phrases sont générée
			#Chacune des nouvelles phrase contien un bigramme dans les deux éléments sont reliés par un '_' et leurs tags concaténés, et le reste inchangé du corpus
			for i in range(0, len(tagged_sent) -1) :
				new_tagged_sent = []
				j = 0
				#Génération de la phrase
				while(j < len(tagged_sent)):
					if(j==i):
						new_tagged_sent.append((tagged_sent[j][0]+'_'+tagged_sent[j+1][0],tagged_sent[j][1]+tagged_sent[j+1][1]))
						j = j+2
					else :
						new_tagged_sent.append(tagged_sent[j])
						j = j+1
				
				#Ajout de la phrase au nouveau corpus		
				self.tagged_sents_bigram.append(new_tagged_sent)
		
		
