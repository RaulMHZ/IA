#autor: Manjarrez Hernandez Raul
#carrera: Ingenieria en Sistemas Computacionales
from segment_tree import SegmentTree  
  
"""una matriz con algunos elementos
aquí estamos ajustando nuestra matriz en el árbol de segmentos donde t es
tomado como objeto del árbol de segmentos"""
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] 

#t se utilizará para realizar operaciones en ese segmento
t = SegmentTree(arr)   

#aquí estamos encontrando valor de número máximo en un rango
a = t.query(0, 10, "max")  
print("El Valor Maximo del Rango es: ", a)   
  
#aquí estamos encontrando el valor de número mínimo en un rango
a = t.query(4, 10, "min")  
print("El Valor Minimo del Rango es: ", a) 
  
#aquí estamos encontrando el valor de suma de un rango
a = t.query(0, 3, "sum")  
print("La suma del Rango es: ", a) 
  
#aquí estamos actualizando el valor de un índice particular 
t.update(2, 57)  
  
#reemplazará el valor de índice '2' con 25
print("El Arreglo Actualizado es : ", arr)  
