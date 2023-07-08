import datetime
import time
import shutil
import json

def copy_files(source, destination):
    try:
        shutil.copy2(source, destination)
        print(f"Arquivo {source} copiado para {destination}")
        with open("log.txt", "a") as log_file:
            log_file.write(f"{source} copiado para {destination}\n")
    except FileNotFoundError:
        print(f"Arquivo {source} não encontrado.")
        with open("log.txt", "a") as log_file:
            log_file.write(f"Arquivo {source} não encontrado\n")
    except Exception as e:
        print(f"Erro ao copiar arquivo: {str(e)}")
        with open("log.txt", "a") as log_file:
            log_file.write(f"Erro ao copiar arquivo: {str(e)}\n")

def load_config(file_path):
    with open(file_path) as config_file:
        config = json.load(config_file)
    return config

def run_scheduler(config):
    while True:
        current_time = datetime.datetime.now()
        print(f"Data e hora atuais: {current_time}")

        current_day = current_time.weekday()
        current_hour = current_time.hour
        current_minute = current_time.minute

        for schedule in config['schedule']:
            if schedule['day'] == current_day:
                for event in schedule['events']:
                    if current_hour == event['hour'] and current_minute >= event['minute'] and current_minute <= 59:
                        copy_files(event['source'], event['destination'])

        time.sleep(60)  # Aguarda 60 segundos antes de verificar novamente

print("Script em execução...")
config = load_config("config.json")
run_scheduler(config)
