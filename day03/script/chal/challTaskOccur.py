mots = ["Cat", "Mice", "Garden"]
count = 0
texte = "thE Cat’s tactic wAS tO surpRISE thE mIce iN tHE gArdeN, nedrag"
texte_lower = texte.lower()

for mot in mots :
    mot_lower = mot.lower()
    count+= texte_lower.count(mot_lower)
    print(mot_lower)
    mot_reversed = mot_lower[::-1]
    count+= texte_lower.count(mot_reversed)


print(count)