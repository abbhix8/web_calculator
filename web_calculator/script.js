// Clear the display
function clearDisplay() {
    document.getElementById("display").value = "";
}

// Append a value to the display
function appendValue(value) {
    document.getElementById("display").value += value;
}

// Calculate the result
function calculateResult() {
    try {
        let expression = document.getElementById("display").value;
        let result = eval(expression);
        document.getElementById("display").value = result;
    } catch (error) {
        alert("Invalid Expression");
    }
}
