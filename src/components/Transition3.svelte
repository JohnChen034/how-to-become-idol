<script>

    export let index;
</script>

{#if index > 8}

    <h1 class="a" >
      <h1 style="font-family: 'IBM Plex Sans', sans-serif; font-weight: 600; font-size:50px; color:#393537;">
        Faces under Camera
      </h1>
      <p style="font-family: 'IBM Plex Sans', sans-serif; font-weight: 500; font-size:25px; color:#393537;">
        Taking pictures with a lens will naturally widen the portrait, but now most LCD TV screens have a display ratio
        of 16:9, which will further widen the portrait. It can be said that I am very picky. Below is a classic
        experimental picture illustrating the faces under different films.
      </p>
      <img src="faceOnCamera.png" alt="" style="width: 500px; height: 500px">
    </h1>
{/if}


<style>

    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    .a {
        font-family: 'IBM Plex Sans', sans-serif;
        font-weight: 600;
        font-size: 80px;
        color: #393537;
        opacity: 0;
        animation: fadeInUp 0.5s ease-out forwards;
        animation-delay: 0.5s;
    }
</style>