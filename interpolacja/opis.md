# Interpolacja Lagrange'a

## Cel
Uzyskanie przybliżenia wyniku pierwiastkowania poprzez wykorzystanie interpolacji wielomianowej. 


## Opis
Chcemy uzyskać wielomian stopnia co najwyżej n, posiadając n+1 punktów, w których wartość jest nam znana.
Naszym zadaniem jest oszacowanie wartość funkcji w punkcie x, zgodnie z następującym wzorem: 

![wzor1](https://github.com/malinowakrew/numerical_methods/blob/master/interpolacja/wz%C3%B3r_1.png)

yn- znana wartość w punkcie xn
Ln- n-ty współczynnik dla punktu x

Naszym zadaniem jest więc wyznaczyć współczynniki Ln.

Posłużymy się wzorem

![wzor2](https://github.com/malinowakrew/numerical_methods/blob/master/interpolacja/wz%C3%B3r_2.png)

Li- i-ty współczynnik obliczany dla punktu xi
xj- inne dane punkty (poza xi)


eng Lagrange interpolation
