<h1>Proyecto - SUP04</h1>

![Chocolate-banner](https://github.com/olivierifederico/proyecto-sup_04/blob/master/__src/chocolate.jpg?raw=true)

---

<h3>Pandas + FastApi + Docker</h3>

- Utilizar archivo choco.csv que se encuentra en la carpeta data

- Renombrar columnas de la siguiente manera: company, name-origin, ref, review, cacao, location, rating, bean, bean-origin

- En una nueva columna con el nombre pur asignar los siguientes valores segun el % de cacao

    - Si es menor que 60: BAJO

    - Si es mayor o igual a 60 y menor a 80: INTERMEDIO

    - Si es es mayor o igual a 80: ALTO

    - Si es igual a 100: PURO

- Crear una columna con el nombre res que este compuesta por:

    - company&pur&rating&location


- Hacer un decorador con el nombre indicado que devuelva un diccionario para cada una de las siguientes consultas

    /puro

    chocolate con 100% de cacao


    /top10

    top 10 en rating de chocolates

    /full

    lista completa con todos los chocolates


    /ref

    chocolates con el valor de ref menor al promedio, solo las columnas company,ref,res
    
    
- Hacer el deploy en render
    
    ---
    
    <h2>Hay premio para el que lo complete </h2>
    
    
    ![meme](https://raw.githubusercontent.com/olivierifederico/proyecto1_sup07/main/_src/PC180288.jpg)
    ---
