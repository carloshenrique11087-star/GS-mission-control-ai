missao = "Orion Test Alpha"
equipe = "Cosmo Prime"

areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]

dados_missao = [
    [24, 92, 88, 96, 90], #temperatura
    [27, 80, 72, 94, 85], #Cominicação
    [31, 65, 58, 91, 70], #Bateria
    [36, 42, 38, 87, 55], #Oxigenio
    [39, 28, 19, 78, 35], #Estabilidade
    [34, 55, 32, 82, 50]  #ciclo
]

def analisar_temperatura(valor):
    if valor < 18:
        return "ATENÇÃO", 1
    elif valor <= 30:
        return "NORMAL", 0
    elif valor <= 35:
        return "ATENÇÃO", 1
    else:
        return "CRÍTICO", 2

def analisar_comunicacao(valor):
    if valor < 30:
        return "CRÍTICO", 2
    elif valor < 60:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0

def analisar_bateria(valor):
    if valor < 20:
        return "CRÍTICO", 2
    elif valor < 50:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0

def analisar_oxigenio(valor):
    if valor < 80:
        return "CRÍTICO", 2
    elif valor < 90:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0

def analisar_estabilidade(valor):
    if valor < 40:
        return "CRÍTICO", 2
    elif valor < 70:
        return "ATENÇÃO", 1
    else:
        return "NORMAL", 0

def classificar_ciclo(risco):
    if risco <= 2:
        return "MISSÃO ESTÁVEL"
    elif risco <= 5:
        return "MISSÃO EM ATENÇÃO"
    else:
        return "MISSÃO CRÍTICA"

def gerar_recomendacao(temp, com, bat, oxi, est):
    recomendacoes = []

    if temp == "CRÍTICO":
        recomendacoes.append("Verificar controle térmico")
    if com == "CRÍTICO":
        recomendacoes.append("Restabelecer comunicação")
    if bat == "CRÍTICO":
        recomendacoes.append("Ativar economia de energia")
    if oxi == "CRÍTICO":
        recomendacoes.append("Acionar suporte à vida")
    if est == "CRÍTICO":
        recomendacoes.append("Reduzir operações não essenciais")

    if len(recomendacoes) == 0:
        return "Manter operação normal"

    return " | ".join(recomendacoes)

def analisar_tendencia(primeiro, ultimo):
    if ultimo > primeiro:
        return "A missão apresentou tendência de piora."
    elif ultimo < primeiro:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável."

def identificar_area_mais_afetada(pontuacoes):
    maior = max(pontuacoes)
    indice = pontuacoes.index(maior)
    return areas_monitoradas[indice], maior

riscos_ciclos = []
pontuacao_areas = [0, 0, 0, 0, 0]

soma_temperatura = 0
soma_comunicacao = 0
soma_bateria = 0
soma_oxigenio = 0
soma_estabilidade = 0

print("=" * 60)
print("MISSION CONTROL AI")
print("=" * 60)
print("Missão:", missao)
print("Equipe:", equipe)
print("Quantidade de ciclos analisados:", len(dados_missao))
print("=" * 60)

for indice, ciclo in enumerate(dados_missao, start=1):

    temperatura = ciclo[0]
    comunicacao = ciclo[1]
    bateria = ciclo[2]
    oxigenio = ciclo[3]
    estabilidade = ciclo[4]

    soma_temperatura += temperatura
    soma_comunicacao += comunicacao
    soma_bateria += bateria
    soma_oxigenio += oxigenio
    soma_estabilidade += estabilidade

    status_temp, risco_temp = analisar_temperatura(temperatura)
    status_com, risco_com = analisar_comunicacao(comunicacao)
    status_bat, risco_bat = analisar_bateria(bateria)
    status_oxi, risco_oxi = analisar_oxigenio(oxigenio)
    status_est, risco_est = analisar_estabilidade(estabilidade)

    pontuacao_areas[0] += risco_temp
    pontuacao_areas[1] += risco_com
    pontuacao_areas[2] += risco_bat
    pontuacao_areas[3] += risco_oxi
    pontuacao_areas[4] += risco_est

    risco_total = (
        risco_temp +
        risco_com +
        risco_bat +
        risco_oxi +
        risco_est
    )

    riscos_ciclos.append(risco_total)

    classificacao = classificar_ciclo(risco_total)

    recomendacao = gerar_recomendacao(
        status_temp,
        status_com,
        status_bat,
        status_oxi,
        status_est
    )

    print(f"\nCICLO {indice}")
    print("-" * 60)
    print(f"Temperatura: {temperatura}°C | {status_temp}")
    print(f"Comunicação: {comunicacao}% | {status_com}")
    print(f"Bateria: {bateria}% | {status_bat}")
    print(f"Oxigênio: {oxigenio}% | {status_oxi}")
    print(f"Estabilidade: {estabilidade}% | {status_est}")
    print(f"Pontuação de risco: {risco_total}")
    print(f"Classificação: {classificacao}")
    print(f"Recomendação: {recomendacao}")

media_temperatura = soma_temperatura / len(dados_missao)
media_comunicacao = soma_comunicacao / len(dados_missao)
media_bateria = soma_bateria / len(dados_missao)
media_oxigenio = soma_oxigenio / len(dados_missao)
media_estabilidade = soma_estabilidade / len(dados_missao)

risco_medio = sum(riscos_ciclos) / len(riscos_ciclos)

maior_risco = max(riscos_ciclos)
ciclo_mais_critico = riscos_ciclos.index(maior_risco) + 1

quantidade_ciclos_criticos = 0

for risco in riscos_ciclos:
    if risco >= 6:
        quantidade_ciclos_criticos += 1

tendencia = analisar_tendencia(
    riscos_ciclos[0],
    riscos_ciclos[-1]
)

area_mais_afetada, pontos_area = identificar_area_mais_afetada(
    pontuacao_areas
)

if risco_medio <= 2:
    classificacao_final = "MISSÃO ESTÁVEL"
elif risco_medio <= 5:
    classificacao_final = "MISSÃO EM ATENÇÃO"
else:
    classificacao_final = "MISSÃO CRÍTICA"

print("\n" + "=" * 60)
print("RELATÓRIO FINAL DA MISSÃO")
print("=" * 60)

print("Missão:", missao)
print("Equipe:", equipe)
print("Quantidade de ciclos:", len(dados_missao))

print(f"Média de temperatura: {media_temperatura:.2f}°C")
print(f"Média de comunicação: {media_comunicacao:.2f}%")
print(f"Média de bateria: {media_bateria:.2f}%")
print(f"Média de oxigênio: {media_oxigenio:.2f}%")
print(f"Média de estabilidade: {media_estabilidade:.2f}%")

print(f"Ciclo mais crítico: {ciclo_mais_critico}")
print(f"Maior pontuação de risco: {maior_risco}")
print(f"Risco médio da missão: {risco_medio:.2f}")
print(f"Quantidade de ciclos críticos: {quantidade_ciclos_criticos}")

print("\nTendência da missão:")
print(tendencia)

print("\nPontuação acumulada por área:")

for i in range(len(areas_monitoradas)):
    print(f"{areas_monitoradas[i]}: {pontuacao_areas[i]} pontos")

print("\nÁrea mais afetada:")
print(area_mais_afetada)

print("\nClassificação final da missão:")
print(classificacao_final)

print("\nConclusão:")

if classificacao_final == "MISSÃO ESTÁVEL":
    print("A missão operou dentro dos parâmetros esperados.")
elif classificacao_final == "MISSÃO EM ATENÇÃO":
    print("A missão apresentou instabilidades moderadas e exige monitoramento.")
else:
    print("A missão apresentou riscos elevados e necessita intervenção imediata.")