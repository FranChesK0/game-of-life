function updateWorld(world, previousWorld) {
    const gameTable = document.getElementById("game-table");
    gameTable.innerHTML = '';

    for (let i = 0; i < world.length; i++) {
        const tr = document.createElement("tr");
        for (let j = 0; j < world[i].length; j++) {
            const cell = document.createElement('td');
            cell.classList.add('cell');
            if (world[i][j]) {
                cell.classList.add('alive');
            } else if (!world[i][j] && previousWorld[i][j]) {
                cell.classList.add('dead');
            }
            tr.appendChild(cell);
        }
        gameTable.appendChild(tr)
    }
}

async function fetchGameState() {
    try {
        const response = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (!response.ok) throw new Error("API request error");
        const data = await response.json();

        updateWorld(data.world, data.previous_world);
        document.getElementById("counter").innerText = data.life_count;
    } catch (error) {
        console.error("Error: ", error);
    }
}
