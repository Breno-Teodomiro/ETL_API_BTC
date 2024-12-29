import requests
from tinydb import TinyDB
from datetime import datetime
import time

def extrair_dados_bitcoin():
    """Extrai o JSON completo da API da Coinbase."""
    url = 'https://api.coinbase.com/v2/prices/spot'
    resposta = requests.get(url)
    return resposta.json()

def tratar_dados_bitcoin(dados_json):
    """Transforma os dados brutos da API e adiciona timestamp."""
    valor = float(dados_json['data']['amount'])
    criptomoeda = dados_json['data']['base']
    moeda = dados_json['data']['currency']
    dados_tratados = {
        "valor": valor,
        "criptomoeda": criptomoeda,
        "moeda": moeda,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
    return dados_tratados

def salvar_dados_tinydb(dados, db_name="bitcoin_dados.json"):
    """Salva os dados em um banco NoSQL usando TinyDB."""
    db = TinyDB(db_name)
    db.insert(dados)
    print("Dados salvos no TinyDB!")

if __name__ == "__main__":
    print("Iniciando ETL com atualização a cada 15 segundos... (CTRL+C para interromper)")

    while True:
        try:
            dados_json = extrair_dados_bitcoin()
            if dados_json:
                dados_tratados = tratar_dados_bitcoin(dados_json)
                print("Dados Tratados:", dados_tratados)
                # Mostrar os dados tratados
                print("Dados Tratados:")
                print(dados_tratados)
            time.sleep(15)
        except KeyboardInterrupt:
            print("\nProcesso interrompido pelo usuário. Finalizando...")
            break
        except Exception as e:
            print(f"Erro durante a execução: {e}")
            time.sleep(15)
