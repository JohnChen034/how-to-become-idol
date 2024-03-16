<script>
    export let index;

    
</script>

<style>
    .a {
        opacity: 0;
        animation: fadeInUp 0.5s ease-out forwards;
        animation-delay: 0.5s;
    }
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
</style>

{#if index > 9}
<div class="a">
    <h1 style="font-family: 'IBM Plex Sans', sans-serif; font-weight: 600; font-size:120px; color:#393537;">
        The path from a nobody to a super idol is extremely tough and difficult!!!
      </h1>
</div>