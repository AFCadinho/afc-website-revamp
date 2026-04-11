const API_BASE = "/api"

export async function fetchHomeMessage(): Promise<string> {
    const response = await fetch(`${API_BASE}/`)

    if (!response.ok) {
        throw new Error("Failed to fetch home message")
    }

    return response.text()
}