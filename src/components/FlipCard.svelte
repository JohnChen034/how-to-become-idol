<script>
  let flipped = false;

  function toggleFlip() {
    flipped = !flipped;
  }
</script>

<div class="card" on:click={toggleFlip}>
  <div class="card-content" style="--rotate: {flipped ? 180 : 0}deg;">
    <div class="card-front">
      <!-- Display the "nobody" image on the front -->
      <img src="flip_nobody.png" alt="Nobody">
    </div>
    <div class="card-back">
      <!-- Display the "idol" image on the back -->
      <img src="flip_idol.png" alt="Super K-pop Idol">
    </div>
  </div>
</div>

<style>
  .card {
    width: 400px;
    height: 600px;
    perspective: 1000px;
    cursor: pointer;
  }

  .card-content {
    width: 100%;
    height: 100%;
    position: relative;
    transition: transform 0.6s;
    transform-style: preserve-3d;
    transform: rotateY(var(--rotate, 0deg));
  }

  .card-front,
  .card-back {
    width: 100%;
    height: 100%;
    background-color: white;
    position: absolute;
    backface-visibility: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 24px;
    border: 1px solid #ccc;
  }

  .card-front img,
  .card-back img {
    max-width: 100%;
    max-height: 100%;
  }

  .card-front {
    background-color: black;
  }

  .card-back {
    background-color: black;
    transform: rotateY(180deg);
  }
</style>
