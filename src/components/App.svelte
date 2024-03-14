<script>
  import {fade} from 'svelte/transition';
  import FlipCard from './FlipCard.svelte';
  import Timeline from './Timeline.svelte';
  import TraineeDebutRate from "./TraineeDebutRate.svelte";
  import kpopTrendLineChart from "./kpopTrendLineChart.svelte";
  import { onMount } from "svelte";

  let layerVisible = 0;
  function showNextLayer() {
    layerVisible = (layerVisible + 1) % 5; // Cycle through 0-4
  }

  let kpopTrend;

  onMount(async () => {
    const response = await fetch('kpopTrend.json');
    kpopTrend = await response.json();
  });


</script>

<main>
  <div class="head_container">
    <h1 style="font-size: 4rem;">The Journey of a Nobody to a Super Idol</h1>
    <FlipCard/>

  </div>

  <p>some content here, introduction stuff</p>
  <p>some content here, introduction stuff</p>

  <kpopTrendLineChart kpopTrend={kpopTrend}></kpopTrendLineChart>

  <Timeline/>

  <TraineeDebutRate></TraineeDebutRate>

  <svg width="1000" height="1000" viewBox="20 0 160 200" xmlns="http://www.w3.org/2000/svg" on:click={showNextLayer}>
    <text x="100" y="170" text-anchor="middle" font-size="16" font-family="Arial" fill="black">Click to show more!!
    </text>

    <!-- Draw and color each layer within the triangle with fade transition and hover effect -->
    {#if layerVisible > 0}
      <polygon in:fade={{ duration: 500 }}
               points="30,150 50,110 150,110 170,150"
               fill="#c6e5f3"
               class="layer"
      />
      <text x="100" y="135" text-anchor="middle" font-size=10 font-family="Arial" fill="black">Audition</text>
    {/if}
    {#if layerVisible > 1}
      <polygon in:fade={{ duration: 500 }}
               points="50,110 70,70 130,70 150,110"
               fill="#a4d4c4"
               class="layer"
      />
      <text x="100" y="95" text-anchor="middle" font-size=10 font-family="Arial" fill="black">Trianee</text>
    {/if}
    {#if layerVisible > 2}
      <polygon in:fade={{ duration: 500 }}
               points="70,70 85,40 115,40 130,70"
               fill="#f9e2af"
               class="layer"
      />
      <text x="100" y="60" text-anchor="middle" font-size=10 font-family="Arial" fill="black">Debut</text>
    {/if}
    {#if layerVisible > 3}
      <polygon in:fade={{ duration: 500 }}
               points="100,10 85,40 115,40"
               fill="#e3c1f4"
               class="layer"
      />
      <text x="100" y="35" text-anchor="middle" font-size=10 font-family="Arial" fill="black">Super Idol</text>
    {/if}

  </svg>



</main>

<style>
  main {
    /*display: flex;*/
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    /*height: 1000vh;*/
    margin: 0 auto;
  }

  .head_container {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 20px;
    padding: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
    background-color: white;
  }

  h1 {
    margin: 20px 0;
    font-family: cursive, sans-serif;
    font-weight: 600;
    font-size: 2rem;
    color: black;
  }

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
