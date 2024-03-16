<script>
    import {onMount} from 'svelte';
    import * as d3 from 'd3';

    let idolsData = [];

    onMount(async () => {
        const data = await d3.csv('debut_idols_data.csv');
        idolsData = processData(data);
        renderChart(idolsData.male, 'male');
        renderChart(idolsData.female, 'female');

        barCreate(idolsData, 'male')
        barCreate(idolsData, 'female')
    });

    function processData(data) {
        // Convert height from cm to meters and calculate BMI
        data.forEach(d => {
            d.Height = +d.Height;
            d.Weight = +d.Weight;
            d.BMI = d.Weight / (d.Height / 100) ** 2;
        });

        // Define BMI categories
        const bmiCategories = ['Underweight', 'Normal', 'Overweight', 'Obese'];
        const bmiCategoryRanges = [0, 18.5, 25, 30, Infinity];

        // Assign BMI categories
        data.forEach(d => {
            const bmiIndex = bmiCategoryRanges.findIndex((value, index, array) => d.BMI < array[index + 1]);
            d.BMICategory = bmiCategories[bmiIndex - 1];
        });

        // Split data by gender
        const male = data.filter(d => d.Gender === 'M');
        const female = data.filter(d => d.Gender === 'F');

        return {male, female};
    }

    function renderChart(data, gender) {
        const svg = d3.select(`#scatter-plot-${gender}`);
        const margin = {top: 20, right: 20, bottom: 30, left: 40};
        const width = +svg.attr('width') - margin.left - margin.right;
        const height = +svg.attr('height') - margin.top - margin.bottom;

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
            .domain([0, 18.5, 25, 30, Infinity]) // Example BMI values for domain
            .range(['grey', 'blue', 'green', 'orange', 'red']) // Corresponding colors

            .interpolate(d3.interpolateRgb);
        const g = svg.append('g')
            .attr('transform', `translate(${margin.left},${margin.top})`);

        g.append('g')
            .attr('transform', `translate(0,${height})`)
            .call(d3.axisBottom(x));

        g.append('g')
            .call(d3.axisLeft(y));

        g.selectAll('.dot')
            .data(data)
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


    }

    function barCreate(data, gender) {
        const svg = d3.select(`#scatter-plot-${gender}`);
        const margin = {top: 20, right: 20, bottom: 30, left: 40};
        const width = +svg.attr('width') - margin.left - margin.right;
        const height = +svg.attr('height') - margin.top - margin.bottom;
        // Add color bar rectangle
        const barHeight = 200;

        const defs = svg.append('defs');


        const bmiColorScale = d3.scaleLinear()
            .domain([0, 18.5, 25, 30, Infinity]) // Example BMI values for domain
            .range(['grey', 'blue', 'green', 'orange', 'red']) // Corresponding colors

        // Add an axis to show the color scale
        const colorAxisScale = d3.scaleLinear()
            .domain(bmiColorScale.domain())
            .range([margin.left, margin.left + width]);

        const colorAxis = d3.axisBottom(colorAxisScale)
            .tickSize(barHeight * 1.5)
            .tickFormat(d3.format('.1f'))
            .tickValues(bmiColorScale.domain());

        svg.append('g')
            .attr('class', 'color-axis')
            .attr('transform', `translate(0, ${height + margin.top + 10})`)
            .call(colorAxis)
            .select('.domain').remove(); // Remove the axis line


    }
</script>

<p>'As u see in the graphs, the range of bmi are mostly underweight for male and especially female idols'</p>
<svg id="scatter-plot-male" width="500" height="400"></svg>
<svg id="scatter-plot-female" width="500" height="400"></svg>


<style>
    .dot {
        stroke: #000;
    }

    svg {
        margin-left: 50px;
        /*margin-top: 20px;*/
    }
</style>
