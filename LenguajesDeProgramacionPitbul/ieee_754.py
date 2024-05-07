def decimal_to_binary(numeration):
    binary = bin(numeration)[2:]  # Convertir a binario y quitar el prefijo '0b'
    #binary = binary.zfill(bits)   # Rellenar con ceros a la izquierda para alcanzar el número de bits especificado
    return binary


def add_void_bits(number, bits):
    zeros = "0" * (bits - len(number))
    return number + zeros


def add_imprecision_bits(number, bits):
    times = 0
    while len(number) < bits:
        match times:
            case 0:
                number += "0"
            case 1:
                number += "0"
            case 2:
                number += "1"
            case 3:
                number += "1"
        if times < 3:
            times += 1
        else:
            times = 0
    return number


def binary_mantissa(dec_number, bits):  # 0.5 -> 1; 0.2 -> 5
    times = ""
    dec_number *= 2
    while dec_number < 1:
        dec_number *= 2
        times += "0"
    if dec_number > 1:
        return add_imprecision_bits(times + "1", bits)
    else:
        return add_void_bits(times + "1", bits)


def binary_to_float(binary, bits):
    sign_bits = int(binary[0])
    if bits < 33:
        exponent_bits = binary[1:9]
        mantissa_bits = binary[9:]
    else:
        exponent_bits = binary[1:12]
        mantissa_bits = binary[12:]

    exponent = int(exponent_bits, 2)
    mantissa = 0.0

    for i in range(len(mantissa_bits)):
        mantissa += (2 ** (-(i))) * int(mantissa_bits[i])
    if bits < 33:
        result = (-1) ** sign_bits * mantissa * (2 ** (exponent - 127))
    else:
        result = (-1) ** sign_bits * mantissa * (2 ** (exponent - 1023))
    return result


def convert_to_ieee754(number, bits):
    int_part_number = abs(int(number))
    dec_part_number = abs(number) - int_part_number

    sign_bit = "1"
    if number >= 0:
        sign_bit = "0"
    if bits < 33:
        mantisa = str(decimal_to_binary(int_part_number)) + binary_mantissa(dec_part_number, 23)
        exponente_seda = decimal_to_binary(127 + len(decimal_to_binary(int_part_number)) - 1)
    else:
        exponente_seda = decimal_to_binary(1023 + len(decimal_to_binary(int_part_number)) - 1)
        mantisa = str(decimal_to_binary(int_part_number)) + binary_mantissa(dec_part_number, 52)

    return sign_bit + exponente_seda + mantisa


def receive_to_convert():
    number = float(input())
    bits = int(input())
    print(convert_to_ieee754(number, bits))
    print(binary_to_float(convert_to_ieee754(number, bits), bits))


receive_to_convert()
