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

    /* This is section1 */;
    <section>
      <div class="head_container">
        <h1 style="font-size: 4rem;">The Journey of a Nobody to a Super Idol</h1>
        <FlipCard/>
      </div>
    </section>

    /* This is section2 */;   
    <section style="background-color: white;">
      <Hook />
    </section>

    /* This is section3 */;
    <section>
      <Timeline />
    </section>

    /* This is section4 */;
    <section>
      <TraineeDebutRate />
    </section>

    /* This is section5 */;
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
    outline: red solid 3px;
  }

  .progress-bars {
    position: absolute;
    background: rgba(170, 51, 120, 0.2) /*  40% opaque */;
    visibility: visible;
  }

  section {
    width: 100%;
    height: 100vh;
    background-color: white;
    outline: magenta solid 3px;
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
  }

  h1 {
    margin: 20px 0;
    font-family: cursive, sans-serif;
    font-weight: 600;
    font-size: 2rem;
    color: black;
  }
</style>
