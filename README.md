# gerenciador_de_anuncios
Um gerenciador de anúncios no qual pode-se cadastrar anúncios e obter informações sobre anúncios cadastrados.

INSTRUÇÕES PARA A FUNÇÃO "main()":
A seguinte função pode ser executada em IDE com integração ao Python, tais como o IDLE.
Para executá-la, basta abrir o programa "Gerenciador_de_Anúncios.py" no IDE e chamar pela função "main()".
A própria função irá lhe conduzir pelo programa, chamando outras funções quando necessário. 

INFORMAÇÕES SOBRE O FUNCIONAMENTO DO PROGRAMA:
Todas as funções são bastante autoexplicativas, mas, resumidamente:
- "ad_registration" recebe uma lista de anúncios, que pode estar vazia ou não, e solicita informações para fazer o cadastro de um novo anúncio. Com as informações cadastradas, ela calcula outras informações através de funcões que ela chama enquanto executada. Ao final, ela guarda essas informações na lista "new_ad", que é esvaziada a cada início de execução da função "ad_registration".
- "total_days" recebe as datas de ínicio e fim do anúncio e calcula o total de dias do anúncio.
- "total_investment" recebe as datas de início e fim do anúncio e o valor do investimento por dia, e calcula o total de investimentos naquele anúncio.
- "calculator_views" recebe o valor total de investimentos e devolve o número máximo de visualizações para aquele anúncio, considerando parâmetros pré estabelecidos fora deste programa.
- "calculator_clicks" recebe o número máximo de visualizações e devolve o número máximo de cliques para aquele anúncio, considerando parâmetros pré estabelecidos fora deste programa.
- "calculator_shares" recebe o número máximo de cliques e devolve o número máximo de compartilhamentos para aquele anúncio, considerando parâmetros pré estabelecidos fora deste programa.
- "consult_ad" recebe a lista de anúncios "ads" e possibilita a consulta dos anúncios previamente cadastrados, utilizando-se do nome do cliente ou do intervalo de tempo, em dias, do anúncio para a busca. 

INSTRUÇÕES PARA OS TESTES:
Para executar os testes, utilize o Prompt de Comando.
É necessário ter o programa "pytest" instalado em sua máquina.
Ao abrir o Prompt, busque pela pasta na qual o programa "Gerenciador_de_Anúncios.py" está localizado.
Em seguida, execute os testes através do comando "pytest Gerenciador_de_Anúncios.py".
