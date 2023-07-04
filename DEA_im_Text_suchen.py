# Gefordert: kommentiertes Python-Programm
# Sie können weitere Hilfsfunktionen verwenden!
# Namen:
#
#
#

########## HILFSFUNKTIONEN ##########

def deaDefine():  # definiert einen DEA A
    Sigma = {'0', '1'}  # Alphabet
    Z = {0, 1, 2}  # Zustandsmenge
    delta = {}  # Ueberfuehrungsfunktion
    delta[0, '0'] = 1
    delta[0, '1'] = 0
    delta[1, '0'] = 1
    delta[1, '1'] = 2
    delta[2, '0'] = 2
    delta[2, '1'] = 2
    F = {2}  # Menge der akzeptierenden Zustaende
    A = [Sigma, Z, delta, 0, F]
    return A


def deaErweiterteUEF(delta, z, w):  # erweiterte Ueberfuehrungsfunktion eines DEA
    for a in w:
        z = delta[z, a]
    return z


def deaRun(A, w):  # testet, ob der DEA A das Wort w akzeptiert
    [Sigma, Z, delta, z0, F] = A
    return deaErweiterteUEF(delta, z0, w) in F

def p_funktion(zustand, eingabezeichen, v):
    w = v[0:zustand] + eingabezeichen
    w_laenge = len(w)
    m = w_laenge + 1 # Hilfe Variable zur Prüfung ob w_laenge in der While geändert wurde
    # wir setzen "m = w_laenge + 1" um nur sicher zu sein, dass wir am Anfang in der While-schleife hereinkommen.

    # Später in der While-Schleife, falls bei dem gleichzeitigen Durchlaufen von w und dem Muster v, man bemerkt dass
    # in eine bestimmte Stelle das Symbol im v und im w nicht übereinstimmen w_laenge wird um 1 dekrementieren und das
    # hat folgende Folge:
    #  * Die Aktuelle Iteration wird abgebrochen wegen "break" denn w, v nicht übereinstimmen es ist sinnlos sie weiter zu durchlaufen
    #  * Die Bedingung "w_laenge < m" wird für die nächste Iteration als True gewertet denn wir haben bei Betreten der While "m = w_laenge" gesetzt und jetzt wir dekrementiren
    #  * Der Muster v wird dann für die nächste Iteration in eine Stelle nach rechts verschoben, dies liegt an der Tatsache, dass bei jeder Iteration wir beginnen
        # immer am Ende des Worts w wegen j = len(w) - 1, und wegen des ersten Parameters von "range" bzw "w_laenge - 1" falls w_laenge in der voherige Iteration um 1 dekre-
        # mentiert wurde, es ergibt sich eine implizite Verschiebung von dem Muster v um eine Stelle nach rechts.

    if(w_laenge > len(v)): # falls die Laenge von w größer als die von dem muster v ist, das bedeutet, dass wir schon im
        return len(v)       # Zustand len(v) sind und wir müssen dort bleiben, deswegen geben wir len(v) zurück.

    while(w_laenge != 0 and w_laenge < m):
        m = w_laenge
        j = len(w) - 1  # j wird genutzt um auf dem Wort w zu iterieren und i auf dem Muster v
        for i in range(w_laenge - 1, -1, -1):
            if(v[i] != w[j]):
                w_laenge -= 1
                break
            j -= 1
    return w_laenge

########## HAUPTFUNKTION ########## (Namen und Signatur nicht ändern!)

def createFastSearchDEA(Sigma, v):
    Z = set(range(0, len(v)+1))  # Zustandmenge
    delta = {}  # Ueberfuehrungsfunktion
    for i in Z:
        for j in Sigma: # Dank dieser beiden eingerückten for-Schleife, wir schauen für jeden Zustand in Z, alle mögliche Eingabe in Sigma
            delta[i, j] = p_funktion(i, j, v)
    F = {len(v)}
    A = [Sigma, Z, delta, 0, F]
    return A

if __name__ == '__main__':  # Hier ist ein französiches Alphabet, ihr könnt weitere Buschtabe hinzufügen wenn ihr wollt.
                            # neben dem Alphabet steht einen Satz bzw. ein Wort, und das muss der Algo suchen
                            # ganz unten steht ein Text, und in dem der Algo unseren Satz suchen muss.
                            # der Algo gibt True zurück wenn er den Satz im Text gefunden hat ansonsten false.
    A = createFastSearchDEA({'a', 'b', 'c', 'd', 'e', 'f', 'g', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '.', '-', ',', '?', '\'', '!', ':'}, "jordan gorddan je me souviens")
    print(A)
    print(deaRun(A, "oh ! le charmant tableau, la suave peinture \
                que celle ou vers saint jean, jesus, le dieu martyr, \
                tend ses deux petits bras ! a cette image pure \
                les meres dans leurs yeux sentent des pleurs venir. \
                c'est la de l'amitie la divine figure : \
                deux enfants dont les mains se cherchent pour s'unir, \
                et si prompts a s'aimer que leur double nature \
                semble se reconnaitre et se ressouvenir. \
                quand l'amour pour regner n'a que l'heure qui passe, \
                l'amitie seule dure, et pare de sa grace \
                sur un front depouille les rides du vieillard. \
                        \
                jordan gorddan je me souviens encore de toi \
                l'amour n'est ici-bas que son ombre infidele, \
                mais plus d'un pauvre coeur desabuse trop tard \
                s'y laisse prendre, helas ! tant l'ombre est encore belle."))

                            # Achtung jede Zeile im Text muss mit dem Symbol "\" beenden, es ist um Python zu sagen, dass
                            # du eine neue Zeile anfangen möchtest.
                            # Und auch alle Buschtabe, die im Text auftauchen müssen vorher oben in der Menge von Buschtabe gegeben,
                            # um unötige Fehler zu vermeiden, gleich für Sonderzeichen wie "?" und so weiter.