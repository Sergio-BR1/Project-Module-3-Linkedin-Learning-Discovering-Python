def lerArquivo(palvAntiga, palvNova, nome):
	linhasAlteradas = [] 
	arquivo = open(nome, "r")
	if (arquivo.mode == "r"):
		conteudo = arquivo.readlines() #lê todas as linhas do arquivo

		#Guarda em uma lista as linhas do arquivo, com a palavra desejada substituída para a nova
		for linha in conteudo:
			linhasAlteradas.append(linha.replace(palvAntiga, palvNova)) 

	arquivo.close()
	return linhasAlteradas
	
def criarArquivo(nome, linhas, extensao):
	arquivo = open(nome+" alterado."+extensao, "w+")

	#escreve no arquivo gerado as linhas com as palavras substituídas
	for linha in linhas:
		arquivo.write(linha)

	arquivo.close()

nome = input("Digite o nome do arquivo que será lido (Incluindo a extensão): ")
palavraAntiga = input("Digite a palavra a ser substituida: ")
palavraNova = input("Digite a palavra que ficará no lugar da antiga: ")
extensao = input("Digite a estensão que deseja que o arquivo seja salvo: ")

escrever = lerArquivo(palavraAntiga, palavraNova, nome)
criarArquivo(nome, escrever, extensao)