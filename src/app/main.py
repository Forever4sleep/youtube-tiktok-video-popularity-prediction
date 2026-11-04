from .settings import settings


def main() -> None:
    print("S3 Key:", settings.app.s3_key)
    print("Google API Key:", settings.app.google_api_key)

if __name__ == "__main__":
    main()  
