import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

#Chargement des données
df = pd.read_csv("/Users/edaarcn/Documents/airbnb-barcelona-price-analysis/data/listings.csv")

#print("Shape :", df.shape) #pour avoir les dimensions de la dataset : (19410, 18)
#print("\nColonnes :")
#print(df.columns.tolist()) #nom des colonnes
#print(df.head())
#print("Valeurs manquantes price :", df["price"].isna().sum()) #Valeurs manquantes price : 4134
"""Colonnes : ['id', 'name', 'host_id', 'host_name', 
'neighbourhood_group', 'neighbourhood', 'latitude', 
'longitude', 'room_type', 'price', 'minimum_nights', 
'number_of_reviews', 'last_review', 'reviews_per_month', 
'calculated_host_listings_count', 'availability_365', 
'number_of_reviews_ltm', 'license']"""

#Nettoyage des données 
df = df.dropna(subset=["price"]) #supprime les lignes où les valeurs sont NaN dans les colonnes spécifiées
#print("Shape après :", df.shape) #Shape après : (15276, 18)

#print(df["price"].describe())
"""count    15276.000000
mean       187.312713 > distribution asymétrique des données à droite, donc logements très chers
std        363.967170 > écart-type
min          9.000000
25%         70.000000
50%        131.000000 > médiane
75%        215.000000
max      10000.000000"""

q95 = df["price"].quantile(0.95)
#print("95e percentile :", q95) #425 euros

df = df[df["price"] <= q95] 
#print("Nouvelle shape :", df.shape) #Nouvelle shape : (14513, 18)
#Les 5% des prix les plus élevés ont été exclus afin d'éviter que des valeurs extrêmes biaisent l'analyse.

#print(df["price"].describe())
"""count    14513.000000
mean       142.282092
std         90.651967
min          9.000000
25%         68.000000
50%        123.000000
75%        200.000000
max        425.000000"""

#Analyse 
#1. Le type de logement influence-t-il le prix ?

moyenne1 = df.groupby("room_type")["price"].mean() 
median1 = df.groupby("room_type")["price"].median() 
#on a regroupé les lignes par type de logement et on veut la moyenne du prix de chaque groupe
#print("Moyenne :\n", moyenne1)
#print("\nMedian :\n", median1)
"""Moyenne :                            Median : 
 room_type
Entire home/apt    171.651016           162.0 > différence faible, distribution stable
Hotel room         208.595745           200.0 > pareil que entire home/apt
Private room        80.476243           62.0  > moyenne bien au-dessus de médiane => quelques chambres privées plus chères
Shared room         58.196078           43.0  > pareil que private room  """

#Le type de logement influence le prix.
#Ordre du plus cher au moins cher : Hotel room, Entire home/apt, Private room, Shared room
#Médiane = montre le prix "typique" > 50% coûte + ou - cher que médiane

"""plt.figure(figsize=(8,5))

sns.boxplot(x="room_type", y="price", data=df)

plt.title("Distribution des prix par type de logement")
plt.xlabel("Type de logement")
plt.ylabel("Prix (€)")
plt.xticks(rotation=45)

plt.show()"""
#Interprétation : 
"""Les hôtels et logements entiers présentent les prix médians les plus élevés.
Les chambres privées et partagées sont significativement moins chères.
Les logements entiers affichent également une plus grande dispersion des prix, 
traduisant une hétérogénéité importante de l’offre (du petit budget au très haut de gamme).
A l'inverse, les hôtels ont une distribution plus resserrée,
suggérant un positionnement tarifaire plus standardisé. 

Insights :
Entire home/apt > Médiane élevée > Dispersion très large
=> Marché très hétérogène (studio vs villa luxe) 
=> donc le prix seul ne suffit pas : analyser quartier, nb avis, disponibilité, etc.
Hotel room > Médiane élevée > Dispersion plus maîtrisée
=> Pricing plus standardisé (grille tarifaire, suivent la concurrence)
Private room > Médiane basse > Beaucoup d’outliers
=> Segment majoritairement low budget mais présence d’offres premium
Shared room > Le moins cher > Distribution resserrée
=> Segment clairement économique"""

"""README :
L’analyse met en évidence une segmentation claire du marché.
Les hôtels et les logements entiers présentent les prix médians les plus élevés.
Toutefois, les logements entiers affichent une dispersion beaucoup plus importante, 
traduisant une forte hétérogénéité de l’offre (du studio économique au logement haut de gamme).
À l’inverse, les hôtels présentent une distribution plus resserrée, suggérant un positionnement 
tarifaire plus standardisé.
Les chambres privées et partagées constituent les segments les plus abordables, 
bien que certaines chambres privées se positionnent sur un segment premium."""

#2. Quels sont les quartiers les + ou - chers ? 
#print(df.groupby("neighbourhood_group")["price"].median().sort_values(ascending=False))
#médian car les prix restent asymétriques, la médiane représente mieux le "prix typique"
"""
Eixample               165.0
Les Corts              146.0
Gràcia                 135.0
Sant Martí             135.0
Sarrià-Sant Gervasi    130.0
Sants-Montjuïc         112.0
Ciutat Vella            89.0 > centre historique mais peu cher, pourquoi ? Peut-être plus de chambres privées, à vérifier.
Sant Andreu             78.0
Horta-Guinardó          74.0
Nou Barris              64.0
La localisation influence fortement le prix."""
#print(df.groupby("neighbourhood_group")["room_type"].value_counts())
"""
Ciutat Vella         Entire home/apt    2120
                     Private room       1192
                     Hotel room            5
                     Shared room           4
Eixample             Entire home/apt    3513
                     Private room       1450
                     Shared room          52
                     Hotel room           29
Gràcia               Entire home/apt     931
                     Private room        354
                     Shared room          12
                     Hotel room            6
Horta-Guinardó       Entire home/apt     223
                     Private room        174
Les Corts            Entire home/apt     226
                     Private room         79
                     Shared room           2
Nou Barris           Private room         99
                     Entire home/apt      85
Sant Andreu          Entire home/apt     117
                     Private room        106
                     Shared room           2
Sant Martí           Entire home/apt    1000
                     Private room        357
                     Shared room          16
                     Hotel room            3
Sants-Montjuïc       Entire home/apt     976
                     Private room        450
                     Shared room           7
                     Hotel room            4
Sarrià-Sant Gervasi  Entire home/apt     606
                     Private room        306
                     Shared room           7"""
#Analyse du prix par quartier ET type de logement 
"""print(
    df.groupby(["neighbourhood_group", "room_type"])["price"]
      .median()
)"""
"""
Ciutat Vella         Entire home/apt    100.5
                     Hotel room         243.0
                     Private room        73.0
                     Shared room         63.0
Eixample             Entire home/apt    198.0
                     Hotel room         181.0
                     Private room        63.5
                     Shared room         46.0
Gràcia               Entire home/apt    163.0
                     Hotel room         203.5
                     Private room        55.5
                     Shared room         39.5
Horta-Guinardó       Entire home/apt    124.0
                     Private room        45.0
Les Corts            Entire home/apt    161.0
                     Private room        59.0
                     Shared room         53.5
Nou Barris           Entire home/apt    174.0
                     Private room        45.0
Sant Andreu          Entire home/apt    101.0
                     Private room        54.5
                     Shared room         53.5
Sant Martí           Entire home/apt    161.0
                     Hotel room         312.0
                     Private room        62.0
                     Shared room         43.0
Sants-Montjuïc       Entire home/apt    152.0
                     Hotel room         176.5
                     Private room        55.0
                     Shared room         42.0
Sarrià-Sant Gervasi  Entire home/apt    150.5
                     Private room        51.0
                     Shared room         22.0"""
"""Eixample domine sur le segment Entire home/apt (198€ médiane).
C’est un positionnement clairement premium.
Ciutat Vella, malgré son attractivité touristique,
semble proposer des logements entiers plus abordables.
Plusieurs hypothèses :
Logements plus petits (centre historique > surfaces réduites)
Concurrence élevée > pression sur les prix
Offre très dense > guerre des prix
À type de logement équivalent, des écarts importants subsistent entre 
quartiers, suggérant que d’autres facteurs non observés (surface, 
standing, qualité du bien) influencent le prix.
La localisation influence fortement le prix des logements Airbnb à Barcelone, avec des écarts médians importants entre quartiers.
Toutefois, certains quartiers centraux comme Ciutat Vella affichent des prix médians inférieurs à des zones comme Eixample, suggérant que la centralité seule n’explique pas les différences observées.
Même à type de logement équivalent, des écarts significatifs persistent entre quartiers, indiquant que d’autres facteurs non observés — tels que la surface, le standing ou la qualité du bien — jouent probablement un rôle déterminant."""

#3. Le nombre d'avis influence-t-il le prix ? 
#print(df["number_of_reviews"].describe())
"""
count    14513.000000
mean        61.766279
std        120.613000
min          0.000000
25%          1.000000
50%          9.000000
75%         69.000000
max       1820.000000
La distribution du nombre d’avis est fortement asymétrique : la majorité des logements ont moins de 10 avis, 
tandis qu’une minorité concentre un volume très élevé d’avis.
"""

"""plt.scatter(df["number_of_reviews"], df["price"]) #seaborn pour les visuels plus poussés
plt.xscale("log")
plt.title("Prix vs Nombre d'avis")
plt.xlabel("Nombre d'avis")
plt.ylabel("Prix (€)")
plt.show()"""

print((df["number_of_reviews"] == 0).sum())

print(df.groupby(df["number_of_reviews"] == 0)["price"].median())
#False    140.0 et True      91.0
"""Les logements sans avis affichent un prix médian significativement inférieur (91€) à ceux disposant d’au moins un avis (140€), suggérant une stratégie 
de prix plus agressive pour attirer les premières réservations.
Les avis semblent refléter davantage l’ancienneté ou la stratégie d’entrée que le positionnement premium."""