#autor: Manjarrez Hernandez Raul
#carrera: Ingenieria en Sistemas Computacionales
def busquedaBinaria(Lista, item):
	    primero = 0
	    ultimo = len(Lista)-1
	    encontrado = False
	
	    while primero<=ultimo and not encontrado:
	        puntoMedio = (primero + ultimo)//2
	        if Lista[puntoMedio] == item:
	            encontrado = True
	        else:
	            if item < Lista[puntoMedio]:
	                ultimo = puntoMedio-1
	            else:
	                primero = puntoMedio+1
	
	    return encontrado
	
