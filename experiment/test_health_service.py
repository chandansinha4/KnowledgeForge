from app.core.config import settings
from app.health.service import HealthService


def main() -> None:
    service = HealthService(settings)

    status = service.get_status()

    print(status)


if __name__ == "__main__":
    main()