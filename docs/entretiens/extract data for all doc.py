import json
import os
import re
import unicodedata
directory = r"E:\2023\NER\Medical speciality\docs\entretiens"
for filename in os.listdir(directory):
    try:
        if filename.endswith(".txt"):  # Vérifiez que le fichier est un fichier texte
            with open(filename, 'r', encoding='utf8') as f:
                # print(filename)
                lines = f.readlines()
                for i in range(len(lines)):
                    nom = re.search("^nom.*", lines[i].lower())
                    if nom is not None:
                        candidat = {
                            "nom": nom.group(0).strip()[12:].translate({ord(i): None for i in ':!?'})
                        }
                    fonction = re.search("^fonction ", lines[i].lower().strip())
                    diplome = re.search("master", lines[i].lower())
                    # visionnaire = re.search("^quelles sont selon vous.*?$", lines[i].lower())
                    visionnaire = re.search("^.*visionnaire.*?$", lines[i].lower())
                    Altruiste = re.search("^altruiste", lines[i].lower())
                    Introspection = re.search("^.*introspection.:", lines[i].lower())
                    Creatif = re.search("^.*créatif.:", lines[i].lower())
                    if fonction is not None:
                        candidat["fonction"] = fonction.group(0).rstrip(':')[9:].translate(
                            {ord(i): None for i in ':!?'})
                        if diplome is None:
                            candidat["diplome"] = unicodedata.normalize('NFKD', lines[i+2].strip())
                    if diplome is not None:
                        candidat["diplome"] = unicodedata.normalize('NFKD', lines[i].strip())



                    if visionnaire is not None:
                        # if (lines[i + 2].lower()).find("visionnaire") != -1 or (lines[i + 2].lower()).find("oui") != -1:
                        if (lines[i ].lower()).find("visionnaire") != -1 or (lines[i].lower()).find("oui") != -1 or (lines[i].lower()).find("Beaucoup") != -1 :
                            candidat["Qualité"] = []
                            candidat["Qualité"].append({"Visionnaire": "oui"})
                        else:
                            candidat["Qualité"] = []
                            candidat["Qualité"].append(
                                {"Visionnaire": unicodedata.normalize('NFKD', lines[i + 2].strip())})
                    if Altruiste is not None:
                        if (lines[i].lower()).find("un peu") != -1 or (lines[i].lower()).find("oui") != -1:
                            candidat["Qualité"].append({"Altruiste": "oui"})
                        else:
                            candidat["Qualité"].append({"Altruiste": unicodedata.normalize('NFKD', lines[i].strip())})
                    if Introspection is not None:
                        if (lines[i].lower()).find("un peu") != -1 or (lines[i].lower()).find("oui") != -1 or (
                                lines[i].lower()).find("beaucoup") != -1:
                            candidat["Qualité"].append({"Introspection": "oui"})
                        else:
                            # candidat["Qualité"].append({"Introspection":unicodedata.normalize('NFKD',  lines[i].strip())})
                            candidat["Qualité"].append(
                                {"Introspection": unicodedata.normalize('NFKD', lines[i].strip())})
                    if Creatif is not None:
                        if (lines[i].lower()).find("un peu") != -1 or (lines[i].lower()).find("oui") != -1 or (
                        lines[i].lower()).find("innovant") != -1:
                            candidat["Qualité"].append({"Créatif": "oui"})
                        else:
                            # candidat["Qualité"].append({"Introspection":unicodedata.normalize('NFKD',  lines[i].strip())})
                            candidat["Qualité"].append({"Créatif": unicodedata.normalize('NFKD', lines[i].strip())})
            with open(filename + '.json', 'w', encoding='utf8') as json_file:
                json.dump(candidat, json_file, ensure_ascii=False)

            # Convert the dictionary to a JSON string
    except:
        pass


# print(candidat)
