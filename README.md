# Menu personalizável pelo usuário em Python

## 🤳 Vídeo no youtube mostrando o projeto (8 minutos)

[<img width="1584" alt="miniatura" src="https://user-images.githubusercontent.com/97196457/149821838-3dc1e86a-94d7-4d33-8923-a99c2e91b36f.png">
](https://youtu.be/tej7xaOFyyg)

## ✍ Ideia geral do projeto
A minha ideia com esse projeto pessoal é criar um menu personalizável com Python. Onde o usuário poderá escolher o **nome do menu, estilo visual de formatação, nome das colunas da sua base de dados, tipos primitivos das colunas e uma base de dados com nome personalizado.**

<img width="1796" alt="três" src="https://user-images.githubusercontent.com/97196457/149817050-0403b29e-aeb6-45ed-ae52-3b272cc010a2.png">

E depois desse processo da personalização do menu, você entrará de fato no menu. Com as opção de **realizar um novo registro, olhar a base de dados e encerrar o programa.**

<img width="1584" alt="menu e opções" src="https://user-images.githubusercontent.com/97196457/149817857-118ed0db-3116-4b27-b436-1f332c828bad.png">

## 🤔 Inspirações e surgimento da ideia

Depois de terminar os cursos de Python 3 do [Curso em Vídeo](https://www.cursoemvideo.com) (05/01/22). Eu resolvi começar o meu projeto pessoal para dar um começo no meu portifólio. Então fiquei condicionado a pensar no que fazer até que surgisse uma ideia (e surgiu no mesmo dia). Mas... o que inspirou essa ideia?

<img width="1584" alt="inspirações" src="https://user-images.githubusercontent.com/97196457/149821501-d563ebc1-8382-4af3-ab65-3115dfa1139f.png">

Dois exercícios que eu fiz durante o curso foram os culpados por essa ideia. 
- O primeiro (imagem da direita) era um exercício para gerar um cardápio, porém, eu decidi incrementar mais um pouco e acrescentar uma personalização do nome do bar e, particulamente, adorei ver e fazer isso.
- O segundo (imagem da esquerda) foi um exercício bem completo para a criação de um menu com uma base de dados em um arquivo de texto.
A união da ideia da personalização e do menu com uma base de dados em um arquivo de texto, foram as geradoras desse meu projeto pessoal.

## 😵 Problemas, dificuldades, erros e como superei tudo

### **Dificuldades**:
- **Por onde começar?** Eu fiquei me perguntando isso até colocar o projeto no papel e destrinchar em partes. Fiz a modularização e separei bem onde ficaria cada função. E, com isso, eu pude ir construindo cada parte aos poucos e integrando cada uma. Apenas quando as partes estavam funcionando bem solo, eu as integrei no arquivo .py principal.

<div align="center">
  <img height="200em" src="https://user-images.githubusercontent.com/97196457/149844351-cde153b6-134a-4ef9-bdfc-9f87a9163d58.jpeg"/>
</div>

### **Problemas e erros**:
- **Git/Github**: quando optei pelo PyCharm, tive que aprender a como usar e como funcionava a integração dele com o Git. Depois de uma hora testando cada botão, entendendo cada funcionalidade, eu acabei achando bem prático até, ainda mais por tudo ser feito na própria IDE. Com o tempo, **entender as branches, commits, push, pull virou algo  fácil**.

<div align="center">
  <img height="150em" src="https://user-images.githubusercontent.com/97196457/149844037-e5e9b952-d78a-46f5-9804-fd0f794ccebc.png"/>
</div>

- **Tipos primitivos**: quando eu ficava um tempo olhando o código, testando com uns prints e o type e não resolvia, eu "**apelava**" e recorria ao debug. Foi uma ferramenta que me salvou e me mostrou exatamente o que estava errado. Recomendo muito usá-la para entender melhor o que está acontecendo e, principalmente, o que está acontecendo de errado.

<div align="center">
  <img height="200em" src="https://user-images.githubusercontent.com/97196457/149842047-6cd4227e-2b7b-4dec-930b-5631c6b83c1d.png"/>
</div>

- **Arquivo da base de dados só era "criado" depois de encerrado o programa**: o último problema que passei foi o fato de não aparecer a base de dados no PyCharm durante a execução do programa. Depois de um bom tempo tentando resolver, acabei por perceber que isso não era um problema e não me causariam outros, já que ele criava o arquivo, só não mostrava no PyCharm. Então acabei por simplesmente ignorar.

<div align="center">
  <img height="200em" src="https://user-images.githubusercontent.com/97196457/149842959-98d234b3-ae89-4368-9b17-eaf5394615e6.png"/>
</div>

- **Listas dentro de funções**: por conta da personalização, optei por trabalhar com listas. No início, eu ficava completamente perdido, até que criei comentários com as listas e os seus índices. E uma outra coisa que eu não contava, era que essa lista quando entrava numa função, ela ficava dentro de uma tupla, o que teria que acrescentar um \[0\] para enfim, poder escolher entre os elementos da lista.

## Ferramentas utilizadas
- PyCharm (Python IDE);
- Git/GitHub.
