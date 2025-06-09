# ALGORITMOS E PROGRAMAÇÃO - PROJETO 01
# Gustavo Leal Gomes e Beatriz Paulino Gomes

def calcular_penalidade(velocidade_registrada, velocidade_permitida, reincidencia):
    if velocidade_registrada <= velocidade_permitida:
        return "Nenhuma infração", 0, 0
    elif velocidade_registrada <= (velocidade_permitida * 1.2):
        return "Infração leve", 130.16, 0
    elif velocidade_registrada <= (velocidade_permitida * 1.5):
        multa = 195.23 * (2 if reincidencia == "sim" else 1)
        return "Infração grave", multa, 5
    else:
        multa = 880.41 * (2 if reincidencia == "sim" else 1)
        return "Infração gravíssima", multa, "7 e perca da carteira"

def solicitar_pagamento(multa):
    pagamento = input("\nDeseja pagar a multa agora? (sim/não) ")
    if pagamento == "sim":
        multa *= 0.8
        print(f"\nPagando agora você recebe um desconto de 20%. Assim, o valor da multa será de R$ {multa:.2f}")
    return multa

def main():
    placa = input("Placa do veículo: ")
    motorista = input("Nome do motorista: ")
    velocidade_registrada = float(input("Velocidade registrada (km/h): "))
    velocidade_permitida = float(input("Velocidade máxima permitida da via (km/h): "))
    reincidencia = input("Já foi multado anteriormente? (sim/não) ")

    penalidade, multa, pontos = calcular_penalidade(velocidade_registrada, velocidade_permitida, reincidencia)
    print(f"\nPenalidade: {penalidade}\nMulta: R$ {multa:.2f}\nPontos na carteira: {pontos}")
    
    if penalidade == "Infração gravíssima":
        print("O motorista deve realizar um curso de reciclagem no Detran.")
    
    solicitar_pagamento(multa)

main()
