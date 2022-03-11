import os
# Função Principal
def main():
    dados()

# Função de coleta de dados
def dados():
    os.system("cls")
    print ("Seja bem - vindo ao calculador de prejuizo salarial")
    salario = int (input ("\nDigite o valor do seu salário: R$ "))
    hrs = int (input ("Digite a quantidade de horas trabalhadas por semana: "))
    salario_minimo = int (input ("Digite o valor do salário minimo hoje: R$ "))
    calculo(salario, hrs, salario_minimo)

# Função do calculo de prejuizo
def calculo(salario, hrs, salario_minimo):
    salario1 = salario
    # Calculo de prejuizo salárial anual
    salario_certo = (hrs * salario_minimo) / 44
    salario_anual = salario * 12
    Sc = int (salario_certo)
    salario_certo_anual = salario_certo * 12
    prejuizo_anual = salario_certo_anual - salario_anual
    Pa = int (prejuizo_anual)

    # Calculo de prejuizo mensal
    prejuizo_mensal = salario_certo - salario
    Pm = int (prejuizo_mensal)

    # Calculo de prejuizo salárial diário
    salario_diario = salario / 28
    salario_diario_certo = salario_certo / 28
    prejuizo_diario = salario_diario_certo - salario_diario
    Pd = int (prejuizo_diario)
    impressão (Pd, Pm, Pa, Sc, salario1)

# Função da Impressão 
def impressão (Pd, Pm, Pa, Sc, salario1):
    print ("\nCalculamos que:")
    print ("Para as horas que você trabalha, o salário correto seria: R$",Sc,"reais , invés de: R$", salario1,"reais")
    print ("Ganhando o que você ganha dentro de sua carga horária, seu prejuizo é de:")
    print ("R$",Pd, "reais por dia")
    print ("R$",Pm, "reais por mês")
    print ("R$",Pa, "reais por ano")
main()
