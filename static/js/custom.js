function regularHours() {
    document.getElementById('regular-hours').style.display = 'block';
    document.getElementById('variable-hours').style.display = 'none'
}

function variableHours() {
    document.getElementById('variable-hours').style.display = 'block';
    document.getElementById('regular-hours').style.display = 'none';
}

function showDay(id, add) {
    const dayId = document.getElementById(id);
    const addDayId = document.getElementById(add);
    dayId.style.display = 'block';
    addDayId.style.display = 'none';
}

function hideDay(id, add) {
    const dayId = document.getElementById(id);
    const addDayId = document.getElementById(add);
    dayId.style.display = 'none';
    addDayId.style.display = 'block';
}
