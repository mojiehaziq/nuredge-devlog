const clientKey = "YOUR_CLIENT_KEY";
const redirectURI = "https://mojiehaziq.github.io/nuredge-devlog/redirect.html";
const scope = "user.info.basic,video.upload";
const authURL = `https://www.tiktok.com/auth/authorize?client_key=${clientKey}&scope=${scope}&response_type=code&redirect_uri=${redirectURI}`;

document.getElementById("loginBtn").onclick = () => {
    window.location.href = authURL;
};

// Simulate Infinite Noon live data feed
function updateInfiniteNoon() {
    document.getElementById("noonData").innerText = "Entropy sync: " + Math.floor(Math.random() * 1000) + " TB streaming";
}
setInterval(updateInfiniteNoon, 3000);

// Simulate trending hashtags
const trends = ["#NovaCoreAI", "#BillionAPI", "#TikTokAutomation", "#InfiniteNoon", "#NurEdgeOS"];
function updateTrends() {
    const list = document.getElementById("trendList");
    list.innerHTML = "";
    trends.forEach(tag => {
        const li = document.createElement("li");
        li.textContent = tag;
        list.appendChild(li);
    });
}
updateTrends();