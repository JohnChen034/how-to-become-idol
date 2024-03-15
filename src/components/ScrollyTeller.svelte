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
    <div class="progress-bars">
      <p>current section: <strong>{index + 1}/{count}</strong></p>
      <progress value={count ? (index + 1) / count : 0} />

      <p>offset in current section</p>
      <progress value={offset || 0} />

      <p>total progress</p>
      <progress value={progress || 0} />
    </div>
  </div>

  <div class="foreground" slot="foreground">

    <section>
      This is the first section.
      <div class="head_container">
        <h1 style="font-size: 4rem;">The Journey of a Nobody to a Super Idol</h1>
        <FlipCard/>
      </div>
    </section>

    <section>
      This is the second section.
      <Hook />
    </section>

    <section>
      This is the third section.
      <Timeline />
    </section>

    <section>
      This is the forth section.
      <TraineeDebutRate />
    </section>

    <section>
      This is the fifth section.
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
    margin: 0 auto;
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
    width.
    height: 80vh;
    background-color: rgba(0, 0, 0, 0.2); /* 20% opaque */
    /* color: white; */
    outline: magenta solid 3px;
    text-align: center;
    max-width: 750px; /* adjust at will */
    color: black;
    padding: 1em;
    margin: 0 0 2em 0;
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
