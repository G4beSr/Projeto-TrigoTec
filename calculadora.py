import math

def calcular_tangente(angulo_graus):
    """
    Calcula a tangente de um ângulo em graus.

    Parâmetros:
        angulo_graus (float): O ângulo em graus.

    Retorna:
        float: A tangente do ângulo.

    Lança:
        ValueError: Se o ângulo for inválido.
    """
    try:
        #Verificar se o ângulo é válido
        if angulo_graus < 0:
            raise ValueError("O ângulo deve ser um número positivo.")

        #Converter graus para radianos
        angulo_radianos = math.radians(angulo_graus)

        #Calcular a tangente
        tangente = math.tan(angulo_radianos)

        return tangente
    except ValueError as e:
        print(f"Erro: {e}")
        return None

# Solicitar o ângulo do usuário
angulo_graus = float(input("Insira o ângulo em graus: "))

# Calcular a tangente
resultado = calcular_tangente(angulo_graus)

# Exibir o resultado
if resultado is not None:
    print(f"A tangente de {angulo_graus} graus é: {resultado:.2f}")
