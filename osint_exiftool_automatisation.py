import os
import subprocess
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Chemin du dossier à surveiller
WATCH_FOLDER = r"./stub/" # Dossier des documents à analyser
EXIFTOOL_PATH = r"exiftool.exe" # Chemin vers exiftool.exe (dans mon cas le chemin est spécifié dans PATH)
RESULTS_FOLDER = os.path.join(WATCH_FOLDER, "./results")

# Créer le dossier "results" s'il n'existe pas
os.makedirs(RESULTS_FOLDER, exist_ok=True)

class WatcherHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:  # Vérifie si c'est bien un fichier
            self.process_file(event.src_path)

    def process_file(self, file_path):
        print(f"Nouveau fichier détecté : {file_path}")
        output_file = f"{file_path}.txt"

        # Récupérer le nom du fichier sans son extension
        base_name = os.path.basename(file_path)
        name, ext = os.path.splitext(base_name)

        # Construire le chemin du fichier de sortie
        output_file = os.path.join(RESULTS_FOLDER, f"{name}.txt")
        print(f"here : {file_path}")

        try:
            result = subprocess.run([EXIFTOOL_PATH, "-charset", "UTF8", file_path], capture_output=True, text=True, encoding="utf-8")

            if result.stdout:
                # Sauvegarder les métadonnées dans un fichier texte
                with open(output_file, "w", encoding="utf-8") as f:
                    f.write(result.stdout)
            
                shutil.copy2(file_path, RESULTS_FOLDER)
                os.remove(file_path)
                print(f"Métadonnées enregistrées dans : {output_file}")
            else:
                print(f"Aucune Métadonnées enregistrées pour : {output_file}")
            
        except Exception as e:
            print(f"Erreur lors de l'analyse : {e}")



if __name__ == "__main__":
    event_handler = WatcherHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_FOLDER, recursive=False)

    print(f"Surveillance du dossier : {WATCH_FOLDER}")
    observer.start()

    try:
        while True:
            pass  # Laisse le programme tourner en boucle
    except KeyboardInterrupt:
        observer.stop()
        print("Arrêt de la surveillance.")

    observer.join()
