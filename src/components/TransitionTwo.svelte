<script>

    export let index;
</script>

{#if index > 6}

    <div class="a">
              <div style="display: flex;
        justify-content: center; /* Align horizontal center */
        align-items: center; /* Align vertical center */
        text-align: center;">
        <h1 style="font-family: 'IBM Plex Sans', sans-serif; font-weight: 600; font-size:80px; color:#393537;">
          How skinny idols are expected to be?
        </h1>
      </div>
    </div>

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