#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Jeu Yoshi Labyrinthe
Jeu dans lequel on doit déplacer Yoshi jusqu'à ses oeufs à travers un labyrinthe comprtant différents niveaux de difficultés.

Script Python
Fichiers : yoshi_labyrinthe.py, classes.py, functions.py, constantes.py
"""

import os.path
import time
import pygame
from pygame.locals import *

from constantes import *
from classes import *
from functions import *

pygame.init()
pygame.font.init()

#On définit la police que l'on shouaite utiliser
police_defaut = pygame.font.SysFont('Comic Sans MS', 30)
police_petit = pygame.font.SysFont('Comic Sans MS', 12)

#Icone
icone = pygame.image.load(IMAGE_ICONE)
pygame.display.set_icon(icone)

#Titre
pygame.display.set_caption(TITRE_FENETRE)

#Limitation de vitesse des boucles d'evenements
pygame.time.Clock().tick(30)

continuer = 1
numero_niveau = 0

#BOUCLE PRINCIPALE
while continuer:

	#Ouverture de la fenêtre Pygame
	largeur_fenetre = LARGEUR_ACCUEIL
	hauteur_fenetre = HAUTEUR_ACCUEIL + HAUTEUR_BANDEAU
	fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

	#Chargement et affichage de l'écran d'accueil
	accueil = pygame.image.load(IMAGE_ACCUEIL).convert_alpha()
	fenetre.blit(accueil, (0,0))

	#Rafraichissement
	pygame.display.flip()

	#On remet ces variables à 1 à chaque tour de boucle
	continuer_accueil = 1

	#On remet ces variables à 0 à chaque tour de boucle
	continuer_jeu = 0
	continuer_scores = 0
	# touche_pressee = 0

	if numero_niveau != 0:
		continuer_accueil = 0
		continuer_jeu = 1

	#BOUCLE D'ACCUEIL
	while continuer_accueil:
	
		for event in pygame.event.get():
		
			#Si l'utilisateur quitte, on met les variables 
			#de boucle à 0 pour n'en parcourir aucune et fermer
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				continuer_accueil = 0
				continuer_jeu = 0
				continuer = 0
				#Variable de choix du niveau
				numero_niveau = 0

			elif event.type == KEYDOWN:
				#Lancement du niveau 1
				if event.key == K_1:
					continuer_accueil = 0 #On quitte l'accueil
					numero_niveau = 1 #On définit le niveau à charger
				#Lancement du niveau 2
				elif event.key == K_2:
					continuer_accueil = 0
					numero_niveau = 2
				#Lancement du niveau 3
				elif event.key == K_3:
					continuer_accueil = 0
					numero_niveau = 3
				#Lancement du niveau 4
				elif event.key == K_4:
					continuer_accueil = 0
					numero_niveau = 4
				#Affichage des meilleurs scores
				elif event.key == K_0:
					continuer_accueil = 0
					continuer_scores = 1


	if continuer_scores:
		afficher_meilleurs_scores(fenetre)

		while continuer_scores:

			for event in pygame.event.get():
		
				if event.type == QUIT:
					continuer_scores = 0
					continuer = 0
			
				elif event.type == KEYDOWN and event.key == K_ESCAPE:
					continuer_scores = 0
		

	#on vérifie que le joueur a bien fait un choix de niveau
	#pour ne pas charger s'il quitte
	if numero_niveau != 0:

		continuer_jeu = 1

		largeur_fenetre = NOMBRE_SPRITE[numero_niveau-1] * TAILLE_SPRITE
		hauteur_fenetre = NOMBRE_SPRITE[numero_niveau-1] * TAILLE_SPRITE + HAUTEUR_BANDEAU

		#Redimension de la fenetre en fonction du niveau
		fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
		#Chargement du fond
		fond = pygame.image.load(IMAGE_FOND).convert_alpha()
		#Chargement du bandeau : LEFT, TOP, WIDTH, HEIGHT
		bandeau = Rect(0, 0, largeur_fenetre, HAUTEUR_BANDEAU)
		
		#Génération d'un niveau à partir d'un fichier
		niveau = Niveau(numero_niveau)
		niveau.generer()
		niveau.afficher(fenetre)

		#Création du timer
		compteur = 0
		#Toutes les secondes on ajoute un event de type USEREVENT à la liste des évenements
		pygame.time.set_timer(USEREVENT, 1000)

		#Création de Yoshi
		yoshi = Perso("images/yoshi_droite.png", "images/yoshi_gauche.png", 
		"images/yoshi_haut.png", "images/yoshi_bas.png", niveau)
		
		rafraichir_fenetre(fenetre, fond, bandeau, niveau, yoshi, compteur)

		#BOUCLE DE JEU
		while continuer_jeu:

			for event in pygame.event.get():
			
				#Si l'utilisateur quitte, on met la variable qui continue le jeu
				#ET la variable générale à 0 pour fermer la fenêtre
				if event.type == QUIT:
					numero_niveau = 0
					continuer_jeu = 0
					continuer = 0
			
				elif event.type == KEYDOWN:
					#Si l'utilisateur presse Echap ici, on revient seulement au menu
					if event.key == K_ESCAPE:
						numero_niveau = 0
						continuer_jeu = 0
						
					#Touches de déplacement de Yoshi
					elif event.key == K_RIGHT:
						yoshi.deplacer('droite')
						rafraichir_jeu(fenetre, fond, niveau, yoshi)
					elif event.key == K_LEFT:
						yoshi.deplacer('gauche')
						rafraichir_jeu(fenetre, fond, niveau, yoshi)
					elif event.key == K_UP:
						yoshi.deplacer('haut')
						rafraichir_jeu(fenetre, fond, niveau, yoshi)
					elif event.key == K_DOWN:
						yoshi.deplacer('bas')
						rafraichir_jeu(fenetre, fond, niveau, yoshi)


					#Code pour gérer le long appuie sur une touche de déplacement

					# elif event.key == K_RIGHT:
					# 	touche_pressee = 1
					# 	while touche_pressee:
					# 		yoshi.deplacer('droite')
					# 		rafraichir_jeu(fenetre, fond, niveau, yoshi)
					# 		pygame.time.wait(200)
					# 		for event in pygame.event.get():
					# 			if event.type == KEYUP:
					# 				touche_pressee = 0
					# elif event.key == K_LEFT:
					# 	touche_pressee = 1
					# 	while touche_pressee:
					# 		yoshi.deplacer('gauche')
					# 		rafraichir_jeu(fenetre, fond, niveau, yoshi)
					# 		pygame.time.wait(200)
					# 		for event in pygame.event.get():
					# 			if event.type == KEYUP:
					# 				touche_pressee = 0
					# elif event.key == K_UP:
					# 	touche_pressee = 1
					# 	while touche_pressee:
					# 		yoshi.deplacer('haut')
					# 		rafraichir_jeu(fenetre, fond, niveau, yoshi)
					# 		pygame.time.wait(200)
					# 		for event in pygame.event.get():
					# 			if event.type == KEYUP:
					# 				touche_pressee = 0
					# elif event.key == K_DOWN:
					# 	touche_pressee = 1
					# 	while touche_pressee:
					# 		yoshi.deplacer('bas')
					# 		rafraichir_jeu(fenetre, fond, niveau, yoshi)
					# 		pygame.time.wait(200)
					# 		for event in pygame.event.get():
					# 			if event.type == KEYUP:
					# 				touche_pressee = 0

				elif event.type == USEREVENT:
					#On incrémente le compteur de temps et on l'affiche
					compteur += 1
					rafraichir_bandeau(fenetre, bandeau, niveau, compteur)


			#Victoire -> Niveau suivant ou retour à l'accueil si dernier niveau
			if niveau.structure[yoshi.case_y][yoshi.case_x] == 'a':

				score_ajoute = 0
				taille_espace = 50
				scores = []
				nouveaux_scores = []

				#On sélectionne le fichier de score correspondant au niveau
				fichier_score = FOLDER_SCORES + "/n%d" % numero_niveau

				#On affiche le texte de victoire
				texte_felicitation = police_defaut.render("Félicitation !", True, (0, 0, 0))
				fenetre.blit(texte_felicitation, (largeur_fenetre / 2 - texte_felicitation.get_rect().width / 2, hauteur_fenetre / 2 - texte_felicitation.get_rect().height / 2))
				pygame.display.flip()

				#Si le fichier des scores correspondant au niveau actuel n'existe pas on créera le fichier en écrivant dedans juste après
				if os.path.isfile(fichier_score):
					#On lit les scores déjà présents dans le fichier correspondant au niveau actuel
					with open(fichier_score, "r") as fichier:
						for ligne in fichier:
							scores.append(ligne)
				
				#On regarde si le score actuel est inférieur à un des meilleurs score du niveau
				for score in scores:
					#Si le score est inférieur on l'ajoute à la place de l'ancien
					if compteur < int(score.split(':')[1]) and score_ajoute == 0:
						score_ajoute = 1
						nouveaux_scores.append(demander_prenom(fenetre, compteur) + ":%d" % compteur)
					#On ajoute aussi l'ancien si on a pas encore 4 scores dans le fichier			
					if len(nouveaux_scores) < 4:
						nouveaux_scores.append(score)

				#Si le score est inférieur a aucun meilleurs scores mais qu'il n'y a pas 4 scores dans le fichier, on l'ajoute tout de même
				if len(nouveaux_scores) < 4 and score_ajoute == 0:
					score_ajoute = 1
					nouveaux_scores.append(demander_prenom(fenetre, compteur) + ":%d" % compteur)

				#On écrit dans le tableau les nouveaux meilleurs scores du niveau
				fichier = open(fichier_score, "w")
				for i in range(0, len(nouveaux_scores)):
					if i == 0:
						fichier.write(nouveaux_scores[i].rstrip())
					else:
						fichier.write("\n" + nouveaux_scores[i].rstrip())
				fichier.close()

				#Si le score du joueur a été ajouté on augmente la taille de l'espace entre les textes
				if score_ajoute:
					taille_espace = 150
				
				#On affiche le texte pour continuer en fonction du niveau
				if (numero_niveau != 4):
					numero_niveau += 1
					texte_continuer = police_petit.render("(Appuyer sur Entrée pour continuer)", True, (0, 0, 0))
				else:
					numero_niveau = 0
					texte_continuer = police_petit.render("(Appuyer sur Entrée pour revenir à l'accueil)", True, (0, 0, 0))
				
				fenetre.blit(texte_continuer, (largeur_fenetre / 2 - texte_continuer.get_rect().width / 2, hauteur_fenetre / 2 - texte_continuer.get_rect().height / 2 + taille_espace))
				pygame.display.flip()

				while continuer_jeu:
					for event in pygame.event.get():
						if event.type == QUIT:
							numero_niveau = 0
							continuer_jeu = 0
							continuer = 0
						
						elif event.type == KEYDOWN:
							#Si l'utilisateur presse Echap ici, on revient seulement au menu
							if event.key == K_ESCAPE:
								numero_niveau = 0
								continuer_jeu = 0
							elif event.key == K_RETURN:
								continuer_jeu = 0
