class Heroi {
    constructor(nome, idade, tipo){
        this.nome = nome;
        this.idade = idade;
        this.setTipo(tipo);
    }

    setTipo(tipo) {

        const tiposValidos = ['guerreiro', 'mago', 'monge', 'ninja'];

        if (tiposValidos.includes(tipo)) {
            this.tipo = tipo;
        } else {
            throw new Error('Tipo de herói inválido');
        }
    }

    atacar() {
        switch (this.tipo) {
            case 'guerreiro':
                return `O ${this.tipo} atacou usando espada`;
            case 'mago':
                return `O ${this.tipo} atacou usando magia`;
            case 'monge':
                return `O ${this.tipo} atacou usando artes marciais`;
            case 'ninja':
                return `O ${this.tipo} atacou usando shuriken`;
            default:
                throw new Error('Dados incorretos!');
        }
    }
}

const tiposHerois = ['guerreiro', 'mago', 'monge', 'ninja'];

for (let i = 0; i < tiposHerois.length; i++) {
    let nome = 'heroi' + i + 1;
    let guerreiro = 'guerreiro' + i + 1;
    nome = new Heroi(guerreiro, 30,  tiposHerois[i]);
    console.log(nome.atacar());
}