import speedtest
import datetime
import keyboard
import time
import os

def create_csv():
    if not os.path.exists("speedtest_results.csv"):
        with open("speedtest_results.csv", "w") as file:
            file.write("data,hora,Download,Upload,ping,server_name,server_location\n")

def run_speedtest():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        st.download()
        st.upload()
        results = st.results.dict()
        return results
    except speedtest.ConfigRetrievalError as e:
        print("Erro ao recuperar configuração:", e)
        return None
    except Exception as e:
        print("Ocorreu um erro inesperado:", e)
        return None

def save_results(results):
    if results:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d,%H:%M:%S")
        download_mbps = results['download'] / 1_000_000
        upload_mbps = results['upload'] / 1_000_000
        ping = results['ping']
        server_name = results['server']['host']
        server_location = results['server']['name']
        with open("speedtest_results.csv", "a") as file:
            file.write(f"{timestamp},{download_mbps:.2f} Mbps,{upload_mbps:.2f} Mbps,{ping} ms,{server_name},{server_location}\n")
        print(f"Data e Hora: {timestamp}")
        print(f"Download: {download_mbps:.2f} Mbps")
        print(f"Upload: {upload_mbps:.2f} Mbps")
        print(f"Ping: {ping} ms")
        print(f"Nome do Servidor: {server_name}")
        print(f"Localização do Servidor: {server_location}")
    else:
        print("Nenhum resultado para salvar.")

def monitor_speedtest():
    print("Pressione 'q' para sair do monitoramento.")
    while not keyboard.is_pressed('q'):
        results = run_speedtest()
        save_results(results)
        print("-" * 40)
        time.sleep(60)  

if __name__ == "__main__":
    create_csv()
    monitor_speedtest()
