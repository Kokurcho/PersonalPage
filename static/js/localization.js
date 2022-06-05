$(document).ready(function () {
    if (localStorage.getItem('lang') === "ru")
    {
        document.getElementById("desc").innerHTML = "Хорошие новости, всех люблю. Затарились с другом одёжкой и потом поели в Теремке, он взял двойную порцию пельменёв, я взял суп гороховый, булочку, гречку с курочкой и чай";
    }
    if (localStorage.getItem('lang') === "en")
    {
        document.getElementById("desc").innerHTML = "Lorem ipsum dolor sit amet consectetur, adipisicing elit. Velit mollitia quis ad consectetur. Quibusdam nostrum minus error unde voluptatibus porro veritatis dicta blanditiis doloribus, molestiae dolorum explicabo repellat reiciendis accusantium obcaecati ratione iste mollitia quis ipsum quaerat.";
    }
});

