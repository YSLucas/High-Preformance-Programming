import random
import copy

def init(n, max_nmr, min_nmr):
    """
    Een functie om de twee arrays aan te maken die nodig zijn om de bucket sort uit te voeren.
    """
    one_dimensional = [random.randint(min_nmr, max_nmr) for i in range(n)]
    # two_dimensional = [ [x, [None for x in range(n-1)]] for x in range(10) ]
    two_dimensional = [ [x, []] for x in range(10) ] # maak een roster aan met 9 rijen. elke rij heeft een lijst waarin de getallen komen te staan

    return one_dimensional, two_dimensional


def sorter(to_sort, bucket, tiental, slice_at):
    """ 
    Deze functie voert de sortering uit, en geeft een lijst terug met de bewerkingen na één gathering pass
    """
    new_list = []

    for i in to_sort:
        if i < tiental:
            bucket[0][1].append(i)
        elif slice_at == 1:
            unit = int(str(i)[-1:])
            bucket[unit][1].append(i)
        else:
            unit = int(str(i)[-(slice_at):-(slice_at - 1)])
            bucket[unit][1].append(i)
    
    for x in range(0, 10):
        new_list.extend(bucket[x][1])

    return new_list
        

def bucket_sort():
    """
    
    """

    lenght_list = int(input("Geef de lengte van de lijst aan:"))
    max_nmr     = int(input("Geef de maximale grootte van de getallen aan:"))
    min_nmr     = int(input("Geef de minimale grootte van de getallen aan:"))
    
    to_sort, bucket = init(lenght_list, max_nmr, min_nmr)

    print(f"De random gegenereerde lijst is: {to_sort}. \nDe lijst wordt nu gesorteerd..")

    clean_bucket = copy.deepcopy(bucket)    # creeer een deepcopy van een lege bucket om te hergebruiken
    tiental = 1                             # geeft aan of het algoritme bij een tiental, honderdtal etc. is
    slice_at = 1                            # variabele om de juiste cijfer in een getal aan te wijzen bij het sorteren
    max_tiental = len(str(max(to_sort)))    # om ervoor te zorgen dat er tot en met het grootste getal wordt gesorteerd

    for i in range(0, max_tiental):
        bucket = copy.deepcopy(clean_bucket)                    # maak de bucket schoon
        to_sort = sorter(to_sort, bucket, tiental, slice_at)   
        

        tiental *= 10   # na elke gathering pass ga je naar de volgende tiental. 10 -> 100 -> 1000
        slice_at += 1   # na elke gathering pass verschuift de focus één cijfer naar links. 
    
    print(f"De lijst is succesvol gesorteerd! Dit is het resultaat: {to_sort}")

bucket_sort()