<script>
  import {fade} from 'svelte/transition';
  import FlipCard from './FlipCard.svelte';
  import Hook from "./hook.svelte"
  import Timeline from './Timeline.svelte';
  import TraineeDebutRate from "./TraineeDebutRate.svelte";
  import Pyramid from "./pyramid.svelte"
  import { onMount } from "svelte";
  import Scroller from "@sveltejs/svelte-scroller";

  let layerVisible = 0;
  function showNextLayer() {
    layerVisible = (layerVisible + 1) % 5; // Cycle through 0-4
  }

  let count, index, offset, progress;
</script>

<Scroller
  top={0.0}
  bottom={1}
  threshold={0.5}
  bind:count
  bind:index
  bind:offset
  bind:progress
>
  <div class="background" slot="background">
  </div>

  <div class="foreground" slot="foreground">

    
    <section>
      <div class="head_container">
        <h1 style="font-size: 4rem;">The Journey of a Nobody to a Super Idol</h1>
        <FlipCard/>
      </div>
    </section>

      
    <section style="background-color: white;">
      <div class="head_container" >
          <Hook />
      </div>
    </section>

    
    <section>
      <Timeline />
    </section>

    
    <section>
      <TraineeDebutRate />
    </section>

    
    <section>
      <Pyramid />
    </section>

  </div>
</Scroller>


<style>
  .background {
    width: 100%;
    height: 100vh;
    position: relative;
    outline: green solid 3px;
  }

  .foreground {
    width: 100%;
    margin: 0;
    height: auto;
    position: relative;
  }

  section {
    width: 100%;
    height: 100vh;
    background-color: white;
    text-align: center;
    color: black;
  }

  .head_container {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 20px;
    padding: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
    background-color: white;
    border-radius: 50px 50px 50px 50px;
    overflow: hidden;
  }

  h1 {
    margin: 20px 0;
    font-family: cursive, sans-serif;
    font-weight: 600;
    font-size: 2rem;
    color: black;
  }
</style>
