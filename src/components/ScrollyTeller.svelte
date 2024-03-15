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

    
    <section style="">
      <p2>
        <div class="head_container">
        <h1 style="font-family: 'IBM Plex Sans', sans-serif; font-weight: 600;">
          The Journey of a Nobody to a Super Idol
        </h1>
        <FlipCard/>
        </div>
      </p2>
    </section>

      
    <section style="">
      <Hook />
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
  @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=IBM+Plex+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap');

  .background {
    width: 100%;
    height: 100vh;
    position: relative;
    outline: green solid 3px;
  }

  .foreground {
    width: 80%;
    height: auto;
    position: relative;
    outline: red solid 3px;
  }

  section {
    width: 100%;
    height: 100vh;
    background-color: rgba(0, 0, 0, 0.2); /* 20% opaque */
    outline: magenta solid 3px;
    text-align: center;
    color: black;
    padding: 1em;
    margin: 0 0 2em 0;
  }

  .p2 {
    position: relative;
    outline: blue solid 3px;
  }

  .head_container {
    height: 100vh;
    display: flex;
    gap: 20px;
    padding: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.4);
    background-color: white;
    border-radius: 50px 50px 50px 50px;
    overflow: hidden;
    position: absolute;
  }

  .h1 {
    margin: 20px 0;
    font-family: 'IBM Plex Sans', sans-serif;
    font-weight: 600;
    font-size: 80;
    color: black;
  }
</style>
