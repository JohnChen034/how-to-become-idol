<script>
  import ScrollyTeller from './ScrollyTeller.svelte'
</script>

<main>
  <ScrollyTeller />
</main>

<style>
  html, body {
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
    overflow: hidden; /* This prevents any scrollbars from the body if your content is larger than the viewport */
  }
</style>
