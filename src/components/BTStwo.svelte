<script>
  let images = [
    'bts.png'
  ];
  let currentImageIndex = 0;

  function showNext() {
    currentImageIndex = (currentImageIndex + 1) % images.length;
  }

  function showPrevious() {
    currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
  }
</script>

<style>
  .carousel-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 20px;
  }

  img {
    max-width: 100%;
    border-radius: 10px; /* Optional: for rounded corners */
  }

  button {
    padding: 10px;
    cursor: pointer;
  }
</style>

<div class="carousel-container">
  <button on:click={showPrevious}>Previous</button>
  <img src={images[currentImageIndex]} alt="Carousel Image">
  <button on:click={showNext}>Next</button>
</div>
