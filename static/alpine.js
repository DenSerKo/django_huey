document.addEventListener('alpine:init', () => {
    Alpine.data('fetcher', () => ({
        count: 1,
        person: {},

        async fetchData() {
            try {
                const url = `https://fake-json-api.mock.beeceptor.com/users/${this.count}`
                console.log(url)
                const response = await fetch(url)
                if (!response.ok) {
                    throw new Error("Network error")
                }
                this.person = await response.json()
            } catch (error) {
                console.log(error.message)
            }
        }
    }))
})