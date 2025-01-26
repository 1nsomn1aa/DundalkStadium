function updateCourts(courts) {
    const gameTypeSelect = document.getElementById("game-type");
    const courtSelect = document.getElementById("court");
    const selectedGameTypeId = gameTypeSelect.value;

    courtSelect.innerHTML = '<option value="">Select a court</option>';

    courts.forEach(court => {
        if (court.game_type_id === selectedGameTypeId) {
            const option = document.createElement("option");
            option.value = court.id;
            option.textContent = court.name;
            courtSelect.appendChild(option);
        }
    });

    courtSelect.disabled = courtSelect.options.length === 1;
}