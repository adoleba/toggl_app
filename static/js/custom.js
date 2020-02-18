function hours() {
    if (document.getElementById('id_different_hours_0').checked === true) {
        document.getElementById('regular-hours').style.display = 'block';
        document.getElementById('variable-hours').style.display = 'none'
    }
    else {
        document.getElementById('variable-hours').style.display = 'block';
        document.getElementById('regular-hours').style.display = 'none';
    }
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

function reloadHours() {
    if (document.getElementById('id_different_hours_0').checked === true) {
        document.getElementById('regular-hours').style.display = 'block';
        document.getElementById('variable-hours').style.display = 'none'
    }
    if (document.getElementById('id_different_hours_1').checked === true) {
        document.getElementById('variable-hours').style.display = 'block';
        document.getElementById('regular-hours').style.display = 'none';
    }

    if (document.getElementById('id_monday_hour_start').value.length !== 0 ||
        document.getElementById('id_monday_hour_end').value.length !== 0) {
        document.getElementById('monday-hours').style.display = 'block';
        document.getElementById('monday-add').style.display = 'none';
    }

    if (document.getElementById('id_tuesday_hour_start').value.length !== 0 ||
        document.getElementById('id_tuesday_hour_end').value.length !== 0) {
        document.getElementById('tuesday-hours').style.display = 'block';
        document.getElementById('tuesday-add').style.display = 'none';
    }

    if (document.getElementById('id_wednesday_hour_start').value.length !== 0 ||
        document.getElementById('id_wednesday_hour_end').value.length !== 0) {
        document.getElementById('wednesday-hours').style.display = 'block';
        document.getElementById('wednesday-add').style.display = 'none';
    }

    if (document.getElementById('id_thursday_hour_start').value.length !== 0 ||
        document.getElementById('id_thursday_hour_end').value.length !== 0) {
        document.getElementById('thursday-hours').style.display = 'block';
        document.getElementById('thursday-add').style.display = 'none';
    }

    if (document.getElementById('id_friday_hour_start').value.length !== 0 ||
        document.getElementById('id_friday_hour_end').value.length !== 0) {
        document.getElementById('friday-hours').style.display = 'block';
        document.getElementById('friday-add').style.display = 'none';
    }
}
