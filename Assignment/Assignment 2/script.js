var quotes= [
    "Your greatest strength lies in the courage to embrace uncertainty.",
    "A unexpected conversation will unlock a hidden opportunity this week.",
    "Patience is not about waiting, but how you move while waiting.",
    "The smallest kindness can create the most profound ripple.",
    "Your creativity is a compass, not confined by traditional maps.",
    "Trust the journey, even when the path seems unclear.",
    "Success whispers in the moments others call failures.",
    "Your dreams are seeds - water them with consistent effort.",
    "Wisdom often arrives disguised as a simple moment of clarity.",
    "The universe rewards those who dare to reimagine possibility."
    ];
function generateQuote() {
    const quotetplace = document.getElementById('quote');
    const choice = Math.floor(Math.random() * quotes.length);
    quotetplace.textContent = quotes[choice];
}

function changeColor(clr) {
    let colors = {
        "color" : {"red": "#FF2929", "green": "#62825D", "blue": "#4335A7", "orange": "#FF885B"},
        "backgroundColor" : {"red": "rgba(255, 0, 0, 0.1)", "green": "rgba(0, 255, 0, 0.1)", "blue": "rgba(0, 0, 255, 0.1)", "orange": "rgba(255, 136, 91, 0.1)"},
        "borderColor" : {"red": "#FF2929", "green": "#62825D","blue": "#4335A7","orange": "#FF885B",},
        "font" : {"red": "Lucida Sans Unicode", "green": "Lucida Grande", "blue": "Trebuchet MS", "orange": "Lucida Sans",},
        "fontSize" : {"red": "16px", "green": "20px", "blue": "18px", "orange": "19px",}
    };
    quotebox = document.getElementById("quote-box");
    quotebox.style.color = colors["color"][clr];
    quotebox.style.backgroundColor = colors["backgroundColor"][clr];
    quotebox.style.borderColor = colors["borderColor"][clr];
    quotebox.style.fontFamily = colors["font"][clr];
    quotebox.style.fontSize = colors["fontSize"][clr];

}

function convert() {
    const dropdownMenu = document.getElementById("conv-dropdown");
    const enteredValue = document.getElementById("conv-val");
    const resultArea = document.getElementById("conv-result");
    const selectedUnit = dropdownMenu.value;
    const inputVal = enteredValue.value;
    if (selectedUnit=="lb") {
        var outputVal = inputVal* 0.4536;
        resultArea.textContent = `${inputVal} Pound = ${outputVal} Kilograms`
    } else if (selectedUnit=='kg') {
        var outputVal = inputVal* 2.2046;
        resultArea.textContent = `${inputVal} Kilograms = ${outputVal} Pound`
    }

}