from app.ingestion.youtube import YouTubeTranscriptService


def main() -> None:
    url = input("Enter YouTube URL: ").strip()

    service = YouTubeTranscriptService()

    document = service.ingest(url)

    print("\n" + "=" * 60)
    print("TRANSCRIPT")
    print("=" * 60)

    print(f"Characters: {len(document.transcript):,}")
    print(f"Words: {len(document.transcript.split()):,}")
    print(f"Video ID: {document.video_id}")
    print(f"URL: {document.source_url}")

    print("\nFirst 1000 characters:\n")
    print(document.transcript[:1000])


if __name__ == "__main__":
    main()