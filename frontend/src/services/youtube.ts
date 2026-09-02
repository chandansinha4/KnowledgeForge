import type { YouTubeResponse } from "../types/youtube"

const API_BASE_URL = "http://localhost:8000"

export async function processYouTubeVideo(
  url: string,
): Promise<YouTubeResponse> {
  const response = await fetch(
    `${API_BASE_URL}/api/v1/youtube`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ url }),
    },
  )

  if (!response.ok) {
    throw new Error(
      "Failed to process the YouTube video.",
    )
  }

  return response.json()
}