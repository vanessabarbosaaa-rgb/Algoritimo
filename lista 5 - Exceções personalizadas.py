class SenhaInvalidaError(Exception):
    pass

def verificar_senha(senha):
    if len(senha) < 8:
        raise SenhaInvalidaError("A senha deve ter pelo menos 8 caracteres.")
    if not any(char.isdigit() for char in senha):
        raise SenhaInvalidaError("A senha deve conter pelo menos um número.")

try:
    senha = input("Digite uma senha: ")
    verificar_senha(senha)
    print("Senha válida!")

except SenhaInvalidaError as e:
    print(f"Erro: {e}")