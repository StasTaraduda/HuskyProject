const but = document.getElementById("display");
const search = document.querySelector('.search');
but.onclick = getClient
function getClient() {
    but.style.display = "none"
    search.style.display= "none"
    let xhr = new XMLHttpRequest();
    xhr.open("GET", "/clinicClients/");
    xhr.send();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && this.status == 200 || xhr.status == 304) {
            const client = JSON.parse(this.responseText);
            console.log(client);
            divObj = document.getElementById("clients");
            divObj.innerHTML = "<h3>Клієнти, які записані на сьогоднішнє число<h3>";
            let count = 1
            for (let cl of client) {
                st = divObj.innerHTML;
                strClient = 'Клієнт №'+ ' '+ count + ' ' + cl.first_name + " " + cl.last_name + "<br>";
                console.log(strClient);
                divObj.innerHTML = st + strClient;
                count++;
            }
        }
    }
}
