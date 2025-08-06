"""Database configuration"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./movies.db"

# # Créer un moteur de base de données (engine) qui établit la connexion avec notre base SQLite (movies.db).
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} # Pour SQLite, il est nécessaire de spécifier `check_same_thread=False` pour désactiver la restriction multitheads pour permettre l'accès à la base de données depuis plusieurs threads.(car il peut avoir plusieurs utilisatuers concurrentiels dans une application qui requete l'api au même moment.)
)

# Définir SessionLocal, qui permet de créer des sessions pour interagir avec la base de données.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# autocommit=False signifie que les transactions ne seront pas automatiquement validées, ce qui permet de contrôler manuellement quand les modifications sont enregistrées dans la base de données.
# autoflush=False signifie que les modifications ne seront pas automatiquement synchronisées avec la base de données avant chaque requête, ce qui peut améliorer les performances dans certains cas.
# blind=engine signifie que la session sera liée au moteur de base de données que nous avons créé précédemment, ce qui permet d'exécuter des requêtes sur cette base de données.


# Définir Base, qui servira de classe de base pour nos modèles SQLAlchemy.
Base = declarative_base()

if __name__ == "__main__":
    try:
        with engine.connect() as conn:
            print("Connexion à la database réussie")
    except Exception as e:
        print(f"Erreur de connexion à la database : {e}")