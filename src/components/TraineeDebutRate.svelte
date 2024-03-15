<script>
    let dots = [];
    const center = {x: 750, y: 750}; // Center of the circle
    const maxRadius = 700; // Maximum radius of the filled circle
    const dotRadius = 4; // Radius of each dot
    const spacing = 12.5; // Space between dots
    let userCount = 10000; // Default number of dots or user's input

    // Function to generate dots
    function generateDots() {
        let tempDots = [];
        let dotCounter = 0; // Counter to track the number of dots generated

        for (let r = dotRadius; r < maxRadius; r += spacing) {
            let circumference = 2 * Math.PI * r;
            let dotsPerLevel = Math.floor(circumference / spacing);

            for (let i = 0; i < dotsPerLevel; i++) {
                if (dotCounter >= userCount) { // Check if the count has reached the user-specified number
                    return tempDots;
                }
                let angle = (i / dotsPerLevel) * Math.PI * 2;
                let x = center.x + r * Math.cos(angle);
                let y = center.y + r * Math.sin(angle);
                tempDots.push({x, y});
                dotCounter++;
            }
        }
        return tempDots;
    }

    // Function to handle user input for the number of dots
    function handleUserInput() {
        userCount = parseInt(document.getElementById('dotCountInput').value, 10) || 0;
        dots = generateDots(); // Regenerate dots with new user count
        let resultElement = document.getElementById('resultInputText');
        const temp_length = dots.length

        resultElement.textContent = `You generate ${temp_length} applicants`; // Update the text
        document.getElementById('traineeButton').disabled = false;
        document.getElementById('debutButton').disabled = false;
    }

    // Function to remove 98% of the dots
    function removeTraineeDots() {
        const temp_length = dots.length
        let remainingDotsCount = Math.floor(dots.length * 0.02); // 2% of dots
        let shuffledDots = [...dots].sort(() => 0.5 - Math.random()); // Shuffle array
        dots = shuffledDots.slice(0, remainingDotsCount); // Keep only 2% of the dots
        let resultElement = document.getElementById('resultTraineeText');
        resultElement.textContent = `For ${temp_length} applicants, only ${remainingDotsCount} become trainees.`; // Update the text
        document.getElementById('traineeButton').disabled = true;
    }

    function removeDebutDots() {
        const temp_length = dots.length
        let remainingDotsCount = Math.floor(dots.length * 0.05);
        let shuffledDots = [...dots].sort(() => 0.5 - Math.random());
        dots = shuffledDots.slice(0, remainingDotsCount);
        let resultElement = document.getElementById('resultDebutText');
        resultElement.textContent = `For ${temp_length} trainees, only ${remainingDotsCount} debut successfully each year.`; // Update the text
        document.getElementById('debutButton').disabled = true;
    }

</script>

<div class="container">
    <h1>How much chance do you think you can successfully debut?</h1>
    <h2>Answer: 2% x (1-5%)^t x 5%; "t" represents training period in years</h2>


    <p>Try yourself! Enter the number of Applicants you expect each year:</p>
    <p>
        Reference: In the case of S.M. Entertainment, the company receives 300,000
        applicants in nine countries every year.
    </p>
    <input type="number" id="dotCountInput" value="10000">

    <br>
    <br>
    <br>
    <button id="generateButton" on:click={handleUserInput}>Generate (9761 max)</button>

    <p id="resultInputText"></p>


    <button id="traineeButton" on:click={removeTraineeDots} disabled>Applicants that becomes trainees</button>

    <p id="resultTraineeText"></p>

    <button id="debutButton" on:click={removeDebutDots} disabled>Trainees that debut this year</button>

    <p id="resultDebutText"></p>

    <!-- Your SVG stays the same -->
    <svg id="svgContainer" width="100%" height="800" viewBox="0 0 1500 1500">
        {#each dots as {x, y}}
            <circle cx={x} cy={y} r={dotRadius} fill="black"/>
        {/each}
    </svg>
</div>


<style>
    body {
        font-family: "Arial", sans-serif;
        background-color: #f9f9f9;
        color: #333;
        margin: 0;
        padding: 0;
    }

    .container {
        width: 1200px;
        margin: 50px auto;
        padding: 20px;
        background-color: #fff;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    h1,
    h2 {
        color: #007bff;
        text-align: center;
    }

    p {
        line-height: 1.6;
    }

    button {
        background-color: #007bff;
        color: #fff;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s;
    }

    button:hover {
        background-color: #0056b3;
    }
</style>