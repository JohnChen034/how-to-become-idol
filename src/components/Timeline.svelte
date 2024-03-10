<script>
    import { onMount } from 'svelte';
    import { quadInOut } from 'svelte/easing';
    import { tweened } from 'svelte/motion';

    let timeline = [
        { year: "Year 0~1", label: "Audition", color: "#f1c40f" },
        { year: "Year 1~5", label: "Trainee Start", color: "#e74c3c" },
        { year: "Year 5", label: "Debut", color: "#2ecc71" },
        { year: "Year 5~", label: "Release songs and Albums", color: "#9b59b6" },
        { year: "Year ~", label: "Other Idol activities", color: "#3498db" },

    ];

    const width = 900;
    let duration = 500;
    let index = tweened(0, {duration, easing: quadInOut});
    let dotSize = tweened(3, {duration: 200, easing: quadInOut});

    onMount(() => {
        const interval = setInterval(next, 2500); // Slow down for smoother visual effect

        return () => {
            clearInterval(interval);
        };
    });

    function next() {
        $dotSize = 3;
        if ($index < timeline.length - 1) {
            $index++;
        } else {
            $index = 0;
        }

        setTimeout(() => $dotSize = 10, 500); // Increase for more emphasis
    }
</script>

<!--{-60+$index*200}-->
<svg viewBox="-10 0 {width} 120">
    <!-- Define a gradient for the line -->
    <defs>
        <linearGradient id="lineGradient" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:#e74c3c;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#f1c40f;stop-opacity:1" />
        </linearGradient>
    </defs>

    <line x1="20" y1="95" x2="0" y2="95" stroke="url(#lineGradient)"/>

    {#each timeline as event, i}
        <g>
            <text
                class="label"
                x={25 + i * 200}
                y={$index === i ? 40 : 20}
                text-anchor="middle"
                fill={$index === i ? event.color : '#666'}
            >
                {event.label}
            </text>
            <text
                class="year"
                x={25 + i * 200}
                y={$index === i ? 80 : 60}
                text-anchor="middle"
                font-weight={$index === i ? '700' : '400'}
                fill={$index === i ? event.color : '#555'}
            >
                {event.year}
            </text>
            <circle
                cx={25 + i * 200}
                cy="95"
                r={$index === i ? $dotSize : 3}
                fill={$index === i ? event.color : 'orange'}
                stroke-width="2"
                stroke={$index === i ? 'white' : 'none'}
                style="transition: all 0.3s ease;"
            />
        </g>
    {/each}
</svg>

<style>
    :global(body) {
        display: flex;
        /*justify-content: center; !* Center the SVG horizontally *!*/
        /*align-items: center; !* Center the SVG vertically *!*/
        height: 150vh; /* Take full viewport height */
        margin: 0;
		margin-top: auto;
    }
    svg {
        overflow: visible;
    }
    text {
        transition: fill 0.3s ease, font-size 0.3s ease;
        cursor: pointer;
    }
    .year {
        font-size: 2rem;
        transition: all 0.3s ease;
    }
    .label {
        font-size: 1rem;
        transition: all 0.3s ease;
    }
    line {
        stroke-width: 5px;
        stroke-dasharray: 2 2;
        transition: stroke-dashoffset 0.5s ease;
    }
    circle {
        cursor: pointer;
        transition: all 0.3s ease;
        filter: drop-shadow(0 4px 4px rgba(0,0,0,0.2)); /* Shadow for depth */
    }

</style>
