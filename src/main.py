#!/usr/bin/python3
# -*- coding:utf-8 -*-

#Projet de Sciences des données
#Master 2 IA "Machine Learning for Data Science"

#Import de toutes les méthodes de la classe DistributionalSemantics et de la classe NltkBigrams
from distributional_semantics import DistributionalSemantics as ds
from nltk_bigrams import NltkBigrams as nb
import gensim
from nltk.corpus import brown

#Test des méthodes
#Construction du corpus de bigrammes
corpus_bigrams = nb()

#Entrainement des models gensim
print('Création des vecteurs de sens des mots')
unigram_model = gensim.models.Word2Vec(brown.sents(),min_count = 1,size = 100)
print('Création des vecteurs de sens des bigrammes')
bigram_model = gensim.models.Word2Vec(corpus_bigrams.bigram_sents,min_count = 1,size = 100)

#Calcul de la matrice de composition pour la relation ADJNOUN
W = ds.composition_w(brown.tagged_sents(categories = 'science_fiction', tagset = 'universal'), corpus_bigrams.tagged_sents_bigram, unigram_model, bigram_model, "ADJNOUN")

#Calcul de la matrice de décomposition pour l'étiquette de phrases ADJNOUN
W2 = ds.decomposition_w(brown.tagged_sents(categories = 'science_fiction', tagset = 'universal'), corpus_bigrams.tagged_sents_bigram,bigram_model,unigram_model,"ADJNOUN")

#Calcul de la matrice de décomposition pour l'étiquette de phrases ADJNOUN selon la composition effectuée précédemment
W3 = ds.decomposition_from_composition_w(brown.tagged_sents(categories = 'science_fiction', tagset = 'universal'),unigram_model,W,"ADJNOUN")

#Calcul de composition de vecteurs de sens de "new" et "ones"
P = ds.compose(unigram_model["new"],unigram_model["ones"],W)

#Calcul de décomposition du vecteur P selon W2
u1 , v1 = ds.decompose(P,W2,100)
print(ds.nearest_n(unigram_model,u1))
print(ds.nearest_n(unigram_model,v1))

#Calcul de décomposition du vecteur P selon W3
u2 , v2 = ds.decompose(P,W3,100)
print(ds.nearest_n(unigram_model,u2))
print(ds.nearest_n(unigram_model,v2))

#Malheureusement les résultats ne sont pas satisfiant car les corpus pris pour les entrainement sont beaucoup trop petits (Et cela semble évident)

