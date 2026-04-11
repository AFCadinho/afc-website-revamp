const API_BASE = "/api"

export async function fetchHomeMessage(): Promise<string> {
    const response = await fetch(`${API_BASE}/`)

    if (!response.ok) {
        const body = await response.text()
        throw new Error(`Failed to fetch home message: ${response.status} ${body}`)
    }

    return response.text()
}

export async function fetchTeams() {
    const response = await fetch(`${API_BASE}/teams/`)

    if (!response.ok) {
        const body = await response.text()
        throw new Error(`Failed to fetch teams: ${response.status} ${body}`)
    }

    return response.json()
}