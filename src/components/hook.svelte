<script>
  import { onMount } from 'svelte';

  let sentences = [
    "Have you ever think of becoming a K-pop idol?",
    "If yes,",
    "Do you know how difficult it is to be selected as a trainee in the audition?",
    "Do you know how much effort it takes to debut?"
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

  .sentence {
    opacity: 0;
    animation: fadeIn 1s forwards;
    margin-bottom: 10px;
    font-size: 50px;
    font-family: 'Roboto';
    text-align: left;
    color: #2B2929; /* dark Grey */;
  }

  @keyframes fadeIn {
    to {
      opacity: 1;
    }
  }
</style>

<div>
  {#each displaySentences as sentence, index (sentence)}
    <div class="sentence" style="animation-delay: {index * 0.5}s">{sentence}</div>
  {/each}
</div>