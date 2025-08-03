function testAPI() {
    const mockData = {
        status: "success",
        platform: "NovaCore TikTok API",
        version: "v1.0",
        message: "API connected successfully!",
        sample_user: {
            username: "novacore_ai",
            followers: 1234567,
            engagement_rate: "8.5%"
        }
    };
    document.getElementById("api-output").textContent = JSON.stringify(mockData, null, 2);
}