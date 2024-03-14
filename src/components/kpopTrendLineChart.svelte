<script>
  import * as d3 from "d3";
  import { onMount } from "svelte";

  let kpopTrendData;

  onMount(async () => {
    const response = await fetch('kpopTrend.json');
    kpopTrend = await response.json();
    // You would then pass kpopTrendData to your D3 chart-drawing logic
  });

  // The chart dimensions and margins as optional props.
  export let width = 1000;
  export let height = 400;
  export let marginTop = 60;
  export let marginRight = 30;
  export let marginBottom = 60;
  export let marginLeft = 60;

  const startDate = d3.timeParse("%Y-%m")("2004-01");
  const endDate = d3.timeParse("%Y-%m")("2024-03");
  
  // Create the x (horizontal position) scale.
  const xScale = d3.scaleTime()
    .domain([startDate, endDate])
    .range([marginLeft, width - marginRight]);

  // Create the y (vertical position) scale.
  const yScale = d3.scaleLinear()
    .domain([0, 100])
    .range([height - marginBottom, marginTop]);

  // Creating lines
  const line = d3
      .line()
      .x((d) => xScale(new Date(d.Month)))
      .y((d) => yScale(d.Trend));
</script>

<main>
  <svg
    {width}
    {height}
    viewBox="0 0 {width} {height}"
    style:max-width="100%"
    style:height="auto"
  >

    <!-- Title -->
    <text
      x={(width - marginLeft - marginRight) / 2 + marginLeft}
      y={marginTop / 2}
      fill="currentColor"
      font-family="Trebuchet MS"
      font-size="24px"
      text-anchor="middle"
    >
      Popularity of Kpop Groups
    </text>

    <!-- x axis Title -->
    <text
      x={(width - marginLeft - marginRight) / 2 + marginLeft}
      y={height}
      fill="currentColor"
      font-family="Trebuchet MS"
      font-size="15px"
      text-anchor="middle"
    >
      Month, Year
    </text>

    <!-- X-Axis -->
    <g transform="translate(0,{height - marginBottom})">
      <line stroke="currentColor" stroke-width=2 stroke-opacity="0.3" x1={marginLeft - 6} x2={width} />

      {#each xScale.ticks() as tick}
        <!-- X-Axis Ticks -->
        <line
          stroke="currentColor"
          stroke-opacity="0.3"
          x1={xScale(tick)}
          x2={xScale(tick)}
          y1={0}
          y2={6}
        />

        <!-- X-Axis Tick Labels -->
        <text fill="currentColor" font-family='Trebuchet MS' text-anchor="middle" x={xScale(tick)} y={22}>
          {tick.getFullYear()}
        </text>
      {/each}
    </g>

    <!-- y axis Title -->
    <text
      x={(width - marginLeft - marginRight) / 2 + marginLeft -150}
      y={-470}
      fill="currentColor"
      font-family="Trebuchet MS"
      font-size="15px"
      text-anchor="middle"
      transform="rotate(-90, {(width - marginLeft - marginRight) / 2 + marginLeft}, {marginTop / 2})"
    >
      Trend
    </text>

    <!-- Y-Axis and Grid Lines -->
    <g transform="translate({marginLeft},0)">
      {#each [0, 25, 50, 75, 100] as tick}
        {#if tick !== 0}
          <!-- 
            Grid Lines. 
            Note: First line is skipped since the x-axis is already present at 0. 
          -->
          <line
            stroke="currentColor"
            stroke-opacity="0.1"
            x1={0}
            x2={width - marginLeft}
            y1={yScale(tick)}
            y2={yScale(tick)}
          />

          <!-- 
            Y-Axis Ticks. 
            Note: First tick is skipped since the x-axis already acts as a tick. 
          -->
          <line
            stroke="currentColor"
            stroke-opacity="0.1"
            x1={0}
            x2={-6}
            y1={yScale(tick)}
            y2={yScale(tick)}
          />
        {/if}

        <!-- Y-Axis Tick Labels -->
        <text
          fill="currentColor"
          text-anchor="end"
          dominant-baseline="middle"
          font-family='Trebuchet MS'
          x={-9}
          y={yScale(tick)}
        >
          {tick}
        </text>
      {/each}
    </g>

    {#each lines as line, index}
      <path
        fill="none"
        stroke="red"
        stroke-width="3"
        d={kpopTrend}
      />
    {/each}
  </svg>
</main>