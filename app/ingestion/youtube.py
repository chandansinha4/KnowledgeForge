from __future__ import annotations

from urllib.parse import parse_qs, urlparse

from youtube_transcript_api import YouTubeTranscriptApi

from app.domain.transcript import TranscriptDocument


class YouTubeTranscriptService:
    """
    Service responsible for extracting transcripts from YouTube videos.
    """

    def __init__(self) -> None:
        self._client = YouTubeTranscriptApi()

    async def ingest(
        self,
        url: str,
    ) -> TranscriptDocument:
        """
        Extract the transcript from a YouTube video URL.
        """

        video_id = self._extract_video_id(url)

        transcript = self._client.fetch(
            video_id,
            languages=["en"],
        )

        transcript_text = " ".join(
            snippet.text
            for snippet in transcript
        )

        return TranscriptDocument(
            title="",
            transcript=transcript_text,
        )

    def _extract_video_id(
        self,
        url: str,
    ) -> str:
        """
        Extract the YouTube video ID from a URL.
        """

        parsed_url = urlparse(url)

        if parsed_url.hostname in {"youtu.be", "www.youtu.be"}:
            video_id = parsed_url.path.lstrip("/")

        elif parsed_url.hostname in {
            "youtube.com",
            "www.youtube.com",
            "m.youtube.com",
        }:
            video_id = parse_qs(
                parsed_url.query,
            ).get("v", [None])[0]

        else:
            video_id = None

        if not video_id:
            raise ValueError("Invalid YouTube URL.")

        return video_id