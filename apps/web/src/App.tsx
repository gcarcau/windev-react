import React, { useEffect, useState } from 'react'

export default function App() {
    const [health, setHealth] = useState<string>('...')

    useEffect(() => {
        fetch('/api/health')
            .then((r) => r.json())
            .then((j) => setHealth(j.status))
            .catch(() => setHealth('unreachable'))
    }, [])

    return (
        <div style={{ padding: 20 }}>
            <h1>App Web (Vite)</h1>
            <p>API health: {health}</p>
        </div>
    )
}
