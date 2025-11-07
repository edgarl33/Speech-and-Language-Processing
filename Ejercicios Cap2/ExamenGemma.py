import spacy
from collections import Counter
import matplotlib.pyplot as plt
from itertools import islice

nlp = spacy.load("es_core_news_sm")


texto = """Las hadas, por lo general, son criaturas bellas, dulces, amables y llenas de amor. Pero hubo una vez un hada que no eran tan hermosa. La verdad, es que era horrible, tanto, que parecía una bruja.

El Hada Fea vivía en un bosque encantado en el que todo era perfecto, tan perfecto que ella no encajaba en el paisaje, por eso se fue a vivir apartada en una cueva del rincón más alejado del bosque. Allí cuidaba de los animalitos que vivían con ella, y disfrutaba de la compañía de los niños que la visitaban para escuchar sus cuentos y canciones. Todos la admiraban por su paciencia, la belleza de su voz y la dedicación que prestaba a todo lo que hacía. Para los niños no era importante en absoluto su aspecto.

- Hada, ¿por qué vives apartada? -le preguntaban los niños.
-Porque así vivo más tranquila -contestaba ella.

No quería contarles que en realidad era porque el resto de las hadas la rechazaban por su aspecto.

Un día llegó una visita muy especial al bosque encantado. Era la reina suprema de todas las hadas del universo: el Hada Reina. La cual estaba visitando todos los reinos, países, bosques y parajes donde vivían sus súbditos para comprobar que realmente cumplían su misión: llevar la belleza y la paz allá donde estuvieran.

Para comprobar que todo estaba en orden, el Hada Reina lanzaba un hechizo muy peculiar, que ideaba en función de lo que observaba en cada lugar.

-Ilustrísima Majestad-dijo el Hada Gobernadora de aquel bosque encantado-. Podéis ver que nuestro bosque encantado es un lugar perfecto donde reina la belleza y la armonía.
-Veo que así parece -dijo el Hada Reina-. Veamos a ver si es verdad. Yo conjuro este lugar para que en él reinen los colores más hermosos si lo que decís es verdad, o para que desaparezca el color si realmente hay algo feo aquí.

Pero en ese momento, el bosque encantado empezó a quedarse sin colores, y todo se volvió gris.

-Parece que no es verdad lo que me decís -dijo el Hada Reina-. Tendréis que buscar el motivo de que vuestro hogar haya perdido el color. Cuando lo hagáis, este bosque encantado recuperará todo su brillo y esplendor. Sólo cuando la auténtica belleza viva entre vosotras este lugar volverá a ser perfecto.

Tras la visita del Hada Reina se reunieron urgentemente todas las hadas del consejo del bosque encantado.
-Esto es cosa del Hada Fea -dijo una de las hadas del consejo-. Ella es la culpable.
-Vayamos a buscarla -dijo el Hada Gobernadora del bosque -. Hay que expulsarla de aquí."""
doc = nlp(texto)

tokens = [token.text for token in doc]
#print(tokens)

lemas = [token.lemma_ for token in doc]
#print(lemas)

#for token in doc:
#    print(f"{token.text} {token.pos_} {token.lemma_}")


tokens_sin_stop = [token for token in doc if not token.is_stop and not token.is_punct]
#print([t.text for t in tokens_sin_stop])

sustantivos = [token.lemma_ for token in doc if token.pos_ == "NOUN" and not token.is_stop]
adjetivos   = [token.lemma_ for token in doc if token.pos_ == "ADJ" and not token.is_stop]
verbos      = [token.lemma_ for token in doc if token.pos_ == "VERB" and not token.is_stop]

print("Sustantivos:", sustantivos)
print("Adjetivos:", adjetivos)
print("Verbos:", verbos)


tokens_limpios = [
    token.lemma_.lower()
    for token in doc
    if not token.is_stop and not token.is_punct
]


print(tokens_limpios)


frecuencias = Counter(tokens_limpios)
print(frecuencias)

palabras, conteos = zip(*frecuencias.most_common(10))


plt.figure(figsize=(8,5))
plt.bar(palabras, conteos)
plt.title("Frecuencia de palabras en el texto")
plt.xlabel("Palabras")
plt.ylabel("Frecuencia")
plt.xticks(rotation=45)
plt.show()

num_tokens = len(tokens_limpios)         
num_types = len(set(tokens_limpios))    

print(f"Tokens (total de palabras): {num_tokens}")
print(f"Types (palabras únicas): {num_types}")

def ngrams(lista, n):
    return list(zip(*[islice(lista, i, None) for i in range(n)]))

bigramas = ngrams(tokens_limpios, 2)
trigramas = ngrams(tokens_limpios, 3)

print("\nBigrams:")
for b in bigramas:
    print(b)

print("\nTrigrams:")
for t in trigramas:
    print(t)

#Cuantos sustantivos diferentes hay. 
#Menos 60 lineas
#Que la gráfica sea bopnitca
