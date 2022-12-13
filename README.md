# API_chuck_norris - Kevin Soffa

## Rotas

### GET - Random
/kevin <br>
Nenhum item obrigatório
<hr>

### GET - Lista de Categorias
/kevin/categorias <br>
Nenhum item obrigatório
<hr>

### GET - Categoria ou Palavra
/kevin/procurar?categoria={palavra}&paginacao_limite={limite}
#### Queryparams Obrigatorio ?categoria={palavra} -- String
#### Queryparams NÃO Obrigatorio ?paginacao_limite={limite} -- Int

<hr>

### GET - Categoria ou Palavra [Random]
kevin/random/categoria?categoria=food
#### Queryparams Obrigatorio ?categoria={palavra} -- String

## Observações
As rotas de requisições da API estão no arquivo .env
