<script>
    let showImage = false;
    const building = 'building.jpg';
</script>

<button on:click={() => showImage = !showImage}>
    {showImage ? 'Hide Image' : 'Show Image'}
</button>

{#if showImage}
    <img src={building} alt="Example">
{/if}






<div class=container>
    <h1>How to become an Idol Trainee</h1>
    <p>In order to become an idol, you have to be an idol trainee who has a contract with an agency.</p>
    <p>Therefore, what are the paths to become an idol trainee?</p>

    <h2>1. Street Casting</h2>
    <p>Street casting is literally being cast on the street.</p>
    <p>Each agency has a rookie development team that finds and fosters new talent.</p>
    <p>Casting staff in this rookie development team scouts and casts people on the streets.</p>
    <p>They approach someone to cast them if their appearance matches the image of the idol group they are planning.</p>
    <p>Just because you've been offered a position through street casting doesn't mean you can become an idol trainee right away.</p>
    <p>The contract is written after going through a very basic audition and camera test process.</p>

    <h2>2. Agency Audition</h2>
    <p>Many K-pop agencies conduct various auditions to recruit new talent.</p>
    <p>There can be periodic auditions that agencies announce, ongoing recruitment auditions, and national or global audition tours.</p>
    <p></p>
    <p></p>
    <p></p>
    <p></p>

    <h2>3. Connecting with Idol Academy</h2>
    <p>You can also enter an agency through an academy that prepares you to be an idol. </p>
    <p>They focus on dance and vocal training. Some agencies run their own academies.</p>
    <p>cost about 400,000 won to 600,000 won a month (approx. 300 to 500 USD)</p>
    <p>If the academy is closely connected to the agency, they recommend talented students to the agency.</p>
    <p>Or, the agency can contact the academy after watching the student evaluation videos uploaded by the academy.</p>
    <p>Also, in the case of large academies, agency representatives can visit the academy to hold auditions.</p>
    <p>he competition rate is lower at these private auditions held in the academy, so chances of become a trainee are a little higher.</p>
</div>