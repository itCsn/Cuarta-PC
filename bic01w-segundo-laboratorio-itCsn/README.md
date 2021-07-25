# BIC01: Segundo Laboratorio

## Primera Parte

Implemente un programa que realize lo siguiente:

1.  Solicite al usuario el costo total de una vivienda a adquirir.
2.  Solicite al usuario el ingreso de su salario anual.
3.  Solicite al usuario el ingreso del porcentaje del salario que ahorrará mensualmente.
4.  Muestre en consola el **número de meses que le tomará al usuario ahorrar el monto de la inicial**.

Considere lo siguiente:

* El monto de la inicial es el 25% del costo total de la vivienda, ingresado por el usuario en el paso 1.
* El monto ahorrado tiene un **interes anual** de 4%. El interes anual es pagado en partes, **al final de cada mes**.
  Estos intereses incrementarán el monto ahorrado.
* Cada mes, el usuario destina un porcentaje de su salario **mensual**, ingresado por el usuario en el paso 3, que 
  incrementará el monto ahorrado.


La implementación debe realizarse en el archivo `parteuno.py`, entre las 
líneas marcadas como `#INICIO` y `#FIN`. 
**No remueva o modifique el código base**.

Los mensajes en consola **deben** tener el siguiente formato:

```
Ingrese el costo de la casa: 1000000
Ingrese su salario anual: 120000
Ingrese el porcentaje de ahorro mensual: 0.10
Numero de meses: 183
```

## Segunda Parte

Extender el programa desarrollado en la primera parte para considerar **aumentos semestrales** del salario.
El nuevo programa debe realizar lo siguiente:

1.  Solicite al usuario el costo total de una vivienda a adquirir.
2.  Solicite al usuario el ingreso de su salario anual.
3.  Solicite al usuario el ingreso el porcentaje del salario que ahorrará mensualmente.
4.  Solicite al usuario el ingreso el porcentaje de incremento salarial.
5.  Muestre en consola el **número de meses que le tomará al usuario ahorrar el monto de la inicial**.

Considere que **cada seis meses**, el salario deberá incrementarse en el porcentaje ingresado por el usuario 
en el paso 4.

La implementación debe realizarse en el archivo `partedos.py`, entre las 
líneas marcadas como `#INICIO` y `#FIN`. 
**No remueva o modifique el código base**.

Los mensajes en consola **deben** tener el siguiente formato:

```
Ingrese el costo de la casa: 500000
Ingrese su salario anual: 120000
Ingrese el porcentaje de ahorro mensual: 0.05
Ingrese el porcentaje de aumento semestral: 0.03
Numero de meses: 142
```

## Tercera Parte

Implemente un programa que realize lo siguiente:

1.  Solicite al usuario el ingreso de su salario anual.
2.  Muestre en consola el **porcentaje mensual de ahorro óptimo, para poder pagar la inicial de una casa de un millón de 
    soles en tres años**.
3.  Si no es posible ahorrar el monto de la inicial en tres años, mostrar un mensaje en consola. 

Considere lo siguiente:
* El monto de la inicial es el 25% del costo total de la vivienda.
* El monto ahorrado tiene un **interes anual** de 4%. 
  La generación de intereses funciona igual que la primera parte.
* Cada semestre, el salario del usuario se incrementa en 7%. 
  El incremento salarial funciona igual que en la segunda parte.   
* El resultado producido en el paso 2 debe generar ahorros que difieran, como máximo, en 100 soles de la inicial
requerida.
  
La implementación debe realizarse en el archivo `partetres.py`, entre las 
líneas marcadas como `#INICIO` y `#FIN`. 
**No remueva o modifique el código base**.

Los mensajes en consola **deben** tener el siguiente formato:

```
Ingrese su salario anual: 150000
Porcentaje de ahorro: 0.44091796875
```

```
Ingrese su salario anual: 10000
No es posible pagar la inicial en 36 meses
```

