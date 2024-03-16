<script>
  let images = [
    'difficulty1.PNG',
    'difficulty2.PNG',
    'difficulty3.PNG',
    'difficulty4.PNG',
    'difficulty5.PNG'
  ];
  let currentImageIndex = 0;

  function nextImage() {
    currentImageIndex = (currentImageIndex + 1) % images.length;
  }

  function previousImage() {
    currentImageIndex =
      (currentImageIndex - 1 + images.length) % images.length;
  }
</script>

<div class="image-slider">
  <button on:click={previousImage}>&lt;</button>
  <img src={images[currentImageIndex]} alt="Sliding Image" />
  <button on:click={nextImage}>&gt;</button>
</div>

<style>
  .image-slider {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%; /* Adjust as needed */
    height: 100vh; /* Adjust as needed */
  }

  .image-slider img {
    width: 100%; /* Adjust as needed */
    height: auto; /* Adjust as needed */
    /* Add styles for transitions if needed */
  }

  button {
    /* Add button styling here */
  }
</style>
