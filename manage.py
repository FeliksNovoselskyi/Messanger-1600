from app.settings import main_app

def main():
    try:
        main_app.run(
            debug = True,
            port = 8000
        )
        
    except Exception as error:
        print(f"Помилка під час запуску проєкта: {error}")

if __name__ == "__main__":
    main()
