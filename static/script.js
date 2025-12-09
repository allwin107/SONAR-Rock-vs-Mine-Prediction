document.addEventListener('DOMContentLoaded', () => {
    const sonarInput = document.getElementById('sonar-data');
    const analyzeBtn = document.getElementById('analyze-btn');
    const clearBtn = document.getElementById('clear-btn');
    const fillRockBtn = document.getElementById('fill-rock');
    const fillMineBtn = document.getElementById('fill-mine');
    const resultSection = document.getElementById('result-section');
    const resultContent = document.getElementById('result-content');
    const loader = document.getElementById('loader');
    const predictionBadge = document.getElementById('prediction-badge');
    const confidenceBar = document.getElementById('confidence-bar');
    const confidenceValue = document.getElementById('confidence-value');

    // Sample Data
    const sampleRock = "0.0200,0.0371,0.0428,0.0207,0.0954,0.0986,0.1539,0.1601,0.3109,0.2111,0.1609,0.1582,0.2238,0.0645,0.0660,0.2273,0.3100,0.2999,0.5078,0.4797,0.5783,0.5071,0.4328,0.5550,0.6711,0.6415,0.7104,0.8080,0.6791,0.3857,0.1307,0.2604,0.5121,0.7547,0.8537,0.8507,0.6692,0.6097,0.4943,0.2744,0.0510,0.2834,0.2825,0.4256,0.2641,0.1386,0.1051,0.1343,0.0383,0.0324,0.0232,0.0027,0.0065,0.0159,0.0072,0.0167,0.0180,0.0084,0.0090,0.0032";

    // Using Row 208 from csv which is a Mine
    const sampleMine = "0.0260,0.0363,0.0136,0.0272,0.0214,0.0338,0.0655,0.1400,0.1843,0.2354,0.2720,0.2442,0.1665,0.0336,0.1302,0.1708,0.2177,0.3175,0.3714,0.4552,0.5700,0.7397,0.8062,0.8837,0.9432,1.0000,0.9375,0.7603,0.7123,0.8358,0.7622,0.4567,0.1715,0.1549,0.1641,0.1869,0.2655,0.1713,0.0959,0.0768,0.0847,0.2076,0.2505,0.1862,0.1439,0.1470,0.0991,0.0041,0.0154,0.0116,0.0181,0.0146,0.0129,0.0047,0.0039,0.0061,0.0040,0.0036,0.0061,0.0115";

    fillRockBtn.addEventListener('click', () => {
        sonarInput.value = sampleRock;
        resetResult();
    });

    fillMineBtn.addEventListener('click', () => {
        sonarInput.value = sampleMine;
        resetResult();
    });

    clearBtn.addEventListener('click', () => {
        sonarInput.value = '';
        resetResult();
    });

    analyzeBtn.addEventListener('click', async () => {
        const inputData = sonarInput.value.trim();
        if (!inputData) {
            alert("Please enter sonar data.");
            return;
        }

        // Show loader
        resultSection.classList.remove('hidden');
        loader.classList.remove('hidden');
        resultContent.classList.add('hidden');

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ features: inputData }),
            });

            const data = await response.json();

            if (response.ok) {
                displayResult(data.prediction, data.confidence);
            } else {
                alert(`Error: ${data.error}`);
                resultSection.classList.add('hidden');
            }
        } catch (error) {
            alert("Failed to connect to the server.");
            resultSection.classList.add('hidden');
        } finally {
            loader.classList.add('hidden');
        }
    });

    function displayResult(prediction, confidence) {
        resultContent.classList.remove('hidden');

        predictionBadge.textContent = prediction;
        predictionBadge.className = 'badge'; // Reset class

        // Remove % sign for width calculation
        const confidenceNum = parseFloat(confidence);

        if (prediction === 'Rock') {
            predictionBadge.classList.add('rock');
            confidenceBar.style.backgroundColor = 'var(--accent-rock)';
        } else {
            predictionBadge.classList.add('mine');
            confidenceBar.style.backgroundColor = 'var(--accent-mine)';
        }

        confidenceValue.textContent = confidence;
        confidenceBar.style.width = confidence;
    }

    function resetResult() {
        resultSection.classList.add('hidden');
    }
});
