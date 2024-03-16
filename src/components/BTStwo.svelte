<script>
  import Carousel from "svelte-carousel";
  const images = [
    {
      url: "static/difficulty1.PNG",
      description: "image1",
    },
    {
      url: "static/difficulty2.PNG",
      description: "image2",
    },
    {
      url: "static/difficulty3.PNG",
      description: "image3",
    },
    {
      url: "static/difficulty4.PNG",
      description: "image4",
    },
    {
      url: "static/difficulty5.PNG",
      description: "image5",
    },
  ];
  let carousel; // for calling methods of the carousel instance
  const handleNextClick = () => {
    carousel.goToNext();
  };
</script>

<Carousel
    bind:this={carousel}
    let:loaded
    autoplay
    autoplayDuration={3000}
    autoplayProgressVisible
>
    {#each images as src, imageIndex (src)}
      <div class="img-container">
        {#if loaded.includes(imageIndex)}
          <img src={src.url} alt={src.description} width={1000} height={600} />
        {/if}
      </div>
    {/each}
</Carousel>