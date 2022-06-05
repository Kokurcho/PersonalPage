 $(document).ready(function(){

    if (localStorage.getItem('visits') == null)
{
    localStorage.setItem('visits', 0)
    var row = "Select your language";
    $('#storageDataString').append(row);
}
    else
{
    var langSelected = localStorage.getItem('lang');
    var lastVisitDate = localStorage.getItem('visitDate');
    var row = $('<p>Ваш предпочитаемый язык : '+ langSelected + '. <br>Ваша последняя дата визита : '+ lastVisitDate +'</br></p>');
    $('#storageDataString').append(row);
}
    alert("Кол-во посещений страницы = " + visited);
    var visited = parseInt(localStorage.getItem('visits'));
    visited += 1;
    localStorage.setItem('visits', visited);
    var button = document.querySelector("#btn1");
    button.addEventListener("click", function(){
    var selectedLang = $('#langSelect').val();
    localStorage.setItem('lang', selectedLang);
    localStorage.setItem('visitDate', new Date());
    alert('Язык перевода выбран успешно!');
    location.reload();
});
});

