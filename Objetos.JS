let livro = {
  nome = 'Conde de Monte Cristo',
  cod:0001,
  categoria: 'ficção, aventrura';
};

for (const propriedade in livro) {
  console.log('${propriedade}:${livro[propriedade]}');
}

//resultado => nome:Conde de monte cristo
//resultado => cod: 0001
//resultado => profissao:ação e aventura
