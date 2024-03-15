<script>
  import {fade} from 'svelte/transition';
  import FlipCard from './FlipCard.svelte';
  import Hook from "./hook.svelte"
  import Timeline from './Timeline.svelte';
  import TraineeDebutRate from "./TraineeDebutRate.svelte";
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

    
    <section style="background-color:#b37eb5;">
      <div class="head_container">
        <h1 style="font-family: 'IBM Plex Sans', sans-serif; font-weight: 600; font-size:50px;">
          The Journey of a Nobody to a Super Idol
        </h1>
        <FlipCard/>
      </div>
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
    width: 95%;
    margin: 0 auto;
    height: auto;
    position: relative;
    outline: red solid 3px;
  }

  section {
    height: 100vh;
    width: 97%;
    background-color: rgba(0, 0, 0, 0.2); /* 20% opaque */
    outline: magenta solid 3px;
    text-align: center;
    color: black;
    margin: 0 0 2em 0;
    display: flex; /* Use flexbox for positioning the child */
    justify-content: center; /* Center horizontally */
    align-items: center; /* Center vertically */
    flex-direction: column; /* Stack children vertically */
  }

  .head_container {
    height: 95vh;
    width: 75vw;
    gap: 20px;
    padding: 20px;
    background-color: #b37eb5;
    display: flex; /* Use flexbox for positioning the child */
    justify-content: center; /* Center horizontally */
    align-items: center; /* Center vertically */
    flex-direction: column; /* Stack children vertically */
  }

  .h1 {
    margin: 20px 0;
    font-family: 'IBM Plex Sans', sans-serif;
    font-weight: 600;
    font-size: 80;
    color: black;
  }
</style>
