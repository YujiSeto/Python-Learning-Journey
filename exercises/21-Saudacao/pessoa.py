class Pessoa:
    """Isto é uma classe nova chamada Pessoa"""
    
    idade = 15

    def saudacao(self):
        print('Olá Pessoas!')

# Output: 15
print(Pessoa.idade)

# Output: <function Pessoa.saudacao at 0x...>
print(Pessoa.saudacao)

# Output: “Isto é uma classe nova chamada Pessoa”
print(Pessoa.__doc__)

matheus = Pessoa()