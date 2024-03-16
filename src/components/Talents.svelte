<script>
    let talents = [
        {
            name: 'Dance',
            img: 'talents/img_1.png',
            info: "Dance auditions are a battlefield where only the most precise and passionate survive. Companies are on the lookout for individuals who not only execute complex choreographies but also infuse each movement with a unique flair. Among the ranks, a young dancer once made waves with his innovative fusion of traditional Korean dance and contemporary hip-hop, showcasing an unparalleled synchronization and rhythm that ultimately set him apart, turning him into a dancing sensation within the trainee ranks."
        },
        {
            name: 'Sing',
            img: 'talents/img.png',
            info: "In the relentless pursuit of excellence, a K-pop company sifts through thousands of applicants to find a voice that doesn't just sing a song, but brings it to life. A trainee must have more than just a good voice; they need the ability to stir emotions and captivate an audience. Among those vying for a spot, one notable story is that of a contestant from a small town who, against all odds, enchanted the judges with her hauntingly beautiful rendition of a classic ballad. Her vocal control and emotional depth outshone her peers, setting a new standard for what it means to have a \"company-worthy\" voice."

        },
        {
            name: 'visual',
            img: 'talents/visual.png',
            info: "In a world where visuals can be as impactful as talent, K-pop companies often hold auditions that resemble a search for the face that could launch a thousand ships. The competition is fierce, as they seek someone with an exceptional look that can charm fans and create a memorable stage presence. An aspirant once turned heads not just for her striking features but for the poise and confidence she exuded, transforming the stage into her realm the moment she stepped on it. Her distinctive look and aura made her the talk of the town, proving that a powerful visual appeal can indeed eclipse the brightest of stars."
        }
    ];
</script>

<style>
    .talents-container {
        display: flex;
        gap: 180px; /* Adjust as needed */
        margin-top: 40px;
    }

    .talent {
        position: relative;
        display: flex;
        align-items: center;
        flex-direction: column;
        width: 300px; /* Increased image size */
        cursor: pointer;
    }

    .talent img {
        object-fit: cover; /* Resize the image to cover the area without stretching */
        border-radius: 10px; /* Optional: adds rounded corners to your images */
        width: 100%;
        height: auto;
        filter: grayscale(100%);
        transition: filter 0.3s ease, transform 0.3s ease;
        /*border-radius: 10px;*/
        cursor: pointer;
    }

    .talent img:hover {
        filter: none;
    }

    .talent:hover img {
        filter: none; /* Remove the grayscale filter when the container is hovered */
    }

    .talent:hover .title {
        background-color: #5e4b8b; /* Purple background */
        color: white; /* White text */
    }



    .tooltip {
        position: absolute;
        top: 50%;
        transform: translateY(-50%);
        left: 110%;
        background-color: #5e4b8b; /* A shade of purple for the background */
        color: #fff; /* White text color */
        padding: 12px;
        border-radius: 8px;
        visibility: hidden;
        opacity: 0;
        transition: visibility 0.2s, opacity 0.2s ease-out;
        min-width: 200px;
        text-align: left;
        white-space: normal;
        z-index: 10;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Subtle shadow for depth */
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; /* Stylish font */
        font-size: 0.9rem;
        line-height: 1.4;
        letter-spacing: 0.5px;
    }

    .talent:hover .tooltip {
        visibility: visible;
        opacity: 1;
    }


    /* For smaller screens, align the tooltip on the left side */
    @media (max-width: 768px) {
        .tooltip {
            left: auto;
            right: 110%; /* Place tooltip on the left of the image */
        }
    }


    .title {
        font-size: 1.2rem; /* Larger font size for titles */
        color: #5e4b8b; /* White text on hover */
        font-weight: bold; /* Makes the font bold */
        text-align: center; /* Centers the text within its container */
        padding: 10px 20px; /* Padding for aesthetic spacing */
        border-radius: 5px; /* Rounded corners */
        transition: background-color 0.3s ease-in-out, color 0.3s ease-in-out; /* Transition for the hover effect */
        cursor: pointer; /* Changes the mouse cursor to indicate these are interactive */
    }


</style>

<h1>In general, companies look at these aspects:</h1>


<div class="talents-container">
    {#each talents as talent (talent.name)}
        <div class="talent">
            <div class="title">{talent.name}</div>
            <img src={talent.img} alt={talent.name}/>
            <div class="tooltip">{talent.info}</div>
        </div>
    {/each}
</div>