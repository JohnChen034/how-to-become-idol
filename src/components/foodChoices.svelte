<script>
  import { onMount } from 'svelte';
  export let imgLinks;
  export let mealName;
  let state = false;
  let menuElement;

  function expand() {
    state = !state; // Change to true only for automatic expansion
  }
    function scrollExpand() {
    state = true; // Change to true only for automatic expansion
  }

  onMount(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            scrollExpand();
          }
        });
      },
      {
        // Adjust these options to control when the callback is invoked
        // For example, threshold: 0.5 means the callback will run when 50% of the element is visible
        threshold: 0.1
      }
    );

    observer.observe(menuElement);

    return () => {
      observer.unobserve(menuElement);
    };
  });
</script>

<style>
  .menu {
    display: flex;
    position: relative;
    width: 300px;
    margin-left: 50px;

  }
  .menu {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: flex-start;
    position: relative;
    width: 130%;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    border-radius: 20px;
    margin: 10px;
    margin-left: 50px;
  }
  .toggle {
    height: 60px;
    width: 80px;
    display: flex;
    font-family: Cursive;
    align-items: center;
    justify-content: center;
    transition: 1s;
    cursor: pointer;
    margin: 40px;
    transition: transform .2s;
    border-radius: 70px ;
  }
  .toggle:hover {
    transform: scale(1.2);
  }
  .items {
    display: flex;
    flex-direction: row;
    transform-origin: left;
    transition: 0.5s;
    transform: scaleX(var(--scale, 0));
  }
  img {
    width: 80px;
  height: 140px;
    margin-right: 10px; /* Space between images */
    border-radius: 10px; /* Rounded corners for images */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Shadow for images */
  }

    p {
    margin: 0; /* Remove margin from <p> to fix alignment */
    font-size: 1em; /* Adjust text size as needed */
    user-select: none; /* Prevent text from being selectable */
  }
</style>

<div class="menu" bind:this={menuElement}>
  <div class="toggle" on:click={expand}>
        <p>{mealName}</p>
  </div>
  <div class="items" style="--scale: {state ? 3 : 0};">
    {#each imgLinks as link}
      <img src={link} alt="Food image" />
    {/each}
  </div>
</div>
