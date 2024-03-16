<script>
  import FlipCard from './FlipCard.svelte';
  import Hook from "./hook.svelte"
  import BTSone from "./BTSone.svelte"
  import BTStwo from "./BTStwo.svelte"
  import TraineeDebutRate from "./TraineeDebutRate.svelte";
  import Scroller from "@sveltejs/svelte-scroller";
  import Bmi_graph from "./bmi_graph.svelte";
  import LoseWeight from "./loseWeight.svelte";
  import Talents from "./Talents.svelte";
  import TransitionOne from "./TransitionOne.svelte";
  import TransitionTwo from "./TransitionTwo.svelte";
  import Transition3 from "./Transition3.svelte";
  import Conclusion from "./conclusion.svelte"
  import ConclusionTwo from "./conclusionTwo.svelte"
  import VizExplain from "./vizExplain.svelte"
  import YouShouldKnow from "./youShouldKnow.svelte"
  import YouShouldKnowTwo from "./youShouldKnowTwo.svelte"


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
        <h1 style="font-family: 'IBM Plex Sans', sans-serif; font-weight: 600; font-size:100px; color:#393537;">
          The Journey of a Nobody to a Super Idol
        </h1>
        <FlipCard/>
        <p style="font-family: 'IBM Plex Sans', sans-serif; font-weight: 600; font-size:50px; color:#393537;">Darren Liu, Jiayu Chen</p>
      </div>
    </section>

      
    <section style="background-color:#b37eb5;">
        <Hook {index}/>
    </section>


    <section style="background-color:#b37eb5; justify-content: flex-start; flex-direction: row;">
      <div class="container">
        <BTSone {index}/>
      </div>
      <img src="bts.png" alt="bts member photo" class="bts-member"/>
    </section>


    <section style="background-color:#b37eb5;">
      <h1 style="font-family: 'IBM Plex Sans', sans-serif; font-weight: 600; font-size:80px; color:#393537;">
        Let's See How Tough BTS Suffered Before Debut!!!
      </h1>
      <BTStwo {index}/>
    </section>

    
    <section>
      <TraineeDebutRate  {index}/>
    </section>


    <section>
    <TransitionOne {index}/>

    </section>


    <section>
      <Talents {index}></Talents>
    </section>


    <section>


      <TransitionTwo {index}></TransitionTwo>
    </section>


    <section>
      <Bmi_graph {index}></Bmi_graph>
    </section>


    <section>
<Transition3 {index}/>
    </section>


    <section>
      <LoseWeight  {index}></LoseWeight>
    </section>


    <section>
      <Conclusion />
    </section>


    <section>
      <ConclusionTwo />
    </section>

    <section style="justify-content: flex-start; flex-direction: row;">
      <VizExplain />
    </section>

    <section>
      <YouShouldKnow />
    </section>

    <section>
      <YouShouldKnowTwo />
    </section>
  </div>
</Scroller>


<style>
  @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=IBM+Plex+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap');

  :global(body) {
    margin: 0;
  }
  .background {
    width: 100%;
    height: 100vh;
    position: relative;
    /*outline: green solid 3px;*/
  }


  .foreground {
    width: 100%;
    margin: 0 auto;
    height: auto;
    position: relative;
  }

  section {
    height: 100vh;
    width: 100%;
    background-color: #b37eb5;
    text-align: center;
    color: black;
    margin: 0 0 0 0;
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

  .container
  .loseWeight_container {
    height: 80vh;
    width: 75vw;
    gap: 20px;
    background-color: #b37eb5;
    display: flex; /* Use flexbox for positioning the child */
    justify-content: center; /* Center horizontally */
    align-items: center; /* Center vertically */
    flex-direction: column; /* Stack children vertically */
    border-radius: 50px 50px 50px 50px;
    overflow: hidden;
  }

  .bts-member {
    padding-top: 10px;    /* Padding at the top */
    padding-right: 15px;  /* Padding on the right */
    padding-bottom: 5px;  /* Padding at the bottom */
    padding-left: 50px;   /* Padding on the left */
    border-radius: 50px 50x 20px 20px;
  }
</style>
