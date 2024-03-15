<script>
  import {fade} from 'svelte/transition';
  import FlipCard from './FlipCard.svelte';
  import Timeline from './Timeline.svelte';
  import TraineeDebutRate from "./TraineeDebutRate.svelte";
  import BeforeTrainee from "./beforeTrainee.svelte";
  import Hook from "./hook.svelte"
  import { onMount } from "svelte";
  import Scroller from '@sveltejs/svelte-scroller';

  let layerVisible = 0;
  function showNextLayer() {
    layerVisible = (layerVisible + 1) % 5; // Cycle through 0-4
  }
</script>

<Scroller>
  <div class="page">
    <h1>The Journey of a Nobody to a Super Idol</h1>
    <FlipCard />
  </div>
  
  <div class="page">
    <Hook />
  </div>

  <div class="page">
    <Timeline />
  </div>

  <div class="page">
    <TraineeDebutRate />
  </div>
</Scroller>

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

  .page {
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
  }
</style>
