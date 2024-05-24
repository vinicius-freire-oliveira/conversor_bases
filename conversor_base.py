class ConversorBase:
    # Método para converter binário para decimal
    def binario_para_decimal(binario):
        return int(binario, 2)

    # Método para converter decimal para binário
    def decimal_para_binario(decimal):
        return bin(decimal)[2:]

    # Método para converter octal para decimal
    def octal_para_decimal(octal):
        return int(octal, 8)

    # Método para converter decimal para octal
    def decimal_para_octal(decimal):
        return oct(decimal)[2:]

    # Método para converter hexadecimal para decimal
    def hexadecimal_para_decimal(hexadecimal):
        return int(hexadecimal, 16)

    # Método para converter decimal para hexadecimal
    def decimal_para_hexadecimal(decimal):
        return hex(decimal)[2:].upper()

# Exemplos de uso:

# Converter binário para decimal
binario = '101010'
print(f"{binario} em binário é {ConversorBase.binario_para_decimal(binario)} em decimal")

# Converter decimal para binário
decimal = 42
print(f"{decimal} em decimal é {ConversorBase.decimal_para_binario(decimal)} em binário")

# Converter octal para decimal
octal = '52'
print(f"{octal} em octal é {ConversorBase.octal_para_decimal(octal)} em decimal")

# Converter decimal para octal
decimal = 42
print(f"{decimal} em decimal é {ConversorBase.decimal_para_octal(decimal)} em octal")

# Converter hexadecimal para decimal
hexadecimal = '2A'
print(f"{hexadecimal} em hexadecimal é {ConversorBase.hexadecimal_para_decimal(hexadecimal)} em decimal")

# Converter decimal para hexadecimal
decimal = 42
print(f"{decimal} em decimal é {ConversorBase.decimal_para_hexadecimal(decimal)} em hexadecimal")
