<script>
    let currentImage = null;
    let selectedButton = null;

    // Function to change the image and the selected button
    function showImage(imageNumber) {
        currentImage = `bts${imageNumber}.PNG`;
        selectedButton = imageNumber;
    }
</script>

<div class=container>
    <h1>The Rise of K-pop</h1>
    <p>K-pop has huge increase in popularity. More and more K-pop groups get recognition by global music awards</p>

    <h1>Street Casting</h1>
    <p>Street casting is that the casting staff in agencies scouts and casts people on the streets to finds and fosters new talent.</p>
    <p>The following slides shows of how casting staff find new talent</p>

    <!-- Buttons -->
    <button on:click={() => showImage(1)} class:selected={selectedButton === 1}>1</button>
    <button on:click={() => showImage(2)} class:selected={selectedButton === 2}>2</button>
    <button on:click={() => showImage(3)} class:selected={selectedButton === 3}>3</button>
    <button on:click={() => showImage(4)} class:selected={selectedButton === 4}>4</button>
    <button on:click={() => showImage(5)} class:selected={selectedButton === 5}>5</button>

<!-- Image Display -->
{#if currentImage}
  <img src={currentImage} width=1000 height=500 alt="Displayed image" />
{/if}

    <h2>The Career Path of BTS</h2>
    <h2>We would like to explore:</h2>
    <p>The mystery behind K-pop agencies transforming ordinary people into K-pop idols</p>
</div>

<style>
  .selected {
    background-color: #007bff; /* Blue color, you can change it to whatever you want */
    color: white;
  }
</style>