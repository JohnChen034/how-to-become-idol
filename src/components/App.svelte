<script>
  import { onMount } from 'svelte';

  let people = [];

  onMount(async () => {
    const response = await fetch('people.json');
    people = await response.json();
  });
</script>

<svg width="5000" height="5000">
  {#each people as person (person.id)}
    <image
      href="/person_icon1.jpeg"
      x={person.x - person.radius}
      y={person.y - person.radius}
      width={person.radius * 2}
      height={person.radius * 2}
    />




  {/each}
</svg>
