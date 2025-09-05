document.addEventListener('DOMContentLoaded', () => {
    // Get references to all necessary HTML elements
    const calculateButton = document.getElementById('calculate-button');
    const coordinatesInput = document.getElementById('coordinates-input');
    const cepOutput = document.getElementById('cep-output');
    const meanXOutput = document.getElementById('mean-x-output');
    const meanYOutput = document.getElementById('mean-y-output');
    const stdXOutput = document.getElementById('std-x-output');
    const stdYOutput = document.getElementById('std-y-output');
    const inputError = document.getElementById('input-error');

    // Add a click event listener to the "Calculate" button
    calculateButton.addEventListener('click', () => {
        // Hide any previous error messages
        inputError.classList.add('hidden');
        
        // Get the user's input and clean up whitespace
        const inputValue = coordinatesInput.value.trim();

        // Validate that input exists
        if (!inputValue) {
            inputError.textContent = "Please enter coordinate data.";
            inputError.classList.remove('hidden');
            return;
        }

        // Split the input into lines, trim whitespace from each, and filter out any empty lines
        const lines = inputValue.split(/\r?\n/).map(l => l.trim()).filter(l => l.length > 0);
        const coordinates = [];

        // Loop through each line to parse the coordinates
        for (const line of lines) {
            const parts = line.split(',');
            
            // Validate that there are exactly two parts (x and y)
            if (parts.length !== 2) {
                inputError.textContent = "Each line must contain exactly two numbers separated by a comma.";
                inputError.classList.remove('hidden');
                return;
            }

            // Parse the x and y values as floating-point numbers
            const x = parseFloat(parts[0].trim());
            const y = parseFloat(parts[1].trim());

            // Validate that the parsed values are numbers
            if (isNaN(x) || isNaN(y)) {
                inputError.textContent = "Please enter valid numerical coordinates.";
                inputError.classList.remove('hidden');
                return;
            }

            // Add the valid coordinate pair to our array
            coordinates.push({ x, y });
        }

        // Validate that there are at least two data points for calculation
        if (coordinates.length < 2) {
            inputError.textContent = "At least two coordinate pairs are required for calculation.";
            inputError.classList.remove('hidden');
            return;
        }

        // Calculate the mean of x and y coordinates
        const meanX = coordinates.reduce((sum, p) => sum + p.x, 0) / coordinates.length;
        const meanY = coordinates.reduce((sum, p) => sum + p.y, 0) / coordinates.length;

        // Calculate the sum of squared differences from the mean for both axes
        const sumSqDiffX = coordinates.reduce((sum, p) => sum + Math.pow(p.x - meanX, 2), 0);
        const sumSqDiffY = coordinates.reduce((sum, p) => sum + Math.pow(p.y - meanY, 2), 0);

        // Calculate the sample standard deviation for both axes
        const stdX = Math.sqrt(sumSqDiffX / (coordinates.length - 1));
        const stdY = Math.sqrt(sumSqDiffY / (coordinates.length - 1));

        // Calculate the radial standard deviation
        const sigmaR = Math.sqrt(stdX * stdX + stdY * stdY);

        // Calculate the CEP value using the simplified constant (≈ 1.17741)
        const cepValue = 1.17741 * sigmaR;

        // Update the HTML elements with the final results, formatted to 2 or 3 decimal places
        cepOutput.textContent = cepValue.toFixed(3);
        meanXOutput.textContent = meanX.toFixed(2);
        meanYOutput.textContent = meanY.toFixed(2);
        stdXOutput.textContent = stdX.toFixed(2);
        stdYOutput.textContent = stdY.toFixed(2);
    });
});
