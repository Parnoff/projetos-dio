
let nomeJogador = [
    /* NomeJogador|Vitórias|Derrotas */
    ['Player1', 100, 101],
    ['Player2', 10001, 500],
    ['Player3', 80, 65],
    ['Player4', 190, 111],
    ['Player5', 100, 1]
];

let classRank = [
    /*Número Máximo Vitórias | Nível */
    [10,'Ferro'],
    [20,'Bronze'],
    [50,'Prata'],
    [80,'Ouro'],
    [90,'Diamante'],
    [100,'Lendário'],
    [101,'Imortal']
];

for (let i = 0; i < nomeJogador.length; i++) {
    let vitoria = nomeJogador[i][1]
    let derrota = nomeJogador[i][2]
    calcularPartidasRankeadas(vitoria,derrota)
};

function calcularPartidasRankeadas(vitorias, derrotas) {

    let resultado = vitorias - derrotas
    let mensagem1 = 'O Herói tem de saldo de '
    let mensagem2 = ' está no nível de '

    if (resultado <= classRank[0][0]) {
        console.log(mensagem1 + resultado + mensagem2 + classRank[0][1]);
    } else {
        for (let y = 0; y < classRank.length; y++) {
            if (resultado >= classRank[y][0] && (y === classRank.length - 1 || resultado < classRank[y + 1][0])) {
                console.log(mensagem1 + resultado + mensagem2 + classRank[y][1]);
                break;
            }
        }
    }
};