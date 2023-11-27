from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/'index)
def index():
  return '''
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Resultado</title>

    <style>
      * {
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    background-image: url('back.png');
    background-size: cover;
    background-repeat: no-repeat;
    border-radius: 20px;
    background-size: 100% 100%;
    background-attachment: fixed;
    font-family: Arial, sans-serif;
    margin: 50px;
    padding: 50px;
    display: flex;
    flex-direction: column;
    background-color: #333;
    border-radius: 30px;
    border: solid 3px rgb(61, 173, 61);
}

div {
    display: block;
    padding: 100px;
    border: solid 3px rgb(61, 173, 61);
    margin: 20px;
    border-radius: 30px;
    /* Arredonda as bordas do Divs */
}

section {
    display: block;
    padding: 100px;
    border: solid 3px rgb(61, 173, 61);
    margin: 20px;
    border-radius: 30px;
    /* Arredonda as bordas do section */
}

footer {
    border: solid 3px rgb(61, 173, 61);
    border-radius: 30px;
    color: rgb(61, 173, 61);
    text-align: center;
    padding: 5px;
}

.margen-class {
    padding: 30px;
    border: solid 3px rgb(61, 173, 61);
    margin: 30px;
    border-radius: 30px;
    /* Arredonda as bordas das classes .margen-class */
}


/* Arredonda as bordas do body */

header {
    border-radius: 15px;
    color: #fff;
    padding: 10px 0;
    margin-bottom: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.container-text {
    padding: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}

.container-text-white {
    padding: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: white;
    flex-direction: column;
}

span {
    color: #2ecc71;
}

.text h3 {
    color: #2ecc71;
    font-size: 28px;
}

h3 {
    color: #fff;
}

h2 {
    color: #fff;
    text-align: center;
}

h1 {
    color: #fff;
}

h4 {
    color: #fff;
}

p {
    color: #fff;
}

label {
    color: #fff;
}

.text h1 {
    color: #fff;
    font-size: 36px;
}

.center {
    text-align: center;
}

button {
    color: #2ecc71;
    background: transparent;
    padding: 5px;
    border-radius: 15px;
    font-size: 12px;
    cursor: pointer;
    width: 150px;
}

input:hover {
    background-color: rgb(61, 173, 61);
    color: #fff;
    transition: 0.5s;
}

.btn {
    background: transparent;
    color: #fff;
    padding: 10px 20px;
    border: solid 2px rgb(61, 173, 61);
    border-radius: 10px;
    cursor: pointer;
    margin-top: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    /* Adiciona margem de 20px na parte superior */
}

.logo {
    height: 40px;
    width: 40px;
    background: transparent;
    border: 1px solid #2ecc71;
    color: #2ecc71;
    border-radius: 50%;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 15px;
    cursor: pointer;
}

#form {
    display: block;
    /* Torna a seção um contêiner block */
    padding: 10px;
    margin: 50px;
    border: solid 3px rgb(61, 173, 61);
    border-radius: 30px;
    /* Arredonda as bordas do .project */
}


/*
.margen-class {
    padding: 30px;
    border: solid 3px rgb(61, 173, 61);
    margin: 30px;
    border-radius: 30px;
     Arredonda as bordas das classes .margen-class 
}
*/


/*
.column {
    border-radius: 10px;
    flex: 1;
    /* Faz com que as colunas ocupem a mesma largura 
    padding: 10px;
    /* Adicione preenchimento interno para separação 
    border: 3px solid rgb(61, 173, 61);
     Adicione bordas para separação visual 
}
*/


/*MOBILE*/


/* Exemplo de media query para dispositivos móveis */

@media screen and (max-width: 768px) {
    body {
        padding: 20px;
        /* Reduza o preenchimento */
    }
    header {
        padding: 20px;
    }
}
    </style>
</head>

<body>

    <h1 class="center">Resultado</h1>
    <section>
        <h2>Lista Completa</h2>
        <div>
            <ul class="container-text-white" id="dataList"></ul>
        </div>
        <h2>Menor Nome</h2>
        <div class="container-text-white" id="minName"></div>
        <h2>Maior Nome</h2>
        <div class="container-text-white" id="maxName"></div>
        <h2>Menor Idade</h2>
        <div class="container-text-white" id="minAge"></div>
        <h2>Idade Mediana</h2>
        <div class="container-text-white" id="medianAge"></div>
    </section>
</body>
<script>
    var data = JSON.parse(localStorage.getItem("data"));

    // Ordenar a lista por nome em ordem crescente
    data.sort(function(a, b) {
        return a.name.localeCompare(b.name);
    });

    var dataList = document.getElementById("dataList");
    var minName = document.getElementById("minName");
    var maxName = document.getElementById("maxName");
    var minAge = document.getElementById("minAge");
    var medianAge = document.getElementById("medianAge");

    for (var i = 0; i < data.length; i++) {
        var listItem = document.createElement("li");
        listItem.textContent = data[i].name + " - " + data[i].age;
        dataList.appendChild(listItem);
    }

    minName.textContent = data[0].name;
    maxName.textContent = data[data.length - 1].name;

    // Encontrar a menor idade
    var ages = data.map(function(item) {
        return item.age;
    });
    minAge.textContent = Math.min(...ages);

    // Encontrar a idade mediana
    ages.sort(function(a, b) {
        return a - b;
    });
    var middle = Math.floor(ages.length / 2);
    medianAge.textContent = ages.length % 2 === 0 ? (ages[middle - 1] + ages[middle]) / 2 : ages[middle];
</script>
<br>
<br>
<footer>
    <p>&copy; 2023 EC.Computação</p>
</footer>

</html>
'''
