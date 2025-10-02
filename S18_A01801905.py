#Exercise 1 
temperatures=[ 20,30,21,26,27,31,36]
avgTemperature = sum(temperatures) / len(temperatures)

print("The average Temperature is",avgTemperature)

for temperature in temperatures:
  if temperature >=avgTemperature:
    print(temperature,"is above range")
  else:
    print(temperature,"is below average")

#EXERCISE 2
studentNames=["Maria","Amanda","Santiago","Ricardo","Juana","Raul"]
studentGrades=[90,87,70,66,50,77]
avgstudentGrades= sum(studentGrades) / len(studentGrades)

estudiantesReprobados = []
print("The average studentGrades is",avgstudentGrades)
for grade in studentGrades:
  if grade <70:
      estudiante = studentNames[studentGrades.index(grade)]
      estudiantesReprobados.append(estudiante)
      
 
print(estudiantesReprobados)

#EXERCISE 3
compraste=["huevo","manzana","papel"]
yaComprado=[False,False,False]

for producto in compraste:
  respuesta=input("Ya compraste: " +producto + "?[Y/N]")
  if respuesta=="Y":
    yaComprado[compraste.index(producto)] = True


  
