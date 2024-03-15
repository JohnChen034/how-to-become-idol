<script>
  import { onMount } from 'svelte';

  let text = "Have you ever think of becoming a K-pop idol?";
  let words = text.split(' ');
  let displayWords = [];

  onMount(() => {
    words.forEach((word, index) => {
      setTimeout(() => {
        displayWords = [...displayWords, word];
      }, 500 * index); // Adjust the delay as needed
    });
  });
</script>

<style>
  .word {
    opacity: 0;
    animation: fadeIn 1s forwards;
  }

  @keyframes fadeIn {
    to {
      opacity: 1;
    }
  }
</style>

<div>
  {#each displayWords as word, index (word)}
    <span class="word" style="animation-delay: {index * 0.5}s">{word} </span>
  {/each}
</div>




<p>Have you ever think of becoming an K-pop idol?</p>
<p>If yes</p>
<p>Do you know how difficult it is to be selected as a trainee in the audition</p>
<p>Do you know how much effort it takes to debut</p>