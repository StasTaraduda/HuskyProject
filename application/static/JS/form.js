var clearButton = document.getElementById("clear")
clearButton.addEventListener("click",Clear)
// var saveButton = document.getElementById("save")
// saveButton.addEventListener("click",Save)
var modalClose = document.querySelector(".modal_close")
modalClose.addEventListener("click",closeModal)
var form = document.querySelector("form")
form.addEventListener("submit", event =>{
    form.checkValidity()
    event.preventDefault()
    Save()
})
var name2 = document.getElementById("name")
name2.addEventListener("invalid", event =>{
    console.log(name2.validationMessage)
})
Weekendblocking()

function Save(){
    var name = document.getElementById("name")
    var animalType = document.getElementById("animal")
    var date = document.getElementById("date")
    var human = document.getElementById("human")
    var surname = document.getElementById("surname")
    var email = document.getElementById("email")
    var number = document.getElementById("number")
    // if(!name.checkValidity()){
    //     console.log(name.validationMessage)
    // }else{
    //     console.log(name.value)
    // }
    // if(!number.checkValidity()){
    //     console.log(number.validationMessage)
    // }else{

    //     console.log(number.value)
    // }


    // if(name.value.length == 0 ){
    //     alert("Введіть значення")
    // }else if(!((name.value[0]>='А' && name.value[0] <= 'Я') || (name.value[0]>='A' && name.value[0]<='Z'))){
    //     alert("І'мя тваринки повинно починатися з великої літери")

    // }else if(animalType.value == "empty"){
    //     alert("Виберіть тип тваринки")

    // }else if(date.value.length == 0){
    //     alert("Виберіть дату прийому будь ласка")

    // }else if(human.value.length==0){
    //     alert("Введіть ім'я власника")

    // }else if(!((human.value[0]>='А' && human.value[0] <= 'Я') || (human.value[0]>='A' && human.value[0]<='Z'))){
    //     alert("І'мя власника повинно починатися з великої літери")
        
    // }else if(surname.value.length == 0){
    //     alert("Введіть прізвище влсасника тваринки")

    // }else if(!((surname.value[0]>='А' && surname.value[0] <= 'Я') || (surname.value[0]>='A' && surname.value[0]<='Z'))){
    //     alert("Прізвище власника повинно починатися з великої літери")
        
    // }else if(email.value.length == 0){
    //     alert("Введіть адресу електроної почти")

    // }else if(number.value.length == 0 || number.value.length < 11 || number.value.length >14){
    //     alert("Ви неправильно ввкли номер телефону або взагалі не ввели спробуйте ще раз")
    // }
    
    // else{
        document.querySelector(".modal").style.visibility = "visible"
        var modalContent = document.querySelector(".modal_content")
        modalContent.insertAdjacentHTML("afterbegin",`
        Дякую за надану інформацію!Вашу домашня тваринка зареєстрованна на прийом до лікаря.<br>
        Кличка:${name.value}<br>
        Тип тваринки:${animalType.value}<br>
        Дата:${date.value}<br>
        Ім'я власника:${human.value}<br>
        Прізвище власника:${surname.value}<br>
        Адреса електроної почти:${email.value}<br>
        Номер телефону: ${number.value}<br>
        `)
        // alert(`Дякую за надану інформацію!Вашу домашня тваринка зареєстрованна на прийом до лікаря.
        // Кличка:${name.value}
        // Тип тваринки:${animalType.value}
        // Дата:${date.value}
        // Ім'я власника:${human.value}
        // Прізвище власника:${surname.value}
        // Адреса електроної почти:${email.value}
        // Номер телефону: ${number.value}`)
    // }
    
}
function Clear(){
    var name = document.getElementById("name")
    var animalType = document.getElementById("animal")
    var date = document.getElementById("date")
    var human = document.getElementById("human")
    var surname = document.getElementById("surname")
    var email = document.getElementById("email")
    var number = document.getElementById("number")
    name.value = ""
    animalType.value = ""
    date.value = ""
    human.value=""
    surname.value=""
    email.value=""
    number.value=""
}

function closeModal(){
    document.querySelector(".modal").style.visibility = "hidden"

}

function Weekendblocking(){
    const validate = dateString => {
        const day = (new Date(dateString)).getDay();
        if (day==0 || day==6) {
          return false;
        }
        return true;
      }
        document.querySelector('#date').onchange = evt => {
        if (!validate(evt.target.value)) {
          evt.target.value = '';
          alert('У вихідні дні вет клініка не працює, виберіть будь-який робочій день')
        }
      }
}


function Save2(){
    alert("Окей");
}