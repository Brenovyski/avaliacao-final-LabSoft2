Avaliação Final – PCS 3853-3553

Duas aplicações distribuídas com dois micro-serviços cada. Um micro-serviço permite que um usuário compre um ingresso num estádio de football e reserve seu lugar na arquibancada. O outro micro serviço permite ver o mapa das arquibancadas e as vagas disponíveis.
Quando o usuário da primeira aplicação ou micro serviço compra um ingresso, imediatamente, um outro usuário utiliza a outra aplicação e ve a vaga reservada, Operação realizada em tempo real.
Restrições de projeto
- As aplicações são distribuídas, ou seja, as operações são independentes;
- Utilize contêiners para cada aplicação;
- Os bancos de dados são independentes e diferentes. Não existem relacionamentos;
Implemente o “Pattern” “Publisher – Subscriber” para atualizar em tempo real as informações dos bancos de dados das duas aplicações;
Utilizar GitHub para enviar o código.
