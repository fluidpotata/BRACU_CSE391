var quotes=[
    "Some pretty cool quote"
]

function generateQuote() {
    const quotebox = document.getElementById('quote-box');
    quotebox.textContent = quotes[0];
}