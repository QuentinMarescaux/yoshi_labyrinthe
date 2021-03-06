"""Fonctions utiles du jeu de Labyrinthe Yoshi"""

import random
import os.path
import pygame
from pygame.locals import *
from pygame.draw import *
from pygame.font import *

from constantes import *


def rafraichir_bandeau(fenetre, bandeau, niveau, compteur):
	police_defaut = pygame.font.SysFont('Comic Sans MS', 30)
	largeur_fenetre = fenetre.get_size()[0]

	rect(fenetre, Color(255, 255, 255), bandeau, 0)
	fenetre.blit(police_defaut.render("Niveau %d" % niveau.numero, True, (255,0,0)), (20, 0))
	fenetre.blit(police_defaut.render("%d" % compteur, True, (255,0,0)), (largeur_fenetre-50, 0))

	pygame.display.flip()


def rafraichir_jeu(fenetre, fond, niveau, yoshi):
	#Affichage de yoshi à sa nouvelle position
	fenetre.blit(fond, (0, HAUTEUR_BANDEAU))
	niveau.afficher(fenetre)
	fenetre.blit(yoshi.direction, (yoshi.x, yoshi.y + HAUTEUR_BANDEAU))

	pygame.display.flip()


def rafraichir_fenetre(fenetre, fond, bandeau, niveau, yoshi, compteur):
	rafraichir_bandeau(fenetre, bandeau, niveau, compteur)
	rafraichir_jeu(fenetre, fond, niveau, yoshi)


def afficher_meilleurs_scores(fenetre):
	police_defaut = pygame.font.SysFont('Comic Sans MS', 30)
	police_petit = pygame.font.SysFont('Comic Sans MS', 20)
	largeur_fenetre = fenetre.get_size()[0]
	hauteur_fenetre = fenetre.get_size()[1]

	# LEFT, TOP, WIDTH, HEIGHT
	scores_n1 = Rect(0, 0, largeur_fenetre / 2, hauteur_fenetre / 2)
	scores_n2 = Rect(largeur_fenetre / 2, 0, largeur_fenetre / 2, hauteur_fenetre / 2)
	scores_n3 = Rect(0, hauteur_fenetre / 2, largeur_fenetre / 2, hauteur_fenetre / 2)
	scores_n4 = Rect(largeur_fenetre / 2, hauteur_fenetre / 2, largeur_fenetre / 2, hauteur_fenetre / 2)

	texte_n1 = police_defaut.render("Niveau 1", True, (0, 0, 0))
	texte_n2 = police_defaut.render("Niveau 2", True, (0, 0, 0))
	texte_n3 = police_defaut.render("Niveau 3", True, (0, 0, 0))
	texte_n4 = police_defaut.render("Niveau 4", True, (0, 0, 0))

	rect(fenetre, Color(255, 0, 0), scores_n1, 0)
	rect(fenetre, Color(0, 255, 0), scores_n2, 0)
	rect(fenetre, Color(0, 0, 255), scores_n3, 0)
	rect(fenetre, Color(255, 255, 255), scores_n4, 0)

	fenetre.blit(texte_n1, (scores_n1.width / 2 - texte_n1.get_rect().width / 2, 0))
	fenetre.blit(texte_n2, (largeur_fenetre / 2 + scores_n2.width / 2 - texte_n2.get_rect().width / 2, 0))
	fenetre.blit(texte_n3, (scores_n3.width / 2 - texte_n3.get_rect().width / 2, hauteur_fenetre / 2))
	fenetre.blit(texte_n4, (largeur_fenetre / 2 + scores_n4.width / 2 - texte_n4.get_rect().width / 2, hauteur_fenetre / 2))

	fichier_score = FOLDER_SCORES + "/n1"
	if os.path.isfile(fichier_score):
		hauteur = 60
		with open(fichier_score, "r") as fichier:
			for ligne in fichier:
				texte = police_petit.render(ligne.rstrip(), True, (0, 0, 0))
				fenetre.blit(texte, (scores_n1.width / 2 - texte.get_rect().width / 2, hauteur))
				hauteur += 40

	fichier_score = FOLDER_SCORES + "/n2"
	if os.path.isfile(fichier_score):
		hauteur = 60
		with open(fichier_score, "r") as fichier:
			for ligne in fichier:
				texte = police_petit.render(ligne.rstrip(), True, (0, 0, 0))
				fenetre.blit(texte, (largeur_fenetre / 2 + scores_n2.width / 2 - texte.get_rect().width / 2, hauteur))
				hauteur += 40

	fichier_score = FOLDER_SCORES + "/n3"
	if os.path.isfile(fichier_score):
		hauteur = 60
		with open(fichier_score, "r") as fichier:
			for ligne in fichier:
				texte = police_petit.render(ligne.rstrip(), True, (0, 0, 0))
				fenetre.blit(texte, (scores_n3.width / 2 - texte.get_rect().width / 2, hauteur_fenetre / 2 + hauteur))
				hauteur += 40

	fichier_score = FOLDER_SCORES + "/n4"
	if os.path.isfile(fichier_score):
		hauteur = 60
		with open(fichier_score, "r") as fichier:
			for ligne in fichier:
				texte = police_petit.render(ligne.rstrip(), True, (0, 0, 0))
				fenetre.blit(texte, (largeur_fenetre / 2 + scores_n4.width / 2 - texte.get_rect().width / 2, hauteur_fenetre / 2 + hauteur))
				hauteur += 40

	pygame.display.flip()


def debug_liste(liste, texte=""):
	if texte == "":
		texte == "Liste :"

	print(texte)

	for element in liste:
		print (element)