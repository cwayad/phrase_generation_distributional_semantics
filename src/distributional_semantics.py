#!/usr/bin/python3
# -*- coding:utf-8 -*-

#Pour tout ce qui est calcul matriciel on importe numpy
import numpy as np
import scipy as sp

class DistributionalSemantics :
	'''Classe contenant les méthodes statiques de Semantique Distributionnelle		
	'''
	
	@staticmethod
	def composition_w(tagged_sents,tagged_sents_p,Lw,Lp,relation):
		'''Méthode de calcul de Wr de composition
		En entrée :
		| tagged_sents : liste de listes de paire mot/tag du corpus d'ou vient Lw 
		| tagged_sents_p : liste de listes contenant des phrases/tag d'ou vient Lp
		| Lw : dictionnaire à clé de mots et valeurs vecteurs de sens des mots
		| Lp : dictionnaire à clé phrases et valeurs vecteurs de sens des phrases
		| relation : relation syntaxique r de Wr sous la forme de chaine de caractères
		En sortie :
		| W : matrice de composition pour la relation syntaxique "relation" selon les lexicons
		'''
		
		#Déclaration des matrices des vecteurs des sens des mots composant de la relation 
		U = []
		V = []
		#Déclaration de la matrices des vecteurs de sens des phrases ayant pour tag la relation
		P = [] 
		
		#Recherche des vecteurs de sens représentant les éléments sattisfaisant la relation "relation" :
		#Parcours de toutes les phrases du corpus
		for tagged_sent in tagged_sents:
			#Parcours des mots du corpus à la recherches des bons tags
			for i in range(0, len(tagged_sent)-1):
				if(tagged_sent[i][1]+tagged_sent[i+1][1] == relation):
					U.append(Lw[tagged_sent[i][0]])
					V.append(Lw[tagged_sent[i+1][0]])
		
		#Recherche des vecteurs de sens représentant les phrases ou la relation syntaxique entre les mots est "relation"
		#Parcours de toutes les phrases dans le corpus des phrases/tag
		for tagged_sent in tagged_sents_p :
			#Parcours de tous les mots de la phrase pour voir si il y en a un qui a comme tag "relation"
			for i in range(0,len(tagged_sent)):
				if(tagged_sent[i][1] == relation):
					P.append(Lp[tagged_sent[i][0]])
						
		#Transformation des matrices U,V et P en matrices numpy
		u = np.matrix(U)
		v = np.matrix(V)
		p = np.matrix(P)
		#Concaténation des matrices u et v
		uv = np.hstack((u,v))
		
		#Résolution du problème des moindres carrés (Least square)
		W, residus, rang, s = np.linalg.lstsq(uv,p)
		
		#Retourner la valeur de la matrice de composition de la relation "relation" 
		return W
	
	@staticmethod
	def decomposition_w(tagged_sents,tagged_sents_p,Lp,Lw,relation):
		'''Méthode de calcul de W'r de décomposition
		En entrée :
		| tagged_sents : liste de listes de paire mot/tag du corpus d'ou vient Lw 
		| tagged_sents_p : liste de listes contenant des phrases/tag d'ou vient Lp
		| Lp : dictionnaire à clé phrases et valeurs vecteurs de sens des phrases
		| Lw : dictionnaire à clé de mots et valeurs vecteurs de sens des mots
		| relation : relation syntaxique r de Wr sous la forme de chaine de caractères
		En sortie :
		| W : matrice de décomposition pour la relation syntaxique "relation" selon les lexicons
		'''
		
		#Déclaration des matrices des vecteurs des sens des mots composant de la relation 
		U = []
		V = []
		#Déclaration de la matrices des vecteurs de sens des phrases ayant pour tag la relation
		P = [] 
		
		#Recherche des vecteurs de sens représentant les éléments sattisfaisant la relation "relation" :
		#Parcours de toutes les phrases du corpus
		for tagged_sent in tagged_sents:
			#Parcours des mots du corpus à la recherches des bons tags
			for i in range(0, len(tagged_sent)-1):
				if(tagged_sent[i][1]+tagged_sent[i+1][1] == relation):
					U.append(Lw[tagged_sent[i][0]])
					V.append(Lw[tagged_sent[i+1][0]])
		
		#Recherche des vecteurs de sens représentant les phrases ou la relation syntaxique entre les mots est "relation"
		#Parcours de toutes les phrases dans le corpus des phrases/tag
		for tagged_sent in tagged_sents_p :
			#Parcours de tous les mots de la phrase pour voir si il y en a un qui a comme tag "relation"
			for i in range(0,len(tagged_sent)):
				if(tagged_sent[i][1] == relation):
					P.append(Lp[tagged_sent[i][0]])
						
		#Transformation des matrices U,V et P en matrices numpy
		u = np.matrix(U)
		v = np.matrix(V)
		p = np.matrix(P)
		#Concaténation des matrices u et v
		uv = np.hstack((u,v))
		
		#Résolution du problème des moindres carrés (Least square)
		W, residus, rang, s = np.linalg.lstsq(p,uv)
		
		#Retourner la valeur de la matrice de décomposition de la relation "relation" 
		return W
	
	@staticmethod
	def decomposition_from_composition_w(tagged_sents,Lw,w,relation):
		'''Méthode de calcul de l'inverse d'une composition pour obtenir une matrice de décomposition
		En entrée :
		| tagged_sents : liste de listes de paire mot/tag du corpus d'ou vient Lw 
		| Lw : dictionnaire à clé de mots et valeurs vecteurs de sens des mots
		| w : Matrice de composition pour la relation "relation"
		| relation : relation syntaxique r de Wr sous la forme de chaine de caractères
		En sortie :
		| W : matrice de décomposition pour la relation syntaxique "relation" selon la matrice de comoposition "w"
		'''
		
		#Déclaration des matrices des vecteurs des sens des mots composant de la relation 
		U = []
		V = []
		
		#Recherche des vecteurs de sens représentant les éléments sattisfaisant la relation "relation" :
		#Parcours de toutes les phrases du corpus
		for tagged_sent in tagged_sents:
			#Parcours des mots du corpus à la recherches des bons tags
			for i in range(0, len(tagged_sent)-1):
				if(tagged_sent[i][1]+tagged_sent[i+1][1] == relation):
					U.append(Lw[tagged_sent[i][0]])
					V.append(Lw[tagged_sent[i+1][0]])
		
		#Transformation des matrices U et V en matrices numpy
		u = np.matrix(U)
		v = np.matrix(V)
		#Concaténation des matrices u et v
		uv = np.hstack((u,v))
		
		#Résolution du problème des moindres carrés (Least square)
		W, residusr, rangr, sr = np.linalg.lstsq(np.dot(uv,w),uv)
		
		#Retourner la valeur de la matrice de décomposition de la relation "relation" 
		return W
		
	@staticmethod
	def compose(u,v,w):
		'''Méthode permettant de combiner deux vecteurs de sens pour obtenir un vecteur de sens combiné
		En entrée :
		| u : premier vecteur de sens
		| v : second vecteur de sens
		| w : matrice de composition pour la relation syntaxique entre les deux vecteurs de sens
		En sortie :
		| p : vecteur de sens combiné
		'''
		
		#La composition n'est qu'un produit matriciel
		p = np.dot(np.hstack((u,v)),w)
		return p
		
	@staticmethod
	def decompose(p,w,dim):
		'''Méthode permettant d'obtenir deux vecteurs de sens à partir d'un seul vecteur de sens
		En entrée :
		| p : vecteur de sens à décomposer
		| w : matrice de décomposition pour la relation des composant du vecteur p
		| dim : dimention des vecteurs de sens
		En sortie :
		| u : premier vecteur de sens composant p
		| v : second vecteur de sens composant p
		'''
		
		#La décomposition n'est qu'un produit factoriel également
		uv = np.dot(p,w)
		UV = np.array(uv)[0]
		#séparation des vecteurs de sens u et v selon la dimenstion des vecteurs de sens
		u = UV[0:dim]
		v = UV[dim-1:-1]
		
		#retourner les deux vecteurs de sens
		return u,v
		
	@staticmethod
	def nearest_n(Lw,v):
		'''Méthode permettant de retrouver le mot le plus proche dans le lexique selon le vecteur de sens
		En entrée :
		| Lw : model Word2Vect contenant le lexique des mots, dictionnaire ou les clés sont des mots et les valeurs sont des vecteurs 
		| v : vecteur de sens à approximé
		En sortie :
		| mot : chaine de caractère représentant le mot le plus proche dans le lexique
		'''
		
		#Initialisation de la distance maximum à la disantce entre un élément du lexique et le vecteur
		mot = list(Lw.vocab.keys())[0]
		dist_min = sp.spatial.distance.euclidean(Lw[mot],v)
		
		#Parcours du vocabulaire
		for word in Lw.vocab.keys() :
			tmp_dist = sp.spatial.distance.euclidean(Lw[word],v)
			if(tmp_dist < dist_min):
				dist_min = tmp_dist
				mot = word
		
		#Renvoyer le mot le plus proche dans le lexique
		return mot
	
