// Definição da classe ItemMagico
class ItemMagico {
    // Construtor que recebe os atributos do item mágico
    constructor(tipo, dano, resistencia) {
      this.tipo = tipo;
      this.dano = dano;
      this.resistencia = resistencia;
    }
  
    calcularDano() {
      return this.tipo === 'arma' ? this.dano * 2 : this.dano;
    }
  }
  
  // Solicita ao usuário para digitar o tipo do item mágico, o dano no item e a resistência do item
  const tipoItem = 'Espada';
  const danoItem = 200;
  const resistenciaItem = 300;
  
  // Cria um objeto ItemMagico personalizado com base nos dados fornecidos pelo usuário
  const itemPersonalizado = new ItemMagico(tipoItem, danoItem, resistenciaItem);
  
  // Imprime os atributos do item personalizado
  console.log("Tipo: " + itemPersonalizado.tipo);
  console.log("Dano: " + itemPersonalizado.dano);
  console.log("Resistencia: " + itemPersonalizado.resistencia);
  
  // Calcula e imprime o dano causado pelo item personalizado em um combate simulado
  const danoTotal = itemPersonalizado.calcularDano();
  console.log("Dano em combate: " + danoTotal);
  