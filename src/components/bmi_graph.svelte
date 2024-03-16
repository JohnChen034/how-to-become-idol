<script>
    import {onMount} from 'svelte';
    import * as d3 from 'd3';

    export let index;
    let idolsData = [];

    onMount(async () => {
        const data = await d3.csv('debut_idols_data.csv');
        idolsData = processData(data);
        renderChart(idolsData.male, 'male');
        renderChart(idolsData.female, 'female');

    });

    function processData(data) {
        data.forEach(d => {
            d.Height = +d.Height;
            d.Weight = +d.Weight;
            d.BMI = d.Weight / (d.Height / 100) ** 2;
        });

        const bmiCategories = ['Underweight', 'Normal', 'Overweight', 'Obese'];
        const bmiCategoryRanges = [0, 18.5, 25, 30, Infinity];

        data.forEach(d => {
            const bmiIndex = bmiCategoryRanges.findIndex((value, index, array) => d.BMI < array[index + 1]);
            d.BMICategory = bmiCategories[bmiIndex - 1];
        });

        const male = data.filter(d => d.Gender === 'M');
        const female = data.filter(d => d.Gender === 'F');

        return {male, female};
    }

    function renderChart(data, gender) {
        const svg = d3.select(`#scatter-plot-${gender}`);
        const margin = {top: 20, right: 20, bottom: 30, left: 40};
        const width = +svg.attr('width') - margin.left - margin.right;
        const height = +svg.attr('height') - margin.top - margin.bottom;


        let filteredData = data.filter(d => {
            return isFinite(d.BMI) && d.Height !== 0 && d.Weight !== 0;
        });

        // Set specific domain ranges for male and female
        let xDomain, yDomain;
        if (gender === 'male') {
            xDomain = [160, d3.max(data, d => d.Height)];
            yDomain = [30, 100];
        } else if (gender === 'female') {
            xDomain = [140, d3.max(data, d => d.Height)];
            yDomain = [30, 100];
        }

        const x = d3.scaleLinear()
            .domain(xDomain)
            .range([0, width]);

        const y = d3.scaleLinear()
            .domain(yDomain)
            .range([height, 0]);


        const bmiColorScale = d3.scaleLinear()
            .domain([0, 18.5, 25, 30, 35])
            .range(['grey', 'blue', 'green', 'orange', 'red'])
            .interpolate(d3.interpolateRgb);

        const g = svg.append('g')
            .attr('transform', `translate(${margin.left},${margin.top})`);

        g.append('g')
            .attr('transform', `translate(0,${height})`)
            .call(d3.axisBottom(x));

        g.append('g')
            .call(d3.axisLeft(y));

        g.selectAll('.dot')
            .data(filteredData)
            .enter().append('circle')
            .attr('class', 'dot')
            .attr('r', 2)
            .attr('cx', d => x(d.Height))
            .attr('cy', d => y(d.Weight))
            .style('fill', d => bmiColorScale(d.BMI));

        // Add title
        svg.append('text')
            .attr('x', (width / 2))
            .attr('y', margin.top / 2 + 40)
            .attr('text-anchor', 'middle')
            .style('font-size', '16px')
            .style('text-decoration', 'underline')
            .text(`${gender === 'male' ? 'Male' : 'Female'} BMI Distribution`);

        const gradientId = `gradient-${gender}`;
        const defs = svg.append('defs');
        const linearGradient = defs.append('linearGradient')
            .attr('id', gradientId)
            .attr('x1', '0%')
            .attr('x2', '0%')
            .attr('y1', '100%')
            .attr('y2', '0%');

        bmiColorScale.range().forEach((color, index, array) => {
            linearGradient.append('stop')
                .attr('offset', `${(index / (array.length - 1)) * 100}%`)
                .attr('stop-color', color);
        });

    const legend = svg.selectAll(".legend")
        .data(bmiColorScale.domain())
        .enter().append("g")
        .attr("class", "legend")
        .attr("transform", function(d, i) { return "translate(0," + i * 20 + ")"; });

    // Draw legend colored rectangles
    legend.append("rect")
        .attr("x", width - 18)
        .attr("width", 18)
        .attr("height", 18)
        .style("fill", bmiColorScale);

    // Draw legend text
    legend.append("text")
        .attr("x", width +5)
        .attr("y", 9)
        .attr("dy", ".35em")
        .style("text-anchor", "start")
        .text(function(d) { return '< ' + d; });

    }


</script>

{#if index > 7}

    <div class="a">
        <div class="content-container">
    <div class="text-container">
        <p class="intro-text">below is an analysis on the BMI from the current debutted idols body data</p>

        <p></p>
        <img src="bmi_chart.png" alt="BMI Chart" class="bmi-chart-image">
        <p class="additional-info">'As you see in the graphs, the range of BMI is mostly underweight for male and especially female idols'</p>

    </div>
    <div class="charts-container">
        <svg id="scatter-plot-male" width="500" height="400"></svg>
        <svg id="scatter-plot-female" width="500" height="400"></svg>
    </div>
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
        opacity: 0;
        animation: fadeInUp 0.5s ease-out forwards;
        animation-delay: 0.5s;
    }
    body {
        background-color: #5e4b8b; /* Set the background to purple */
        color: #fff; /* Set the text color to white for contrast */
        font-family: "Arial", sans-serif;
    }

    .content-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        max-width: 1200px; /* Adjust as needed */
        margin: 0 auto;
        padding: 20px;
        gap: 20px;
    }

    .text-container {
        text-align: center;
    }

    .intro-text {
        font-weight: bold;
        margin-bottom: 10px;
    }

    .additional-info {
        font-style: italic;
        margin-top: 10px;
    }

    .bmi-chart-image {
        max-width: 100%;
        height: auto;
        border: 3px solid #fff; /* A white border around the image for contrast */
        border-radius: 4px; /* Slight rounding of corners */
        padding: 4px; /* Spacing around the image */
        margin: 20px 0; /* Space above and below the image */
    }

    .charts-container {
        display: flex;
        justify-content: space-between;
        gap: 50px; /* Adjust the gap between the SVGs */
    }

    .legend {
        font-size: 12px;
        font-family: Arial, sans-serif;
        fill: #fff; /* Set legend text to white */
    }

    .legend rect {
        stroke: #fff;
        stroke-width: 1px; /* A thinner stroke for the legend boxes */
    }

    svg {
        border: 1px solid #fff; /* A white border for contrast */
        border-radius: 4px;
        background-color: #f0e6f6; /* A lighter purple background for the SVG */
        overflow: visible;
    }
    .dot {
        stroke: #000;
    }

    svg {
        margin-left: 50px;
        /*margin-top: 20px;*/
        font-family: 'IBM Plex Sans', sans-serif;
        font-weight: 600; font-size:10px;
        color:#393537;
        overflow: visible; /* This allows the svg contents to not be clipped, adjust as needed */

    }
</style>
