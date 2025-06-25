from pathlib import Path   

# Define the base directory
BASE_DIR = Path(__file__).resolve().parent

# Define paths for various directories
DB_DIR = BASE_DIR / "database"
MODEL_DIR = BASE_DIR / "models"

# Path to library.db
LIBRARY_DB_PATH = DB_DIR / "library.db"


def print_all ()-> None:
    print(f"BASE_DIR: {BASE_DIR}")
    print(f"DB_DIR: {DB_DIR}")
    print(f"MODEL_DIR: {MODEL_DIR}")

if __name__ == "__main__":
    print_all()