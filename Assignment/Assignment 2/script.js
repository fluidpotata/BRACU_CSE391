var quotes=[
    "Some pretty cool quote"
]

function generateQuote() {
    const quotetplace = document.getElementById('quote');
    quotetplace.textContent = quotes[0];
}