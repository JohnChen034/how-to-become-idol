<script>
  let images = [
    'slide1.png',
    'slide2.png',
    'slide3.png',
    'slide4.png',
    'slide5.png'
  ];
  let currentImageIndex = 0;
export let index;
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
    position: relative; /* Added to position the buttons absolutely relative to this container */
  }

  img {
    width:60vw;
    height:65vh;
    border-radius: 10px; /* Optional: for rounded corners */
  }

  button {
    padding: 0; /* Changed from 10px to 0 to remove padding */
    cursor: pointer;
    background-color: #C5C5C5; /* Button background color */
    border: none;
    position: absolute; /* Position buttons absolutely */
    top: 50%; /* Center vertically */
    transform: translateY(-50%);
    border-radius: 50%; /* Make button round */
    width: 50px; /* Button width */
    height: 50px; /* Button height */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Button shadow */
  }

  /* Create the arrow inside the button using pseudo-elements */
  button::before {
    content: '';
    display: inline-block;
    border: solid black;
    border-width: 0 3px 3px 0; /* Controls the thickness of the arrow */
    padding: 10px; /* Arrow size */
    transform: translate(-50%, -50%) rotate(270deg); /* Adjust these values to change the arrow's angle */
    position: absolute;
    top: 50%;
    left: 50%;
  }

  /* Adjust button positioning */
  .carousel-container > button:first-child {
    left: 10px;
    transform: translateY(-50%) rotate(-135deg);
  }

  .carousel-container > button:last-child {
    right: 10px;
    transform: translateY(-50%) rotate(45deg);
  }
    @keyframes fadeIn {
    to {
      opacity: 1;
    }
  }
</style>

<!--{#if index > 3}-->

<div class="carousel-container">
  <button on:click={showPrevious}></button>
  <img src={images[currentImageIndex]} alt="Carousel Image">
  <button on:click={showNext}></button>
</div>

<!--{/if}-->
