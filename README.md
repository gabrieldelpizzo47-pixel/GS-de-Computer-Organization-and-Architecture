# 🚀 Mission Control AI – Sistema de Alerta por Lógica Digital

## 📖 Sobre o Projeto

Este projeto foi desenvolvido para a disciplina **Computer Organization and Architecture**, como parte da **Global Solution 2026.1** da FIAP.

A proposta consiste no desenvolvimento de um sistema de alerta para uma missão espacial experimental, utilizando conceitos de lógica digital para identificar condições críticas da operação e acionar alertas visuais.

O sistema foi implementado no **Tinkercad**, utilizando **Arduino UNO**, interruptores e LEDs para simular o monitoramento da missão.

---

## 🎯 Objetivo

Desenvolver um sistema capaz de analisar diferentes condições operacionais de uma missão espacial e emitir alertas automáticos por meio da aplicação de expressões booleanas e portas lógicas.

---

## ⚙️ Tecnologias Utilizadas

* Arduino UNO
* Tinkercad
* Linguagem C++
* Lógica Digital
* Expressões Booleanas

---

## 🛰️ Variáveis Monitoradas

| Variável | Significado                 |
| -------- | --------------------------- |
| A        | Falha de comunicação        |
| B        | Temperatura crítica         |
| C        | Baixo nível de energia      |
| D        | Falha em módulo operacional |
| E        | Perda de estabilidade       |

---

## 🧠 Expressão Booleana

O sistema utiliza a seguinte expressão lógica para determinar situações de alerta:

```text
X = (A · C) + (B · D) + (E · ¬C)
```

Onde:

* **A · C** → Falha de comunicação associada ao baixo nível de energia;
* **B · D** → Temperatura crítica associada à falha operacional;
* **E · ¬C** → Perda de estabilidade na ausência de baixo nível de energia.

Quando a expressão resulta em **X = 1**, o sistema ativa o alerta.

---

## 💡 Funcionamento do Sistema

### Estado Normal

Quando nenhuma das condições críticas previstas pela expressão booleana é identificada, o LED verde permanece aceso, indicando operação normal da missão.

### Estado de Alerta

Quando pelo menos uma das condições críticas é satisfeita, o LED vermelho é acionado, sinalizando a necessidade de intervenção da equipe responsável.

---

## 🔌 Componentes Utilizados

* Arduino UNO
* 5 Interruptores (DIP Switch)
* 1 LED Verde
* 1 LED Vermelho
* Resistores
* Protoboard
* Jumpers

---

## 📁 Estrutura do Projeto

```text
mission-control-ai/
│
├── README.md
├── mission_control_ai.ino
└── relatorio.pdf
```

---


## 👨‍💻 Integrantes

* RM 572899 – Patrick Fernandes Martins Pais
* RM 570436 – Gabriel Del Pizzo Pintor
* RM 570540 – Ian Rodrigues Martins


---

## 📚 Conclusão

O projeto permitiu aplicar conceitos fundamentais de organização de computadores e lógica digital na construção de um sistema inteligente de monitoramento. A utilização de expressões booleanas associadas a componentes eletrônicos demonstrou como sistemas computacionais podem auxiliar na identificação automática de condições críticas em missões espaciais.
