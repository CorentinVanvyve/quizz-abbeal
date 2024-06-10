name = input("Tape ton prénom: ")
print("\n")
print("Bonjour " + name + ". Bienvenue dans le jeu que j'ai codé spêcialement pour les membres de Abbeal.\nCe jeu a pour but de tester tes connaisances sur l'entreprise mais aussi sur moi-même, si tu réussis, tu auras la chance d'obtenir une récompense.")
print("\n")
print("Maintenant, à toi de jouer!")
print("\n")

def question(sentence, answer):
  print(sentence)
  user_answer = input("Réponse : ")

  while user_answer != answer:
    print("Mauvaise réponse! Réessaye.\n")
    print(sentence)
    user_answer = input("Réponse : ")
  print("\n")
  print('Bien joué, continuons.')
  print("\n")


question("Dans combien de pays différent Abbeal est présent ?\n", '3')
question("Laquelle de ces technos back end n'est pas utilisée chez Abbeal (Tape juste le nombre): \n1. Java\n2. Python\n3. Ruby\n", '3')
question("Quelle est l'année de création du premier bureau Abbeal ?", '2015')
question("Maintenant, parlons un peu de moi, ou plutôt de mes origines. Laquelle de ces bières n'est pas belge (Tape juste le nombre): \n1. La chouffe\n2. Heineken\n3. Grimbergen\n", '2')
question("Lequel de ces faits me concernant est faux (Tape juste le nombre) :\n1. Je me suis fait braquer par des sicarios mexicains à Guadalajara\n2. J'ai servi une biere au Roi des belges lors de la fête nationale\n3. J'ai partagé une pizza avec le fils du président mexicain", '2')

print("\n")
print("Maintenant que tu as réussis le test, tu as droit à ta récompense. Tu peux aller la chercher à la reception de l'espace CoWork.")

