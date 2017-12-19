
teste = "futebol"

def meuConversor(text):
    wordList = list(set(text))
    vocab_to_int = dict()
    int_to_vocab = dict()

    for index in range(len(wordList)):
        vocab_to_int[wordList[index]] = index
        int_to_vocab[index] = wordList[index]
        
    return (vocab_to_int, int_to_vocab)

retorno = meuConversor(teste);
print(retorno)

print(set('Python'))