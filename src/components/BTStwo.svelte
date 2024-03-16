<script>
  import { onMount } from 'svelte';

  let sentences = [
    "BTS is one of the most successful boy bands in South Korea, ",
    "with a huge global fan base and many authoritative awards",
    "However,",
    "Behind their tremendous success, there lies an unseen side of hardships."
  ];
  let displaySentences = [];

  onMount(() => {
    sentences.forEach((sentence, index) => {
      setTimeout(() => {
        displaySentences = [...displaySentences, sentence];
      }, 2000 * index); // Adjust the delay as needed for sentences
    });
  });
</script>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=IBM+Plex+Sans:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&display=swap');

  .sentence {
    opacity: 0;
    animation: fadeIn 1s forwards;
    margin-top: 30px;
    margin-bottom: 30px;
    font-size: 50px;
    font-family: 'IBM Plex Sans', sans-serif;
    font-weight: 600;
    text-align: center;
    color:#393537;; /* dark Grey */;
  }

  @keyframes fadeIn {
    to {
      opacity: 1;
    }
  }
</style>

<div>
  {#each displaySentences as sentence, index (sentence)}
    <div class="sentence" style="animation-delay: {index * 0.2}s">{sentence}</div>
  {/each}
</div>