<script>
  import { fade } from 'svelte/transition';
  let layerVisible = 0;

  function showNextLayer() {
    layerVisible = (layerVisible + 1) % 5; // Cycle through 0-4
  }
</script>

<main>
  <h1>Interactive Colored Triangle Layers</h1>

  <button on:click={showNextLayer}>Show Next Layer</button>

  <svg width="1000" height="1000" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
    <!-- Draw the outer triangle -->
    <polygon points="100,10 10,190 190,190" fill="none" stroke="black" stroke-width="0"/>

    <!-- Draw and color each layer within the triangle with fade transition and hover effect -->
    {#if layerVisible > 0}
      <polygon in:fade={{ duration: 500 }}
               points="30,150 50,110 150,110 170,150"
               fill="#c6e5f3"
               class="layer"
      />
    {/if}
    {#if layerVisible > 1}
      <polygon in:fade={{ duration: 500 }}
               points="50,110 70,70 130,70 150,110"
               fill="#a4d4c4"
               class="layer"
      />
    {/if}
    {#if layerVisible > 2}
      <polygon in:fade={{ duration: 500 }}
               points="70,70 85,40 115,40 130,70"
               fill="#f9e2af"
               class="layer"
      />
    {/if}
    {#if layerVisible > 3}
      <polygon in:fade={{ duration: 500 }}
               points="100,10 85,40 115,40"
               fill="#e3c1f4"
               class="layer"
      />
    {/if}
  </svg>
</main>

<style>
  /* Add styles here if necessary */
  svg {
    display: block;
    margin: auto;
    background-color: #fff; /* white background */
  }

  button {
    display: block;
    margin: 1em auto;
    padding: 0.5em 1em;
    font-size: 1em;
    cursor: pointer;
  }

  /* Style for layer hover effect */
  .layer:hover {
    fill-opacity: 0.7; /* Adjust opacity to make the layer look brighter on hover */
  }

</style>
