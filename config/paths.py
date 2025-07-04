from pathlib import Path   

# Define the base directory
BASE_DIR = Path(__file__).resolve().parent.parent
# This assumes the script is in a subdirectory of the project root
# Adjust the path as necessary if the structure is different

# Define paths for various directories
DB_DIR = BASE_DIR / "database"
MODEL_DIR = BASE_DIR / "models"

# Ensure the directories exist
DB_DIR.mkdir(parents=True, exist_ok=True)
# Path to library.db, in root. (Before Dockerfile was implemented, this was in the database directory)
LIBRARY_DB_PATH = DB_DIR / "library.db"

# Dockerfile will copy the database file to the container
DATA_DIR = BASE_DIR / "data"
# Ensure the data directory exists
DATA_DIR.mkdir(parents=True, exist_ok=True)
# Define the database URL
DB_URL = f"sqlite:///{DATA_DIR / 'library.db'}"

def print_all ()-> None:
    print(f"BASE_DIR: {BASE_DIR}")
    print(f"DB_DIR: {DB_DIR}")
    print(f"MODEL_DIR: {MODEL_DIR}")
    print(f"LIBRARY_DB_PATH: {LIBRARY_DB_PATH}")
    print(f"DB_URL: {DB_URL}")

if __name__ == "__main__":
    print_all()