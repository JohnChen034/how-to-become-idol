<script>

    export let index;
</script>

{#if index > 4}

    <h1 class="a" style="">
        What aspects do the companies apply to filters applicants?
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