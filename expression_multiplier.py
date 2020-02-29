from s_array import SArray

class ExpressionMultiplier:
    
  def __init__(self):
    symbols_amount = int(input("Symbols amount: "))

    symbols = []
    repetitions = []
    print("Symbol minValue maxValue [eg: xxx 0 5]:")
    while(symbols_amount != 0):
      symbols_amount-= 1

      x = input().split()
      symbols.append(x[0])
      repetitions.append([int(x[1]), int(x[2])])

    print(self.multiply_expression(symbols, repetitions))
    
  def multiply_expression(self, symbols, repetitions) :
    repetition_matrix = dict()
    for index, symbol in enumerate(symbols):
      symbol_repetitions = []

      for repetition in range(repetitions[index][0], repetitions[index][1]+1):
        if repetition < 0:
          continue
        symbol_repetitions.append(symbol * repetition)

      repetition_matrix[symbol] = SArray(*symbol_repetitions)
    x = SArray('')
    for symbol_repetitions in repetition_matrix:
      x *= repetition_matrix[symbol_repetitions]
    return x.items


ExpressionMultiplier()