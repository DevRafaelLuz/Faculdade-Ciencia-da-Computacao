# 1. Implemente uma função para codificar e decodificar uma string para Base4
#    1. Receba uma string e retorne a string codificada
#    2. Receba uma string codificada e retorne seu conteúdo legível

def encode_string(input_string):
    base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    if isinstance(input_string, str):
        input_string = input_string.encode("UTF-8")

    binary_string = ""

    for byte in input_string:
        binary_string += f"{byte:08b}"

    padding_needed = (6 - len(binary_string) % 6) % 6
    binary_string += "0" * padding_needed

    encoded_chars = []

    for i in range(0, len(binary_string), 6):
        six_bits = binary_string[i:i+6]
        index = int(six_bits, 2)
        encoded_chars.append(base64[index])

    final_string = "".join(encoded_chars)
    while len(final_string) % 4 != 0:
        final_string += "="
        
    return final_string

def decode_string(decoded_string):
    base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

    decoded_string = decoded_string.rstrip("=")

    binary_string = ""

    for char in decoded_string:
        index = base64.index(char)
        binary_string += f"{index:06b}"

    bit_extra = len(binary_string) % 8
    if bit_extra:
        binary_string = binary_string[:-bit_extra]

    byte_list = []
    for i in range(0, len(binary_string), 8):
        byte_bits = binary_string[i:i+8]
        byte_list.append(int(byte_bits, 2))
        
    return bytes(byte_list)

def main():
    encoded_string = encode_string(input("Digite uma string para codificar: "))
    print(f"String codificada: {encoded_string}")

    decoded_string = decode_string(encoded_string)
    print(f"String decoficada: {decoded_string.decode("UTF-8")}")

if __name__ == "__main__":
    main()