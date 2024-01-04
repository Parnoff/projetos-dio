let nome_heroi = [
    ['Mr Robot', 300],
    ['Capitão Caverna', 100001],
    ['Herói1', 2001],
    ['Herói2', 5500],
    ['Herói3', 9500]
];

let class_heroi = [
    [1000,'Ferro'],
    [2000,'Bronze'],
    [5000,'Prata'],
    [6000,'Ouro'],
    [8000,'Platina'],
    [9000,'Ascendente'],
    [10000,'Imortal'],
    [10001,'Radiante']
]

for (let i = 0; i < nome_heroi.length; i++) {

    let pontuacaoHeroi = nome_heroi[i][1];

    if (pontuacaoHeroi <= 1000) {
        console.log(nome_heroi[i][0] + ' - Ferro');
    } else {
        for (let y = 0; y < class_heroi.length; y++) {
            if (pontuacaoHeroi >= class_heroi[y][0] && (y === class_heroi.length - 1 || pontuacaoHeroi < class_heroi[y + 1][0])) {
                console.log('O Herói de nome ' + nome_heroi[i][0] + ' está no nível de ' + class_heroi[y][1]);
                break;
            }
        }
    }
}
