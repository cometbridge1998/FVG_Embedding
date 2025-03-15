# -*- coding: utf-8 -*-

import math
import io

import pandas as pd



SVC_NN = pd.read_csv(io.StringIO('''
Abrede
Aussicht
Dienst
Frage
Rechnung
Zusammenhang
Anklage
Arrest
Beobachtung
Beweis
Kontrolle
Schutz
Strafe
Gebote
Abstimmung
Auswahl
Debatte
Diskussion
Entscheidung
Erörterung
Rede
Verfügung
Verhandlung
Wahl
'''), header=None, names=["NN"])

colnames = ["Ranking", "NN", "Total", "Expected", "Observed", "Documents"]
collocations = pd.read_csv('resources/collocations/stellen_TAZ/collocation_list.txt', sep="\t", names=colnames, header=None)

NNs = SVC_NN.NN.to_list()

collocations["SVC"] = collocations["NN"].isin(NNs)

collocations["MI"] = collocations.apply(lambda x: math.log2( x["Observed"] / x["Expected"]), axis=1)

SVCs = collocations[collocations["SVC"] == True][["NN", "Ranking", "Expected", "Observed", "MI"]].reset_index(drop=True)
SVCs = SVCs.round(2)
SVCs.to_csv("SVCs_in_Collocations.tsv", sep="\t", index=False)

High_MI = ["Weichen", "Antrag", "Fragen", "Stufe", "Anzeige"]
Other_High_MI = collocations[collocations["NN"].isin(High_MI)].sort_values(by=["MI"], ascending=False)[["NN", "Ranking", "Expected", "Observed", "MI"]]
Other_High_MI = Other_High_MI.reset_index(drop=True).round(2)
Other_High_MI.to_csv("Non_SVCs.tsv", sep="\t", index=False)

