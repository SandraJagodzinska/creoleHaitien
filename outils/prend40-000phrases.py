n = 1
nom = 1000
with open("../SUD_all_treebanks_utilities/treebanks/SUD_French-GSD/fr_gsd-sud-train.conllu", 'r', encoding="utf-8") as main :
    fichier = "fr_gsd-sud-train{}.conllu".format(nom)
    while True:
        text = main.readline()
        if text != "" or text =="\n":
            d = text.split(" ")
            if len(d) > 2:
                if d[1] == "sent_id" and n<=1000:
                    f=open(fichier, 'a')
                    f.write(text)
                    f.close()
                    n+=1
                elif d[1] == "sent_id" and n>1000:
                    n = 1
                    nom+=1000
                    fichier = "fr_gsd-sud-train{}.conllu".format(nom)
                    f=open(fichier, 'a')
                    f.write("# global.columns = ID FORM LEMMA UPOS XPOS FEATS HEAD DEPREL DEPS MISC \n")
                    f.write(text)
                    f.close()
                    n+=1
                else :
                    f=open(fichier, 'a')
                    f.write(text)
                    f.close()
            else :
                f=open(fichier, 'a')
                f.write(text)
                f.close()
        else:
            print("toto")
            f.close()
            break
            False
    f.close()