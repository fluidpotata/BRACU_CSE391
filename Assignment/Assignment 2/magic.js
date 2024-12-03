const textArea = document.getElementById('formDisplay');
let isCapitalized = false;

function clearAll() {
    textArea.value = '';
}

function toggleCapitalize() {
    if (isCapitalized) {
        textArea.value = textArea.value.toLowerCase();
        isCapitalized = false;
    } else {
        textArea.value = textArea.value.toUpperCase();
        isCapitalized = true;
    }
}

function sortLines() {
    const lines = textArea.value.split('\n');
    lines.sort();
    textArea.value = lines.join('\n');
}

function reverseLines() {
    const lines = textArea.value.split('\n');
    const reversedLines = [];
    for (let i = 0; i < lines.length; i++) {
        reversedLines.push(lines[i].split('').reverse().join(''));
    }
    textArea.value = reversedLines.join('\n');
}

function stripBlank() {
    const lines = textArea.value.split('\n');
    const strippedLines = [];
    for (let i = 0; i < lines.length; i++) {
        const trimmedLine = lines[i].trim();
        if (trimmedLine !== '') {
            strippedLines.push(lines[i]);
        }
    }
    textArea.value = strippedLines.join('\n');
}
function addNumbers() {
    const lines = textArea.value.split('\n');
    const numberedLines = [];
    for (let i = 0; i < lines.length; i++) {
        const trimmedLine = lines[i];
        numberedLines.push((i + 1) + '. ' + trimmedLine);
    }
    textArea.value = numberedLines.join('\n');
}

function shuffleLines() {
    const lines = textArea.value.split('\n');
    const nonEmptyLines = [];
    for (let i = 0; i < lines.length; i++) {
        nonEmptyLines.push(lines[i]);
    }
    for (let i = nonEmptyLines.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        const temp = nonEmptyLines[i];
        nonEmptyLines[i] = nonEmptyLines[j];
        nonEmptyLines[j] = temp;
    }
    textArea.value = nonEmptyLines.join('\n');
}