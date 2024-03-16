<script>
    export let index;
</script>

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
        opacity: 0;
        animation: fadeInUp 0.5s ease-out forwards;
        animation-delay: 0.5s;
    }
</style>

{#if index > 10}

<div class="a">
    <h1 style="font-family: 'IBM Plex Sans', sans-serif; font-weight: 600; font-size:120px; color:#393537;">
        Conclusion
    </h1>
</div>
{/if}