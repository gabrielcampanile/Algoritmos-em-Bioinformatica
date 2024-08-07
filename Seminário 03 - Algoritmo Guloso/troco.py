def get_change(amount, coins):
    # Ordena as moedas em ordem decrescente
    coins.sort(reverse=True)

    result = []
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)
    
    if amount != 0:
        return None  # Não é possível dar o troco exato com as moedas disponíveis
    
    return result

# Exemplo de uso
coins = [1, 5, 10, 25]
amount = 63
change = get_change(amount, coins)

if change is not None:
    print(f"Troco para {amount} é: {change}")
else:
    print(f"Não é possível dar o troco exato para {amount} com as moedas disponíveis.")
