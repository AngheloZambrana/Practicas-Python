def decimal_to_binary(numeration):
    binary = bin(numeration)[2:]  # Convertir a binario y quitar el prefijo '0b'
    return binary


def add_void_bits(number, bits):
    zeros = "0" * (bits - len(number))
    return number + zeros


def add_imprecision_bits(number, bits):
    while len(number) < bits:
        number += "0"
    return number


def binary_mantisa(dec_number):
    mantisa = ""
    while len(mantisa) < 23:
        dec_number *= 2
        if dec_number >= 1:
            mantisa += "1"
            dec_number -= 1
        else:
            mantisa += "0"
    return mantisa


def binary_to_float(binary):
    # Separar los bits en partes
    sign_bit = int(binary[0])
    exponent_bits = binary[1:9]
    mantissa_bits = binary[9:]

    # Convertir los bits en valores decimales
    exponent = int(exponent_bits, 2)
    mantissa = 0.0  # Agregar el bit implícito

    for i in range(1, len(mantissa_bits)):
        if mantissa_bits[i] == "1":
            mantissa += 2 ** (-(i))

    # Aplicar la fórmula
    result = (-1) ** sign_bit * (1 + mantissa) * 2 ** (exponent - 127)

    return result


def receive_to_convert():
    number = float(input())
    sign_bit = "1" if number < 0 else "0"

    # Calcular la parte entera y fraccionaria
    int_part_number = abs(int(number))
    dec_part_number = abs(number) - int_part_number

    # Calcular el exponente
    exponent = 127 + len(decimal_to_binary(int_part_number)) - 1
    exponent_bits = add_void_bits(decimal_to_binary(exponent), 8)

    # Calcular la mantisa
    mantissa = binary_mantisa(dec_part_number)
    mantissa_bits = add_void_bits(mantissa, 23)

    # Imprimir la representación binaria
    binary_representation = sign_bit + exponent_bits + mantissa_bits
    print("Representación binaria:", binary_representation)

    # Convertir el binario de vuelta a float
    float_value = binary_to_float(binary_representation)
    print("Número en punto flotante:", float_value)


receive_to_convert()
