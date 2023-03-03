# TCC-Helper

Um chatbot criado para auxiliar com dúvidas da disciplina de TCC1.

## 🚀 Inicialização

Verifique se você possui o [Python3+](https://www.python.org/downloads/) instalado.

Antes de usar o chatbot, instale os pacotes necessários utilizando:

```sh
pip install requirements.txt -r
```

Com os pacotes instalados, para treinar o ChatBot, utilize o comando abaixo:

```sh
python3 main.py -t
```

Para executar a Interface gŕafica, utilize o comando abaixo:

```sh
python3 main.py -l
```

## 📚 Arquivo "intents.json"

```json
{
  "intents": [
    {
      "tag": "saudacao",
      "patterns": ["Olá", "Opa", "Oi", "Tudo Bem"],
      "responses": ["Oi", "Olá"]
    },
    {
      "tag": "despedida",
      "patterns": ["Valeu", "tchau", "Obrigado", "tks"],
      "responses": ["Até breve", "Falou", "Tchau"]
    },
    {
      "tag": "integrantes_grupo",
      "patterns": [
        "Quantos integrantes deve ter o grupo de TCC?",
        "Grupo de quantos?",
        "Quantas pessoas?",
        "Quantos integrantes?"
      ],
      "responses": ["Os grupos devem buscar ter 4 integrantes"]
    },
    {
      "tag": "prof_orientador_outro_departamento",
      "patterns": [
        "O professor orientador pode ser de outro departamento?",
        "O departamento do orientador precisa ser o mesmo do meu curso?"
      ],
      "responses": [
        "Sem problemas, o professor orientador pode ser de outro departamento!"
      ]
    },
    {
      "tag": "cronograma_aulas",
      "patterns": [
        "Onde posso encontrar a programação das aulas?",
        "Onde encontro o cronograma?",
        "Onde encontro as datas?",
        "Data das entregas"
      ],
      "responses": ["O cronograma da disciplina pode ser encontrado no Moodle"]
    },
    {
      "tag": "atividades_e_entregas",
      "patterns": [
        "Onde posso enviar as atividades e entregas?",
        "Onde envio as atividades?"
      ],
      "responses": [
        "As atividades e entregas devem ser enviadas no Moodle nas datas determinadas"
      ]
    },
    {
      "tag": "grupo_whatsapp",
      "patterns": [
        "Como posso participar do grupo do WhatsApp?",
        "Onde posso tirar minha dúvidas?",
        "WhatsApp"
      ],
      "responses": [
        "Você pode tirar algumas de suas dúvidas através do grupo de WhatsApp! Se você não participa do grupo do WhatsApp da disciplina, você pode solicitar ao professor Ricardo Destro"
      ]
    },
    {
      "tag": "prazos",
      "patterns": [
        "Qual o prazo para desenvolver o trabalho?",
        "Quanto tempo tenho?",
        "Quantos semestres tenho para fazer?"
      ],
      "responses": [
        "Os alunos têm dois semestres para desenvolver todas as atividades relacionadas ao trabalho, e no final de cada semestre serão avaliados por uma banca de professores"
      ]
    },
    {
      "tag": "avaliacao_final",
      "patterns": [
        "Como é a avaliação final?",
        "Como é a banca?",
        "Forma de avaliação",
        "Como a banca avalia?"
      ],
      "responses": [
        "A avaliação final do trabalho é uma composição da avaliação da banca, do professor orientador e dos professores da disciplina de Trabalho de Final de Curso.\n\nA avaliação da banca é definitiva, ou seja, é ela quem determina se o trabalho será aprovado ou não.\n\nEmbora o trabalho seja realizado em grupo, a avaliação será individual, ou seja, o aluno será avaliado por sua contribuição efetiva no trabalho realizado."
      ]
    },
    {
      "tag": "resultado_final",
      "patterns": [
        "Qual é o resultado final do TCC?",
        "O que devo entregar?",
        "Quais são as entregas?",
        "O que preciso fazer?",
        "O que preciso escrever?",
        "Preciso criar um programa?"
      ],
      "responses": [
        "Para o resultado final do TCC é esperado uma monografia e um programa/artefato desenvolvido pelos integrantes do grupo."
      ]
    }
  ]
}
```
O arquivo JSON acima é um exemplo de como um chatbot pode ser configurado. Ele contém uma lista de intenções ("intents") que o chatbot pode reconhecer e responder de acordo.

Cada intenção é composta de uma tag ("tag") que identifica a intenção, um conjunto de padrões ("patterns") que representam as possíveis frases que o usuário pode usar para expressar essa intenção, e um conjunto de respostas ("responses") que o chatbot pode fornecer quando essa intenção é reconhecida.

No arquivo acima, temos intenções como "saudação", "despedida", "integrantes_grupo", "prof_orientador_outro_departamento", "cronograma_aulas", "atividades_e_entregas", "grupo_whatsapp", "prazos", "avaliacao_final" e "resultado_final".

## 🕮 Descrição das Tags Utilizadas

* **"saudacao"**: Essa tag contém as expressões de cumprimento que o chatbot pode reconhecer e responder de forma adequada, como "Olá", "Oi" e "Tudo bem". As respostas para essas expressões também estão definidas na tag, como "Oi" e "Olá".

* **"despedida"**: Assim como a tag "saudacao", essa tag contém expressões de despedida que o chatbot pode reconhecer e responder de forma apropriada, como "tchau" e "obrigado". As respostas também estão definidas na tag, como "Até breve" e "Falou".

* **"integrantes_grupo"**: Essa tag trata de uma questão importante para quem está fazendo TCC: quantas pessoas devem compor o grupo de trabalho. A tag contém as diferentes formas que o usuário pode expressar a pergunta sobre o número de integrantes e a resposta do chatbot, que é "Os grupos devem buscar ter 4 integrantes".

* **"prof_orientador_outro_departamento"**: Nessa tag, é tratada a dúvida sobre a possibilidade de ter um professor orientador de outro departamento que não o do curso do aluno. As expressões que o usuário pode utilizar para perguntar sobre isso estão definidas na tag, assim como a resposta do chatbot, que tranquiliza o usuário afirmando que é possível ter um orientador de outro departamento.

* **"cronograma_aulas"**: Essa tag aborda a questão de onde encontrar as datas e programação das aulas relacionadas à disciplina do TCC. As diferentes formas de expressar a pergunta sobre isso estão definidas na tag, assim como a resposta do chatbot, que informa que o cronograma da disciplina pode ser encontrado no Moodle.

* **"atividades_e_entregas"**: Aqui é tratada a questão de onde enviar as atividades e entregas relacionadas ao TCC. As diferentes formas de expressar a pergunta sobre isso estão definidas na tag, assim como a resposta do chatbot, que informa que as atividades e entregas devem ser enviadas no Moodle nas datas determinadas.

* **"grupo_whatsapp"**: Nessa tag, é explicado como o usuário pode participar do grupo do WhatsApp para tirar dúvidas relacionadas à disciplina do TCC. As diferentes formas de expressar a pergunta sobre isso estão definidas na tag, assim como a resposta do chatbot, que informa que é possível solicitar a participação no grupo ao professor Ricardo Destro.

* **"prazos"**: Essa tag aborda a questão do prazo para desenvolver o trabalho do TCC. As diferentes formas de expressar a pergunta sobre isso estão definidas na tag, assim como a resposta do chatbot, que informa que os alunos têm dois semestres para desenvolver todas as atividades relacionadas ao trabalho e que serão avaliados por uma banca de professores.

* **"avaliacao_final"**: Nessa tag, é explicado como funciona a avaliação final do trabalho do TCC. As diferentes formas de expressar a pergunta sobre isso estão definidas na tag, assim como a resposta do chatbot, que explica que a avaliação final é uma composição da avaliação da banca, do professor orientador e dos professores da disciplina. Também é esclarecido que a avaliação da banca é definitiva e que a avaliação será individual, mesmo que

## 🗨️ Exemplo de Diálogo
<p align="center">
  <img alt="Dialog" align="center" src ="https://github.com/hugolinhareso/TCC-Helper/blob/main/resources/dialog.png" width="700" height="500"></img>
<p>

## 🧑‍💻 Autores

**Hugo Linhares**

- Github: [@hugolinhareso](https://github.com/hugolinhareso)
- RA: 22.120.046-2

**João Pedro**

- Github: [@akajhon](https://github.com/akajhon)
- RA: 22.120.021-5

## 📝 Licença

Esse projeto está sob a licença [MIT](https://github.com/hugolinhareso/round-robin/blob/main/LICENSE).
