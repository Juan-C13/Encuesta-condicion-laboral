"""Problema: Se va a realizar una encuesta donde se le pregunta a
cada persona el sexo y la condición laboral."""

cantidad=int(input("¿Cuántas personas va a encuestar?:"))
print("")
MsiTrabajan=0
HnoTrabajan=0
TotalM=0
TotalH=0

for i in range(1,cantidad+1,1):
    a=0
    while a==0:
        sexo=int(input("Digite su sexo: (1-Masculino, 2-Femenino):"))
        condicionL=int(input("Especifíque si trabaja o no: (1-Si, 2-No):"))
        print("")
        if (sexo==1 or sexo==2) and (condicionL==1 or condicionL==2):
            a=a+1
        else:
            print("Los valores ingresados no son válidos, vuelva a intentarlo")
            print("")
    if sexo==2 and condicionL==1:
        MsiTrabajan=MsiTrabajan+1
    if sexo==1 and condicionL==2:
        HnoTrabajan=HnoTrabajan+1
    if sexo==2:
        TotalM=TotalM+1
    if sexo==1:
        TotalH=TotalH+1

porcentajeH=(TotalH/cantidad)*100

print("--------------RESULTADOS--------------")
print("El total de mujeres que trabajan es:",MsiTrabajan)
print("El total de hombres desempleados es:",HnoTrabajan)
print("El total de mujeres es:",TotalM)
print("El porcentaje de hombres es:",porcentajeH)
